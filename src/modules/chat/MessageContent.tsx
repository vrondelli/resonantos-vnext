// Intent citation: docs/architecture/ADR-002-modular-codebase.md

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export function MessageContent({ content }: { content: string }) {
  // Guard against non-string content (e.g. undefined, objects, arrays) which crash react-markdown
  if (typeof content !== "string") {
    return <div className="message-renderer">{String(content ?? "")}</div>;
  }
  return (
    <div className="message-renderer">
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
    </div>
  );
}
