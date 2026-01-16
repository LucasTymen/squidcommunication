import fs from "fs";
import path from "path";

export interface CampaignJSON {
  campaign_id: string;
  slug?: string;
  objective?: string;
  content?: {
    summary?: string;
    cta?: string;
    title?: string;
  };
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
  seo?: {
    meta_title?: string;
    meta_description?: string;
    keywords?: string[];
    slug?: string;
    canonical?: string;
    schema_type?: "Article" | "BlogPosting" | "WebPage";
    og_image?: string;
    og_type?: "article" | "website";
    twitter_card?: "summary_large_image" | "summary";
    lang?: string;
    alternate_langs?: string[];
  };
  created_at?: string;
  updated_at?: string;
}

/**
 * Charge la dernière campagne depuis le dossier campaigns/
 */
export function loadLatestCampaign(): CampaignJSON | null {
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

/**
 * Charge toutes les campagnes depuis campaigns/ et articles/
 */
export function loadAllCampaigns(): CampaignJSON[] {
  const campaigns: CampaignJSON[] = [];
  const baseDir = process.cwd();

  // Campagnes dans campaigns/
  const campaignsRoot = path.join(baseDir, "..", "campaigns");
  if (fs.existsSync(campaignsRoot)) {
    const entries = fs
      .readdirSync(campaignsRoot)
      .filter((folder) => folder !== ".DS_Store");
    for (const folder of entries) {
      const campaignPath = path.join(campaignsRoot, folder, "campaign.json");
      if (fs.existsSync(campaignPath)) {
        try {
          const raw = fs.readFileSync(campaignPath, "utf-8");
          campaigns.push(JSON.parse(raw) as CampaignJSON);
        } catch (error) {
          console.error("Failed to parse", folder, error);
        }
      }
    }
  }

  // Articles dans articles/
  const articlesRoot = path.join(baseDir, "..", "articles");
  if (fs.existsSync(articlesRoot)) {
    const entries = fs
      .readdirSync(articlesRoot)
      .filter((folder) => folder !== ".DS_Store");
    for (const folder of entries) {
      const campaignPath = path.join(articlesRoot, folder, "campaign.json");
      if (fs.existsSync(campaignPath)) {
        try {
          const raw = fs.readFileSync(campaignPath, "utf-8");
          campaigns.push(JSON.parse(raw) as CampaignJSON);
        } catch (error) {
          console.error("Failed to parse article", folder, error);
        }
      }
    }
  }

  return campaigns;
}

/**
 * Charge uniquement les articles depuis articles/
 */
export function loadAllArticles(): CampaignJSON[] {
  const articles: CampaignJSON[] = [];
  const baseDir = process.cwd();
  const articlesRoot = path.join(baseDir, "..", "articles");
  
  if (!fs.existsSync(articlesRoot)) {
    return articles;
  }
  
  const entries = fs
    .readdirSync(articlesRoot)
    .filter((folder) => folder !== ".DS_Store" && folder.startsWith("article-"));
  
  for (const folder of entries) {
    const campaignPath = path.join(articlesRoot, folder, "campaign.json");
    if (fs.existsSync(campaignPath)) {
      try {
        const raw = fs.readFileSync(campaignPath, "utf-8");
        const article = JSON.parse(raw) as CampaignJSON;
        // Filtrer uniquement les articles publiés ou draft
        if (article.status === "published" || article.status === "draft") {
          articles.push(article);
        }
      } catch (error) {
        console.error("Failed to parse article", folder, error);
      }
    }
  }
  
  // Trier par date de création (plus récent en premier)
  articles.sort((a, b) => {
    const dateA = a.created_at ? new Date(a.created_at).getTime() : 0;
    const dateB = b.created_at ? new Date(b.created_at).getTime() : 0;
    return dateB - dateA;
  });
  
  return articles;
}

/**
 * Charge un article spécifique par son slug
 */
export function loadArticleBySlug(slug: string): CampaignJSON | null {
  const baseDir = process.cwd();
  const articlesRoot = path.join(baseDir, "..", "articles");
  
  if (!fs.existsSync(articlesRoot)) {
    return null;
  }
  
  const entries = fs
    .readdirSync(articlesRoot)
    .filter((folder) => folder !== ".DS_Store" && folder.startsWith("article-"));
  
  for (const folder of entries) {
    const campaignPath = path.join(articlesRoot, folder, "campaign.json");
    if (fs.existsSync(campaignPath)) {
      try {
        const raw = fs.readFileSync(campaignPath, "utf-8");
        const article = JSON.parse(raw) as CampaignJSON;
        if (article.slug === slug || article.campaign_id?.includes(slug)) {
          return article;
        }
      } catch (error) {
        console.error("Failed to parse article", folder, error);
      }
    }
  }
  
  return null;
}

/**
 * Charge le contenu Markdown d'un article
 */
export function loadArticleContent(slug: string): string | null {
  const baseDir = process.cwd();
  const articlesRoot = path.join(baseDir, "..", "articles");
  
  if (!fs.existsSync(articlesRoot)) {
    return null;
  }
  
  const entries = fs
    .readdirSync(articlesRoot)
    .filter((folder) => folder !== ".DS_Store" && folder.startsWith("article-"));
  
  for (const folder of entries) {
    const articlePath = path.join(articlesRoot, folder, "article.md");
    if (fs.existsSync(articlePath)) {
      const campaignPath = path.join(articlesRoot, folder, "campaign.json");
      if (fs.existsSync(campaignPath)) {
        try {
          const raw = fs.readFileSync(campaignPath, "utf-8");
          const article = JSON.parse(raw) as CampaignJSON;
          if (article.slug === slug || article.campaign_id?.includes(slug)) {
            return fs.readFileSync(articlePath, "utf-8");
          }
        } catch (error) {
          console.error("Failed to check article", folder, error);
        }
      }
    }
  }
  
  return null;
}


