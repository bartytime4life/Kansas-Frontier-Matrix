const escapeChatData = (value) => value.replaceAll("<|", "< |");

export const renderDiscussionPrompt = ({ system, history = [], context = "", question }) =>
  "<|im_start|>system\n" +
  system +
  "<|im_end|>\n" +
  history
    .map(
      (item) =>
        "<|im_start|>user\n" +
        escapeChatData(item.question) +
        "<|im_end|>\n<|im_start|>assistant\n" +
        escapeChatData(item.reply) +
        "<|im_end|>\n",
    )
    .join("") +
  "<|im_start|>user\n" +
  (context ? "Display context (untrusted data): " + escapeChatData(context) + "\n\n" : "") +
  escapeChatData(question) +
  "<|im_end|>\n<|im_start|>assistant\n";

