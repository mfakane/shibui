#!/usr/bin/env python3
"""Small dependency-free checks for the static Shibui reference implementation."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.has_main = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "main":
            self.has_main = True
        if tag == "title":
            self.has_title = True
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag in {"a", "link"}:
            destination = values.get("href")
            if destination:
                self.links.append(destination)


def check_html(path: Path) -> list[str]:
    parser = DocumentParser()
    parser.feed(path.read_text(encoding="utf-8"))
    errors = []
    if not parser.has_main:
        errors.append(f"{path}: missing main landmark")
    if not parser.has_title:
        errors.append(f"{path}: missing title")
    for link in parser.links:
        if link.startswith(("#", "http:", "https:", "mailto:")):
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        if not target.exists():
            errors.append(f"{path}: broken link {link}")
    return errors


def main() -> int:
    errors: list[str] = []
    html_files = [ROOT / "index.html", *sorted((ROOT / "examples").glob("*.html"))]
    for path in html_files:
        errors.extend(check_html(path))

    css = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "css").glob("*.css"))
    forbidden = {
        "box shadow": r"box-shadow\s*:\s*(?!none)",
        "text shadow": r"text-shadow\s*:\s*(?!none)",
        "gradient": r"(?:linear|radial|conic)-gradient\(",
    }
    for label, pattern in forbidden.items():
        if re.search(pattern, css, flags=re.IGNORECASE):
            errors.append(f"CSS contains forbidden {label}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(html_files)} HTML pages and Shibui standard-profile visual defaults.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
