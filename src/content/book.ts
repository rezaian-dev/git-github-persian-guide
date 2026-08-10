// نمای کل کتاب — تبدیل‌شده از نسخهٔ HTML؛ فایل تولیدشده، ویرایش دستی لازم نیست.
// Book index — generated from the HTML edition; generated file.

import type { ReaderChapter } from "./types";

import ch01 from "./chapters/ch-01";
import ch02 from "./chapters/ch-02";
import ch03 from "./chapters/ch-03";
import ch04 from "./chapters/ch-04";
import ch05 from "./chapters/ch-05";
import ch06 from "./chapters/ch-06";
import ch07 from "./chapters/ch-07";
import ch08 from "./chapters/ch-08";
import ch09 from "./chapters/ch-09";
import ch10 from "./chapters/ch-10";
import ch11 from "./chapters/ch-11";
import ch12 from "./chapters/ch-12";
import ch13 from "./chapters/ch-13";
import ch14 from "./chapters/ch-14";
import ch15 from "./chapters/ch-15";
import ch16 from "./chapters/ch-16";
import ch17 from "./chapters/ch-17";
import ch18 from "./chapters/ch-18";
import ch19 from "./chapters/ch-19";
import ch20 from "./chapters/ch-20";
import ch21 from "./chapters/ch-21";
import ch22 from "./chapters/ch-22";
import ch23 from "./chapters/ch-23";
import ch24 from "./chapters/ch-24";
import ch25 from "./chapters/ch-25";
import ch26 from "./chapters/ch-26";
import ch27 from "./chapters/ch-27";
import ch28 from "./chapters/ch-28";
import ch29 from "./chapters/ch-29";
import ch30 from "./chapters/ch-30";
import ch31 from "./chapters/ch-31";
import ch32 from "./chapters/ch-32";
import ch33 from "./chapters/ch-33";
import ch34 from "./chapters/ch-34";
import ch35 from "./chapters/ch-35";
import ch36 from "./chapters/ch-36";

export const CHAPTERS: ReaderChapter[] = [
  ch01,
  ch02,
  ch03,
  ch04,
  ch05,
  ch06,
  ch07,
  ch08,
  ch09,
  ch10,
  ch11,
  ch12,
  ch13,
  ch14,
  ch15,
  ch16,
  ch17,
  ch18,
  ch19,
  ch20,
  ch21,
  ch22,
  ch23,
  ch24,
  ch25,
  ch26,
  ch27,
  ch28,
  ch29,
  ch30,
  ch31,
  ch32,
  ch33,
  ch34,
  ch35,
  ch36,
];

export function chapterByN(n: number): ReaderChapter | undefined {
  return CHAPTERS.find((c) => c.n === n);
}

export type BookPartMeta = {
  index: number;
  name: string;
  label: string;
  chapters: { n: number; num: string; title: string; label: string }[];
};

export const BOOK_PARTS: BookPartMeta[] = [
  {
    index: 0,
    name: "بخش یکم",
    label: "بنیادها و مدل ذهنی Git",
    chapters: [
    { n: 1, num: "01", title: "معرفی Git و نقشه راه ۲۰۲۶ — از صفر تا Senior", label: "فصل ۱ · معرفی Git و نقشه راه" },
    { n: 2, num: "02", title: "نصب و هویت — ستاپ حرفه‌ای Git در ۲۰۲۶", label: "فصل ۲ · نصب و هویت" },
    { n: 3, num: "03", title: "سه درخت — Working Tree، Index و Repository", label: "فصل ۳ · سه درخت Git" },
    { n: 4, num: "04", title: "اولین مخزن — init تا log", label: "فصل ۴ · اولین مخزن" },
    { n: 5, num: "05", title: "اشیای Git — blob، tree، commit و hash", label: "فصل ۵ · اشیای Git" },
    { n: 6, num: "06", title: "شاخه‌ها — اشاره‌گر، نه کپی", label: "فصل ۶ · شاخه‌ها" },
    { n: 7, num: "07", title: "ادغام — fast-forward، merge commit و تعارض", label: "فصل ۷ · ادغام و تعارض" },
    { n: 8, num: "08", title: "Undo — restore، reset، revert و reflog", label: "فصل ۸ · Undo در Git" },
    { n: 9, num: "09", title: "نادیده‌گرفتن و فایل بزرگ — gitignore، attributes، LFS", label: "فصل ۹ · gitignore و LFS" },
    { n: 10, num: "10", title: "Source Control از صفر — Ctrl+Shift+G", label: "فصل ۱۰ · Source Control از صفر" },
    ],
  },
  {
    index: 1,
    name: "بخش دوم",
    label: "کار روزانه، VS Code و GitHub",
    chapters: [
    { n: 11, num: "11", title: "Source Control فوق‌پیشرفته — Graph تا PR", label: "فصل ۱۱ · Source Control پیشرفته" },
    { n: 12, num: "12", title: "دیدن تغییر — diff، log، blame و bisect", label: "فصل ۱۲ · diff و log" },
    { n: 13, num: "13", title: "کار موازی — stash، worktree و sparse-checkout", label: "فصل ۱۳ · stash و worktree" },
    { n: 14, num: "14", title: "Remote — fetch، pull، push و tracking", label: "فصل ۱۴ · Remote" },
    { n: 15, num: "15", title: "GitHub — ریپو، README و چهرهٔ عمومی پروژه", label: "فصل ۱۵ · ریپوی GitHub" },
    { n: 16, num: "16", title: "Clone، Fork و Upstream — ورود به کد دیگران", label: "فصل ۱۶ · Clone و Fork" },
    { n: 17, num: "17", title: "Pull Request — دروازهٔ کیفیت تیم", label: "فصل ۱۷ · Pull Request" },
    { n: 18, num: "18", title: "Code Review — فرهنگ، نه گیر دادن", label: "فصل ۱۸ · Code Review" },
    { n: 19, num: "19", title: "GitHub CLI — gh به‌جای کلیک اضافه", label: "فصل ۱۹ · GitHub CLI" },
    { n: 20, num: "20", title: "Issues، Projects و Discussions — کار تیمی روی GitHub", label: "فصل ۲۰ · Issues و Projects" },
    { n: 21, num: "21", title: "استراتژی شاخه — GitHub Flow تا Trunk-Based", label: "فصل ۲۱ · استراتژی شاخه" },
    { n: 22, num: "22", title: "Conventional Commits — پیام به‌عنوان API", label: "فصل ۲۲ · Conventional Commits" },
    ],
  },
  {
    index: 2,
    name: "بخش سوم",
    label: "پیشرفته، امنیت، CI و Production",
    chapters: [
    { n: 23, num: "23", title: "Rebase تعاملی — بازنویسی تاریخچه مثل مجسمه‌ساز", label: "فصل ۲۳ · Rebase تعاملی" },
    { n: 24, num: "24", title: "Cherry-pick، revert پیشرفته و rerere", label: "فصل ۲۴ · Cherry-pick و rerere" },
    { n: 25, num: "25", title: "Hooks و کیفیت کامیت — lint قبل از push", label: "فصل ۲۵ · Hooks" },
    { n: 26, num: "26", title: "هویت و راز — امضا، 2FA، passkey و secret", label: "فصل ۲۶ · امضا و امنیت هویت" },
    { n: 27, num: "27", title: "Rulesets — سیاست شاخه در سطح سازمان", label: "فصل ۲۷ · Rulesets" },
    { n: 28, num: "28", title: "GitHub Actions — از رویداد تا استقرار", label: "فصل ۲۸ · GitHub Actions" },
    { n: 29, num: "29", title: "امنیت زنجیرهٔ تأمین — Dependabot، CodeQL، Secret Scanning", label: "فصل ۲۹ · امنیت زنجیره تأمین" },
    { n: 30, num: "30", title: "داخلی Git — packfile، gc، fsck و reftable", label: "فصل ۳۰ · داخلی Git" },
    { n: 31, num: "31", title: "مخازن بزرگ — partial clone، Scalar و monorepo", label: "فصل ۳۱ · مخازن بزرگ" },
    { n: 32, num: "32", title: "Copilot و Coding Agent — Git در عصر عامل‌ها", label: "فصل ۳۲ · Copilot و Agent" },
    ],
  },
  {
    index: 3,
    name: "بخش چهارم",
    label: "کارگاه، نکات طلایی و مصاحبه",
    chapters: [
    { n: 33, num: "33", title: "۳۰ نکته و ترفند طلایی Git و GitHub", label: "فصل ۳۳ · ۳۰ نکته طلایی" },
    { n: 34, num: "34", title: "کارگاه — چهار مینی‌پروژه از صفر تا PR", label: "فصل ۳۴ · کارگاه عملی" },
    { n: 35, num: "35", title: "۲۰ اشتباه رایج و راه‌حل", label: "فصل ۳۵ · ۲۰ اشتباه رایج" },
    { n: 36, num: "36", title: "مصاحبه، واژه‌نامه و نقشه راه بعد از کتاب", label: "فصل ۳۶ · مصاحبه و واژه‌نامه" },
    ],
  }
];

export const BOOK = {
  title: "مرجع جامع و حرفه‌ای Git و GitHub",
  author: "محمدرضا رضائیان",
  description: "مرجع فارسی Git و GitHub ۲۰۲۶ — از صفر تا سطح فوق‌پیشرفته با تمرکز روی VS Code",
  version: "1.0.0",
  totalChapters: CHAPTERS.length,
  parts: BOOK_PARTS,
};

export const CLOSING_HTML = "<div class=\"closing-card\">\n    <div class=\"closing-kicker\">پایان مرجع</div>\n    <h1>حالا تاریخچه را تو می‌نویسی 🚀</h1>\n    <p>اگر این کتاب برایتان مفید بود، آن را با تیم‌تان به اشتراک بگذارید. Git فقط فرمان نیست؛ مدل ذهنی زمان، همکاری و کیفیت است.</p>\n    <div class=\"closing-tags\"><span>Git 2.51+</span><span>GitHub 2026</span><span>VS Code</span><span>Actions</span><span>Rulesets</span></div>\n    <div class=\"closing-links\">\n      <div><span class=\"lbl\">گیت‌هاب</span><a class=\"ltr\" href=\"https://github.com/rezaian-dev\">github.com/rezaian-dev</a></div>\n      <div><span class=\"lbl\">مرجع JavaScript</span><a class=\"ltr\" href=\"https://github.com/rezaian-dev/javascript-persian-guide\">javascript-persian-guide</a></div>\n    </div>\n    <div class=\"closing-author\">گردآوری و تدوین حرفه‌ای · نسخه ۲۰۲۶ · ویرایش ۱.۰.۰</div>\n  </div>";
