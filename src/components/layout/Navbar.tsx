"use client";

import Link from "next/link";
import { m, AnimatePresence, useScroll, useMotionValueEvent } from "motion/react";
import { useState } from "react";
import { GitBranch, Menu, X, BookOpen } from "lucide-react";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";

const LINKS = [
  { href: "#features", label: "ویژگی‌ها" },
  { href: "#path", label: "مسیر کتاب" },
  { href: "#preview", label: "پیش‌نمایش" },
  { href: "#chapters", label: "فصل‌ها" },
  { href: "#editions", label: "نسخه‌ها" },
  { href: "#series", label: "مجموعه" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [hidden, setHidden] = useState(false);
  const { scrollY } = useScroll();

  useMotionValueEvent(scrollY, "change", (latest) => {
    const prev = scrollY.getPrevious() ?? 0;
    setScrolled(latest > 24);
    setHidden(latest > prev && latest > 220);
  });

  return (
    <m.header
      className={cn(
        "fixed inset-x-0 top-0 z-50 border-b transition-colors duration-300",
        scrolled || open ? "border-border bg-background/80 backdrop-blur-xl" : "border-transparent"
      )}
      animate={{ y: hidden && !open ? "-110%" : "0%" }}
      transition={{ duration: 0.35, ease: "easeInOut" }}
    >
      <nav className="container flex min-h-18 items-center gap-4" aria-label="ناوبری اصلی">
        <Link href="/" className="flex shrink-0 items-center gap-2.5" onClick={() => setOpen(false)}>
          <span className="grid size-10 place-items-center rounded-xl bg-linear-to-br from-gold to-primary shadow-[0_6px_24px_-6px_rgb(255_106_43_/_0.55)]">
            <GitBranch className="size-5 text-primary-foreground" />
          </span>
          <span className="font-mono text-sm font-bold leading-tight">
            Git &amp; GitHub 2026
            <small className="block text-[10.5px] font-medium text-muted-foreground">راهنمای فارسی · ۳۶ فصل</small>
          </span>
        </Link>

        <ul
          className={cn(
            "mx-auto flex-col gap-0.5 rounded-2xl border border-input bg-popover/95 p-2.5 shadow-[0_40px_120px_-20px_rgb(6_10_24_/_0.6)] backdrop-blur-xl",
            "absolute top-[calc(100%+12px)] inset-x-0",
            "lg:static lg:flex lg:flex-row lg:items-center lg:gap-0.5 lg:rounded-none lg:border-0 lg:bg-transparent lg:p-0 lg:shadow-none lg:backdrop-blur-none",
            open ? "flex" : "hidden"
          )}
        >
          {LINKS.map((l) => (
            <li key={l.href}>
              <a
                href={l.href}
                onClick={() => setOpen(false)}
                className="block rounded-lg px-3 py-3 text-sm font-semibold text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground lg:py-2.5"
              >
                {l.label}
              </a>
            </li>
          ))}
        </ul>

        <div className="ms-auto flex items-center gap-2">
          <Button asChild size="sm" className="hidden sm:inline-flex">
            <Link href="/chapters" onClick={() => setOpen(false)}>
              <BookOpen /> مطالعه آنلاین
            </Link>
          </Button>
          <button
            type="button"
            className="grid size-11 place-items-center rounded-xl border border-input bg-secondary/50 text-foreground lg:hidden"
            aria-expanded={open}
            aria-label={open ? "بستن منو" : "بازکردن منو"}
            onClick={() => setOpen((o) => !o)}
          >
            <AnimatePresence mode="wait" initial={false}>
              <m.span
                key={open ? "x" : "m"}
                initial={{ opacity: 0, rotate: -90 }}
                animate={{ opacity: 1, rotate: 0 }}
                exit={{ opacity: 0, rotate: 90 }}
                transition={{ duration: 0.15 }}
                className="grid"
              >
                {open ? <X className="size-5" /> : <Menu className="size-5" />}
              </m.span>
            </AnimatePresence>
          </button>
        </div>
      </nav>
    </m.header>
  );
}
