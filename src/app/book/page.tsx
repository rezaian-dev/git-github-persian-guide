import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, BookOpen, Download, ListTree } from "lucide-react";

import Background from "@/components/layout/Background";
import ScrollProgress from "@/components/layout/ScrollProgress";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { PARTS } from "@/lib/chapters";
import { PDF_URL } from "@/lib/links";
import { BOOK } from "@/content/book";

const fa = new Intl.NumberFormat("fa-IR");

export const metadata: Metadata = {
  title: "کتاب آنلاین | Git و GitHub ۲۰۲۶",
  description:
    "مطالعهٔ آنلاین هر ۳۶ فصل مرجع فارسی Git و GitHub ۲۰۲۶ — راست‌به‌چپ، رایگان و بدون نیاز به دانلود.",
};

export default function BookHomePage() {
  return (
    <>
      <Background />
      <ScrollProgress />
      <Navbar />

      <main className="container pb-24 pt-32 md:pt-36">
        <header className="mx-auto mb-16 max-w-2xl text-center">
          <span
            dir="ltr"
            className="mb-4 flex items-center justify-center gap-2.5 font-mono text-[11px] font-bold uppercase tracking-[0.24em] text-primary-soft"
          >
            <i className="h-px w-6 bg-primary shadow-[0_0_12px_var(--color-primary)]" aria-hidden="true" />
            Online reader
          </span>
          <h1 className="text-[clamp(30px,4.6vw,50px)] font-extrabold leading-tight">
            کتاب را <span className="grad-text">اینجا بخوان</span>
          </h1>
          <p className="mt-4 text-base leading-8 text-muted-foreground">
            کل {fa.format(BOOK.totalChapters)} فصل مرجع، همین‌جا در مرورگر — راست‌به‌چپ، با بلوک‌های کد رنگی،
            جدول‌ها و شکل‌ها. فصلی را انتخاب کن یا از ابتدا شروع کن.
          </p>
          <div className="mt-7 flex flex-wrap justify-center gap-3">
            <Button asChild size="lg">
              <Link href="/book/1">
                <BookOpen /> شروع مطالعه
              </Link>
            </Button>
            <Button asChild variant="outline" size="lg">
              <a href={PDF_URL} download>
                <Download /> دانلود PDF
              </a>
            </Button>
          </div>
        </header>

        <div className="mx-auto grid max-w-4xl gap-3.5">
          {BOOK.parts.map((part) => {
            const meta = PARTS[part.index];
            return (
              <Card key={part.index} className="gap-0 p-0">
                <div className="flex items-center gap-4 px-5 py-5 md:px-6">
                  <span className="grid size-11 shrink-0 place-items-center rounded-xl border border-primary/20 bg-linear-to-br from-primary/15 to-sky/10 text-xl">
                    {meta?.emoji ?? "📘"}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block text-base font-extrabold md:text-[17px]">
                      {part.name} · {part.label}
                    </span>
                    <span className="mt-0.5 block text-xs text-primary-soft">{meta?.tagline ?? meta?.range}</span>
                  </span>
                  <span dir="ltr" className="hidden shrink-0 font-mono text-xs text-muted-foreground sm:block">
                    {part.chapters.length} chapters
                  </span>
                </div>
                <CardContent className="grid gap-1.5 sm:grid-cols-2">
                  {part.chapters.map((c) => (
                    <Link
                      key={c.n}
                      href={`/book/${c.n}`}
                      className="flex items-center gap-3 rounded-xl border border-transparent px-3.5 py-2.5 transition-colors hover:border-border hover:bg-secondary/40"
                    >
                      <span
                        dir="ltr"
                        className="grid size-7 shrink-0 place-items-center rounded-lg border border-primary/20 bg-primary/10 font-mono text-[11px] font-bold text-primary-soft"
                      >
                        {c.num}
                      </span>
                      <span className="text-[13.5px] text-sub">{c.title}</span>
                    </Link>
                  ))}
                </CardContent>
              </Card>
            );
          })}
        </div>

        <div className="mt-10 flex justify-center">
          <Button asChild variant="outline">
            <Link href="/chapters">
              <ListTree /> نمای تفصیلی فصل‌ها
              <ArrowRight />
            </Link>
          </Button>
        </div>
      </main>

      <Footer />
    </>
  );
}
