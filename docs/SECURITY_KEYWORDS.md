# 🔒 Liste de Mots-Clés Sensibles - Articles

**Objectif** : Éviter de divulguer des informations techniques sensibles dans les articles publics.

**Utilisation** : Scripts de validation et génération de contenu doivent détecter et alerter sur ces termes.

---

## 🚫 Mots-Clés à Éviter Absolument

### Outils OSINT / Forensics
- `OSINT`
- `forensic`
- `kali linux`
- `the harvester`
- `sherlock`
- `holehe`
- `h8mail`
- `recon-ng`
- `maltego`
- `shodan`
- `censys`
- `whois`
- `nmap`
- `metasploit`
- `burp suite`
- `wireshark`

### Outils de Qualité Détournés
- Tous les noms d'outils de qualité utilisés de manière détournée
- Outils de sécurité utilisés pour d'autres fins

### Dépendances Techniques Sensibles
- Noms de packages Python liés à l'OSINT
- Bibliothèques de scraping avancées utilisées de manière détournée
- Outils de sécurité réseau

### Informations Techniques Sensibles
- IPs internes (`192.168.*`, `10.*`, `172.16.*`)
- Credentials (mots de passe, tokens, API keys)
- URLs internes non publiques
- Chemins de fichiers système
- Configurations Docker internes sensibles
- Secrets de production

---

## ⚠️ Mots-Clés à Utiliser avec Prudence

### Techniques Génériques (OK si expliqués génériquement)
- `enrichissement multi-sources` ✅ (au lieu de "sherlock + holehe")
- `scraping anonymisé` ✅ (au lieu de "Tor + OSINT")
- `validation emails` ✅ (au lieu de détails techniques)
- `recherche contacts B2B` ✅ (au lieu de détails OSINT)

### Alternatives Recommandées

| ❌ À éviter | ✅ Alternative recommandée |
|------------|---------------------------|
| "J'utilise Sherlock et Holehe" | "Enrichissement multi-sources validées" |
| "OSINT tools" | "Outils d'enrichissement B2B" |
| "Forensic analysis" | "Analyse de données" |
| "Kali Linux tools" | "Outils de sécurité réseau" |
| "The Harvester" | "Recherche automatique de contacts" |

---

## 🔍 Patterns de Détection

### Regex Patterns à Détecter
```python
# IPs internes
r'192\.168\.\d+\.\d+'
r'10\.\d+\.\d+\.\d+'
r'172\.(1[6-9]|2[0-9]|3[0-1])\.\d+\.\d+'

# Credentials patterns
r'password\s*[:=]\s*\S+'
r'api[_-]?key\s*[:=]\s*\S+'
r'token\s*[:=]\s*\S+'
r'secret\s*[:=]\s*\S+'

# Outils OSINT (case-insensitive)
r'\b(osint|forensic|kali|harvester|sherlock|holehe|h8mail|recon-ng|maltego|shodan|censys)\b'
```

---

## ✅ Validation Automatique

Les scripts de génération et validation doivent :
1. Scanner le contenu Markdown généré
2. Détecter les patterns sensibles
3. Alerter l'utilisateur avec suggestions d'alternatives
4. Bloquer la publication si termes critiques détectés

---

**Dernière mise à jour** : 2025-01-XX  
**Maintenu par** : Scripts automatisés + validation manuelle

