# 📊 Modèle de données - Campagnes SquidCommunication

> Version 0.1.0 — 2025-11-13

## Objectifs

- Centraliser les métadonnées de communication dans un format unique et versionné
- Faciliter la génération automatique de contenus et d’analytics
- Permettre la synchronisation bidirectionnelle avec `squidResearch`

## Structure générale (`campaign.json`)

```json
{
  "schema_version": "1.0",
  "campaign_id": "2025-11-hub-communication",
  "slug": "hub-communication",
  "created_at": "2025-11-12T16:25:00Z",
  "updated_at": "2025-11-13T15:30:00Z",
  "owner": "Lucas Tymen",
  "status": "draft",
  "objective": "",
  "message_key": "",
  "narrative_arc": {
    "episode": 1,
    "series": "LinkedIn - Saga de lancement",
    "summary": "",
    "next_episode": "2025-11-hub-communication-episode-02"
  },
  "platforms": ["linkedin", "instagram"],
  "kpis": {
    "target": {
      "linkedin_impressions": 500,
      "instagram_views": 200,
      "cta_clicks": 25
    },
    "actual": {
      "linkedin_impressions": 0,
      "instagram_views": 0,
      "cta_clicks": 0
    },
    "source": "manual | api | synced"
  },
  "mcp_collaboration": {
    "calendar_event_id": "",
    "notion_template": "",
    "drive_folder": "",
    "tasks": []
  },
  "content": {
    "summary": "",
    "angle": "storytelling | technique | data-driven",
    "hashtags": [],
    "cta": "",
    "assets": {
      "original": "campaigns/<slug>/assets/original/",
      "sanitized": "campaigns/<slug>/assets/sanitized/"
    }
  },
  "seo": {
    "meta_title": "",
    "meta_description": "",
    "keywords": [],
    "slug": "",
    "canonical": "",
    "schema_type": "Article | BlogPosting | WebPage",
    "og_image": "",
    "og_type": "article | website",
    "twitter_card": "summary_large_image | summary",
    "lang": "fr",
    "alternate_langs": []
  },
  "posts": [
    {
      "post_id": "linkedin-01",
      "platform": "linkedin",
      "format": "simple | carousel | video",
      "status": "draft | scheduled | published",
      "template": "templates/linkedin/simple_post.json",
      "scheduled_date": "2025-11-15T10:00:00Z",
      "file": "linkedin/post-01.md",
      "analytics": {
        "impressions": 0,
        "engagement": {
          "likes": 0,
          "comments": 0,
          "shares": 0
        }
      }
    }
  ],
  "security_checklist": {
    "no_ip_visible": false,
    "credentials_masked": false,
    "no_tokens": false,
    "client_data_anonymized": false,
    "internal_urls_masked": false,
    "env_vars_hidden": false,
    "validation_script_run": false,
    "validated_by": "",
    "validated_at": ""
  },
  "sync": {
    "source_repo": "squidResearch",
    "last_pulled": null,
    "last_pushed": null,
    "lock": false
  },
  "notes": []
}
```

## Types & contraintes principales

| Champ | Type | Obligatoire | Règles |
|-------|------|-------------|--------|
| `schema_version` | string | ✅ | SemVer (`"1.0"`)|
| `campaign_id` | string | ✅ | Doit correspondre au chemin dossier |
| `narrative_arc` | object | optionnel | Active le mode "série/feuilleton" |
| `kpis.target` | object | ✅ | Clés métriques libres, valeurs numériques |
| `kpis.actual` | object | ✅ | Synchronisé via `update_metrics.py` |
| `posts` | array | ✅ | Min 1, références aux fichiers Markdown générés |
| `sync` | object | ✅ | Gère les opérations bidirectionnelles |

## Fichiers complémentaires

- `analytics.json` : alimenté après publication (`archive/`)
- `report.md` : synthèse qualitative (optionnel)
- `assets/analytics/*.csv` : exports plateforme (convertis via `update_metrics.py`)
- `data/communication/contact_results.json` : stockage des contacts enrichis (hypothèses d’e-mails + statut)

## Roadmap data-driven

1. **v1.0** : structure actuelle (`campaign.json` + templates Markdown)
2. **v1.1** : ajout d'un catalogue d'épisodes/storytelling (`narrative_arc`)
3. **v1.2** : intégration API LinkedIn/Instagram pour remplir `kpis.actual`
4. **v1.3** : ajout section SEO/GEO (`seo` object avec metadata, schema.org, hreflang)
5. **v2.0** : tableau de bord consolidé (`docs/reports/dashboard.json`)

---

> Référence croisée : `docs/workflow.md`, `templates/linkedin/`, `communication_log.md`
