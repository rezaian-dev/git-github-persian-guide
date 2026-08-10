"use client";

import { useRouter } from "next/navigation";
import { ChevronDown } from "lucide-react";

import { BOOK } from "@/content/book";

const fa = new Intl.NumberFormat("fa-IR");

/** انتخاب‌گر فصل — پرش مستقیم بین ۳۶ فصل کتاب. */
export default function ChapterSelect({ current }: { current: number }) {
  const router = useRouter();

  return (
    <label className="relative flex min-w-0 items-center">
      <span className="sr-only">رفتن به فصل</span>
      <select
        dir="rtl"
        value={current}
        onChange={(e) => router.push(`/book/${e.target.value}`)}
        className="max-w-[46vw] cursor-pointer appearance-none truncate rounded-lg border border-border bg-secondary/60 py-1.5 ps-3 pe-8 text-[12.5px] font-bold text-sub outline-none transition-colors hover:border-primary/40 focus-visible:border-primary/60 sm:max-w-xs md:text-[13px]"
      >
        {BOOK.parts.map((part) => (
          <optgroup key={part.index} label={`${part.name} — ${part.label}`}>
            {part.chapters.map((c) => (
              <option key={c.n} value={c.n}>
                {fa.format(c.n)} — {c.title}
              </option>
            ))}
          </optgroup>
        ))}
      </select>
      <ChevronDown className="pointer-events-none absolute end-2.5 size-3.5 text-muted-foreground" aria-hidden="true" />
    </label>
  );
}
