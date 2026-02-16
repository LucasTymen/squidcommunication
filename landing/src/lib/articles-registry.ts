import fs from "fs";
import path from "path";

export interface ArticleFromRegistry {
  id: string;
  slug: string;
  title: string;
  category: string;
  status: string;
  content_markdown: string;
  summary?: string;
  planning?: { publish_date?: string };
  seo?: { meta_description?: string; tags?: string[] };
}

export interface RegistryMetadata {
  total_articles: number;
  published: number;
  ready: number;
  draft: number;
  last_updated?: string;
}

/**
 * Charge les articles publiés depuis articles-complete.json (registre principal).
 * Utilisé pour la page d'accueil quand on veut afficher le flux d'activité.
 */
export function loadArticlesFromRegistry(
  options?: { limit?: number; statuses?: string[] }
): { articles: ArticleFromRegistry[]; metadata: RegistryMetadata } {
  const baseDir = process.cwd();
  const registryPath = path.join(baseDir, "..", "articles-complete.json");

  const defaultMetadata: RegistryMetadata = {
    total_articles: 0,
    published: 0,
    ready: 0,
    draft: 0,
  };

  if (!fs.existsSync(registryPath)) {
    return { articles: [], metadata: defaultMetadata };
  }

  try {
    const raw = fs.readFileSync(registryPath, "utf-8");
    const data = JSON.parse(raw);
    const metadata = (data.metadata || defaultMetadata) as RegistryMetadata;
    const allArticles = (data.articles || []) as ArticleFromRegistry[];

    const statuses = options?.statuses ?? ["published", "ready"];
    const limit = options?.limit ?? 12;

    const articles = allArticles
      .filter((a) => statuses.includes(a.status || "draft"))
      .sort((a, b) => {
        const dateA = a.planning?.publish_date || "1970-01-01";
        const dateB = b.planning?.publish_date || "1970-01-01";
        return dateB.localeCompare(dateA);
      })
      .slice(0, limit)
      .map((a) => ({
        ...a,
        summary:
          a.summary ||
          a.content_markdown?.split("\n\n")[0]?.slice(0, 200) ||
          a.seo?.meta_description,
      }));

    return { articles, metadata };
  } catch (err) {
    console.error("Failed to load articles registry:", err);
    return { articles: [], metadata: defaultMetadata };
  }
}
