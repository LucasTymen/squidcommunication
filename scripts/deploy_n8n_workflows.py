#!/usr/bin/env python3
"""Déploie les workflows n8n depuis squidCommunication vers le serveur n8n local.

Usage:
    python scripts/deploy_n8n_workflows.py [--workflow <name>] [--all] [--dry-run]
    
Exemples:
    # Déployer tous les workflows
    python scripts/deploy_n8n_workflows.py --all
    
    # Déployer un workflow spécifique
    python scripts/deploy_n8n_workflows.py --workflow generate_article_variants
    
    # Simuler le déploiement
    python scripts/deploy_n8n_workflows.py --all --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Optional
import requests
from requests.auth import HTTPBasicAuth

SUPER_ADMIN_USERS = {"lucas"}


def ensure_super_admin() -> None:
    current_user = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    if current_user not in SUPER_ADMIN_USERS:
        raise SystemExit(
            "Accès réservé au super-admin. Merci d'exécuter ce script depuis le compte autorisé."
        )


ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = ROOT / "workflows" / "n8n"

# Configuration n8n (peut être surchargée par variables d'environnement)
N8N_URL = os.getenv("N8N_URL", "http://localhost:5679")
N8N_USERNAME = os.getenv("N8N_USERNAME", "lucas")
N8N_PASSWORD = os.getenv("N8N_PASSWORD", "")  # À définir dans .env ou prompt
N8N_API_KEY = os.getenv("N8N_API_KEY", "")  # Alternative : API key au lieu de basic auth


def load_workflow_json(workflow_path: Path) -> Dict:
    """Charge un workflow JSON depuis le fichier."""
    if not workflow_path.exists():
        raise FileNotFoundError(f"Workflow non trouvé : {workflow_path}")
    
    with workflow_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_n8n_workflows(api_url: str, auth: Optional[HTTPBasicAuth] = None, api_key: Optional[str] = None) -> List[Dict]:
    """Récupère la liste des workflows existants dans n8n."""
    headers = {}
    if api_key:
        headers["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.get(
            f"{api_url}/api/v1/workflows",
            auth=auth,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"❌ Erreur lors de la connexion à n8n : {e}")


def workflow_exists(workflows: List[Dict], workflow_name: str) -> Optional[Dict]:
    """Vérifie si un workflow existe déjà dans n8n."""
    for wf in workflows:
        if wf.get("name") == workflow_name:
            return wf
    return None


def create_or_update_workflow(
    workflow_data: Dict,
    api_url: str,
    auth: Optional[HTTPBasicAuth] = None,
    api_key: Optional[str] = None,
    dry_run: bool = False
) -> Dict:
    """Crée ou met à jour un workflow dans n8n."""
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["X-N8N-API-KEY"] = api_key
    
    workflow_name = workflow_data.get("name", "Unnamed Workflow")
    
    # Vérifier si le workflow existe déjà
    existing_workflows = get_n8n_workflows(api_url, auth, api_key)
    existing = workflow_exists(existing_workflows, workflow_name)
    
    if dry_run:
        if existing:
            print(f"[DRY-RUN] Mise à jour du workflow : {workflow_name} (ID: {existing.get('id')})")
        else:
            print(f"[DRY-RUN] Création du workflow : {workflow_name}")
        return {"id": "dry-run-id", "name": workflow_name}
    
    try:
        if existing:
            # Mise à jour
            workflow_id = existing.get("id")
            response = requests.put(
                f"{api_url}/api/v1/workflows/{workflow_id}",
                json=workflow_data,
                auth=auth,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            print(f"✅ Workflow mis à jour : {workflow_name} (ID: {workflow_id})")
            return response.json()
        else:
            # Création
            response = requests.post(
                f"{api_url}/api/v1/workflows",
                json=workflow_data,
                auth=auth,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            print(f"✅ Workflow créé : {workflow_name} (ID: {result.get('id')})")
            return result
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"❌ Erreur lors de la création/mise à jour du workflow {workflow_name} : {e}")


def activate_workflow(
    workflow_id: str,
    api_url: str,
    auth: Optional[HTTPBasicAuth] = None,
    api_key: Optional[str] = None,
    dry_run: bool = False
) -> None:
    """Active un workflow dans n8n."""
    if dry_run:
        print(f"[DRY-RUN] Activation du workflow ID: {workflow_id}")
        return
    
    headers = {}
    if api_key:
        headers["X-N8N-API-KEY"] = api_key
    
    try:
        response = requests.post(
            f"{api_url}/api/v1/workflows/{workflow_id}/activate",
            auth=auth,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        print(f"✅ Workflow activé : {workflow_id}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️  Impossible d'activer le workflow {workflow_id} : {e}")


def get_auth() -> tuple[Optional[HTTPBasicAuth], Optional[str]]:
    """Récupère les credentials pour n8n."""
    if N8N_API_KEY:
        return None, N8N_API_KEY
    elif N8N_PASSWORD:
        return HTTPBasicAuth(N8N_USERNAME, N8N_PASSWORD), None
    else:
        # Prompt pour le mot de passe si non défini
        import getpass
        password = getpass.getpass(f"Mot de passe n8n pour {N8N_USERNAME}: ")
        return HTTPBasicAuth(N8N_USERNAME, password), None


def list_available_workflows() -> List[Path]:
    """Liste tous les workflows disponibles dans workflows/n8n/."""
    if not WORKFLOWS_DIR.exists():
        return []
    
    return [
        f for f in WORKFLOWS_DIR.glob("*.json")
        if f.is_file() and f.name != ".gitkeep"
    ]


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Déploie les workflows n8n vers le serveur local",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python scripts/deploy_n8n_workflows.py --all
  python scripts/deploy_n8n_workflows.py --workflow generate_article_variants
  python scripts/deploy_n8n_workflows.py --all --dry-run
  python scripts/deploy_n8n_workflows.py --all --activate
""",
    )
    parser.add_argument(
        "--workflow",
        help="Nom du workflow à déployer (sans extension .json)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Déployer tous les workflows disponibles",
    )
    parser.add_argument(
        "--activate",
        action="store_true",
        help="Activer automatiquement les workflows après déploiement",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simuler le déploiement sans modifier n8n",
    )
    parser.add_argument(
        "--n8n-url",
        default=N8N_URL,
        help=f"URL du serveur n8n (défaut: {N8N_URL})",
    )
    return parser.parse_args(argv)


def main() -> None:
    """Point d'entrée principal."""
    ensure_super_admin()
    args = parse_args()
    
    if not args.workflow and not args.all:
        parser = argparse.ArgumentParser()
        parser.print_help()
        raise SystemExit("\n❌ Spécifiez --workflow <name> ou --all")
    
    # Récupérer les credentials
    auth, api_key = get_auth()
    
    # Lister les workflows disponibles
    available_workflows = list_available_workflows()
    
    if not available_workflows:
        raise SystemExit(f"❌ Aucun workflow trouvé dans {WORKFLOWS_DIR}")
    
    print(f"📋 {len(available_workflows)} workflow(s) trouvé(s)")
    
    # Déterminer quels workflows déployer
    workflows_to_deploy: List[Path] = []
    
    if args.all:
        workflows_to_deploy = available_workflows
    elif args.workflow:
        workflow_path = WORKFLOWS_DIR / f"{args.workflow}.json"
        if not workflow_path.exists():
            raise SystemExit(f"❌ Workflow non trouvé : {workflow_path}")
        workflows_to_deploy = [workflow_path]
    
    # Déployer chaque workflow
    print(f"\n🚀 Déploiement vers {args.n8n_url}")
    if args.dry_run:
        print("⚠️  Mode DRY-RUN activé (aucune modification réelle)\n")
    
    deployed_workflows = []
    
    for workflow_path in workflows_to_deploy:
        workflow_name = workflow_path.stem
        print(f"\n📦 Traitement : {workflow_name}")
        
        try:
            workflow_data = load_workflow_json(workflow_path)
            result = create_or_update_workflow(
                workflow_data,
                args.n8n_url,
                auth,
                api_key,
                args.dry_run
            )
            
            if args.activate and not args.dry_run:
                workflow_id = result.get("id")
                if workflow_id:
                    activate_workflow(workflow_id, args.n8n_url, auth, api_key, args.dry_run)
            
            deployed_workflows.append(workflow_name)
            
        except Exception as e:
            print(f"❌ Erreur lors du déploiement de {workflow_name} : {e}")
            continue
    
    print(f"\n✅ {len(deployed_workflows)} workflow(s) déployé(s) avec succès")
    if deployed_workflows:
        print("   Workflows déployés :")
        for name in deployed_workflows:
            print(f"   - {name}")


if __name__ == "__main__":
    main()

