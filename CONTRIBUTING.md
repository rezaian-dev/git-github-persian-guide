<div dir="rtl">

# 🛠️ راهنمای توسعه‌دهندگان

این مخزن یک اپلیکیشن خالص **Next.js (App Router + TypeScript + Tailwind)** است: متن هر ۳۶ فصل به‌صورت ماژول‌های محتوا در `src/content/chapters` نگهداری می‌شود و ریدر آنلاین (`/book`) آن‌ها را رندر می‌کند. خروجی‌های آمادهٔ PDF و EPUB در `public/pdf` قرار دارند و شکل‌های کتاب در `public/book/figures`.

## اجرای محلی

نیازمند Node.js ۲۰.۹+ :

```bash
git clone https://github.com/rezaian-dev/git-github-persian-guide.git
cd git-github-persian-guide
npm install
npm run dev          # http://localhost:3000
npm run build        # بیلد پروداکشن (Vercel)
npm run build:pages  # خروجی استاتیک در out/ (GitHub Pages)
```

## انتشار

- **GitHub Pages** توسط [GitHub Action](.github/workflows/deploy-pages.yml) منتشر می‌شود: با هر پوش به `master`، بیلد استاتیک گرفته و مستقیم دیپلوی می‌شود — هیچ فایل خروجی‌ای در مخزن کامیت نمی‌شود. کافی است در Settings → Pages گزینهٔ **Source** روی `GitHub Actions` باشد.
- **Vercel**: اپلیکیشن در ریشهٔ مخزن قرار دارد و Vercel آن را به‌صورت خودکار تشخیص می‌دهد؛ کافی است مخزن را Import و Deploy کنید.

## بنر README

بنر (`assets/readme/readme-hero.png`) با کامپوننت `src/components/banner/ReadmeBanner.tsx` ساخته و از مسیر `/banner` با مرورگر headless در ابعاد ۳۸۴۰×۱۹۲۰ اکسپورت می‌شود. نشان Git و GitHub استفاده‌شده نسخه‌های رسمی‌اند (جزئیات در README، بخش «سپاس و نشان‌ها»)؛ هنگام ویرایش، آن‌ها را تحریف یا با نشان دیگری جایگزین نکنید.

## مشارکت

مشارکت شما خوش‌آمد است 🙌 — Pull Request بهتر است کوچک، متمرکز و با دلیل تغییر باشد. فرمان‌های آموزشی داخل متن کتاب (مثل `reset` یا `rebase`) را روی این مخزن اجرا نکنید.

</div>
