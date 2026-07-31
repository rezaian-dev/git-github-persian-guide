/**
 * Two build targets share this config:
 *
 *   npm run build        → Vercel / Node (no basePath, server features available)
 *   npm run build:pages  → static export for GitHub Pages under /git-github-persian-guide
 *
 * PAGES_BUILD=1 switches on `output: "export"` + basePath so the same source
 * ships to both hosts without hand-editing anything.
 */
const isPages = process.env.PAGES_BUILD === "1";
const basePath = isPages ? "/git-github-persian-guide" : "";

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,

  ...(isPages && {
    output: "export",
    basePath,
    // GitHub Pages has no image optimizer.
    images: { unoptimized: true },
  }),

  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },

  // The HTML edition is a static file at public/book/index.html and its
  // assets (figures/, fonts/) are referenced RELATIVELY. That only resolves
  // when the browser URL keeps its trailing slash — on /book the relative
  // "figures/x.svg" would resolve to /figures/x.svg and 404.
  //
  // Next redirects /book/ -> /book by default, so force trailing slashes and
  // rewrite the directory URL onto the real file.
  trailingSlash: true,

  ...(!isPages && {
    async rewrites() {
      return [{ source: "/book/", destination: "/book/index.html" }];
    },
  }),

  // Dev-only: allow the sandbox preview proxy origins.
  allowedDevOrigins: ["*.e2b.app", "*.e2b.dev", "localhost", "127.0.0.1"],
};

export default nextConfig;
