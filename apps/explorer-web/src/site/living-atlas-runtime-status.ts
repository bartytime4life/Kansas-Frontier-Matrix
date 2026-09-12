import { MAP_INTERACTION_TOOLS } from "../features/living_atlas";

export type LivingAtlasRuntimeStatusGuard = Readonly<{
  destroy: () => void;
}>;

export type LivingAtlasRuntimeStatusMutation =
  | "KEEP"
  | "RELEASE"
  | "RESTORE";

const ACTION_SELECTOR = 'button[data-atlas-action]';
const INTERACTION_PREFIX = "interaction:";
const READY_STATUS_PREFIX = "Renderer READY";
const STATUS_SELECTOR = '.atlas-runtime-state[role="status"]';
const GUARD_DATASET_KEY = "livingAtlasRuntimeStatusGuard";

export function resolveHeldInteractionStatus(
  action: string | undefined,
): string | null {
  if (action === undefined || !action.startsWith(INTERACTION_PREFIX)) {
    return null;
  }

  const toolId = action.slice(INTERACTION_PREFIX.length);
  const tool = MAP_INTERACTION_TOOLS.find((entry) => entry.id === toolId);
  if (tool === undefined || tool.state !== "HELD") return null;

  return `${tool.name} HELD · ${tool.statusReason}`;
}

export function resolveLivingAtlasRuntimeStatusMutation(
  currentStatus: string,
  heldStatus: string | null,
): LivingAtlasRuntimeStatusMutation {
  if (heldStatus === null || currentStatus === heldStatus) return "KEEP";
  if (currentStatus.startsWith(READY_STATUS_PREFIX)) return "RESTORE";
  return "RELEASE";
}

export function mountLivingAtlasRuntimeStatusGuard(
  root: HTMLElement,
): LivingAtlasRuntimeStatusGuard | null {
  if (root.dataset[GUARD_DATASET_KEY] === "mounted") return null;

  const status = root.querySelector<HTMLElement>(STATUS_SELECTOR);
  const MutationObserverConstructor =
    root.ownerDocument.defaultView?.MutationObserver;
  if (status === null || MutationObserverConstructor === undefined) return null;

  root.dataset[GUARD_DATASET_KEY] = "mounted";
  let heldStatus: string | null = null;

  const observer = new MutationObserverConstructor(() => {
    const currentStatus = status.textContent ?? "";
    const mutation = resolveLivingAtlasRuntimeStatusMutation(
      currentStatus,
      heldStatus,
    );

    if (mutation === "RESTORE" && heldStatus !== null) {
      status.dataset.statusSource = "interaction";
      status.textContent = heldStatus;
    } else if (mutation === "RELEASE") {
      heldStatus = null;
      status.dataset.statusSource = "runtime";
    }
  });
  observer.observe(status, {
    characterData: true,
    childList: true,
    subtree: true,
  });

  const handleAction = (event: MouseEvent): void => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const actionButton = target.closest<HTMLButtonElement>(ACTION_SELECTOR);
    if (actionButton === null || !root.contains(actionButton)) return;

    const nextHeldStatus = resolveHeldInteractionStatus(
      actionButton.dataset.atlasAction,
    );
    heldStatus = nextHeldStatus;
    if (nextHeldStatus === null) return;

    status.dataset.statusSource = "interaction";
    status.textContent = nextHeldStatus;
  };
  root.addEventListener("click", handleAction);

  return Object.freeze({
    destroy: () => {
      observer.disconnect();
      root.removeEventListener("click", handleAction);
      delete root.dataset[GUARD_DATASET_KEY];
    },
  });
}

function bootstrapLivingAtlasRuntimeStatusGuard(): void {
  const root = document.querySelector<HTMLElement>("#root");
  if (root === null) return;
  if (mountLivingAtlasRuntimeStatusGuard(root) !== null) return;

  const MutationObserverConstructor =
    root.ownerDocument.defaultView?.MutationObserver;
  if (MutationObserverConstructor === undefined) return;

  const bootstrapObserver = new MutationObserverConstructor(() => {
    if (mountLivingAtlasRuntimeStatusGuard(root) !== null) {
      bootstrapObserver.disconnect();
    }
  });
  bootstrapObserver.observe(root, { childList: true, subtree: true });
}

if (typeof document !== "undefined") {
  bootstrapLivingAtlasRuntimeStatusGuard();
}
