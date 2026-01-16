import Link from "next/link";
import { loadAllArticles } from "@/lib/campaigns";
import type { CampaignJSON } from "@/lib/campaigns";

function formatDate(iso?: string) {
  if (!iso) return "Date inconnue";
  try {
    return new Intl.DateTimeFormat("fr-FR", {
      day: "2-digit",
      month: "long",
      year: "numeric",
    }).format(new Date(iso));
  } catch {
    return iso;
  }
}

export const metadata = {
  title: "Blog | SquidResearch",
  description: "Articles techniques, tutoriels et actualités sur l'automatisation B2B, le scraping intelligent et le broadcasting multi-canal.",
};

export default function BlogPage() {
  const articles = loadAllArticles();

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(132,94,247,0.28),_transparent_45%)] text-slate-100">
      <main className="relative mx-auto flex min-h-screen w-full max-w-6xl flex-col gap-16 px-6 py-20 md:px-10">
        <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_20%_20%,rgba(90,217,255,0.18),transparent_35%),radial-gradient(circle_at_80%_0%,rgba(132,94,247,0.22),transparent_30%),radial-gradient(circle_at_50%_80%,rgba(255,95,109,0.18),transparent_45%)]" />

        <section className="space-y-8">
          <div>
            <Link
              href="/"
              className="inline-flex items-center gap-2 text-sm text-slate-300/70 hover:text-slate-100 transition-colors mb-8"
            >
              ← Retour à l'accueil
            </Link>
            <h1 className="text-5xl font-semibold leading-tight text-white mb-4">
              Blog SquidResearch
            </h1>
            <p className="text-lg text-slate-200/85 max-w-2xl">
              Articles techniques, tutoriels et actualités sur l'automatisation B2B, le scraping intelligent et le broadcasting multi-canal optimisé.
            </p>
          </div>

          {articles.length === 0 ? (
            <div className="rounded-3xl border border-white/10 bg-white/5 p-12 backdrop-blur-xl text-center">
              <p className="text-slate-300/70 text-lg">
                Aucun article pour le moment. Bientôt disponible !
              </p>
            </div>
          ) : (
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {articles.map((article) => {
                const slug = article.slug || article.campaign_id?.split("-").slice(-1)[0] || "";
                const title = article.content?.title || article.campaign_id || "Sans titre";
                const summary = article.content?.summary || article.objective || "";
                const category = article.content?.category || "Général";
                const tags = article.content?.tags || [];
                const createdDate = article.created_at;

                return (
                  <Link
                    key={article.campaign_id}
                    href={`/blog/${slug}`}
                    className="group rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl shadow-[0_20px_60px_-20px_rgba(15,15,40,0.65)] transition-all hover:border-white/20 hover:bg-white/10 hover:scale-[1.02]"
                  >
                    <div className="space-y-4">
                      <div className="flex items-center gap-2 flex-wrap">
                        <span className="inline-flex items-center rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-sky-200/90">
                          {category}
                        </span>
                        {tags.slice(0, 2).map((tag, idx) => (
                          <span
                            key={idx}
                            className="inline-flex items-center rounded-full bg-white/5 px-2 py-1 text-xs text-slate-300/70"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                      <h2 className="text-xl font-semibold text-white group-hover:text-sky-200 transition-colors">
                        {title}
                      </h2>
                      <p className="text-sm text-slate-300/70 line-clamp-3">
                        {summary}
                      </p>
                      <div className="flex items-center justify-between pt-2 border-t border-white/10">
                        <time className="text-xs text-slate-400/70">
                          {formatDate(createdDate)}
                        </time>
                        <span className="text-xs text-sky-200/90 group-hover:text-sky-200 transition-colors">
                          Lire l'article →
                        </span>
                      </div>
                    </div>
                  </Link>
                );
              })}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

