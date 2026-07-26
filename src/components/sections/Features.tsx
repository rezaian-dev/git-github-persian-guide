"use client";

import { Layers, Code2, GitBranch, ShieldCheck, GraduationCap } from "lucide-react";

import SectionHeader from "@/components/layout/SectionHeader";
import Reveal from "@/components/motion/Reveal";
import TiltCard from "@/components/motion/TiltCard";
import GitHubIcon from "@/components/icons/GitHubIcon";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const FEATURES = [
  { icon: Layers, title: "مدل ذهنی، نه حفظ API", text: "Working Tree، Index و HEAD را طوری می‌فهمی که `switch` و `rebase` دیگر رمز نباشند." },
  { icon: Code2, title: "دو مسیر: CLI و VS Code", text: "هر مهارت یک‌بار در ترمینال و یک‌بار با کلیک‌های دقیق در پنل `Ctrl+Shift+G`." },
  { icon: GitHubIcon, title: "GitHub ۲۰۲۶", text: "Flow، Rulesets، Actions، Dependabot، CodeQL و Coding Agent." },
  { icon: GitBranch, title: "مسیر رسمی ۲۰۲۶", text: "`git switch` و `git restore` به‌جای `checkout` دوچهره؛ آزمایش‌شده روی Git ۲.۴۷+." },
  { icon: ShieldCheck, title: "امنیت زنجیرهٔ تأمین", text: "امضا، رازها، Rulesets و اسکن وابستگی از commit تا Production." },
  { icon: GraduationCap, title: "کارگاه و مصاحبه", text: "چهار مینی‌پروژه، بیست اشتباه رایج و واژه‌نامهٔ آمادگی مصاحبه." },
];

export default function Features() {
  return (
    <section className="py-24 md:py-32" id="features">
      <div className="container">
        <SectionHeader
          eyebrow="Why this guide"
          title={<>برای <span className="grad-text">تسلط واقعی</span>، نه حفظ فرمان</>}
          lead="هر مفهوم روی سه درخت و DAG سوار می‌شود؛ بعد همان کار را در ترمینال و در Source Control انجام می‌دهی."
        />
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {FEATURES.map((f, i) => (
            <Reveal key={f.title} delay={(i % 3) * 0.08}>
              <TiltCard className="h-full">
                <Card className="h-full">
                  <CardHeader>
                    <span className="mb-1 grid size-12 place-items-center rounded-[14px] border border-primary/25 bg-linear-to-br from-primary/15 to-sky/10 text-primary-soft">
                      <f.icon className="size-6" />
                    </span>
                    <CardTitle className="text-[17px]">{f.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="flex-1 text-[13.5px] leading-7 text-muted-foreground">
                    {f.text.split("`").map((p, j) =>
                      j % 2 === 1 ? (
                        <code key={j} className="rounded-md border border-border bg-secondary/60 px-1.5 py-0.5 font-mono text-xs text-primary-soft">{p}</code>
                      ) : (
                        <span key={j}>{p}</span>
                      )
                    )}
                  </CardContent>
                </Card>
              </TiltCard>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
