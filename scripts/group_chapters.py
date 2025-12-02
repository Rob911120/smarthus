#!/usr/bin/env python3
"""Grupperar PDF-sidor till kapitel baserat på kapitel.yaml"""

import shutil
from pathlib import Path
from typing import Optional

import yaml


def load_chapter_config(doc_dir: Path) -> Optional[dict]:
    """Ladda kapitelkonfiguration från YAML."""
    config_path = doc_dir / "kapitel.yaml"
    if not config_path.exists():
        return None
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_chapters(doc_dir: Path, config: dict) -> int:
    """Skapa kapitel-mappar och kopiera sidor. Returnerar antal kapitel."""
    sidor_dir = doc_dir / "sidor"
    kapitel_dir = doc_dir / "kapitel"
    kapitel_dir.mkdir(exist_ok=True)

    for kap in config["kapitel"]:
        namn = kap["namn"]
        start, slut = kap["sidor"]

        kap_dir = kapitel_dir / namn
        kap_dir.mkdir(exist_ok=True)

        sidor_kopierade = 0
        for sida in range(start, slut + 1):
            src = sidor_dir / f"sida-{sida:02d}.pdf"
            if src.exists():
                shutil.copy(src, kap_dir / src.name)
                sidor_kopierade += 1

        print(f"  {namn}: sidor {start}-{slut} ({sidor_kopierade} filer)")

    return len(config["kapitel"])


def main():
    docs_dir = Path("docs")
    total_kapitel = 0

    print("Grupperar sidor till kapitel...\n")

    for sidor_dir in sorted(docs_dir.rglob("sidor")):
        parent = sidor_dir.parent
        config = load_chapter_config(parent)

        if config:
            print(f"{parent}:")
            kapitel = create_chapters(parent, config)
            total_kapitel += kapitel
            print()
        else:
            print(f"{parent}: ingen kapitel.yaml hittad (hoppar över)\n")

    print(f"Totalt: {total_kapitel} kapitel skapade")


if __name__ == "__main__":
    main()
