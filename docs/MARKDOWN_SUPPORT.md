# 📝 Support Markdown dans les Articles

**Objectif** : Permettre aux responsables de communication de coller du texte enrichi en Markdown directement dans les articles, avec préservation de la mise en forme.

---

## ✅ Format Supporté

Les fichiers `.md` dans `articles/*/linkedin/` acceptent et préservent le **Markdown standard** :

### Syntaxe Supportée

**Titres**
```markdown
# Titre H1
## Titre H2
### Titre H3
```

**Gras et Italique**
```markdown
**texte en gras**
*texte en italique*
***texte gras et italique***
```

**Listes**
```markdown
- Item 1
- Item 2
  - Sous-item 2.1
  - Sous-item 2.2

1. Item numéroté 1
2. Item numéroté 2
```

**Liens**
```markdown
[Texte du lien](https://example.com)
```

**Code**
```markdown
`code inline`

```python
# Bloc de code
def fonction():
    return "exemple"
```
```

**Séparateurs**
```markdown
---
```

**Citations**
```markdown
> Citation importante
```

**Tableaux**
```markdown
| Colonne 1 | Colonne 2 |
|-----------|-----------|
| Donnée 1  | Donnée 2  |
```

---

## 🎯 Cas d'Usage

### Workflow Recommandé

1. **Rédiger dans un éditeur Markdown** (Notion, Obsidian, VS Code, etc.)
2. **Copier le contenu** avec toute la mise en forme Markdown
3. **Coller directement** dans le fichier `.md` de l'article
4. **Le Markdown est préservé** et peut être utilisé tel quel

### Exemple

**Dans Notion/Obsidian** :
```markdown
## Section importante

Voici un **texte en gras** avec une liste :
- Point 1
- Point 2
```

**Coller dans** `articles/article-X/linkedin/post-01.md` :
→ Le Markdown est préservé ✅

---

## 📋 Compatibilité par Plateforme

### LinkedIn
- ✅ **Gras** : `**texte**`
- ✅ **Italique** : `*texte*`
- ✅ **Listes** : `-` ou `1.`
- ✅ **Titres** : `##` (rendu en gras)
- ✅ **Séparateurs** : `---`
- ⚠️ **Code** : Support limité (utiliser `code` inline)
- ❌ **Tableaux** : Non supporté (convertir en liste)

### Instagram
- ✅ **Gras** : `**texte**`
- ✅ **Italique** : `*texte*`
- ⚠️ **Listes** : Support limité (utiliser des emojis)
- ❌ **Titres** : Non supporté
- ❌ **Code** : Non supporté

### Twitter/X
- ✅ **Gras** : `**texte**`
- ✅ **Italique** : `*texte*`
- ⚠️ **Listes** : Support limité
- ❌ **Titres** : Non supporté
- ❌ **Code** : Non supporté

---

## 🔧 Conversion Automatique (Futur)

**Roadmap** : Script de conversion Markdown → Format plateforme

```bash
# Conversion automatique
python scripts/convert_markdown.py \
  --input articles/article-X/linkedin/post-01.md \
  --platform linkedin \
  --output articles/article-X/linkedin/post-01-linkedin.md
```

**Fonctionnalités prévues** :
- Conversion tableaux → listes (LinkedIn)
- Adaptation longueur (Instagram)
- Optimisation hashtags
- Conversion emojis

---

## 📝 Bonnes Pratiques

### Pour les Responsables de Coms

1. **Utiliser un éditeur Markdown** pour rédiger
   - Notion (export Markdown)
   - Obsidian
   - VS Code
   - Typora

2. **Préserver la structure** :
   - Titres pour les sections
   - Listes pour les points clés
   - Gras pour les métriques importantes

3. **Tester la compatibilité** :
   - Vérifier le rendu sur LinkedIn avant publication
   - Adapter si nécessaire (tableaux → listes)

### Pour les Développeurs

1. **Préserver le Markdown brut** dans les fichiers `.md`
2. **Ne pas convertir** automatiquement (sauf script dédié)
3. **Documenter** les limitations par plateforme

---

## 🎨 Exemple Complet

**Fichier source** (`post-01.md`) :
```markdown
# Titre Principal

## Section 1

Voici un **texte important** avec des métriques :
- Métrique 1 : **93%**
- Métrique 2 : **24x ROI**

## Section 2

> Citation importante

Liste numérotée :
1. Point 1
2. Point 2
```

**Rendu LinkedIn** :
- Titres en gras
- Liste à puces formatée
- Citation indentée
- Gras préservé

---

## 📚 Références

- [Markdown Guide](https://www.markdownguide.org/)
- [LinkedIn Formatting](https://www.linkedin.com/help/linkedin/answer/a521940)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)

---

**Dernière mise à jour** : 2025-12-12

