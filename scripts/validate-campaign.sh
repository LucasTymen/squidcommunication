#!/bin/bash

# ==========================================
# validate-campaign.sh
# ==========================================
# Script de validation sécurité pour campagnes SquidResearch
# Vérifie qu'aucune donnée sensible n'est présente avant publication
#
# Usage: ./validate-campaign.sh <campaign-folder>
# Example: ./validate-campaign.sh campaigns/2025-11-hub-communication
# ==========================================

set -euo pipefail

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compteurs
WARNINGS=0
ERRORS=0
CAMPAIGN_DIR="$1"

# Patterns à vérifier
PATTERNS_CRITICAL=(
    "password"
    "token"
    "secret"
    "api[_-]?key"
    "bearer"
    "authorization:"
    "sk-[a-zA-Z0-9]{48}"  # OpenAI keys
    "AIza[0-9A-Za-z_-]{35}"  # Google API keys
)

PATTERNS_WARNING=(
    "192\.168\.[0-9]{1,3}\.[0-9]{1,3}"  # Private IPs
    "10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"  # Private IPs
    "localhost"
    "127\.0\.0\.1"
    "@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}"  # Emails (might be ok)
)

echo "========================================"
echo "🔒 Validation Sécurité Campagne"
echo "========================================"
echo ""

# Vérifier que le dossier existe
if [ ! -d "$CAMPAIGN_DIR" ]; then
    echo -e "${RED}❌ ERREUR: Dossier $CAMPAIGN_DIR introuvable${NC}"
    exit 1
fi

echo "📁 Campagne: $CAMPAIGN_DIR"
echo ""

# ==========================================
# 1. VÉRIFICATIONS CRITIQUES (ERREURS)
# ==========================================
echo "🔴 Vérifications critiques (blocantes)..."
echo ""

for pattern in "${PATTERNS_CRITICAL[@]}"; do
    echo -n "  Recherche: $pattern... "

    # Recherche dans tous les fichiers sauf binaires
    # Exclure campaign.json (contient des champs "token", "secret" légitimes)
    if grep -r -i -E "$pattern" "$CAMPAIGN_DIR/assets/sanitized/" 2>/dev/null || \
       grep -r -i -E "$pattern" "$CAMPAIGN_DIR"/*/*.json 2>/dev/null || \
       grep -r -i -E "$pattern" "$CAMPAIGN_DIR"/*/*.md 2>/dev/null; then

        echo -e "${RED}TROUVÉ ❌${NC}"
        ERRORS=$((ERRORS + 1))

        # Montrer les fichiers concernés (exclure campaign.json)
        grep -r -l -i -E "$pattern" "$CAMPAIGN_DIR" 2>/dev/null | grep -v "campaign.json" | while read file; do
            echo -e "    ${RED}→ $file${NC}"
        done
    else
        echo -e "${GREEN}OK ✓${NC}"
    fi
done

echo ""

# ==========================================
# 2. VÉRIFICATIONS WARNINGS (NON-BLOCANTES)
# ==========================================
echo "🟡 Vérifications warnings (à vérifier)..."
echo ""

for pattern in "${PATTERNS_WARNING[@]}"; do
    echo -n "  Recherche: $pattern... "

    if grep -r -i -E "$pattern" "$CAMPAIGN_DIR/assets/sanitized/" 2>/dev/null || \
       grep -r -i -E "$pattern" "$CAMPAIGN_DIR"/*.json 2>/dev/null || \
       grep -r -i -E "$pattern" "$CAMPAIGN_DIR"/*/*.md 2>/dev/null; then

        echo -e "${YELLOW}TROUVÉ ⚠️${NC}"
        WARNINGS=$((WARNINGS + 1))

        # Montrer les fichiers concernés
        grep -r -l -i -E "$pattern" "$CAMPAIGN_DIR" 2>/dev/null | while read file; do
            echo -e "    ${YELLOW}→ $file${NC}"
        done
    else
        echo -e "${GREEN}OK ✓${NC}"
    fi
done

echo ""

# ==========================================
# 3. VÉRIFICATIONS STRUCTURE
# ==========================================
echo "📂 Vérifications structure..."
echo ""

# Vérifier la présence de campaign.json
if [ -f "$CAMPAIGN_DIR/campaign.json" ]; then
    echo -e "  ${GREEN}✓ campaign.json présent${NC}"
else
    echo -e "  ${RED}✗ campaign.json manquant${NC}"
    ERRORS=$((ERRORS + 1))
fi

# Vérifier la présence du dossier assets/sanitized
if [ -d "$CAMPAIGN_DIR/assets/sanitized" ]; then
    echo -e "  ${GREEN}✓ assets/sanitized/ présent${NC}"

    # Compter les assets
    num_assets=$(find "$CAMPAIGN_DIR/assets/sanitized" -type f | wc -l)
    echo -e "    ${num_assets} fichier(s) trouvé(s)"
else
    echo -e "  ${YELLOW}⚠ assets/sanitized/ manquant (normal si pas d'assets)${NC}"
fi

# Vérifier que assets/original n'est pas vide si sanitized existe
if [ -d "$CAMPAIGN_DIR/assets/original" ]; then
    num_original=$(find "$CAMPAIGN_DIR/assets/original" -type f | wc -l)
    num_sanitized=$(find "$CAMPAIGN_DIR/assets/sanitized" -type f 2>/dev/null | wc -l)

    if [ $num_original -gt 0 ] && [ $num_sanitized -eq 0 ]; then
        echo -e "  ${YELLOW}⚠ Assets original présents mais aucun sanitized${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
fi

echo ""

# ==========================================
# 4. RÉSUMÉ FINAL
# ==========================================
echo "========================================"
echo "📊 RÉSUMÉ"
echo "========================================"
echo ""
echo -e "Erreurs critiques: ${RED}$ERRORS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

if [ $ERRORS -gt 0 ]; then
    echo -e "${RED}❌ VALIDATION ÉCHOUÉE${NC}"
    echo "⚠️  Des données sensibles ont été détectées."
    echo "   Corrigez les erreurs avant publication."
    echo ""
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}⚠️  VALIDATION AVEC WARNINGS${NC}"
    echo "   Vérifiez manuellement les warnings avant publication."
    echo ""
    exit 0
else
    echo -e "${GREEN}✅ VALIDATION RÉUSSIE${NC}"
    echo "   La campagne peut être publiée en toute sécurité."
    echo ""
    exit 0
fi
