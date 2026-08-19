import type { Metadata, Viewport } from "next";
import localFont from "next/font/local";
import MotionProvider from "@/components/providers/MotionProvider";
import "./globals.css";

const vazirmatn = localFont({
  src: [
    { path: "../fonts/Vazirmatn-Regular.woff2", weight: "400" },
    { path: "../fonts/Vazirmatn-Medium.woff2", weight: "500" },
    { path: "../fonts/Vazirmatn-Bold.woff2", weight: "700" },
    { path: "../fonts/Vazirmatn-ExtraBold.woff2", weight: "800" },
  ],
  variable: "--font-vazirmatn",
  display: "swap",
});

const jetbrains = localFont({
  src: [
    { path: "../fonts/JetBrainsMono-Regular.woff2", weight: "400" },
    { path: "../fonts/JetBrainsMono-Bold.woff2", weight: "700" },
  ],
  variable: "--font-jetbrains",
  display: "swap",
});

const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export const metadata: Metadata = {
  metadataBase: new URL("https://rezaian-dev.github.io"),
  icons: {
    icon: [
      { url: `${BASE}/favicon.ico`, sizes: "48x48" },
      { url: `${BASE}/git-logo-64.png`, sizes: "64x64", type: "image/png" },
      { url: `${BASE}/favicon.svg`, type: "image/svg+xml" },
    ],
    apple: [{ url: `${BASE}/icon-180.png`, sizes: "180x180" }],
  },
  title: "Git و GitHub ۲۰۲۶ | راهنمای فارسی از صفر تا سطح حرفه‌ای",
  description:
    "مرجع فارسی Git ۲.۵۱+ و GitHub ۲۰۲۶ در ۳۶ فصل — مدل ذهنی سه درخت، VS Code Source Control، Pull Request، Actions و Rulesets. رایگان برای مطالعه و استفادهٔ غیرتجاری.",
  openGraph: {
    title: "Git و GitHub ۲۰۲۶ | راهنمای فارسی",
    description:
      "۳۶ فصل، ۱۴۵ صفحه — از مدل ذهنی سه درخت تا Source Control در VS Code و GitHub ۲۰۲۶.",
    url: "https://rezaian-dev.github.io/git-github-persian-guide/",
    siteName: "Persian Developer Handbook",
    images: [
      {
        url: "https://rezaian-dev.github.io/git-github-persian-guide/social-card.jpg",
        width: 1280,
        height: 640,
        alt: "Git و GitHub ۲۰۲۶ — مرجع فارسی",
      },
    ],
    locale: "fa_IR",
    type: "book",
  },
  twitter: {
    card: "summary_large_image",
    images: ["https://rezaian-dev.github.io/git-github-persian-guide/social-card.jpg"],
  },
};

export const viewport: Viewport = {
  themeColor: "#131829",
  colorScheme: "dark",
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="fa"
      dir="rtl"
      data-scroll-behavior="smooth"
      className={`${vazirmatn.variable} ${jetbrains.variable}`}
    >
      <body>
        <MotionProvider>{children}</MotionProvider>
      </body>
    </html>
  );
}
