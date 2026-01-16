import type { Metadata } from "next";
import type { CampaignJSON } from "./campaigns";

const DEFAULT_SITE_URL = "https://communication.squidresearch.com";
const DEFAULT_TITLE = "SquidCommunication - Hub de communication SquidResearch";
const DEFAULT_DESCRIPTION =
  "Centre éditorial et hub de communication pour SquidResearch. Campagnes data-driven, articles techniques, et stratégie de croissance.";

/**
 * Génère les métadonnées Next.js depuis les données SEO d'une campagne
 */
export function generateMetadata(campaign?: CampaignJSON | null): Metadata {
  const seo = campaign?.seo;
  const title =
    seo?.meta_title ||
    campaign?.content?.title ||
    campaign?.campaign_id ||
    DEFAULT_TITLE;
  const description =
    seo?.meta_description ||
    campaign?.content?.summary ||
    DEFAULT_DESCRIPTION;
  const keywords = seo?.keywords || [];
  const slug = seo?.slug || campaign?.slug || campaign?.campaign_id || "";
  const canonical = seo?.canonical || `${DEFAULT_SITE_URL}/${slug ? `campaigns/${slug}` : ""}`;
  const ogImage =
    seo?.og_image || `${DEFAULT_SITE_URL}/og-default.png`;
  const ogType = seo?.og_type || "article";
  const twitterCard = seo?.twitter_card || "summary_large_image";
  const lang = seo?.lang || "fr";

  return {
    title: {
      default: title,
      template: "%s | SquidCommunication",
    },
    description,
    keywords: keywords.length > 0 ? keywords : undefined,
    authors: [{ name: "Lucas Tymen" }],
    creator: "Lucas Tymen",
    publisher: "SquidResearch",
    metadataBase: new URL(DEFAULT_SITE_URL),
    alternates: {
      canonical,
      languages: seo?.alternate_langs?.reduce(
        (acc: Record<string, string>, lang: string) => ({ ...acc, [lang]: `${canonical}?lang=${lang}` }),
        { [lang]: canonical }
      ) || { [lang]: canonical },
    },
    openGraph: {
      title,
      description,
      url: canonical,
      siteName: "SquidCommunication",
      images: [
        {
          url: ogImage,
          width: 1200,
          height: 630,
          alt: title,
        },
      ],
      locale: lang === "fr" ? "fr_FR" : "en_US",
      type: ogType,
      publishedTime: campaign?.created_at || undefined,
      modifiedTime: campaign?.updated_at || campaign?.created_at || undefined,
    },
    twitter: {
      card: twitterCard,
      title,
      description,
      images: [ogImage],
      creator: "@lucastymen",
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-video-preview": -1,
        "max-image-preview": "large",
        "max-snippet": -1,
      },
    },
  };
}

/**
 * Génère le Schema.org JSON-LD pour une campagne
 */
export function generateSchemaOrg(campaign?: CampaignJSON | null): object {
  const seo = campaign?.seo;
  const schemaType = seo?.schema_type || "Article";
  const title =
    seo?.meta_title ||
    campaign?.content?.title ||
    campaign?.campaign_id ||
    DEFAULT_TITLE;
  const description =
    seo?.meta_description ||
    campaign?.content?.summary ||
    DEFAULT_DESCRIPTION;
  const slug = seo?.slug || campaign?.slug || campaign?.campaign_id || "";
  const canonical =
    seo?.canonical ||
    `${DEFAULT_SITE_URL}/${slug ? `campaigns/${slug}` : ""}`;
  const ogImage =
    seo?.og_image || `${DEFAULT_SITE_URL}/og-default.png`;

  const baseSchema = {
    "@context": "https://schema.org",
    "@type": schemaType,
    headline: title,
    description,
    url: canonical,
    image: ogImage,
    author: {
      "@type": "Person",
      name: "Lucas Tymen",
      url: "https://www.linkedin.com/in/lucastymen/",
    },
    publisher: {
      "@type": "Organization",
      name: "SquidResearch",
      url: "https://squidresearch.com",
      logo: {
        "@type": "ImageObject",
        url: `${DEFAULT_SITE_URL}/logo.png`,
      },
    },
    datePublished: campaign?.created_at || undefined,
    dateModified: campaign?.updated_at || campaign?.created_at || undefined,
    inLanguage: seo?.lang || "fr",
  };

  if (schemaType === "Article" || schemaType === "BlogPosting") {
    return {
      ...baseSchema,
      "@type": schemaType,
      keywords: seo?.keywords?.join(", ") || undefined,
    };
  }

  return baseSchema;
}

/**
 * Génère le Schema.org JSON-LD pour l'organisation
 */
export function generateOrganizationSchema(): object {
  return {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: "SquidResearch",
    url: "https://squidresearch.com",
    logo: `${DEFAULT_SITE_URL}/logo.png`,
    sameAs: [
      "https://www.linkedin.com/company/squidresearch",
      "https://github.com/lucastymen",
    ],
    contactPoint: {
      "@type": "ContactPoint",
      email: "contact@squidresearch.com",
      contactType: "Customer Service",
    },
  };
}

