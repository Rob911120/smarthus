#!/usr/bin/env python3
"""Delar upp original.pdf filer i enskilda sidor."""

import fitz  # PyMuPDF
from pathlib import Path


def split_pdf(pdf_path: Path) -> int:
    """Delar upp en PDF i enskilda sidor. Returnerar antal sidor."""
    doc = fitz.open(pdf_path)
    output_dir = pdf_path.parent / "sidor"
    output_dir.mkdir(exist_ok=True)

    num_pages = len(doc)

    for page_num in range(num_pages):
        page_doc = fitz.open()
        page_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
        output_path = output_dir / f"sida-{page_num + 1:02d}.pdf"
        page_doc.save(output_path)
        page_doc.close()

    doc.close()
    return num_pages


def main():
    docs_dir = Path("docs")
    total_pages = 0

    for original in docs_dir.rglob("original.pdf"):
        pages = split_pdf(original)
        total_pages += pages
        print(f"{original}: {pages} sidor")

    print(f"\nTotalt: {total_pages} sidor uppdelade")


if __name__ == "__main__":
    main()
