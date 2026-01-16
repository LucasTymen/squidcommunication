/**
 * Fonctions utilitaires pour le rendu Markdown basique
 * 
 * Note: Pour un rendu Markdown plus avancé, considérer l'utilisation de
 * react-markdown ou remark/rehype dans le futur.
 */

/**
 * Convertit du Markdown basique en HTML
 * Version simplifiée pour un rendu rapide sans dépendances externes
 */
export function markdownToHtml(markdown: string): string {
  let html = markdown;

  // Code blocks (avant les autres remplacements)
  html = html.replace(/```[\s\S]*?```/g, (match) => {
    const code = match.replace(/```/g, "").trim();
    return `<pre><code>${escapeHtml(code)}</code></pre>`;
  });

  // Headers (dans l'ordre décroissant pour éviter les conflits)
  html = html.replace(/^#### (.*?)$/gm, "<h4>$1</h4>");
  html = html.replace(/^### (.*?)$/gm, "<h3>$1</h3>");
  html = html.replace(/^## (.*?)$/gm, "<h2>$1</h2>");
  html = html.replace(/^# (.*?)$/gm, "<h1>$1</h1>");

  // Horizontal rules
  html = html.replace(/^---$/gm, "<hr />");
  html = html.replace(/^\*\*\*$/gm, "<hr />");

  // Lists (basique - avant les paragraphes)
  const lines = html.split("\n");
  let inList = false;
  let listItems: string[] = [];
  const processedLines: string[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const listMatch = line.match(/^[\-\*\+]\s+(.+)$/);

    if (listMatch) {
      if (!inList) {
        inList = true;
        listItems = [];
      }
      listItems.push(`<li>${listMatch[1]}</li>`);
    } else {
      if (inList && listItems.length > 0) {
        processedLines.push(`<ul>${listItems.join("\n")}</ul>`);
        listItems = [];
        inList = false;
      }
      processedLines.push(line);
    }
  }

  if (inList && listItems.length > 0) {
    processedLines.push(`<ul>${listItems.join("\n")}</ul>`);
  }

  html = processedLines.join("\n");

  // Links
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  // Bold
  html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

  // Italic (après bold pour éviter les conflits)
  html = html.replace(/(?<!\*)\*([^*]+?)\*(?!\*)/g, "<em>$1</em>");

  // Inline code (après les autres remplacements)
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");

  // Paragraphs (traitement des lignes vides)
  const paragraphs = html.split(/\n\s*\n/);
  html = paragraphs
    .map((p) => {
      p = p.trim();
      if (!p) return "";
      // Ne pas envelopper les éléments HTML existants
      if (p.startsWith("<") && (p.startsWith("<h") || p.startsWith("<ul") || p.startsWith("<ol") || p.startsWith("<pre") || p.startsWith("<hr"))) {
        return p;
      }
      return `<p>${p}</p>`;
    })
    .filter((p) => p)
    .join("\n\n");

  return html;
}

/**
 * Échappe les caractères HTML
 */
function escapeHtml(text: string): string {
  const map: Record<string, string> = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  };
  return text.replace(/[&<>"']/g, (m) => map[m]);
}

