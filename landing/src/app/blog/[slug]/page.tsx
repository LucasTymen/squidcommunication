import Link from "next/link";
import { notFound } from "next/navigation";
import { loadArticleBySlug, loadArticleContent } from "@/lib/campaigns";
import type { CampaignJSON } from "@/lib/campaigns";
import { generateMetadata as generateSEOMetadata, generateSchemaOrg } from "@/lib/seo";

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

interface BlogArticlePageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: BlogArticlePageProps) {
  const { slug } = await params;
  const article = loadArticleBySlug(slug);
  
  if (!article) {
    return {
      title: "Article non trouvé",
    };
  }
  
  return generateSEOMetadata(article);
}

export default async function BlogArticlePage({ params }: BlogArticlePageProps) {
  const { slug } = await params;
  const article = loadArticleBySlug(slug);
  
  if (!article) {
    notFound();
  }
  
  const content = loadArticleContent(slug);
  const schemaOrg = generateSchemaOrg(article);
  
  const title = article.content?.title || article.campaign_id || "Sans titre";
  const summary = article.content?.summary || "";
  const category = article.content?.category || "Général";
  const tags = article.content?.tags || [];
  const author = article.content?.author || article.owner || "Lucas Tymen";
  const createdDate = article.created_at;
  const updatedDate = article.updated_at || article.created_at;

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schemaOrg) }}
      />
      <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(132,94,247,0.28),_transparent_45%)] text-slate-100">
        <main className="relative mx-auto flex min-h-screen w-full max-w-4xl flex-col gap-12 px-6 py-20 md:px-10">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(circle_at_20%_20%,rgba(90,217,255,0.18),transparent_35%),radial-gradient(circle_at_80%_0%,rgba(132,94,247,0.22),transparent_30%),radial-gradient(circle_at_50%_80%,rgba(255,95,109,0.18),transparent_45%)]" />

          {/* Navigation */}
          <div>
            <Link
              href="/blog"
              className="inline-flex items-center gap-2 text-sm text-slate-300/70 hover:text-slate-100 transition-colors mb-8"
            >
              ← Retour au blog
            </Link>
          </div>

          {/* En-tête de l'article */}
          <article className="space-y-8">
            <header className="space-y-6">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="inline-flex items-center rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-sky-200/90">
                  {category}
                </span>
                {tags.map((tag, idx) => (
                  <span
                    key={idx}
                    className="inline-flex items-center rounded-full bg-white/5 px-2 py-1 text-xs text-slate-300/70"
                  >
                    {tag}
                  </span>
                ))}
              </div>
              
              <h1 className="text-4xl md:text-5xl font-semibold leading-tight text-white">
                {title}
              </h1>
              
              {summary && (
                <p className="text-lg text-slate-200/85 leading-relaxed">
                  {summary}
                </p>
              )}
              
              <div className="flex items-center gap-4 text-sm text-slate-300/70 border-t border-white/10 pt-6">
                <div>
                  <span className="font-medium text-slate-200/90">Par {author}</span>
                </div>
                <span>•</span>
                <time dateTime={createdDate}>
                  {formatDate(createdDate)}
                </time>
                {updatedDate && updatedDate !== createdDate && (
                  <>
                    <span>•</span>
                    <span className="text-xs">Mis à jour le {formatDate(updatedDate)}</span>
                  </>
                )}
              </div>
            </header>

            {/* Contenu de l'article */}
            <div className="rounded-3xl border border-white/10 bg-white/5 p-8 md:p-12 backdrop-blur-xl shadow-[0_20px_60px_-20px_rgba(15,15,40,0.65)]">
              {content ? (
                <div
                  className="prose prose-invert prose-lg max-w-none
                    prose-headings:text-white prose-headings:font-semibold
                    prose-p:text-slate-200/90 prose-p:leading-relaxed
                    prose-a:text-sky-300 prose-a:no-underline hover:prose-a:text-sky-200 hover:prose-a:underline
                    prose-strong:text-white prose-strong:font-semibold
                    prose-code:text-sky-200 prose-code:bg-white/10 prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded
                    prose-pre:bg-slate-900/50 prose-pre:border prose-pre:border-white/10
                    prose-ul:text-slate-200/90 prose-ol:text-slate-200/90
                    prose-li:text-slate-200/90
                    prose-blockquote:border-l-sky-400 prose-blockquote:text-slate-300/80
                    prose-hr:border-white/10"
                  dangerouslySetInnerHTML={{
                    __html: markdownToHtml(content),
                  }}
                />
              ) : (
                <div className="text-center py-12">
                  <p className="text-slate-300/70">
                    Contenu en cours de rédaction...
                  </p>
                </div>
              )}
            </div>

            {/* Footer de l'article */}
            <footer className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">
              <div className="flex flex-col md:flex-row items-center justify-between gap-6">
                <div className="text-sm text-slate-300/70">
                  <p>Partager cet article :</p>
                </div>
                <div className="flex gap-4">
                  <a
                    href={`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(
                      `https://communication.squidresearch.com/blog/${slug}`
                    )}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 rounded-full border border-white/30 px-4 py-2 text-sm font-medium text-sky-100/80 transition-colors hover:border-white hover:text-white"
                  >
                    LinkedIn
                  </a>
                  <a
                    href={`https://twitter.com/intent/tweet?url=${encodeURIComponent(
                      `https://communication.squidresearch.com/blog/${slug}`
                    )}&text=${encodeURIComponent(title)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 rounded-full border border-white/30 px-4 py-2 text-sm font-medium text-sky-100/80 transition-colors hover:border-white hover:text-white"
                  >
                    Twitter
                  </a>
                </div>
              </div>
              <div className="mt-8 pt-8 border-t border-white/10">
                <Link
                  href="/blog"
                  className="inline-flex items-center gap-2 text-sm text-sky-200/90 hover:text-sky-200 transition-colors"
                >
                  ← Retour au blog
                </Link>
              </div>
            </footer>
          </article>
        </main>
      </div>
    </>
  );
}

