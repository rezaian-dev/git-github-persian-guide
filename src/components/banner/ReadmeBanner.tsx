import GitMark from "@/components/icons/GitMark";
import GitHubIcon from "@/components/icons/GitHubIcon";
import { asset } from "@/lib/links";

/**
 * README hero banner — 1280×640 @1x, exported to 3840×1920 PNG.
 * Rendered by /banner and screenshotted with headless Chromium; no external
 * fonts or scripts involved. Persian text uses Vazirmatn, Latin uses
 * JetBrains Mono (both bundled via next/font in the root layout).
 */
export default function ReadmeBanner() {
  return (
    <div
      id="readme-banner"
      dir="rtl"
      className="relative h-[640px] w-[1280px] overflow-hidden bg-[#0c1122] font-sans text-white"
    >
      {/* backdrop: faint grid + warm/cool glows + quiet branch graph */}
      <div className="bg-grid absolute inset-0 opacity-70" aria-hidden="true" />
      <div
        className="absolute -top-40 right-[-120px] size-[560px] rounded-full bg-[radial-gradient(circle,rgb(255_106_43_/_0.28),transparent_65%)] blur-2xl"
        aria-hidden="true"
      />
      <div
        className="absolute -bottom-48 left-[-100px] size-[520px] rounded-full bg-[radial-gradient(circle,rgb(86_200_250_/_0.14),transparent_65%)] blur-2xl"
        aria-hidden="true"
      />
      <svg
        className="absolute inset-0 size-full"
        viewBox="0 0 1280 640"
        fill="none"
        aria-hidden="true"
      >
        <g stroke="#ff6a2b" strokeOpacity="0.3" strokeWidth="2">
          <path d="M-20 452 C 140 452, 220 428, 380 428" />
          <path d="M200 452 C 260 452, 290 428, 340 428" strokeOpacity="0.2" />
        </g>
        <g fill="#ff6a2b">
          <circle cx="110" cy="452" r="6" fillOpacity="0.5" />
          <circle cx="380" cy="428" r="7" fillOpacity="0.6" />
        </g>
        <g stroke="#56c8fa" strokeOpacity="0.22" strokeWidth="2">
          <path d="M-20 92 C 180 92, 280 118, 470 118" />
        </g>
        <circle cx="470" cy="118" r="6" fill="#56c8fa" fillOpacity="0.45" />
      </svg>

      <div className="relative flex h-full flex-col px-16 pb-9 pt-11">
        {/* main row: copy (start/right) + marks (end/left) */}
        <div className="flex flex-1 items-center gap-10">
          <div className="min-w-0 flex-1">
            <p
              dir="ltr"
              className="flex items-center justify-end gap-3 font-mono text-[15px] font-bold uppercase tracking-[0.32em] text-[#ffc199]"
            >
              <span className="h-[3px] w-10 rounded-full bg-[#ff6a2b]" aria-hidden="true" />
              Persian Developer Handbook
            </p>
            <p className="mt-4 text-[46px] font-extrabold leading-[1.25]">مرجع جامع</p>
            <p dir="ltr" className="mt-1 flex items-center gap-4 text-left font-mono text-[76px] font-extrabold leading-none tracking-tight">
              Git <span className="grad-text">&amp;</span> GitHub
              <span className="rounded-2xl bg-[#ff6a2b] px-4 py-2 font-mono text-[26px] font-bold tracking-normal text-[#24090a]">
                2026
              </span>
            </p>
            <p className="mt-4 text-[23px] font-medium leading-[1.9] text-[#c6cbdb]">
              راهنمای فارسی از صفر تا سطح حرفه‌ای — یک کتاب، دو مسیر: ترمینال و VS Code
            </p>
            <div className="mt-5 flex flex-wrap gap-3">
              {["۳۶ فصل", "۱۴۵ صفحه", "ترمینال + VS Code", "PDF · EPUB · وب"].map((t) => (
                <span
                  key={t}
                  className="rounded-full bg-gradient-to-l from-[#ffdba3] to-[#ff6a2b] px-6 py-2 text-[21px] font-extrabold text-[#24090a]"
                >
                  {t}
                </span>
              ))}
            </div>
          </div>

          {/* official subject marks — unmodified, high contrast */}
          <div className="flex shrink-0 items-center gap-5" dir="ltr">
            <figure className="flex flex-col items-center gap-3">
              <span className="grid size-[148px] place-items-center rounded-[32px] border border-white/40 bg-white shadow-[0_24px_70px_-20px_rgb(0_0_0_/_0.6)]">
                <GitMark className="size-[104px]" />
              </span>
              <figcaption className="font-mono text-[17px] font-bold text-[#a8afc4]">Git</figcaption>
            </figure>
            <span dir="ltr" className="pb-9 font-mono text-[26px] font-bold text-[#5b6378]">
              +
            </span>
            <figure className="flex flex-col items-center gap-3">
              <span className="grid size-[148px] place-items-center rounded-[32px] border border-white/40 bg-white shadow-[0_24px_70px_-20px_rgb(0_0_0_/_0.6)]">
                <GitHubIcon size={96} className="text-black" />
              </span>
              <figcaption className="font-mono text-[17px] font-bold text-[#a8afc4]">
                GitHub
              </figcaption>
            </figure>
          </div>
        </div>

        {/* footer: independent section below a divider */}
        <div className="h-px w-full bg-white/20" data-testid="banner-divider" aria-hidden="true" />
        <div className="flex items-center justify-between pt-7" data-testid="banner-footer">
          <div className="flex items-center gap-4">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={asset("/author.webp")}
              alt=""
              width={640}
              height={640}
              className="size-[68px] rounded-full border-2 border-[#ff6a2b]/70 object-cover"
            />
            <div>
              <p className="text-[25px] font-extrabold leading-snug">محمدرضا رضائیان</p>
              <p className="mt-0.5 text-[17px] font-medium text-[#a8afc4]">
                نویسنده و توسعه‌دهنده · راهنمای مستقل فارسی
              </p>
            </div>
          </div>
          <div className="flex flex-col items-end gap-1.5">
            <p dir="ltr" className="font-mono text-[20px] font-bold text-[#dce0ea]">
              github.com/rezaian-dev
            </p>
            <p className="text-[16px] font-medium text-[#7f879c]">
              CC BY-NC-SA 4.0 · رایگان برای استفادهٔ غیرتجاری
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
