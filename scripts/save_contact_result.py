#!/usr/bin/env python3
"""Append contact enrichment results to the JSON store (no more .txt outputs).

Usage examples:
    python scripts/save_contact_result.py \
        --campaign 2025-11-hub-communication \
        --full-name "Alice Martin" \
        --company "Acme" \
        --domain acme.com \
        --hypothesis alice.martin@acme.com:valid \
        --hypothesis amartin@acme.com:unknown

    # Inject from a JSON blob (stdin)
    cat payload.json | python scripts/save_contact_result.py --from-stdin
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parent.parent
CONTACT_STORE = ROOT / "data" / "communication" / "contact_results.json"


@dataclass
class EmailHypothesis:
    address: str
    status: str  # valid | invalid | unknown


@dataclass
class ContactResult:
    full_name: Optional[str]
    company: Optional[str]
    domain: Optional[str]
    campaign_id: Optional[str]
    source: Optional[str]
    notes: Optional[str]
    email_hypotheses: List[EmailHypothesis]


def load_store(path: Path) -> dict:
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            try:
                return json.load(fh)
            except json.JSONDecodeError:
                pass
    # fallback structure
    return {"contacts": []}


def persist_store(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def parse_hypothesis(value: str) -> EmailHypothesis:
    if ":" in value:
        address, status = value.split(":", 1)
    else:
        address, status = value, "unknown"
    status = status.strip().lower() or "unknown"
    return EmailHypothesis(address=address.strip(), status=status)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Save contact enrichment results to JSON")
    parser.add_argument("--campaign", dest="campaign_id", help="Campaign identifier", default=None)
    parser.add_argument("--full-name", dest="full_name", help="Full name", default=None)
    parser.add_argument("--company", help="Company name", default=None)
    parser.add_argument("--domain", help="Company domain", default=None)
    parser.add_argument("--source", help="Origin of the data (scraper, maltego, etc.)", default=None)
    parser.add_argument("--notes", help="Additional comments", default=None)
    parser.add_argument(
        "--hypothesis",
        action="append",
        default=[],
        help="Email hypothesis in the form address:status (status = valid|invalid|unknown)",
    )
    parser.add_argument(
        "--from-stdin",
        action="store_true",
        help="Read a JSON blob from stdin to append (overrides other flags)",
    )
    return parser.parse_args()


def build_contact_from_args(args: argparse.Namespace) -> ContactResult:
    hypotheses = [parse_hypothesis(value) for value in args.hypothesis]
    return ContactResult(
        full_name=args.full_name,
        company=args.company,
        domain=args.domain,
        campaign_id=args.campaign_id,
        source=args.source,
        notes=args.notes,
        email_hypotheses=hypotheses,
    )


def append_contact(result: ContactResult) -> None:
    store = load_store(CONTACT_STORE)
    store.setdefault("contacts", [])
    store["contacts"].append(asdict(result))
    persist_store(CONTACT_STORE, store)


def main() -> None:
    args = parse_args()
    if args.from_stdin:
        payload = json.load(sys.stdin)
        if isinstance(payload, list):
            for entry in payload:
                append_contact(ContactResult(**entry))
        else:
            append_contact(ContactResult(**payload))
    else:
        result = build_contact_from_args(args)
        append_contact(result)
    print(f"✅ Résultat ajouté dans {CONTACT_STORE}")


if __name__ == "__main__":
    main()
