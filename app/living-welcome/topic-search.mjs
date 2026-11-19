// Search navigation metadata only. A match does not establish data availability.
const normalize = value => String(value ?? '').normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase();

export function filterTopics(topics, query, group = 'All') {
  const words = normalize(query).match(/[\p{L}\p{N}]+/gu) ?? [];
  return topics.filter(topic => {
    if (group !== 'All' && topic.group !== group) return false;
    const text = normalize([topic.title, topic.id, topic.group, topic.description,
      ...(topic.facets ?? []), topic.look?.name].join(' '));
    return words.every(word => text.includes(word));
  });
}
