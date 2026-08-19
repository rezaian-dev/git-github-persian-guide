/**
 * Central place for every outbound/asset URL.
 *
 * Why this exists: the site ships to two hosts.
 *   - Vercel / local  → served from "/"
 *   - GitHub Pages    → served from "/git-github-persian-guide"
 *
 * `next/link` prefixes basePath automatically, so route helpers below return
 * plain paths. Plain <a> / <img> and `next/image` with `unoptimized: true`
 * (the Pages export has no image optimizer, so the file path passes through
 * untouched) do NOT get a prefix — use `asset()` for those so downloads and
 * images never 404 on Pages. Never combine `asset()` with `next/link`.
 */

const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

/** Prefix a public/ asset with the active basePath. */
export function asset(path: string): string {
  const clean = path.startsWith("/") ? path : `/${path}`;
  return `${BASE}${clean}`;
}

/** Canonical origin of the published site. */
export const SITE_URL = "https://rezaian-dev.github.io/git-github-persian-guide";

/**
 * The online reader — a native part of this Next.js app (`/book`).
 * Use with `next/link` only: it prefixes the basePath by itself.
 */
export const BOOK_URL = "/book";

/** Deep-link to a single chapter inside the reader (use with `next/link`). */
export function chapterUrl(n: number): string {
  return `/book/${n}`;
}

export const PDF_URL = asset("/pdf/Git-GitHub-Persian-Guide.pdf");
export const EPUB_URL = asset("/pdf/Git-GitHub-Persian-Guide.epub");

export const REPO_URL = "https://github.com/rezaian-dev/git-github-persian-guide";
export const ISSUES_URL = `${REPO_URL}/issues`;
export const AUTHOR_URL = "https://github.com/rezaian-dev";
