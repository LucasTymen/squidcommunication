# 🌌 Landing SquidCommunication (BOGOSS)

Landing Next.js pour présenter la saga SquidResearch. Design "BOGOSS" (dégradés néon + glassmorphism) et contenu 100 % data-driven, directement alimenté par les campagnes présentes dans `../campaigns/`.

## ⚙️ Prérequis

- Node.js **>= 20.9.0** (Next.js 16 l’exige)
  ```bash
  # Exemple avec nvm
  nvm install 22
  nvm use 22
  ```
- npm (installé avec Node)

## 🏗️ Installation

```bash
cd landing
npm install
```

## 🚀 Développement local

```bash
npm run dev
```

- Ouvre [http://localhost:3000](http://localhost:3000)
- Les contenus dynamiques lisent automatiquement la dernière campagne (`../campaigns/<slug>/campaign.json`)
- Les métriques affichées proviennent des sections `kpis.target` et `kpis.actual`

## 🧪 Vérifications

```bash
npm run lint   # vérifie eslint + tailwind
npm run build  # build Next.js (utilisé par Vercel)
```

## 🎨 Style BOGOSS

- Dégradés radiaux + halos (violet/bleu/rose)
- Cartes glassmorphism, ombres douces, typographie claire
- Sections clés : Hero feuilleton, timeline des épisodes, progression des KPIs, CTA newsletter

## 🔄 Lien avec SquidCommunication

- `page.tsx` lit les fichiers JSON dans `../campaigns/`
- Les scripts Python (`scripts/create_campaign.py`, `scripts/update_metrics.py`) doivent être exécutés avant de déployer pour refléter les dernières données

## ☁️ Déploiement Vercel

1. Repo GitHub lié à ton compte Vercel : <https://vercel.com/lucas-tymens-projects>
2. Crée un projet Vercel en ciblant ce dossier (`landing/`)
3. Variables d’environnement (si besoin) à configurer dans Vercel Dashboard
4. Pipeline recommandée :
   - `npm run lint`
   - `npm run build`
   - Vercel prend en charge `npm run start`

## 📬 Contacts

- LinkedIn : [Lucas Tymen](https://www.linkedin.com/in/lucastymen/)
- Email : contact@squidresearch.com
