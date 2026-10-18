const escapeChatData = (value) => value.replaceAll("<|", "< |");
export const CONTINUE_REPLY = "Continue your previous reply from where it stopped. Finish the explanation without repeating it.";

export const renderDiscussionPrompt = ({ system, history = [], context = "", question, assistantPrefix = "" }) =>
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
  "<|im_end|>\n<|im_start|>assistant\n" + escapeChatData(assistantPrefix);

// Older turns may be omitted, but never the original question or partial reply.
export function prepareDiscussionPrompt({system,history=[],context="",question},countTokens) {
  const retained=history.slice();
  let assistantPrefix="",contextTrimmed=false;
  if(question===CONTINUE_REPLY) {
    const previous=retained.pop();
    if(!previous||previous.question===CONTINUE_REPLY)throw Object.assign(new Error("MODEL_CONTEXT_LIMIT"),{code:"MODEL_CONTEXT_LIMIT"});
    question=previous.question;assistantPrefix=previous.reply;
  }
  const render=()=>renderDiscussionPrompt({system,history:retained,context,question,assistantPrefix});
  let prompt=render();
  while(countTokens(prompt)>512&&retained.length) {retained.shift();contextTrimmed=true;prompt=render();}
  if(countTokens(prompt)>512)throw Object.assign(new Error("MODEL_CONTEXT_LIMIT"),{code:"MODEL_CONTEXT_LIMIT"});
  return {prompt,contextTrimmed};
}

