import { MetadataRoute } from "next";
import { loadAllCampaigns, loadAllArticles } from "@/lib/campaigns";

const SITE_URL = "https://communication.squidresearch.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const campaigns = loadAllCampaigns();
  const articles = loadAllArticles();
  const now = new Date();

  const routes: MetadataRoute.Sitemap = [
    {
      url: SITE_URL,
      lastModified: now,
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: `${SITE_URL}/blog`,
      lastModified: now,
      changeFrequency: "weekly",
      priority: 0.9,
    },
  ];

  // Ajouter chaque campagne
  for (const campaign of campaigns) {
    // Ignorer les articles (traités séparément)
    if (campaign.platforms?.includes("blog")) continue;
    
    const slug = campaign.seo?.slug || campaign.slug || campaign.campaign_id;
    const url = `${SITE_URL}/campaigns/${slug}`;
    const lastModified = campaign.updated_at
      ? new Date(campaign.updated_at)
      : campaign.created_at
      ? new Date(campaign.created_at)
      : now;

    routes.push({
      url,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.8,
    });
  }

  // Ajouter chaque article de blog
  for (const article of articles) {
    const slug = article.seo?.slug || article.slug || article.campaign_id?.split("-").slice(-1)[0] || "";
    if (!slug) continue;
    
    const url = `${SITE_URL}/blog/${slug}`;
    const lastModified = article.updated_at
      ? new Date(article.updated_at)
      : article.created_at
      ? new Date(article.created_at)
      : now;

    routes.push({
      url,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.8,
    });
  }

  return routes;
}


