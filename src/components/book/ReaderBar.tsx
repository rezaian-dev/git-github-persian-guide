import Link from "next/link";
import { BookOpen, Download, ArrowRight } from "lucide-react";

import ChapterSelect from "@/components/book/ChapterSelect";
import { PDF_URL } from "@/lib/links";

/** نوار بالای صفحهٔ مطالعه — ناوبری کتاب، انتخاب فصل و دانلود. */
export default function ReaderBar({ current }: { current: number }) {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex h-14 w-full max-w-6xl items-center justify-between gap-3 px-4 md:px-5">
        <Link
          href="/book"
          className="flex min-w-0 items-center gap-2.5 text-sm font-extrabold text-foreground transition-colors hover:text-primary-soft"
        >
          <span className="grid size-8 shrink-0 place-items-center rounded-lg border border-primary/25 bg-primary/10 text-primary-soft">
            <BookOpen className="size-4" />
          </span>
          <span className="hidden truncate sm:block">Git و GitHub ۲۰۲۶</span>
          <span dir="ltr" className="truncate font-mono text-[11px] font-bold text-faint sm:hidden">
            Git&nbsp;2026
          </span>
        </Link>

        <ChapterSelect current={current} />

        <nav className="flex shrink-0 items-center gap-1.5" aria-label="ناوبری ریدر">
          <Link
            href="/"
            title="بازگشت به سایت"
            aria-label="بازگشت به سایت"
            className="grid size-9 place-items-center rounded-lg border border-border bg-secondary/40 text-sub transition-colors hover:border-primary/40 hover:text-primary-soft"
          >
            <ArrowRight className="size-4" />
          </Link>
          <a
            href={PDF_URL}
            download
            title="دانلود PDF"
            aria-label="دانلود PDF"
            className="grid size-9 place-items-center rounded-lg border border-border bg-secondary/40 text-sub transition-colors hover:border-primary/40 hover:text-primary-soft"
          >
            <Download className="size-4" />
          </a>
        </nav>
      </div>
    </header>
  );
}
