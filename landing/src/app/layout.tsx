import type { Metadata } from "next";
import Link from "next/link";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { loadLatestCampaign } from "@/lib/campaigns";
import { generateMetadata as generateSEOMetadata } from "@/lib/seo";
import { generateOrganizationSchema } from "@/lib/seo";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = generateSEOMetadata(loadLatestCampaign());

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const orgSchema = generateOrganizationSchema();

  return (
    <html lang="fr">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(orgSchema) }}
        />
        <header className="fixed top-0 left-0 right-0 z-50 border-b border-white/10 bg-slate-950/80 backdrop-blur-xl">
          <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
            <Link href="/" className="text-lg font-semibold text-white hover:text-sky-200 transition-colors">
              SquidResearch
            </Link>
            <div className="flex gap-6">
              <Link href="/" className="text-sm text-slate-300 hover:text-white transition-colors">
                Accueil
              </Link>
              <Link href="/blog" className="text-sm text-slate-300 hover:text-white transition-colors">
                Blog
              </Link>
              <a
                href="https://www.linkedin.com/in/lucastymen/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-slate-300 hover:text-white transition-colors"
              >
                LinkedIn
              </a>
            </div>
          </nav>
        </header>
        <div className="pt-16">{children}</div>
      </body>
    </html>
  );
}
