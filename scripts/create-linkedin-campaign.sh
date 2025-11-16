#!/bin/bash

# ==========================================
# create-linkedin-campaign.sh
# ==========================================
# Script pour créer rapidement une campagne LinkedIn multi-messages
# Génère : campaign.json, posts (simple ou carousel), schedule.json, assets/
#
# Usage: ./create-linkedin-campaign.sh <slug> <type> <nb_messages>
# Example: ./create-linkedin-campaign.sh "feature-matching" simple 5
# ==========================================

set -euo pipefail

# Couleurs
GREEN="\033[0;32m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m"

# Vérifier les arguments
if [ $# -lt 3 ]; then
    echo -e "${RED}Usage: $0 <slug> <type> <nb_messages>${NC}"
    echo ""
    echo "Arguments:"
    echo "  slug         : Identifiant de la campagne (ex: feature-matching)"
    echo "  type         : simple ou carousel"
    echo "  nb_messages  : Nombre de posts (3 à 5)"
    echo ""
    echo "Examples:"
    echo "  $0 feature-matching simple 5"
    echo "  $0 tutorial-enrichment carousel 3"
    exit 1
fi

SLUG="$1"
TYPE="$2"
NB_MESSAGES="$3"

# Validation
if [[ ! "$TYPE" =~ ^(simple|carousel)$ ]]; then
    echo -e "${RED}❌ Type invalide. Utilisez simple ou carousel${NC}"
    exit 1
fi

if [[ ! "$NB_MESSAGES" =~ ^[3-5]$ ]]; then
    echo -e "${RED}❌ Nombre de messages invalide. Utilisez 3, 4 ou 5${NC}"
    exit 1
fi

# Chemins
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DATE=$(date +%Y-%m)
CAMPAIGN_ID="${DATE}-${SLUG}"
CAMPAIGN_DIR="${REPO_ROOT}/campaigns/${CAMPAIGN_ID}"
TEMPLATES_DIR="${REPO_ROOT}/templates"

# Template à utiliser
if [ "$TYPE" = "simple" ]; then
    POST_TEMPLATE="${TEMPLATES_DIR}/linkedin-post-simple.md"
else
    POST_TEMPLATE="${TEMPLATES_DIR}/linkedin-post-carousel.md"
fi

# Vérifier que le template existe
if [ ! -f "$POST_TEMPLATE" ]; then
    echo -e "${RED}❌ Template non trouvé : $POST_TEMPLATE${NC}"
    exit 1
fi

echo "========================================"
echo -e "${BLUE}🚀 Création campagne LinkedIn${NC}"
echo "========================================"
echo ""
echo -e "  ${GREEN}Campagne${NC} : ${CAMPAIGN_ID}"
echo -e "  ${GREEN}Type${NC}     : ${TYPE}"
echo -e "  ${GREEN}Messages${NC} : ${NB_MESSAGES}"
echo ""

# Créer la structure
mkdir -p "${CAMPAIGN_DIR}/linkedin"
mkdir -p "${CAMPAIGN_DIR}/assets/original"
mkdir -p "${CAMPAIGN_DIR}/assets/sanitized"
mkdir -p "${CAMPAIGN_DIR}/archive"

# Générer campaign.json
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date +"%Y-%m-%dT%H:%M:%SZ")
python3 <<PYTHON_SCRIPT
import json
from datetime import datetime, timedelta

campaign_id = "${CAMPAIGN_ID}"
now = datetime.utcnow().isoformat() + "Z"

campaign = {
    "campaign_id": campaign_id,
    "created_at": now,
    "updated_at": now,
    "status": "draft",
    "objective": "[À définir : Notoriété / Engagement / Lead Gen / Recrutement]",
    "message_key": "[Message clé de la campagne en une phrase]",
    "platforms": ["linkedin"],
    "post_type": "${TYPE}",
    "nb_posts": ${NB_MESSAGES},
    "mcp_collaboration": {
        "calendar_event_id": "",
        "notion_template": "",
        "drive_folder": "",
        "tasks": [
            "Créer événements GCal pour chaque date de publication",
            "Organiser dossier Drive pour assets campagne",
            "Générer template Notion pour suivi KPIs",
            "Préparer templates Canvas pour visuels LinkedIn"
        ]
    },
    "content": {
        "summary": "[Résumé de la campagne]",
        "hashtags": [
            "#SquidResearch",
            "#IA",
            "#ProspectionB2B"
        ],
        "cta": "[Appel à l action principal]"
    },
    "links": {
        "assets": f"campaigns/{campaign_id}/assets/",
        "analytics": f"campaigns/{campaign_id}/archive/analytics.json"
    },
    "posts": []
}

# Générer les posts
posts = []
base_date = datetime.now() + timedelta(days=1)
for i in range(1, ${NB_MESSAGES} + 1):
    post_date = base_date + timedelta(days=(i - 1) * 2)
    post_num = f"{i:02d}"
    posts.append({
        "platform": "linkedin",
        "type": "${TYPE}",
        "status": "draft",
        "scheduled_date": post_date.strftime("%Y-%m-%dT10:00:00Z"),
        "title": f"Post {post_num} - [À définir]",
        "file": f"linkedin/post-{post_num}.md"
    })

campaign["posts"] = posts

with open("${CAMPAIGN_DIR}/campaign.json", "w", encoding="utf-8") as f:
    json.dump(campaign, f, indent=2, ensure_ascii=False)
PYTHON_SCRIPT

# Générer les posts depuis templates
echo -e "${YELLOW}📝 Génération des ${NB_MESSAGES} posts...${NC}"

for i in $(seq 1 $NB_MESSAGES); do
    POST_NUM=$(printf "%02d" $i)
    POST_FILE="${CAMPAIGN_DIR}/linkedin/post-${POST_NUM}.md"
    
    # Calculer la date (via Python pour cohérence)
    PUBLISH_DATE=$(python3 -c "from datetime import datetime, timedelta; print((datetime.now() + timedelta(days=1 + ($i - 1) * 2)).strftime(
