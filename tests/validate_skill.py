#!/usr/bin/env python3
"""Verify that the distributable skill works without its source repository."""

from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value)


def validate(bundle):
    errors = []
    entry = (bundle / "SKILL.md").read_text(encoding="utf-8")
    if not entry.startswith("---\n") or not re.search(r"^name: shibui$", entry, re.M):
        errors.append("Missing shibui skill frontmatter")
    if not re.search(r"^description: .+", entry, re.M):
        errors.append("Missing description")
    for path in bundle.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        targets = []
        if path.suffix == ".html":
            parser = Links()
            parser.feed(text)
            targets = parser.targets
        elif path.suffix == ".css":
            targets = re.findall(r"url\(\s*['\"]?([^'\"\s)]+)['\"]?\s*\)", text)
        elif path.suffix == ".md":
            targets = re.findall(r"\]\(([^\s)]+)\)", text)
            # Skill instructions also use inline code for local file paths.
            targets += [value for value in re.findall(r"`([^`\n]+)`", text)
                        if " " not in value and (value.endswith("/") or
                        re.search(r"\.(?:md|html|css|yaml)$", value))]
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(bundle.resolve()) or not resolved.exists():
                errors.append(f"{path.relative_to(bundle)}: missing or external {target}")
    return errors


def main():
    with tempfile.TemporaryDirectory(prefix="shibui-skill-") as directory:
        installed = Path(directory) / "shibui"
        shutil.copytree(ROOT / "skills/shibui", installed)
        errors = validate(installed)
        if errors:
            print("\n".join(errors))
            return 1
        # A decorative CSS background must also survive installation.
        hero = installed / "assets/assets/shibui-hero.svg"
        data = hero.read_bytes()
        hero.unlink()
        if not validate(installed):
            raise AssertionError("Missing CSS background was not detected")
        hero.write_bytes(data)
        # Prove that a broken bundled dependency is rejected.
        (installed / "assets/css/tokens.css").unlink()
        if not validate(installed):
            raise AssertionError("Missing bundled CSS was not detected")
    print("Validated isolated skill: frontmatter, instructions, document links, and HTML dependencies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
