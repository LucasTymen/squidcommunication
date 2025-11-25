#!/usr/bin/env python3
"""
Génération des slides HTML pour les articles
Utilise uniquement des métriques réelles vérifiables
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Template de base pour les slides
SLIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <title>SquidResearch — {episode} (Slide {num})</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: 'Poppins', Arial, sans-serif;
      color: #f8fafc;
      background: radial-gradient(circle at 20% 20%, rgba(90, 217, 255, 0.28), transparent 45%),
                  radial-gradient(circle at 80% 0%, rgba(132, 94, 247, 0.35), transparent 40%),
                  linear-gradient(135deg, #090817 0%, #1c0f39 45%, #2f1b63 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 60px;
    }}
    .card {{
      width: 1080px;
      height: 1080px;
      border-radius: 48px;
      padding: 80px 100px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.35);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(148, 163, 184, 0.2);
      box-shadow: 0 40px 90px -30px rgba(17, 24, 39, 0.7);
      position: relative;
    }}
    .badge {{
      align-self: flex-start;
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 18px;
      text-transform: uppercase;
      letter-spacing: 0.35em;
      background: linear-gradient(90deg, rgba(139, 92, 246, 0.85), rgba(14, 165, 233, 0.75));
      color: #0b1120;
      font-weight: 600;
      animation: badgePulse 2s ease-in-out infinite;
    }}
    h1 {{
      font-size: 72px;
      line-height: 1.05;
      margin: 0;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: titleGradient 3s ease-in-out infinite;
    }}
    h2 {{
      font-size: 36px;
      font-weight: 500;
      margin: 16px 0 0;
      color: rgba(226, 232, 240, 0.9);
      animation: fadeInUp 0.8s ease-out;
    }}
    .content {{
      font-size: 24px;
      color: rgba(203, 213, 225, 0.85);
      margin: 20px 0;
      line-height: 1.4;
      animation: fadeInUp 1s ease-out 0.2s both;
    }}
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin: 40px 0;
    }}
    .metric-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 2px solid rgba(99, 102, 241, 0.4);
      border-radius: 20px;
      padding: 32px;
      text-align: center;
      backdrop-filter: blur(8px);
      animation: fadeInUp 1s ease-out both;
    }}
    .metric-value {{
      font-size: 56px;
      font-weight: 800;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}
    .metric-label {{
      font-size: 18px;
      color: rgba(203, 213, 225, 0.8);
      font-weight: 500;
    }}
    .footer {{
      font-size: 24px;
      color: rgba(148, 163, 184, 0.85);
      animation: fadeInUp 1.2s ease-out 1s both;
    }}
    @keyframes badgePulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.9; transform: scale(1.02); }}
    }}
    @keyframes titleGradient {{
      0%, 100% {{ filter: hue-rotate(0deg); }}
      50% {{ filter: hue-rotate(10deg); }}
    }}
    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">{badge}</div>
    <div>
      {content}
    </div>
    <div class="footer">Saga data-driven · Style BOGOSS</div>
  </div>
</body>
</html>"""

# Contenu des slides par article
ARTICLES = {
    'article-3-algorithmes-matching-intelligents': {
        'episode': 'Épisode 3',
        'badge': 'Épisode 3',
        'slides': [
            {
                'num': 1,
                'content': '''<h1>Algorithmes de Matching Intelligents</h1>
      <h2>Comment matcher un candidat avec 1000+ offres en &lt; 5s ?</h2>
      <p class="content">5 algorithmes spécialisés basés sur des modèles mathématiques pour un matching précis et rapide</p>
      <div class="metrics-grid">
        <div class="metric-card" style="animation-delay: 0.3s;">
          <div class="metric-value">5</div>
          <div class="metric-label">Algorithmes Spécialisés</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.4s;">
          <div class="metric-value">26/26</div>
          <div class="metric-label">Tests Passent</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.5s;">
          <div class="metric-value">62%</div>
          <div class="metric-label">Coverage Global</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.6s;">
          <div class="metric-value">&gt;85%</div>
          <div class="metric-label">Modules Critiques</div>
        </div>
      </div>'''
            },
            {
                'num': 2,
                'content': '''<h1>Le Problème</h1>
      <h2>Matching manuel = heures de travail</h2>
      <p class="content">Rechercher manuellement parmi des milliers d'offres d'emploi ou de candidats est chronophage et sujet aux erreurs humaines.</p>
      <p class="content">Sans automatisation, un recruteur peut passer des heures à matcher des profils.</p>'''
            },
            {
                'num': 3,
                'content': '''<h1>La Solution</h1>
      <h2>5 algorithmes spécialisés</h2>
      <p class="content">Chaque algorithme utilise un modèle mathématique spécifique pour calculer des scores de matching normalisés (0-100) avec un niveau de confiance.</p>
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">JobSearch</div>
          <div class="metric-label">Candidat → Offres</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">TalentSourcing</div>
          <div class="metric-label">Offre → Candidats</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">SkillsMatching</div>
          <div class="metric-label">Compétences pures</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">CompanyOutreach</div>
          <div class="metric-label">Approche entreprises</div>
        </div>
      </div>'''
            },
            {
                'num': 4,
                'content': '''<h1>Algorithme 1 : JobSearch</h1>
      <h2>Candidat → Offres d'emploi</h2>
      <p class="content">Calcule le score de compatibilité entre un profil candidat et une offre d'emploi.</p>
      <p class="content">Prend en compte : compétences, expérience, localisation, salaire, type de contrat.</p>
      <p class="content">Score normalisé 0-100 avec explication automatique du match.</p>'''
            },
            {
                'num': 5,
                'content': '''<h1>Algorithme 2 : TalentSourcing</h1>
      <h2>Offre → Candidats</h2>
      <p class="content">Trouve les meilleurs candidats pour une offre d'emploi spécifique.</p>
      <p class="content">Recherche dans la base de candidats selon les critères de l'offre.</p>
      <p class="content">Tri par score de matching décroissant avec niveau de confiance.</p>'''
            },
            {
                'num': 6,
                'content': '''<h1>Algorithme 3 : SkillsMatching</h1>
      <h2>Matching par compétences</h2>
      <p class="content">Focus sur les compétences techniques et soft skills.</p>
      <p class="content">Compare les compétences requises vs disponibles avec pondération intelligente.</p>
      <p class="content">Détecte les compétences complémentaires et les gaps.</p>'''
            },
            {
                'num': 7,
                'content': '''<h1>Résultats</h1>
      <h2>Tests & Coverage</h2>
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">26/26</div>
          <div class="metric-label">Tests Passent</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">62%</div>
          <div class="metric-label">Coverage Global</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">&gt;85%</div>
          <div class="metric-label">Modules Critiques</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">5</div>
          <div class="metric-label">Algorithmes Opérationnels</div>
        </div>
      </div>
      <p class="content">Scores normalisés 0-100, calcul de confiance, explications automatiques.</p>'''
            },
            {
                'num': 8,
                'content': '''<h1>Découvrir les Algorithmes</h1>
      <h2>Matching intelligent pour prospection B2B</h2>
      <p class="content">5 algorithmes spécialisés basés sur des modèles mathématiques.</p>
      <p class="content">26/26 tests passent, coverage 62% (modules critiques &gt;85%).</p>
      <p class="content" style="font-size: 20px; margin-top: 40px;">
        #SquidResearch #Matching #Algorithmes #IA #DataDriven #B2B #TechInnovation #Python #Django #Recrutement #Sourcing
      </p>'''
            }
        ]
    },
    'article-4-import-csv-intelligent': {
        'episode': 'Épisode 4',
        'badge': 'Épisode 4',
        'slides': [
            {
                'num': 1,
                'content': '''<h1>Import CSV Intelligent</h1>
      <h2>145 entreprises ignorées → 145 créées : comment ?</h2>
      <p class="content">Détection automatique des colonnes et normalisation intelligente</p>
      <div class="metrics-grid">
        <div class="metric-card" style="animation-delay: 0.3s;">
          <div class="metric-value">145</div>
          <div class="metric-label">Créées</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.4s;">
          <div class="metric-value">0</div>
          <div class="metric-label">Ignorées</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.5s;">
          <div class="metric-value">100%</div>
          <div class="metric-label">Succès</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.6s;">
          <div class="metric-value">Auto</div>
          <div class="metric-label">Détection Colonnes</div>
        </div>
      </div>'''
            },
            {
                'num': 2,
                'content': '''<h1>Le Problème</h1>
      <h2>Module normalisation "tout pourri"</h2>
      <p class="content">Avant la refactorisation : 145 éléments ignorés, 0 créés, 0 mis à jour.</p>
      <p class="content">Le module ne détectait pas correctement les colonnes CSV, causant 100% d'échec.</p>
      <p class="content">Variantes de colonnes non supportées (Entreprise, Société, Nom, Company, etc.).</p>'''
            },
            {
                'num': 3,
                'content': '''<h1>La Solution</h1>
      <h2>IntelligentMapper + détection auto colonnes</h2>
      <p class="content">Détection automatique intelligente des colonnes avec reconnaissance de multiples variantes.</p>
      <p class="content">Transformation automatique vers schéma unifié avant import.</p>
      <p class="content">Fallback intelligent si nom non trouvé dans les colonnes normalisées.</p>'''
            },
            {
                'num': 4,
                'content': '''<h1>Détection Intelligente</h1>
      <h2>Multi-variantes supportées</h2>
      <p class="content">Reconnaissance automatique de :</p>
      <p class="content">• Entreprise, Société, Nom, Company, Organisation</p>
      <p class="content">• Domaine, Domain, Website, URL, Site Web</p>
      <p class="content">• Recherche insensible à la casse avec fallback intelligent.</p>'''
            },
            {
                'num': 5,
                'content': '''<h1>Normalisation</h1>
      <h2>Transformation automatique</h2>
      <p class="content">Chaque ligne CSV est normalisée vers un schéma unifié avant import.</p>
      <p class="content">Nettoyage automatique : extraction domaine depuis URLs, suppression "www."</p>
      <p class="content">Conservation des données brutes dans _raw_data pour référence.</p>'''
            },
            {
                'num': 6,
                'content': '''<h1>Résultats</h1>
      <h2>100% de succès</h2>
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">145</div>
          <div class="metric-label">Créées</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">0</div>
          <div class="metric-label">Ignorées</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">100%</div>
          <div class="metric-label">Succès</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Auto</div>
          <div class="metric-label">Détection</div>
        </div>
      </div>
      <p class="content">Avant : 145 ignorés → Après : 145 créés (100% succès)</p>'''
            },
            {
                'num': 7,
                'content': '''<h1>Tester l'Import Intelligent</h1>
      <h2>Normalisation automatique pour CSV</h2>
      <p class="content">Détection automatique des colonnes avec IntelligentMapper.</p>
      <p class="content">Support multi-variantes, fallback intelligent, nettoyage automatique.</p>
      <p class="content" style="font-size: 20px; margin-top: 40px;">
        #SquidResearch #ImportCSV #Normalisation #IA #DataDriven #B2B #TechInnovation #Python #Django #Automatisation
      </p>'''
            }
        ]
    },
    'article-5-15-job-boards-francais': {
        'episode': 'Épisode 5',
        'badge': 'Épisode 5',
        'slides': [
            {
                'num': 1,
                'content': '''<h1>15 Job Boards Français</h1>
      <h2>Comment chercher sur 15 job boards en 1 clic ?</h2>
      <p class="content">Service unifié pour rechercher des offres d'emploi sur les 15 principaux job boards français</p>
      <div class="metrics-grid">
        <div class="metric-card" style="animation-delay: 0.3s;">
          <div class="metric-value">15</div>
          <div class="metric-label">Job Boards</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.4s;">
          <div class="metric-value">6</div>
          <div class="metric-label">Nouveaux Connecteurs</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.5s;">
          <div class="metric-value">Parallèle</div>
          <div class="metric-label">Recherche Async</div>
        </div>
        <div class="metric-card" style="animation-delay: 0.6s;">
          <div class="metric-value">Auto</div>
          <div class="metric-label">Déduplication</div>
        </div>
      </div>'''
            },
            {
                'num': 2,
                'content': '''<h1>Le Problème</h1>
      <h2>Recherche manuelle = 15 sites à visiter</h2>
      <p class="content">Sans automatisation, il faut visiter manuellement chaque job board pour trouver des offres.</p>
      <p class="content">Chaque site a sa propre interface, ses propres critères de recherche.</p>
      <p class="content">Temps perdu, résultats dispersés, pas de vue unifiée.</p>'''
            },
            {
                'num': 3,
                'content': '''<h1>La Solution</h1>
      <h2>Service unifié 15 job boards</h2>
      <p class="content">Un seul point d'entrée pour rechercher sur tous les job boards français.</p>
      <p class="content">APIs officielles prioritaires, fallback scraping si API non disponible.</p>
      <p class="content">Recherche parallèle asynchrone pour performance optimale.</p>'''
            },
            {
                'num': 4,
                'content': '''<h1>Job Boards Supportés</h1>
      <h2>15 principaux job boards français</h2>
      <p class="content" style="font-size: 20px; line-height: 1.6;">
        Indeed • HelloWork • APEC • LinkedIn Jobs • Welcome to the Jungle<br>
        Monster • Glassdoor • Pôle Emploi • Choose Your Boss<br>
        RegionsJob • Cadremploi • JobTeaser • Talent.io<br>
        LesJeudis • Qapa
      </p>
      <p class="content">6 nouveaux connecteurs créés : Pôle Emploi, Choose Your Boss, JobTeaser, Talent.io, LesJeudis, Qapa</p>'''
            },
            {
                'num': 5,
                'content': '''<h1>Architecture</h1>
      <h2>APIs prioritaires + fallback scraping</h2>
      <p class="content">Utilisation prioritaire des APIs officielles quand disponibles.</p>
      <p class="content">Fallback automatique sur scraping si API non disponible.</p>
      <p class="content">Rate limiting et anti-blocage intégrés pour chaque job board.</p>
      <p class="content">Cache pour éviter les requêtes répétées.</p>'''
            },
            {
                'num': 6,
                'content': '''<h1>Fonctionnalités</h1>
      <h2>Recherche parallèle, déduplication, rate limiting</h2>
      <p class="content">Recherche parallèle asynchrone : tous les job boards interrogés simultanément.</p>
      <p class="content">Déduplication automatique : résultats unifiés sans doublons.</p>
      <p class="content">Rate limiting adaptatif par job board pour éviter les blocages.</p>
      <p class="content">Gestion d'erreurs robuste : continuation même en cas d'échec partiel.</p>'''
            },
            {
                'num': 7,
                'content': '''<h1>Résultats</h1>
      <h2>Recherche multi-sources en &lt; 10s</h2>
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-value">15</div>
          <div class="metric-label">Job Boards</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">&lt;10s</div>
          <div class="metric-label">Temps Réponse</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Parallèle</div>
          <div class="metric-label">Recherche Async</div>
        </div>
        <div class="metric-card">
          <div class="metric-value">Auto</div>
          <div class="metric-label">Déduplication</div>
        </div>
      </div>
      <p class="content">Un seul clic pour rechercher sur 15 job boards simultanément.</p>'''
            },
            {
                'num': 8,
                'content': '''<h1>Découvrir l'Intégration</h1>
      <h2>15 job boards français unifiés</h2>
      <p class="content">Service unifié avec APIs prioritaires et fallback scraping.</p>
      <p class="content">Recherche parallèle asynchrone, déduplication automatique, rate limiting.</p>
      <p class="content" style="font-size: 20px; margin-top: 40px;">
        #SquidResearch #JobBoards #RechercheEmploi #B2B #DataDriven #TechInnovation #Python #Django #Automation #Recrutement
      </p>'''
            }
        ]
    }
}

def generate_slides():
    """Génère toutes les slides pour tous les articles"""
    for article_slug, article_data in ARTICLES.items():
        article_dir = BASE_DIR / 'articles' / article_slug / 'Presentation'
        article_dir.mkdir(parents=True, exist_ok=True)
        
        for slide_data in article_data['slides']:
            slide_path = article_dir / f"slide{slide_data['num']}.html"
            
            content = SLIDE_TEMPLATE.format(
                episode=article_data['episode'],
                num=slide_data['num'],
                badge=article_data['badge'],
                content=slide_data['content']
            )
            
            slide_path.write_text(content, encoding='utf-8')
            print(f"✅ Créé : {slide_path}")

if __name__ == '__main__':
    generate_slides()
    print("\n🎉 Toutes les slides ont été générées !")

