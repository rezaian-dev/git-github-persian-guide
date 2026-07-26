export type Chapter = { n: number; title: string };

export type Part = {
  id: string;
  emoji: string;
  label: string;
  range: string;
  tagline: string;
  outcome: string;
  chapters: Chapter[];
};

export const PARTS: Part[] = [
  {
    id: "part-1",
    emoji: "🌱",
    label: "بنیادها و مدل ذهنی",
    range: "فصل‌های ۱ تا ۱۰",
    tagline: "نصب، سه درخت، اشیاء، شاخه، ادغام، Undo و Source Control از صفر.",
    outcome: "دیگر نمی‌پرسی «این فرمان کدام لایه را عوض کرد؟»",
    chapters: [
      { n: 1, title: "معرفی Git و نقشه راه ۲۰۲۶" },
      { n: 2, title: "نصب و هویت" },
      { n: 3, title: "سه درخت" },
      { n: 4, title: "اولین مخزن" },
      { n: 5, title: "اشیای Git" },
      { n: 6, title: "شاخه‌ها" },
      { n: 7, title: "ادغام و تعارض" },
      { n: 8, title: "Undo" },
      { n: 9, title: "gitignore، attributes، LFS" },
      { n: 10, title: "Source Control از صفر — Ctrl+Shift+G" },
    ],
  },
  {
    id: "part-2",
    emoji: "🔁",
    label: "کار روزانه، VS Code و GitHub",
    range: "فصل‌های ۱۱ تا ۲۲",
    tagline: "Graph تا PR، remote، fork، Code Review، gh و Conventional Commits.",
    outcome: "همکاری واقعی روی GitHub بدون حدس زدن UI.",
    chapters: [
      { n: 11, title: "Source Control فوق‌پیشرفته" },
      { n: 12, title: "diff، log، blame، bisect" },
      { n: 13, title: "stash، worktree، sparse-checkout" },
      { n: 14, title: "Remote" },
      { n: 15, title: "ریپوی GitHub" },
      { n: 16, title: "Clone، Fork و Upstream" },
      { n: 17, title: "Pull Request" },
      { n: 18, title: "Code Review" },
      { n: 19, title: "GitHub CLI" },
      { n: 20, title: "Issues و Projects" },
      { n: 21, title: "استراتژی شاخه" },
      { n: 22, title: "Conventional Commits" },
    ],
  },
  {
    id: "part-3",
    emoji: "🚀",
    label: "پیشرفته، امنیت و CI",
    range: "فصل‌های ۲۳ تا ۳۲",
    tagline: "rebase، hooks، امضا، Rulesets، Actions و زنجیرهٔ تأمین.",
    outcome: "سیاست تیم و کیفیت Production.",
    chapters: [
      { n: 23, title: "Rebase تعاملی" },
      { n: 24, title: "Cherry-pick و rerere" },
      { n: 25, title: "Hooks" },
      { n: 26, title: "امضا و راز" },
      { n: 27, title: "Rulesets" },
      { n: 28, title: "GitHub Actions" },
      { n: 29, title: "امنیت زنجیرهٔ تأمین" },
      { n: 30, title: "داخلی Git" },
      { n: 31, title: "مخازن بزرگ" },
      { n: 32, title: "Copilot و Coding Agent" },
    ],
  },
  {
    id: "part-4",
    emoji: "🏁",
    label: "کارگاه و آمادگی شغلی",
    range: "فصل‌های ۳۳ تا ۳۶",
    tagline: "نکات، چهار مینی‌پروژه، اشتباهات رایج و مصاحبه.",
    outcome: "تثبیت مهارت و آمادگی مصاحبه.",
    chapters: [
      { n: 33, title: "۳۰ نکته طلایی" },
      { n: 34, title: "کارگاه چهار مینی‌پروژه" },
      { n: 35, title: "۲۰ اشتباه رایج" },
      { n: 36, title: "مصاحبه، واژه‌نامه و نقشه راه" },
    ],
  },
];

export const TOTAL_CHAPTERS = PARTS.reduce((sum, p) => sum + p.chapters.length, 0);
