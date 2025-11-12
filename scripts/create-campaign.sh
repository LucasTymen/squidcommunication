#!/bin/bash

# ==========================================
# create-campaign.sh
# ==========================================
# Script pour créer rapidement une nouvelle campagne
#
# Usage: ./create-campaign.sh <campaign-slug> [platforms...]
# Example: ./create-campaign.sh "feature-matching" linkedin instagram
# ==========================================

set -euo pipefail

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Vérifier les arguments
if [ $# -lt 1 ]; then
    echo "Usage: $0 <campaign-slug> [platforms...]"
    echo ""
    echo "Example:"
    echo "  $0 feature-matching linkedin instagram"
    echo ""
    echo "Platforms supportées: linkedin, instagram, newsletter, blog"
    exit 1
fi

SLUG="$1"
shift
PLATFORMS=("$@")

# Si aucune plateforme spécifiée, demander
if [ ${#PLATFORMS[@]} -eq 0 ]; then
    echo "Plateformes à cibler (séparées par des espaces) :"
    echo "  Options: linkedin instagram newsletter blog"
    read -p "> " -a PLATFORMS
fi

# Générer l'ID de campagne avec date
DATE=$(date +%Y-%m)
CAMPAIGN_ID="${DATE}-${SLUG}"
CAMPAIGN_DIR="../campaigns/${CAMPAIGN_ID}"

echo "========================================"
echo -e "${BLUE}🚀 Création de campagne${NC}"
echo "========================================"
echo ""
echo "ID: $CAMPAIGN_ID"
echo "Plateformes: ${PLATFORMS[*]}"
echo ""

# Vérifier que la campagne n'existe pas déjà
if [ -d "$CAMPAIGN_DIR" ]; then
    echo -e "${YELLOW}⚠️  La campagne $CAMPAIGN_ID existe déjà !${NC}"
    read -p "Écraser ? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Annulé."
        exit 1
    fi
    rm -rf "$CAMPAIGN_DIR"
fi

# Créer la structure
echo -e "${BLUE}📁 Création de la structure...${NC}"

mkdir -p "$CAMPAIGN_DIR"
mkdir -p "$CAMPAIGN_DIR/assets/original"
mkdir -p "$CAMPAIGN_DIR/assets/sanitized"
mkdir -p "$CAMPAIGN_DIR/archive"

# Créer un dossier pour chaque plateforme
for platform in "${PLATFORMS[@]}"; do
    mkdir -p "$CAMPAIGN_DIR/$platform"
    echo "  ✓ $platform/"
done

# Générer le fichier campaign.json
echo -e "${BLUE}📝 Génération de campaign.json...${NC}"

PLATFORMS_JSON=$(printf ',"%s"' "${PLATFORMS[@]}")
PLATFORMS_JSON="[${PLATFORMS_JSON:1}]"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > "$CAMPAIGN_DIR/campaign.json" <<EOF
{
  "campaign_id": "$CAMPAIGN_ID",
  "created_at": "$TIMESTAMP",
  "updated_at": "$TIMESTAMP",
  "status": "draft",
  "objective": "",
  "message_key": "",
  "platforms": $PLATFORMS_JSON,
  "mcp_collaboration": {
    "calendar_event_id": "",
    "notion_template": "",
    "drive_folder": "",
    "tasks": []
  },
  "content": {
    "summary": "",
    "hashtags": [
      "#SquidResearch"
    ],
    "cta": ""
  },
  "links": {
    "assets": "campaigns/$CAMPAIGN_ID/assets/",
    "analytics": "campaigns/$CAMPAIGN_ID/archive/analytics.json"
  },
  "posts": [],
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
  "kpis": {
    "target": {
      "linkedin_impressions": 0,
      "linkedin_engagement": 0,
      "instagram_views": 0,
      "instagram_engagement": 0,
      "cta_clicks": 0,
      "website_visits": 0
    },
    "actual": {
      "linkedin_impressions": 0,
      "linkedin_engagement": 0,
      "instagram_views": 0,
      "instagram_engagement": 0,
      "cta_clicks": 0,
      "website_visits": 0
    }
  },
  "notes": []
}
EOF

# Créer des fichiers templates pour chaque plateforme
for platform in "${PLATFORMS[@]}"; do
    case $platform in
        linkedin)
            cp "../templates/linkedin-post.md" "$CAMPAIGN_DIR/linkedin/post-1.md"
            echo "  ✓ linkedin/post-1.md créé"
            ;;
        instagram)
            cp "../templates/instagram-story.md" "$CAMPAIGN_DIR/instagram/story-1.md"
            echo "  ✓ instagram/story-1.md créé"
            ;;
        newsletter)
            touch "$CAMPAIGN_DIR/newsletter/email-1.md"
            echo "  ✓ newsletter/email-1.md créé"
            ;;
        blog)
            touch "$CAMPAIGN_DIR/blog/article-1.md"
            echo "  ✓ blog/article-1.md créé"
            ;;
    esac
done

# Créer un README pour la campagne
cat > "$CAMPAIGN_DIR/README.md" <<EOF
# Campagne : $CAMPAIGN_ID

## 📅 Informations

- **Créée le** : $TIMESTAMP
- **Statut** : Draft
- **Plateformes** : ${PLATFORMS[*]}

## 🎯 Objectifs

[À remplir]

## 📋 Checklist

- [ ] Compléter campaign.json (objectifs, message_key, KPIs)
- [ ] Rédiger les contenus pour chaque plateforme
- [ ] Créer les assets visuels (captures, designs)
- [ ] Placer les assets dans \`assets/original/\`
- [ ] Créer versions floutées dans \`assets/sanitized/\`
- [ ] Valider la sécurité : \`./scripts/validate-campaign.sh campaigns/$CAMPAIGN_ID\`
- [ ] Planifier avec Claude (GCal, Drive, Notion)
- [ ] Publier selon le planning
- [ ] Collecter les analytics dans \`archive/analytics.json\`

## 🔗 Références

- campaign.json : \`campaigns/$CAMPAIGN_ID/campaign.json\`
- Log principal : \`squidResearch/communication_projet.md\`
EOF

echo ""
echo "========================================"
echo -e "${GREEN}✅ Campagne créée avec succès !${NC}"
echo "========================================"
echo ""
echo "📁 Localisation : $CAMPAIGN_DIR"
echo ""
echo "Prochaines étapes :"
echo "  1. Éditer campaign.json (objectifs, KPIs)"
echo "  2. Rédiger les contenus"
echo "  3. Créer les assets"
echo "  4. Valider : ./scripts/validate-campaign.sh campaigns/$CAMPAIGN_ID"
echo ""
