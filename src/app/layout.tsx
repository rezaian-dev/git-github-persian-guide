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

export const metadata: Metadata = {
  metadataBase: new URL("https://rezaian-dev.github.io"),
  icons: { icon: `${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/git-logo-64.png` },
  title: "Git و GitHub ۲۰۲۶ | راهنمای فارسی از صفر تا سطح حرفه‌ای",
  description:
    "مرجع فارسی Git ۲.۵۱+ و GitHub ۲۰۲۶ در ۳۶ فصل — مدل ذهنی سه درخت، VS Code Source Control، Pull Request، Actions و Rulesets. رایگان و متن‌باز.",
  openGraph: {
    title: "Git و GitHub ۲۰۲۶ | راهنمای فارسی",
    description:
      "۳۶ فصل، ۱۴۵ صفحه — از مدل ذهنی سه درخت تا Source Control در VS Code و GitHub ۲۰۲۶.",
    url: "https://rezaian-dev.github.io/git-github-persian-guide/",
    siteName: "Persian Developer Handbook",
    images: [{ url: `${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/social-card.jpg`, width: 1280, height: 640 }],
    locale: "fa_IR",
    type: "book",
  },
  twitter: { card: "summary_large_image" },
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
    <html lang="fa" dir="rtl" className={`${vazirmatn.variable} ${jetbrains.variable}`}>
      <body>
        <MotionProvider>{children}</MotionProvider>
      </body>
    </html>
  );
}
