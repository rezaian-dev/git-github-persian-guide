const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

/**
 * Prefix book-figure images with the active basePath so they resolve on both
 * hosts (Vercel serves from "/", GitHub Pages from "/git-github-persian-guide").
 * External links open in a new tab so the reader never loses its place.
 */
export function prepareChapterHtml(html: string): string {
  return html
    .replaceAll('src="/book/', `src="${BASE}/book/`)
    .replace(/<a\s+(?=[^>]*href="https?:)/g, '<a target="_blank" rel="noopener" ');
}

type Props = {
  html: string;
  as?: "article" | "div";
};

/**
 * Renders one chapter of trusted local book content.
 * The content layer stores chapters as HTML strings (text stays selectable);
 * this component is the single place that prepares and mounts them.
 */
export default function ChapterArticle({ html, as = "article" }: Props) {
  const Tag = as;
  return <Tag className="reader" dangerouslySetInnerHTML={{ __html: prepareChapterHtml(html) }} />;
}
