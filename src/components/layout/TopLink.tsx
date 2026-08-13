"use client";

/** "Back to top" that works on every route — no #top anchor needed. */
export default function TopLink() {
  return (
    <button
      type="button"
      onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
      className="cursor-pointer text-sub transition-colors hover:text-primary-soft"
    >
      بازگشت به بالا ↑
    </button>
  );
}
