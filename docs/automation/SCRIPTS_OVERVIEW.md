# ⚙️ Scripts & Automations - SquidCommunication

| Script | Description | Mode | Status |
|--------|-------------|------|--------|
| `scripts/create_campaign.py` | Génère l'ossature d'une campagne (folders, `campaign.json`, brouillons Markdown) | CLI | ✅ En place |
| `scripts/save_contact_result.py` | Enregistre les résultats d'enrichissement (contacts + hypothèses d'e-mails) dans `data/communication/contact_results.json` | CLI | ✅ En place |
| `scripts/update_metrics.py` | Agrège les analytics (CSV/JSON) et met à jour les KPIs | CLI | ⏳ À venir |
| `scripts/sync_logs.sh` | Synchronisation bilatérale des journaux de communication | Shell | ✅ En place |
| `scripts/sync.py` | Orchestration haute-niveau (logs + campagnes + templates) | CLI | ⏳ À venir |

## Convention CLI

- Tous les scripts Python utilisent `argparse`
- Option `--dry-run` disponible pour simuler les opérations (quand pertinent)
- Option `--pull` / `--push` pour gérer la direction de synchro
- Les scripts respectent le fichier `config/sync_paths.yml`

## Exemples d’utilisation

### Créer une campagne LinkedIn
```bash
python scripts/create_campaign.py "2025-12-ai-feuilleton"   --platforms linkedin instagram   --posts 3   --series "Feuilleton SquidResearch"   --episode 1   --start-date 2025-12-01
```

### Mettre à jour les KPIs
```bash
python scripts/update_metrics.py campaigns/2025-12-ai-feuilleton --source csv
```

### Synchroniser les logs
```bash
./scripts/sync_logs.sh --direction pull   # ramène les updates depuis squidResearch
./scripts/sync_logs.sh --direction push   # pousse les modifications locales
```

### Sauvegarder un contact enrichi
```bash
python scripts/save_contact_result.py   --campaign 2025-11-hub-communication   --full-name "Alice Martin"   --company "Acme"   --domain acme.com   --hypothesis alice.martin@acme.com:valid   --notes "Scraper + Maltego"
```

---

> Pour toute modification, mettre à jour ce fichier ainsi que `docs/workflow.md`
