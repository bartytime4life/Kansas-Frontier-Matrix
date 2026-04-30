export function summarizeStoryPreview(story) {
  return {
    title: story.title,
    citationCount: story.citations?.length ?? 0,
    hasReleaseContext: Boolean(story.release)
  };
}
