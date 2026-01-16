#!/usr/bin/env python3
"""
Script de correction du dossier marketing : suppression emojis, réduction listes,
remplacement coordonnées hardcodées, application règles anti-tonalité IA.
"""

import re
import sys
from pathlib import Path


def remove_emojis(text: str) -> str:
    """Supprime les emojis du texte."""
    # Pattern pour les emojis Unicode (général)
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub("", text)


def replace_hardcoded_contacts(text: str) -> str:
    """Remplace les coordonnées hardcodées par des références."""
    # Email
    text = re.sub(
        r"contact@squidresearch\.com",
        "[CONTACT_EMAIL]",
        text,
        flags=re.IGNORECASE,
    )
    
    # LinkedIn
    text = re.sub(
        r"https?://(www\.)?linkedin\.com/in/lucastymen/?",
        "[LINKEDIN_URL]",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"linkedin\.com/in/lucastymen",
        "[LINKEDIN_URL]",
        text,
        flags=re.IGNORECASE,
    )
    
    # GitHub
    text = re.sub(
        r"https?://(www\.)?github\.com/LucasTymen/squidresearch",
        "[GITHUB_URL]",
        text,
        flags=re.IGNORECASE,
    )
    
    return text


def remove_llm_phrases(text: str) -> str:
    """Supprime les phrases typiques des LLM."""
    patterns = [
        # Formules de cadrage
        (r"Dans un monde où[^.]*\.", ""),
        (r"À l'ère du[^.]*\.", ""),
        (r"Alors que[^.]*\.", ""),
        
        # Intensifieurs à faible coût (COMMENTÉ : trop agressif, nécessite contexte)
        # (r"\b(crucial|essentiel|absolument|vraiment|énormément)\b", ""),
        
        # Marqueurs artificiels de transition
        (r"\bEt pourtant[^.]*\.", ""),
        (r"\bMais ce n'est pas tout[^.]*\.", ""),
        (r"\bCependant[^.]*\.", ""),
        (r"\bNéanmoins[^.]*\.", ""),
        
        # Métadiscours
        (r"Comme nous l'avons vu[^.]*\.", ""),
        (r"Comme nous allons le voir[^.]*\.", ""),
        (r"Comme mentionné[^.]*\.", ""),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    return text


def reduce_excessive_bullet_points(text: str) -> str:
    """
    Transforme certaines listes à puces en paragraphes pour réduire
    la structure hyper-segmentée. Garde les listes courtes (2-3 items).
    """
    lines = text.split("\n")
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Détecte le début d'une liste à puces (3+ items consécutifs)
        if re.match(r"^[\s]*-[\s]+", line):
            bullet_items = []
            j = i
            
            # Collecte les items consécutifs
            while j < len(lines) and re.match(r"^[\s]*-[\s]+", lines[j]):
                bullet_items.append(lines[j].strip()[2:].strip())  # Enlève "- "
                j += 1
            
            # Si 4+ items, on pourrait les transformer en paragraphe
            # Mais pour l'instant, on garde les listes (trop risqué de transformer automatiquement)
            # On supprime juste les emojis dans les listes
            for item in bullet_items:
                cleaned_item = remove_emojis(item)
                result.append(f"- {cleaned_item}")
            
            i = j
        else:
            result.append(line)
            i += 1
    
    return "\n".join(result)


def clean_section_headers(text: str) -> str:
    """Nettoie les en-têtes de section (supprime emojis)."""
    lines = text.split("\n")
    result = []
    
    for line in lines:
        # Détecte les en-têtes (commencent par ##)
        if re.match(r"^##+[\s]+", line):
            cleaned = remove_emojis(line)
            result.append(cleaned)
        else:
            result.append(line)
    
    return "\n".join(result)


def apply_corrections(content: str) -> str:
    """Applique toutes les corrections au contenu."""
    # 1. Supprimer les emojis
    content = remove_emojis(content)
    
    # 2. Nettoyer les en-têtes
    content = clean_section_headers(content)
    
    # 3. Remplacer coordonnées hardcodées
    content = replace_hardcoded_contacts(content)
    
    # 4. Supprimer phrases LLM typiques
    content = remove_llm_phrases(content)
    
    # 5. Réduire listes excessives (conservatif)
    content = reduce_excessive_bullet_points(content)
    
    # 6. Nettoyer les espaces multiples
    content = re.sub(r"\n{3,}", "\n\n", content)
    content = re.sub(r"[ \t]+", " ", content)
    
    return content


def main():
    """Point d'entrée principal."""
    if len(sys.argv) < 2:
        print("Usage: python correct_dossier_marketing.py <fichier.md> [--dry-run]")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv
    
    if not file_path.exists():
        print(f"Erreur: Le fichier {file_path} n'existe pas")
        sys.exit(1)
    
    # Lire le fichier
    content = file_path.read_text(encoding="utf-8")
    
    # Appliquer les corrections
    corrected = apply_corrections(content)
    
    if dry_run:
        # Afficher les différences
        print("=== CORRECTIONS APPLIQUÉES ===")
        print(f"Taille originale: {len(content)} caractères")
        print(f"Taille corrigée: {len(corrected)} caractères")
        print(f"Différence: {len(corrected) - len(content)} caractères")
        print("\n=== PREVIEW (1000 premiers caractères) ===")
        print(corrected[:1000])
    else:
        # Sauvegarder
        backup_path = file_path.with_suffix(".md.backup")
        file_path.rename(backup_path)
        print(f"Backup créé: {backup_path}")
        
        file_path.write_text(corrected, encoding="utf-8")
        print(f"Fichier corrigé: {file_path}")
        print("\n⚠️  NOTE: Certaines corrections nécessitent une révision manuelle:")
        print("  - Transformation listes → paragraphes (ton naturel)")
        print("  - Réécriture phrases pour éviter structure hyper-segmentée")
        print("  - Vérification cohérence après suppression phrases LLM")


if __name__ == "__main__":
    main()

