import type { Metadata } from "next";

import ReadmeBanner from "@/components/banner/ReadmeBanner";

export const metadata: Metadata = {
  title: "بنر",
  robots: { index: false, follow: false },
};

/**
 * Banner export stage — renders nothing but the 1280×640 artwork so it can
 * be screenshotted to PNG. Not linked from anywhere in the site.
 */
export default function BannerPage() {
  return (
    <main className="grid min-h-dvh place-items-center bg-[#05070f] p-8">
      <ReadmeBanner />
    </main>
  );
}
