import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { BookOpen, ChevronLeft, ChevronRight } from "lucide-react";

import Background from "@/components/layout/Background";
import ReaderBar from "@/components/book/ReaderBar";
import { BOOK, CHAPTERS, CLOSING_HTML, chapterByN } from "@/content/book";
import "../reader.css";

const fa = new Intl.NumberFormat("fa-IR");

/** مسیرهای فصل‌ها با basePath سازگار می‌شوند؛ تصاویر کتاب را همین‌جا پیشوندگذاری می‌کنیم. */
const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

function withBase(html: string): string {
  return html.replaceAll('src="/book/', `src="${BASE}/book/`);
}

export function generateStaticParams() {
  return CHAPTERS.map((c) => ({ n: String(c.n) }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ n: string }>;
}): Promise<Metadata> {
  const { n } = await params;
  const ch = chapterByN(Number(n));
  if (!ch) return {};
  return {
    title: `${ch.label} | Git و GitHub ۲۰۲۶`,
    description: `${ch.title} — فصل ${fa.format(ch.n)} از ${fa.format(BOOK.totalChapters)} فصل مرجع فارسی Git و GitHub ۲۰۲۶. رایگان و متن‌باز.`,
  };
}

export default async function ChapterPage({
  params,
}: {
  params: Promise<{ n: string }>;
}) {
  const { n } = await params;
  const ch = chapterByN(Number(n));
  if (!ch) notFound();

  const idx = CHAPTERS.findIndex((c) => c.n === ch.n);
  const prev = idx > 0 ? CHAPTERS[idx - 1] : null;
  const next = idx < CHAPTERS.length - 1 ? CHAPTERS[idx + 1] : null;
  const part = BOOK.parts[ch.part];

  return (
    <div className="relative min-h-dvh">
      <Background />
      <ReaderBar current={ch.n} />

      <main className="mx-auto w-full max-w-[860px] px-4 pb-20 pt-8 md:px-5 md:pt-12">
        <nav dir="rtl" className="mb-6 flex flex-wrap items-center gap-x-2 gap-y-1 text-[11.5px] font-mono text-faint" aria-label="مسیر">
          <Link href="/" className="transition-colors hover:text-primary-soft">
            سایت
          </Link>
          <span aria-hidden="true">/</span>
          <Link href="/book" className="transition-colors hover:text-primary-soft">
            کتاب
          </Link>
          <span aria-hidden="true">/</span>
          <span className="text-primary-soft">
            {part.name} · {part.label}
          </span>
        </nav>

        <header className="mb-10 flex items-start gap-4 border-b-2 border-primary pb-7 md:gap-5">
          <span
            dir="ltr"
            aria-hidden="true"
            className="select-none pt-1 font-mono text-[clamp(34px,6vw,52px)] font-extrabold leading-none text-transparent [-webkit-text-stroke:1.5px_rgb(255_106_43_/_0.65)]"
          >
            {ch.num}
          </span>
          <div className="min-w-0">
            <p className="mb-1.5 text-[12px] font-bold text-primary-soft">{ch.label}</p>
            <h1 className="text-[clamp(21px,3.4vw,29px)] font-extrabold leading-[1.6] text-foreground">
              {ch.title}
            </h1>
          </div>
        </header>

        <article className="reader" dangerouslySetInnerHTML={{ __html: withBase(ch.html) }} />

        {ch.n === BOOK.totalChapters && (
          <div className="reader" dangerouslySetInnerHTML={{ __html: withBase(CLOSING_HTML) }} />
        )}

        <nav dir="rtl" className="mt-14 grid gap-3 sm:grid-cols-2" aria-label="فصل قبل و بعد">
          {prev ? (
            <Link
              href={`/book/${prev.n}`}
              className="group flex items-center gap-3 rounded-2xl border border-border bg-card/70 px-4 py-3.5 transition-colors hover:border-primary/40 hover:bg-secondary/40"
            >
              <ChevronRight className="size-5 shrink-0 text-primary-soft" />
              <span className="min-w-0">
                <span className="block text-[11px] font-mono text-faint">فصل قبل — {fa.format(prev.n)}</span>
                <span className="block truncate text-[13.5px] font-bold text-sub transition-colors group-hover:text-foreground">
                  {prev.title}
                </span>
              </span>
            </Link>
          ) : (
            <span aria-hidden="true" className="hidden sm:block" />
          )}

          {next ? (
            <Link
              href={`/book/${next.n}`}
              className="group flex items-center justify-end gap-3 rounded-2xl border border-primary/25 bg-primary/[0.07] px-4 py-3.5 text-left transition-colors hover:border-primary/50 hover:bg-primary/[0.12]"
            >
              <span className="min-w-0">
                <span className="block text-[11px] font-mono text-faint">فصل بعد — {fa.format(next.n)}</span>
                <span className="block truncate text-[13.5px] font-bold text-sub transition-colors group-hover:text-foreground">
                  {next.title}
                </span>
              </span>
              <ChevronLeft className="size-5 shrink-0 text-primary-soft" />
            </Link>
          ) : (
            <Link
              href="/book"
              className="group flex items-center justify-end gap-3 rounded-2xl border border-primary/25 bg-primary/[0.07] px-4 py-3.5 transition-colors hover:border-primary/50 hover:bg-primary/[0.12]"
            >
              <span className="min-w-0">
                <span className="block text-[11px] font-mono text-faint">پایان کتاب</span>
                <span className="block text-[13.5px] font-bold text-sub transition-colors group-hover:text-foreground">
                  بازگشت به فهرست
                </span>
              </span>
              <BookOpen className="size-5 shrink-0 text-primary-soft" />
            </Link>
          )}
        </nav>

        <p className="mt-10 text-center text-[11.5px] text-faint">
          فصل {fa.format(ch.n)} از {fa.format(BOOK.totalChapters)} · {BOOK.title} · ویرایش {BOOK.version}
        </p>
      </main>
    </div>
  );
}
