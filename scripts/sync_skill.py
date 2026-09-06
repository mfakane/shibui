#!/usr/bin/env python3
"""Synchronize the committed, self-contained skill bundle from canonical sources."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "skills/shibui"


def expected_files():
    files = {"LICENSE": (ROOT / "LICENSE").read_bytes()}
    for source, target in [("docs", "references"), ("css", "assets/css"), ("examples", "assets/examples")]:
        for path in sorted((ROOT / source).rglob("*")):
            if path.is_file():
                data = path.read_bytes()
                if source == "docs":
                    text = data.decode("utf-8")
                    for prefix in ["css/", "examples/"]:
                        text = text.replace("`" + prefix, "`../assets/" + prefix)
                    data = text.encode("utf-8")
                files[f"{target}/{path.relative_to(ROOT / source).as_posix()}"] = data
    files["references/shibui.yaml"] = (ROOT / "shibui.yaml").read_bytes()
    # Keep the example index's documentation links inside the installed skill.
    files["assets/index.html"] = (ROOT / "index.html").read_text(encoding="utf-8").replace(
        'href="docs/', 'href="../references/'
    ).encode("utf-8")
    return files


def synchronize(check=False):
    expected = expected_files()
    actual = {p.relative_to(BUNDLE).as_posix() for directory in ["references", "assets"]
              for p in (BUNDLE / directory).rglob("*") if p.is_file()}
    stale = sorted(actual - expected.keys())
    changed = sorted(name for name, data in expected.items()
                     if not (BUNDLE / name).is_file() or (BUNDLE / name).read_bytes() != data)
    if check:
        if stale or changed:
            print("Skill bundle out of date; run npm run skill:sync")
            for name in changed + stale:
                print(f"  {name}")
            return 1
    else:
        for name in stale:
            (BUNDLE / name).unlink()
        for name in changed:
            path = BUNDLE / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected[name])
    print(f"Skill bundle {'checked' if check else 'synced'}: {len(expected)} generated files.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    raise SystemExit(synchronize(parser.parse_args().check))
