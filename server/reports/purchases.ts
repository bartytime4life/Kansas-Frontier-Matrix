import { createHash, randomUUID } from "node:crypto";
import { assertQuoteCurrent, assertQuoteOwner, createReportQuote, reportDigest, ReportServiceError,
  type ReportQuote, type ServerReportAssessment } from "./pricing";

export type ReportOrderStatus = "CHECKOUT_CREATING" | "CHECKOUT_UNCERTAIN" | "AWAITING_PAYMENT"
  | "PAYMENT_REVIEW" | "ENTITLED" | "GENERATING" | "READY" | "FAILED" | "CANCELED" | "REFUNDED";
export type ReportArtifact = Readonly<{ fileName: string; contentType: "text/markdown" | "application/json" | "application/pdf";
  bytes: Uint8Array; inputDigest: string; sourceDigest: string; assessmentDigest: string }>;
export type StaffAssignment = Readonly<{ role: "steward" | "admin"; expiresAt: string; revoked: boolean }>;
export type ReportOrder = {
  id: string; ownerId: string; quoteId: string; status: ReportOrderStatus;
  grant: "purchase" | "staff" | null; createdAt: string;
  checkout?: { sessionId: string; url: string };
  transactionId?: string;
  generationLease?: { id: string; expiresAt: string };
  artifact?: ReportArtifact & { digest: string };
};
/** Safe response for quote/checkout/status endpoints; artifact bytes are private. */
export type ReportOrderView = Readonly<{
  id: string; status: ReportOrderStatus; entitlement: "purchase" | "staff" | null;
  checkout: { sessionId: string; url: string } | null;
}>;
const orderView = (order: ReportOrder): ReportOrderView => ({ id: order.id, status: order.status,
  entitlement: order.grant,
  checkout: order.status === "AWAITING_PAYMENT" && order.checkout
    ? { sessionId: order.checkout.sessionId, url: order.checkout.url } : null });

/** Every method runs in one serializable database transaction. No public reads. */
export interface ReportTransaction {
  getQuote(id: string): Promise<ReportQuote | null>;
  putQuote(quote: ReportQuote): Promise<void>;
  getOrder(id: string): Promise<ReportOrder | null>;
  putOrder(order: ReportOrder): Promise<void>;
  staffAssignment(ownerId: string): Promise<StaffAssignment | null>;
  /** Enforced by a UNIQUE(provider, transaction_id) database constraint. */
  claimPayment(provider: string, transactionId: string, orderId: string): Promise<boolean>;
}
export interface ReportRepository {
  transaction<T>(action: (transaction: ReportTransaction) => Promise<T>): Promise<T>;
}

/** Normalized by an authenticated GoDaddy adapter; never accepted from a browser. */
export type VerifiedReportPayment = Readonly<{
  status: "PENDING" | "CAPTURED" | "CANCELED" | "REFUNDED";
  transactionId: string | null; storeId: string; reference: string;
  amountMinor: number; currency: string; inputDigest: string; sourceDigest: string;
}>;
export interface ReportPaymentProvider {
  readonly provider: "godaddy-payments";
  readonly storeId: string;
  /** Exact hosts verified for this merchant's hosted checkout, not arbitrary URLs. */
  readonly checkoutHosts: readonly string[];
  createCheckout(quote: ReportQuote, reference: string): Promise<{ sessionId: string; url: string }>;
  /** Resolve payment by the persisted provider session, not a client transaction ID. */
  verifyCheckout(sessionId: string): Promise<VerifiedReportPayment>;
}

export type ReportPurchaseDependencies = Readonly<{
  repository: ReportRepository;
  payment: ReportPaymentProvider;
  pricing: unknown;
  assess: (input: unknown) => Promise<ServerReportAssessment>;
  render: (quote: ReportQuote) => Promise<ReportArtifact>;
  now?: () => Date;
}>;

const fail = (code: string, status: number): never => { throw new ReportServiceError(code, status); };
const referenceFor = (quote: ReportQuote) => `kfm-report-${quote.id}`;
const activeStaff = (assignment: StaffAssignment | null, now: Date) =>
  assignment !== null && !assignment.revoked && ["steward", "admin"].includes(assignment.role)
  && Number.isFinite(Date.parse(assignment.expiresAt)) && Date.parse(assignment.expiresAt) > now.getTime();
const validId = (value: unknown): value is string => typeof value === "string" && /^[\w.-]{1,256}$/.test(value);

/** ownerId is resolved by a trusted server session adapter, never request JSON. */
export class ReportPurchaseService {
  constructor(private readonly dependencies: ReportPurchaseDependencies) {}
  private now(): Date { return (this.dependencies.now ?? (() => new Date()))(); }

  async quote(ownerId: string, input: unknown): Promise<ReportQuote> {
    const assessment = await this.dependencies.assess(input);
    if (reportDigest(input) !== reportDigest(assessment.input)) return fail("REPORT_ASSESSMENT_SCOPE_MISMATCH", 409);
    const quote = createReportQuote(ownerId, assessment, this.dependencies.pricing, this.now());
    await this.dependencies.repository.transaction((tx) => tx.putQuote(quote));
    return quote;
  }

  private async owned(tx: ReportTransaction, id: string, ownerId: string): Promise<{ quote: ReportQuote; order: ReportOrder }> {
    const order = await tx.getOrder(id);
    if (!order || order.ownerId !== ownerId) return fail("REPORT_NOT_FOUND", 404);
    const quote = await tx.getQuote(order.quoteId);
    if (!quote) return fail("REPORT_NOT_FOUND", 404);
    assertQuoteOwner(quote, ownerId);
    if (quote.assessmentDigest !== reportDigest(quote.assessment)) return fail("REPORT_QUOTE_CORRUPT", 409);
    return { order, quote };
  }

  async start(quoteId: string, ownerId: string, input: unknown): Promise<ReportOrderView> {
    let needsCheckout = false;
    const initial = await this.dependencies.repository.transaction(async (tx) => {
      const quote = await tx.getQuote(quoteId);
      if (!quote) return fail("REPORT_NOT_FOUND", 404);
      assertQuoteOwner(quote, ownerId);
      if (quote.inputDigest !== reportDigest(input)) return fail("REPORT_SCOPE_CHANGED", 409);
      const existing = await tx.getOrder(quoteId);
      // A paid purchase/repeat download retains its original terms after quote expiry.
      if (existing) {
        if (existing.ownerId !== ownerId) return fail("REPORT_NOT_FOUND", 404);
        if (existing.grant === "staff" && !activeStaff(await tx.staffAssignment(ownerId), this.now())) return fail("REPORT_STAFF_EXEMPTION_EXPIRED", 403);
        return existing;
      }
      assertQuoteCurrent(quote, ownerId, input, this.now());
      const staff = activeStaff(await tx.staffAssignment(ownerId), this.now());
      const order: ReportOrder = { id: quoteId, quoteId, ownerId, createdAt: this.now().toISOString(),
        status: staff ? "ENTITLED" : "CHECKOUT_CREATING", grant: staff ? "staff" : null };
      needsCheckout = !staff;
      await tx.putOrder(order);
      return order;
    });
    if (!needsCheckout) return orderView(initial);
    // A lost create response must be reconciled, never blindly retried/charged twice.
    try {
      const quote = await this.dependencies.repository.transaction(async (tx) => (await this.owned(tx, quoteId, ownerId)).quote);
      const checkout = await this.dependencies.payment.createCheckout(quote, referenceFor(quote));
      const url = new URL(checkout.url);
      if (!validId(checkout.sessionId) || url.protocol !== "https:" || url.username || url.password
        || !this.dependencies.payment.checkoutHosts.includes(url.hostname)) return fail("REPORT_CHECKOUT_RESPONSE_INVALID", 502);
      const saved = await this.dependencies.repository.transaction(async (tx) => {
        const { order } = await this.owned(tx, quoteId, ownerId);
        if (order.status !== "CHECKOUT_CREATING") return fail("REPORT_CHECKOUT_STATE_CHANGED", 409);
        order.checkout = { sessionId: checkout.sessionId, url: checkout.url }; order.status = "AWAITING_PAYMENT";
        await tx.putOrder(order); return order;
      });
      return orderView(saved);
    } catch {
      const uncertain = await this.dependencies.repository.transaction(async (tx) => {
        const { order } = await this.owned(tx, quoteId, ownerId);
        if (order.status === "CHECKOUT_CREATING") { order.status = "CHECKOUT_UNCERTAIN"; await tx.putOrder(order); }
        return order;
      });
      return orderView(uncertain);
    }
  }

  async refreshPayment(id: string, ownerId: string): Promise<ReportOrderView> {
    return orderView(await this.refreshOwnedPayment(id, ownerId));
  }

  private async refreshOwnedPayment(id: string, ownerId: string): Promise<ReportOrder> {
    const captured = await this.dependencies.repository.transaction((tx) => this.owned(tx, id, ownerId));
    if (captured.order.grant === "staff") {
      const allowed = await this.dependencies.repository.transaction(async (tx) => activeStaff(await tx.staffAssignment(ownerId), this.now()));
      if (!allowed) return fail("REPORT_STAFF_EXEMPTION_EXPIRED", 403);
      return captured.order;
    }
    if (!captured.order.checkout) return fail("REPORT_CHECKOUT_NOT_READY", 409);
    const payment = await this.dependencies.payment.verifyCheckout(captured.order.checkout.sessionId);
    const quote = captured.quote;
    if ((payment.status !== "PENDING" && !validId(payment.transactionId)) || payment.storeId !== this.dependencies.payment.storeId
      || payment.reference !== referenceFor(quote) || !Number.isSafeInteger(payment.amountMinor)
      || payment.amountMinor !== quote.amountMinor || payment.currency !== quote.currency
      || payment.inputDigest !== quote.inputDigest || payment.sourceDigest !== quote.sourceDigest) {
      return fail("REPORT_PAYMENT_MISMATCH", 409);
    }
    return this.dependencies.repository.transaction(async (tx) => {
      const { order } = await this.owned(tx, id, ownerId);
      if (order.checkout?.sessionId !== captured.order.checkout?.sessionId) return fail("REPORT_CHECKOUT_STATE_CHANGED", 409);
      if (payment.status === "REFUNDED" || payment.status === "CANCELED") {
        order.grant = null; order.status = payment.status; delete order.generationLease;
      } else if (payment.status === "CAPTURED") {
        if (!validId(payment.transactionId)) return fail("REPORT_PAYMENT_MISMATCH", 409);
        // Terminal revocation cannot be undone by a delayed/out-of-order capture read.
        if (order.status === "REFUNDED" || order.status === "CANCELED") return order;
        if (order.transactionId && order.transactionId !== payment.transactionId) return fail("REPORT_PAYMENT_MISMATCH", 409);
        if (!await tx.claimPayment(this.dependencies.payment.provider, payment.transactionId, id)) return fail("REPORT_PAYMENT_ALREADY_USED", 409);
        order.transactionId = payment.transactionId; order.grant = "purchase";
        if (!["GENERATING", "READY", "FAILED"].includes(order.status)) order.status = order.artifact ? "READY" : "ENTITLED";
      } else if (payment.status === "PENDING") {
        order.status = "PAYMENT_REVIEW"; order.grant = null; delete order.generationLease;
      } else return fail("REPORT_PAYMENT_STATE_INVALID", 502);
      await tx.putOrder(order); return order;
    });
  }

  private async requireEntitlement(tx: ReportTransaction, order: ReportOrder, now: Date): Promise<void> {
    if (!order.grant || ["REFUNDED", "CANCELED", "PAYMENT_REVIEW"].includes(order.status)) return fail("REPORT_PAYMENT_REQUIRED", 402);
    if (order.grant === "staff" && !activeStaff(await tx.staffAssignment(order.ownerId), now)) return fail("REPORT_STAFF_EXEMPTION_EXPIRED", 403);
  }

  async fulfill(id: string, ownerId: string): Promise<ReportOrderView> {
    await this.refreshPayment(id, ownerId);
    const leaseId = randomUUID(); let shouldRender = false;
    const claimed = await this.dependencies.repository.transaction(async (tx) => {
      const { order, quote } = await this.owned(tx, id, ownerId);
      await this.requireEntitlement(tx, order, this.now());
      if (order.status === "READY" || (order.status === "GENERATING" && order.generationLease
        && Date.parse(order.generationLease.expiresAt) > this.now().getTime())) return { order, quote };
      order.status = "GENERATING"; order.generationLease = { id: leaseId, expiresAt: new Date(this.now().getTime() + 300000).toISOString() };
      shouldRender = true; await tx.putOrder(order); return { order, quote };
    });
    if (!shouldRender) return orderView(claimed.order);
    try {
      const artifact = await this.dependencies.render(claimed.quote);
      if (!(artifact.bytes instanceof Uint8Array) || artifact.bytes.byteLength < 1 || artifact.bytes.byteLength > 33554432
        || !/^[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}$/.test(artifact.fileName)
        || !["text/markdown", "application/json", "application/pdf"].includes(artifact.contentType)
        || artifact.inputDigest !== claimed.quote.inputDigest || artifact.sourceDigest !== claimed.quote.sourceDigest
        || artifact.assessmentDigest !== claimed.quote.assessmentDigest) return fail("REPORT_ARTIFACT_INVALID", 502);
      // No renderer mutation of the captured assessment is permitted.
      if (reportDigest(claimed.quote.assessment) !== claimed.quote.assessmentDigest) return fail("REPORT_QUOTE_CORRUPT", 409);
      const completed = await this.dependencies.repository.transaction(async (tx) => {
        const { order } = await this.owned(tx, id, ownerId);
        await this.requireEntitlement(tx, order, this.now());
        if (order.generationLease?.id !== leaseId || order.status !== "GENERATING") return order;
        order.artifact = { ...artifact, bytes: new Uint8Array(artifact.bytes), digest: createHash("sha256").update(artifact.bytes).digest("hex") };
        order.status = "READY"; delete order.generationLease;
        await tx.putOrder(order); return order;
      });
      return orderView(completed);
    } catch {
      const failed = await this.dependencies.repository.transaction(async (tx) => {
        const { order } = await this.owned(tx, id, ownerId);
        if (order.generationLease?.id === leaseId) { order.status = "FAILED"; delete order.generationLease; await tx.putOrder(order); }
        return order;
      });
      return orderView(failed);
    }
  }

  async download(id: string, ownerId: string): Promise<ReportArtifact & { digest: string }> {
    await this.refreshPayment(id, ownerId);
    return this.dependencies.repository.transaction(async (tx) => {
      const { order } = await this.owned(tx, id, ownerId);
      await this.requireEntitlement(tx, order, this.now());
      if (order.status !== "READY" || !order.artifact) return fail("REPORT_NOT_READY", 409);
      if (createHash("sha256").update(order.artifact.bytes).digest("hex") !== order.artifact.digest) return fail("REPORT_ARTIFACT_CORRUPT", 409);
      return { ...order.artifact, bytes: new Uint8Array(order.artifact.bytes) };
    });
  }
}
