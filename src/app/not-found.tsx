import type { Metadata } from "next";
import Link from "next/link";
import { Compass, House, BookOpen } from "lucide-react";

import Background from "@/components/layout/Background";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { Button } from "@/components/ui/button";

export const metadata: Metadata = {
  title: "صفحه پیدا نشد | Git و GitHub ۲۰۲۶",
  description: "این مسیر در مرجع فارسی Git و GitHub ۲۰۲۶ وجود ندارد.",
};

export default function NotFound() {
  return (
    <>
      <Background />
      <Navbar />
      <main className="container flex min-h-svh flex-col items-center justify-center py-32 text-center">
        <span className="grid size-16 place-items-center rounded-2xl border border-primary/25 bg-primary/10 text-primary-soft">
          <Compass className="size-8" />
        </span>
        <p dir="ltr" className="mt-6 font-mono text-sm font-bold tracking-[0.3em] text-faint">
          404
        </p>
        <h1 className="mt-3 text-[clamp(28px,4.5vw,46px)] font-extrabold leading-tight">
          این شاخه به جایی <span className="grad-text">وصل نیست</span>
        </h1>
        <p className="mt-4 max-w-md text-[15px] leading-8 text-muted-foreground">
          صفحه‌ای که دنبالش می‌گردی وجود ندارد یا جابه‌جا شده است. از همین‌جا به خانه برگرد یا
          مطالعهٔ کتاب را ادامه بده.
        </p>
        <div className="mt-8 flex flex-wrap justify-center gap-3">
          <Button asChild size="lg">
            <Link href="/">
              <House /> بازگشت به خانه
            </Link>
          </Button>
          <Button asChild size="lg" variant="outline">
            <Link href="/book">
              <BookOpen /> مطالعهٔ کتاب
            </Link>
          </Button>
        </div>
      </main>
      <Footer />
    </>
  );
}
