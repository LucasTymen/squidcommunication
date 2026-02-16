import Link from "next/link";
import { loadLatestCampaign, loadAllArticles } from "@/lib/campaigns";
import type { CampaignJSON } from "@/lib/campaigns";
import { loadArticlesFromRegistry } from "@/lib/articles-registry";
import { generateSchemaOrg } from "@/lib/seo";

function formatDate(iso?: string) {
  if (!iso) return "Non planifié";
  try {
    return new Intl.DateTimeFormat("fr-FR", {
      day: "2-digit",
      month: "short",
      hour: "2-digit",
      minute: "2-digit",
    }).format(new Date(iso));
  } catch {
    return iso;
  }
}

export default function Home() {
  const campaign = loadLatestCampaign();
  const schemaOrg = generateSchemaOrg(campaign);
  const { articles: registryArticles, metadata: registryMeta } = loadArticlesFromRegistry({ limit: 8 });
  const blogArticles = loadAllArticles();
  const title = campaign?.campaign_id ?? "Communication SquidResearch";
  const objective =
    campaign?.objective ??
    "Accroître la visibilité de SquidResearch et embarquer la communauté tech dans notre saga data-driven.";
  const summary =
    campaign?.content?.summary ??
    "Une plateforme d'enrichissement B2B qui se raconte en feuilleton : matching intelligent, scraping maîtrisé et growth engineering.";

  const target = campaign?.kpis?.target ?? {
    linkedin_impressions: 500,
    instagram_views: 200,
    cta_clicks: 25,
  };
  const actual = campaign?.kpis?.actual ?? {
    linkedin_impressions: 0,
    instagram_views: 0,
    cta_clicks: 0,
  };

  const posts = (campaign?.posts ?? []).slice(0, 6);

  const metrics = [
    {
      label: "Objectif LinkedIn",
      value: target.linkedin_impressions ?? 0,
      detail: "Impressions ciblées",
    },
    {
      label: "Objectif Instagram",
      value: target.instagram_views ?? 0,
      detail: "Vues story",
    },
    {
      label: "CTA visés",
      value: target.cta_clicks ?? 0,
      detail: "Clicks ou réponses",
    },
  ];

  const progress = [
    {
      label: "Impressions LinkedIn",
      current: actual.linkedin_impressions ?? 0,
      target: target.linkedin_impressions ?? 1,
    },
    {
      label: "Vues Instagram",
      current: actual.instagram_views ?? 0,
      target: target.instagram_views ?? 1,
    },
    {
      label: "CTA",
      current: actual.cta_clicks ?? 0,
      target: target.cta_clicks ?? 1,
    },
  ];

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schemaOrg) }}
      />
      <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(132,94,247,0.28),_transparent_45%)] text-slate-100">
      <main className="relative mx-auto flex min-h-screen w-full max-w-6xl flex-col gap-16 px-6 py-20 md:px-10">
        <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_20%_20%,rgba(90,217,255,0.18),transparent_35%),radial-gradient(circle_at_80%_0%,rgba(132,94,247,0.22),transparent_30%),radial-gradient(circle_at_50%_80%,rgba(255,95,109,0.18),transparent_45%)]" />

        <section className="rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl shadow-[0_20px_60px_-20px_rgba(15,15,40,0.65)]">
          <div className="flex flex-col gap-10 lg:flex-row lg:items-center lg:justify-between">
            <div className="max-w-2xl space-y-6">
              <p className="inline-flex items-center gap-2 rounded-full bg-white/10 px-4 py-1 text-xs uppercase tracking-[0.3em] text-sky-200/90">
                saga SquidResearch · feuilleton data-driven
              </p>
              <h1 className="text-4xl font-semibold leading-tight text-white md:text-5xl">
                {title}
              </h1>
              <p className="text-lg text-slate-200/85">{summary}</p>
              <p className="text-sm text-slate-300/70">{objective}</p>
              <div className="flex flex-wrap gap-4 pt-2">
                <Link
                  href="/blog"
                  className="group inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-[#8b5cf6] via-[#6366f1] to-[#0ea5e9] px-6 py-3 text-sm font-semibold shadow-lg shadow-indigo-500/30 transition-all hover:scale-[1.01] hover:shadow-xl"
                >
                  Découvrir le blog
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </Link>
                <a
                  href="https://www.linkedin.com/in/lucastymen/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="group inline-flex items-center gap-2 rounded-full border border-white/30 px-6 py-3 text-sm font-semibold text-sky-100/80 transition-colors hover:border-white hover:text-white"
                >
                  Suivre sur LinkedIn
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </a>
              </div>
            </div>
            <div className="grid w-full max-w-sm grid-cols-1 gap-5 sm:grid-cols-3 sm:max-w-none">
              {metrics.map((metric) => (
                <div
                  key={metric.label}
                  className="rounded-2xl border border-white/10 bg-white/10 p-4 text-center shadow-inner shadow-white/20"
                >
                  <p className="text-xs uppercase tracking-widest text-slate-200/70">
                    {metric.label}
                  </p>
                  <p className="mt-2 text-3xl font-bold text-white">
                    {metric.value}
                  </p>
                  <p className="text-xs text-slate-300/70">{metric.detail}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="grid gap-8 rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl shadow-[0_10px_40px_-15px_rgba(15,15,40,0.6)] lg:grid-cols-[1.2fr_1fr]">
          <div className="space-y-6">
            <h2 className="text-2xl font-semibold text-white">
              {posts.length > 0 ? "Épisodes à venir" : "Derniers épisodes publiés"}
            </h2>
            <p className="text-sm text-slate-200/70">
              Chaque publication alimente notre loop data-driven : tests d’angles, itérations produit,
              et insights que nous ramenons dans SquidResearch.
            </p>
            <div className="space-y-4">
              {posts.length > 0 ? posts.map((post) => (
                <div
                  key={post.post_id}
                  className="flex flex-col gap-2 rounded-2xl bg-gradient-to-r from-white/12 to-white/5 p-4 shadow-inner shadow-indigo-900/40 sm:flex-row sm:items-center sm:justify-between"
                >
                  <div>
                    <p className="text-sm font-semibold uppercase tracking-wide text-indigo-200/80">
                      {post.platform}
                    </p>
                    <p className="text-base text-white/90">{post.file}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-xs text-slate-200/60">{post.status ?? "draft"}</p>
                    <p className="text-sm font-medium text-white">{formatDate(post.scheduled_date)}</p>
                  </div>
                </div>
              )) : registryArticles.length > 0 ? (
                registryArticles.slice(0, 6).map((article) => (
                  <Link
                    key={article.id}
                    href={`/blog/${article.slug}`}
                    className="flex flex-col gap-2 rounded-2xl bg-gradient-to-r from-white/12 to-white/5 p-4 shadow-inner shadow-indigo-900/40 transition-all hover:from-white/20 hover:to-white/10"
                  >
                    <p className="text-sm font-semibold text-indigo-200/80">{article.category}</p>
                    <p className="text-base text-white/90 line-clamp-2">{article.title}</p>
                    <p className="text-xs text-slate-200/60">
                      {article.planning?.publish_date
                        ? new Intl.DateTimeFormat("fr-FR", { day: "numeric", month: "short", year: "numeric" }).format(
                            new Date(article.planning.publish_date)
                          )
                        : "Publié"}
                    </p>
                  </Link>
                ))
              ) : (
                <p className="rounded-xl border border-dashed border-white/20 bg-white/5 p-6 text-sm text-slate-200/70">
                  Aucune publication pour le moment. Les prochains articles arrivent bientôt.
                </p>
              )}
            </div>
            {registryArticles.length > 0 && (
              <Link
                href="/blog"
                className="inline-flex items-center gap-2 text-sm font-medium text-sky-200/90 hover:text-sky-200 transition-colors"
              >
                Voir tous les articles ({registryMeta.published + registryMeta.ready}+)
                <span>→</span>
              </Link>
            )}
          </div>
          <div className="flex flex-col justify-between gap-6">
            <div className="rounded-2xl border border-white/10 bg-gradient-to-br from-white/15 via-white/5 to-white/0 p-6 shadow-inner">
              <h3 className="text-lg font-semibold text-white">Collecte & analytics</h3>
              <p className="mt-3 text-sm text-slate-200/70">
                Nos scripts extraient automatiquement les métriques des plateformes et alimentent les dashboards
                SquidResearch. Chaque campagne devient un dataset prêt pour l'optimisation growth.
              </p>
              <p className="mt-4 text-xs text-slate-300/60">
                `scripts/update_metrics.py` · `campaigns/&lt;slug&gt;/archive/analytics.json`
              </p>
            </div>
            <div className="space-y-4 rounded-2xl border border-white/10 bg-[#0f172a]/60 p-6 shadow-lg shadow-cyan-500/20">
              {progress.map((item) => {
                const ratio = Math.min(1, item.current / Math.max(item.target, 1));
                return (
                  <div key={item.label} className="space-y-2">
                    <div className="flex items-center justify-between text-xs text-slate-200/70">
                      <span>{item.label}</span>
                      <span>
                        {item.current}/{item.target}
                      </span>
                    </div>
                    <div className="h-2 w-full overflow-hidden rounded-full bg-white/10">
                      <div
                        className="h-full rounded-full bg-gradient-to-r from-sky-400 via-indigo-500 to-fuchsia-500"
                        style={{ width: `${ratio * 100}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </section>

        <section className="rounded-3xl border border-white/10 bg-gradient-to-br from-sky-500/10 via-indigo-500/10 to-purple-500/10 p-10 backdrop-blur-xl shadow-[0_10px_40px_-15px_rgba(15,15,40,0.6)]">
          <div className="flex flex-col gap-8 md:flex-row md:items-center md:justify-between mb-8">
            <div>
              <h2 className="text-3xl font-bold text-white">Derniers articles du blog</h2>
              <p className="mt-2 text-slate-200/80 max-w-2xl">
                Enrichissement, matching, Python, SEO, growth — retours d'expérience et cas réels sur SquidResearch.
              </p>
            </div>
            <Link
              href="/blog"
              className="inline-flex items-center gap-2 rounded-full bg-white/10 px-6 py-3 text-sm font-semibold text-white transition-all hover:bg-white/20"
            >
              Tous les articles
              <span>→</span>
            </Link>
          </div>
          {blogArticles.length > 0 ? (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {blogArticles.slice(0, 8).map((article) => {
                const slug = article.slug || article.campaign_id || "";
                const title = article.content?.title || article.campaign_id || "Sans titre";
                const summary = article.content?.summary || article.objective || "";
                const category = (article.content?.category || "Général").split("/").pop();
                return (
                  <Link
                    key={article.campaign_id || slug}
                    href={`/blog/${slug}`}
                    className="group rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-sm transition-all hover:border-white/20 hover:bg-white/10"
                  >
                    <span className="inline-block rounded-full bg-indigo-500/30 px-3 py-1 text-xs font-medium text-indigo-200 mb-3">
                      {category}
                    </span>
                    <h3 className="text-lg font-semibold text-white group-hover:text-sky-200 transition-colors line-clamp-2">
                      {title}
                    </h3>
                    <p className="mt-2 text-sm text-slate-300/70 line-clamp-3">{summary}</p>
                  </Link>
                );
              })}
            </div>
          ) : (
            <p className="rounded-xl border border-dashed border-white/20 bg-white/5 p-8 text-center text-slate-200/70">
              Aucun article pour le moment. Synchronisez avec <code className="text-sky-200">python scripts/sync_articles_registry.py</code>
            </p>
          )}
        </section>

        <section className="grid gap-6 rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl shadow-[0_10px_40px_-15px_rgba(15,15,40,0.6)] md:grid-cols-2">
          <div className="space-y-4">
            <h2 className="text-2xl font-semibold text-white">Pipeline automatisé</h2>
            <p className="text-sm text-slate-200/70">
              Les campagnes sont générées via scripts (`create_campaign.py`), validées par notre checklist sécurité
              puis synchronisées avec SquidResearch pour nourrir le produit et les dashboards growth.
            </p>
          </div>
          <div className="space-y-3 text-sm text-slate-200/75">
            <p>✅ Génération de dossiers, templates Markdown et assets placeholders</p>
            <p>✅ Synchronisation bilatérale des journaux (`sync_logs.sh`)</p>
            <p>✅ KPIs cibles vs réalisés pour piloter le storytelling</p>
            <p>✅ Narration en feuilleton pour démontrer nos compétences (Python, Django, scraping, IA)</p>
          </div>
        </section>

        <section className="rounded-3xl border border-white/10 bg-gradient-to-br from-purple-500/20 via-indigo-500/20 to-cyan-500/20 p-10 backdrop-blur-xl shadow-[0_20px_60px_-20px_rgba(132,94,247,0.4)]">
          <h2 className="text-3xl font-bold text-white mb-4">🏗️ Architecture 3 Piliers Modulaires</h2>
          <p className="text-slate-200/80 mb-8 max-w-3xl">
            SquidResearch repose sur 3 modules indépendants et modulables, chacun avec un enjeu stratégique unique. 
            Choisissez le module qui correspond à vos besoins ou combinez-les pour une solution complète.
          </p>
          <div className="grid gap-8 md:grid-cols-3">
            <div className="rounded-2xl border-2 border-emerald-500/30 bg-gradient-to-br from-emerald-500/20 via-teal-500/10 to-cyan-500/10 p-8 backdrop-blur-sm shadow-lg shadow-emerald-500/20">
              <div className="flex items-center gap-3 mb-4">
                <div className="text-3xl">🔍</div>
                <h3 className="text-xl font-bold text-white">Prospector</h3>
              </div>
              <p className="text-sm font-semibold text-emerald-300 mb-3">Intelligence & Enrichissement</p>
              <p className="text-sm text-slate-200/90 mb-4">
                Module d'enrichissement B2B universel : scraping multi-sources, recherche contacts RH, 
                intelligence entreprise. Support infini de sites employeurs vs 8 job boards concurrents.
              </p>
              <div className="space-y-2 text-xs text-slate-300/80 mb-4">
                <p>✅ Scraping universel (∞ sites)</p>
                <p>✅ ENRICHED (extraction complète)</p>
                <p>✅ Recherche contacts multi-sources</p>
                <p>✅ Protection IP Tor intégrée</p>
                <p>✅ 100% taux de réussite mesuré</p>
              </div>
              <div className="pt-4 border-t border-emerald-500/20">
                <p className="text-xs font-semibold text-emerald-300 mb-2">Cas d'usage stratégiques</p>
                <p className="text-xs text-slate-300/70">
                  Freelances, recruteurs, marketers B2B, chercheurs d'emploi. 
                  <strong className="text-white"> Différenciation clé</strong> : Support universel + Tor unique.
                </p>
              </div>
            </div>

            <div className="rounded-2xl border-2 border-blue-500/30 bg-gradient-to-br from-blue-500/20 via-indigo-500/10 to-purple-500/10 p-8 backdrop-blur-sm shadow-lg shadow-blue-500/20">
              <div className="flex items-center gap-3 mb-4">
                <div className="text-3xl">🎯</div>
                <h3 className="text-xl font-bold text-white">Applicator</h3>
              </div>
              <p className="text-sm font-semibold text-blue-300 mb-3">Automation Candidatures & Relances</p>
              <p className="text-sm text-slate-200/90 mb-4">
                Automatisation complète du processus de candidature : One-Click Application (2 min vs 30 min), 
                matching IA CV/offres, relances multi-canal. Gain de temps mesuré : 93% par candidature.
              </p>
              <div className="space-y-2 text-xs text-slate-300/80 mb-4">
                <p>✅ One-Click Application complet</p>
                <p>✅ Matching IA (score 0-100)</p>
                <p>✅ Relances multi-canal (Email/LinkedIn/Tel)</p>
                <p>✅ BotFriendly (optimisation ATS)</p>
                <p>✅ ROI 24-36x mesuré</p>
              </div>
              <div className="pt-4 border-t border-blue-500/20">
                <p className="text-xs font-semibold text-blue-300 mb-2">Cas d'usage stratégiques</p>
                <p className="text-xs text-slate-300/70">
                  Chercheurs d'emploi, freelances, commerciaux. 
                  <strong className="text-white"> Différenciation clé</strong> : Workflow complet vs outils fragmentés.
                </p>
              </div>
            </div>

            <div className="rounded-2xl border-2 border-purple-500/30 bg-gradient-to-br from-purple-500/20 via-pink-500/10 to-rose-500/10 p-8 backdrop-blur-sm shadow-lg shadow-purple-500/20">
              <div className="flex items-center gap-3 mb-4">
                <div className="text-3xl">🎬</div>
                <h3 className="text-xl font-bold text-white">Broadcaster</h3>
              </div>
              <p className="text-sm font-semibold text-purple-300 mb-3">Orchestration Campagnes Multi-Plateformes</p>
              <p className="text-sm text-slate-200/90 mb-4">
                Moteur de campagnes sociales avec génération IA intégrée. Orchestration 8+ plateformes, 
                scénarios automatisés (teasing → lancement), A/B testing. Unique : génération IA + orchestration narrative.
              </p>
              <div className="space-y-2 text-xs text-slate-300/80 mb-4">
                <p>✅ AI Content Factory intégrée</p>
                <p>✅ 8+ plateformes (LinkedIn, Instagram, TikTok...)</p>
                <p>✅ Scénarios automatisés</p>
                <p>✅ A/B testing posts</p>
                <p>✅ OAuth multi-utilisateurs (14 plateformes)</p>
              </div>
              <div className="pt-4 border-t border-purple-500/20">
                <p className="text-xs font-semibold text-purple-300 mb-2">Cas d'usage stratégiques</p>
                <p className="text-xs text-slate-300/70">
                  Créateurs contenu, artistes, startups, marketers. 
                  <strong className="text-white"> Différenciation clé</strong> : IA intégrée vs planification seule.
                </p>
              </div>
            </div>
          </div>
          <div className="mt-8 rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-sm">
            <p className="text-sm text-slate-200/90 text-center">
              <strong className="text-white">Modularité stratégique</strong> : Chaque pilier peut fonctionner indépendamment ou être combiné 
              pour créer des workflows puissants. Prospector → Applicator → Broadcaster : un écosystème complet.
            </p>
          </div>
        </section>

        <section className="rounded-3xl border border-white/10 bg-gradient-to-br from-emerald-500/20 via-teal-500/20 to-cyan-500/20 p-10 backdrop-blur-xl shadow-[0_20px_60px_-20px_rgba(16,185,129,0.3)]">
          <h2 className="text-3xl font-bold text-white mb-6">📊 Statistiques Projet</h2>
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 text-center backdrop-blur-sm">
              <p className="text-4xl font-bold text-emerald-400 mb-2">50K+</p>
              <p className="text-sm text-slate-200/80">Lignes de code</p>
            </div>
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 text-center backdrop-blur-sm">
              <p className="text-4xl font-bold text-cyan-400 mb-2">83</p>
              <p className="text-sm text-slate-200/80">Apps Django</p>
            </div>
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 text-center backdrop-blur-sm">
              <p className="text-4xl font-bold text-purple-400 mb-2">70%</p>
              <p className="text-sm text-slate-200/80">Coverage tests</p>
            </div>
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 text-center backdrop-blur-sm">
              <p className="text-4xl font-bold text-indigo-400 mb-2">{blogArticles.length || registryMeta.total_articles || 97}</p>
              <p className="text-sm text-slate-200/80">Articles</p>
            </div>
          </div>
          <div className="mt-6 grid gap-4 md:grid-cols-2">
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 backdrop-blur-sm">
              <h3 className="text-lg font-semibold text-white mb-3">Stack Technique</h3>
              <div className="text-sm text-slate-200/80 space-y-1">
                <p>🐍 Python 3.11 + Django 5.2.5</p>
                <p>⚛️ React + Next.js 16</p>
                <p>🐳 Docker Compose (9+ services)</p>
                <p>🔄 Celery + Redis + PostgreSQL</p>
                <p>🤖 n8n + Flowise (orchestration IA)</p>
              </div>
            </div>
            <div className="rounded-2xl border border-white/10 bg-white/10 p-6 backdrop-blur-sm">
              <h3 className="text-lg font-semibold text-white mb-3">Performance Mesurée</h3>
              <div className="text-sm text-slate-200/80 space-y-1">
                <p>⚡ 93% gain temps candidature</p>
                <p>📧 100% taux réussite enrichissement</p>
                <p>🎯 24-36x ROI mesuré</p>
                <p>⚙️ 42s bulk 10 entreprises</p>
                <p>🔍 6-7 emails trouvés/recherche</p>
              </div>
            </div>
          </div>
        </section>

        <section className="rounded-3xl border border-white/10 bg-gradient-to-r from-indigo-500/40 via-sky-500/30 to-cyan-400/25 p-10 text-center shadow-[0_20px_80px_-30px_rgba(20,120,200,0.6)]">
          <h2 className="text-3xl font-bold text-white">Prêt à suivre les prochains épisodes ?</h2>
          <p className="mx-auto mt-4 max-w-2xl text-sm text-slate-50/80">
            Rejoins la newsletter pour recevoir les insights techniques (matching, scraping, growth) et les coulisses du
            projet SquidResearch. Chaque épisode est une capsule d’apprentissage.
          </p>
          <div className="mt-6 flex flex-wrap justify-center gap-4">
            <a
              href="https://www.linkedin.com/in/lucastymen/"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-full bg-white/90 px-6 py-3 text-sm font-semibold text-indigo-900 transition-transform hover:scale-[1.02]"
            >
              Suivre sur LinkedIn
            </a>
            <a
              href="mailto:contact@squidresearch.com?subject=Newsletter%20SquidResearch"
              className="inline-flex items-center gap-2 rounded-full border border-white/60 px-6 py-3 text-sm font-semibold text-white backdrop-blur-sm transition-colors hover:border-white"
            >
              Recevoir la newsletter
            </a>
          </div>
        </section>
      </main>
    </div>
    </>
  );
}

