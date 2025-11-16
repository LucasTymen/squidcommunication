import fs from "fs";
import path from "path";

interface CampaignJSON {
  campaign_id: string;
  objective?: string;
  content?: { summary?: string; cta?: string };
  kpis?: {
    target?: Record<string, number>;
    actual?: Record<string, number>;
  };
  posts?: Array<{
    post_id: string;
    platform: string;
    scheduled_date?: string;
    status?: string;
    file?: string;
  }>;
}

function loadLatestCampaign(): CampaignJSON | null {
  const campaignsRoot = path.join(process.cwd(), "..", "campaigns");
  if (!fs.existsSync(campaignsRoot)) {
    return null;
  }
  const entries = fs
    .readdirSync(campaignsRoot)
    .filter((folder) => folder !== ".DS_Store")
    .map((folder) => ({
      folder,
      stat: fs.statSync(path.join(campaignsRoot, folder)),
    }))
    .sort((a, b) => b.stat.mtime.getTime() - a.stat.mtime.getTime());

  for (const { folder } of entries) {
    const campaignPath = path.join(campaignsRoot, folder, "campaign.json");
    if (!fs.existsSync(campaignPath)) continue;
    try {
      const raw = fs.readFileSync(campaignPath, "utf-8");
      return JSON.parse(raw) as CampaignJSON;
    } catch (error) {
      console.error("Failed to parse", folder, error);
    }
  }
  return null;
}

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
                <a
                  href="https://www.linkedin.com/in/lucastymen/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="group inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-[#8b5cf6] via-[#6366f1] to-[#0ea5e9] px-6 py-3 text-sm font-semibold shadow-lg shadow-indigo-500/30 transition-all hover:scale-[1.01] hover:shadow-xl"
                >
                  Suivre la saga LinkedIn
                  <span className="transition-transform group-hover:translate-x-1">→</span>
                </a>
                <a
                  href="mailto:contact@squidresearch.com"
                  className="inline-flex items-center gap-2 rounded-full border border-white/30 px-6 py-3 text-sm font-semibold text-sky-100/80 transition-colors hover:border-white hover:text-white"
                >
                  Être notifié des nouveaux épisodes
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
            <h2 className="text-2xl font-semibold text-white">Épisodes à venir</h2>
            <p className="text-sm text-slate-200/70">
              Chaque publication alimente notre loop data-driven : tests d’angles, itérations produit,
              et insights que nous ramenons dans SquidResearch.
            </p>
            <div className="space-y-4">
              {posts.length === 0 && (
                <p className="rounded-xl border border-dashed border-white/20 bg-white/5 p-6 text-sm text-slate-200/70">
                  Aucune campagne planifiée pour le moment. Lancez une campagne avec `python scripts/create_campaign.py`.
                </p>
              )}
              {posts.map((post) => (
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
              ))}
            </div>
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
  );
}
