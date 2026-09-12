import { index, integer, sqliteTable, text, uniqueIndex } from "drizzle-orm/sqlite-core";

export const submissions = sqliteTable("data_submissions", {
  id: text("id").primaryKey(),
  ownerKey: text("owner_key").notNull(),
  ownerName: text("owner_name").notNull(),
  title: text("title").notNull(),
  sourceId: text("source_id").notNull(),
  sourceUrl: text("source_url").notNull(),
  description: text("description").notNull(),
  license: text("license").notNull(),
  sensitivity: text("sensitivity").notNull(),
  startDate: text("start_date").notNull(),
  endDate: text("end_date").notNull(),
  fileName: text("file_name").notNull(),
  fileBytes: integer("file_bytes").notNull(),
  fileSha256: text("file_sha256").notNull(),
  objectKey: text("object_key").notNull(),
  status: text("status").notNull().default("submitted"),
  version: integer("version").notNull().default(1),
  createdAt: text("created_at").notNull(),
  updatedAt: text("updated_at").notNull(),
}, (table) => [index("idx_submissions_owner_created").on(table.ownerKey, table.createdAt), index("idx_submissions_status_created").on(table.status, table.createdAt)]);

export const submissionReviews = sqliteTable("data_submission_reviews", {
  id: text("id").primaryKey(),
  submissionId: text("submission_id").notNull().references(() => submissions.id),
  reviewerKey: text("reviewer_key").notNull(),
  reviewerName: text("reviewer_name").notNull(),
  previousStatus: text("previous_status").notNull(),
  status: text("status").notNull(),
  note: text("note").notNull(),
  version: integer("version").notNull(),
  createdAt: text("created_at").notNull(),
}, (table) => [uniqueIndex("idx_review_submission_version").on(table.submissionId, table.version)]);
