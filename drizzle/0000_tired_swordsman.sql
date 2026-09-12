CREATE TABLE `data_submission_reviews` (
	`id` text PRIMARY KEY NOT NULL,
	`submission_id` text NOT NULL,
	`reviewer_key` text NOT NULL,
	`reviewer_name` text NOT NULL,
	`previous_status` text NOT NULL,
	`status` text NOT NULL,
	`note` text NOT NULL,
	`version` integer NOT NULL,
	`created_at` text NOT NULL,
	FOREIGN KEY (`submission_id`) REFERENCES `data_submissions`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE UNIQUE INDEX `idx_review_submission_version` ON `data_submission_reviews` (`submission_id`,`version`);--> statement-breakpoint
CREATE TABLE `data_submissions` (
	`id` text PRIMARY KEY NOT NULL,
	`owner_key` text NOT NULL,
	`owner_name` text NOT NULL,
	`title` text NOT NULL,
	`source_id` text NOT NULL,
	`source_url` text NOT NULL,
	`description` text NOT NULL,
	`license` text NOT NULL,
	`sensitivity` text NOT NULL,
	`start_date` text NOT NULL,
	`end_date` text NOT NULL,
	`file_name` text NOT NULL,
	`file_bytes` integer NOT NULL,
	`file_sha256` text NOT NULL,
	`object_key` text NOT NULL,
	`status` text DEFAULT 'submitted' NOT NULL,
	`version` integer DEFAULT 1 NOT NULL,
	`created_at` text NOT NULL,
	`updated_at` text NOT NULL
);
--> statement-breakpoint
CREATE INDEX `idx_submissions_owner_created` ON `data_submissions` (`owner_key`,`created_at`);--> statement-breakpoint
CREATE INDEX `idx_submissions_status_created` ON `data_submissions` (`status`,`created_at`);