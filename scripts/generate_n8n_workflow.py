#!/usr/bin/env python3
"""Génère un workflow n8n personnalisé pour publier un article.

Usage:
    python scripts/generate_n8n_workflow.py <article-slug> [--platforms linkedin,facebook]
    
Exemples:
    # Générer workflow pour LinkedIn uniquement
    python scripts/generate_n8n_workflow.py article-3-algorithmes-matching-intelligents --platforms linkedin
    
    # Générer workflow multi-plateformes
    python scripts/generate_n8n_workflow.py article-3 --platforms linkedin,facebook,threads,instagram
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = ROOT / "workflows" / "n8n"
TEMPLATE_WORKFLOW = WORKFLOWS_DIR / "publish_article_social.json"


def generate_workflow(article_slug: str, platforms: List[str]) -> dict:
    """Génère un workflow n8n personnalisé."""
    workflow_name = f"Publish {article_slug} to {', '.join(platforms)}"
    
    # Structure de base du workflow
    workflow = {
        "name": workflow_name,
        "nodes": [],
        "connections": {},
        "pinData": {},
        "settings": {
            "executionOrder": "v1"
        },
        "staticData": None,
        "tags": [],
        "triggerCount": 0,
        "updatedAt": datetime.utcnow().isoformat() + "Z",
        "versionId": "1"
    }
    
    # Node 1: Webhook Trigger
    webhook_id = "webhook-trigger"
    workflow["nodes"].append({
        "parameters": {
            "httpMethod": "POST",
            "path": f"publish-{article_slug}",
            "responseMode": "responseNode",
            "options": {}
        },
        "id": webhook_id,
        "name": "Webhook Trigger",
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 1,
        "position": [250, 300],
        "webhookId": f"publish-{article_slug}"
    })
    
    # Node 2: Read Post Content
    read_id = "read-post-content"
    workflow["nodes"].append({
        "parameters": {
            "command": f"cd /home/lucas/tools/squidCommunication && cat articles/{article_slug}/platforms/{{{{ $json.platform }}}}/post-01.md"
        },
        "id": read_id,
        "name": "Read Post Content",
        "type": "n8n-nodes-base.executeCommand",
        "typeVersion": 1,
        "position": [450, 300]
    })
    
    # Nodes pour chaque plateforme
    platform_nodes = {}
    y_offset = 100
    
    for platform in platforms:
        platform_lower = platform.lower()
        
        # Node de publication
        node_id = f"post-{platform_lower}"
        
        node_config = {
            "id": node_id,
            "name": f"Post to {platform.capitalize()}",
            "typeVersion": 1,
            "position": [650, y_offset],
        }
        
        if platform_lower == "linkedin":
            node_config["type"] = "n8n-nodes-base.linkedIn"
            node_config["parameters"] = {
                "resource": "post",
                "operation": "create",
                "text": "={{ $json.post_text }}",
                "additionalFields": {}
            }
            node_config["credentials"] = {
                "linkedInOAuth2Api": {
                    "id": "linkedin-credentials",
                    "name": "LinkedIn OAuth2 API"
                }
            }
        
        elif platform_lower == "facebook":
            node_config["type"] = "n8n-nodes-base.facebook"
            node_config["parameters"] = {
                "resource": "post",
                "operation": "create",
                "message": "={{ $json.post_text }}",
                "additionalFields": {}
            }
            node_config["credentials"] = {
                "facebookGraphApi": {
                    "id": "facebook-credentials",
                    "name": "Facebook Graph API"
                }
            }
        
        elif platform_lower == "threads":
            node_config["type"] = "n8n-nodes-base.metaThreads"
            node_config["parameters"] = {
                "resource": "post",
                "operation": "create",
                "text": "={{ $json.post_text }}",
                "additionalFields": {}
            }
            node_config["credentials"] = {
                "metaThreadsOAuth2Api": {
                    "id": "threads-credentials",
                    "name": "Meta Threads OAuth2 API"
                }
            }
        
        elif platform_lower == "instagram":
            node_config["type"] = "n8n-nodes-base.instagram"
            node_config["parameters"] = {
                "resource": "post",
                "operation": "create",
                "caption": "={{ $json.post_text }}",
                "additionalFields": {}
            }
            node_config["credentials"] = {
                "instagramBasicDisplayOAuth2Api": {
                    "id": "instagram-credentials",
                    "name": "Instagram Basic Display OAuth2 API"
                }
            }
        
        workflow["nodes"].append(node_config)
        platform_nodes[platform_lower] = node_id
        y_offset += 150
    
    # Connections
    workflow["connections"] = {
        "Webhook Trigger": {
            "main": [
                [
                    {"node": "Read Post Content", "type": "main", "index": 0}
                ]
            ]
        },
        "Read Post Content": {
            "main": [
                [
                    {"node": node_id, "type": "main", "index": 0}
                    for node_id in platform_nodes.values()
                ]
            ]
        }
    }
    
    # Ajouter connexions pour chaque plateforme
    for node_id in platform_nodes.values():
        workflow["connections"][f"Post to {node_id.split('-')[-1].capitalize()}"] = {
            "main": [
                [
                    {"node": "Webhook Response", "type": "main", "index": 0}
                ]
            ]
        }
    
    # Webhook Response
    workflow["nodes"].append({
        "parameters": {
            "respondWith": "json",
            "responseBody": f"={{ {{ \"success\": true, \"article_slug\": \"{article_slug}\", \"platforms\": {json.dumps(platforms)}, \"published_at\": new Date().toISOString() }} }}"
        },
        "id": "webhook-response",
        "name": "Webhook Response",
        "type": "n8n-nodes-base.respondToWebhook",
        "typeVersion": 1,
        "position": [850, 300]
    })
    
    return workflow


def parse_args() -> argparse.Namespace:
    """Parse les arguments."""
    parser = argparse.ArgumentParser(description="Génère un workflow n8n pour publier un article")
    parser.add_argument("article_slug", help="Slug de l'article")
    parser.add_argument(
        "--platforms",
        default="linkedin,facebook,threads,instagram",
        help="Plateformes séparées par des virgules (défaut: toutes)"
    )
    parser.add_argument(
        "--output",
        help="Fichier de sortie (défaut: workflows/n8n/publish_<article-slug>.json)"
    )
    return parser.parse_args()


def main() -> None:
    """Point d'entrée principal."""
    args = parse_args()
    
    # Normaliser le slug
    slug = args.article_slug.replace("article-", "") if args.article_slug.startswith("article-") else args.article_slug
    article_slug = f"article-{slug}" if not slug.startswith("article-") else slug
    
    # Parser les plateformes
    platforms = [p.strip() for p in args.platforms.split(",")]
    
    # Générer le workflow
    workflow = generate_workflow(article_slug, platforms)
    
    # Déterminer le fichier de sortie
    if args.output:
        output_file = Path(args.output)
    else:
        output_file = WORKFLOWS_DIR / f"publish_{article_slug}.json"
    
    # Écrire le workflow
    WORKFLOWS_DIR.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Workflow généré : {output_file}")
    print(f"   Plateformes : {', '.join(platforms)}")
    print(f"\n📝 Pour déployer dans n8n :")
    print(f"   1. Ouvrir n8n : http://localhost:5679")
    print(f"   2. Workflows → Import from File")
    print(f"   3. Sélectionner : {output_file}")
    print(f"   4. Configurer les credentials OAuth2 pour chaque plateforme")


if __name__ == "__main__":
    main()

