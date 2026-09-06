#!/usr/bin/env python3
"""Validate the publishable ELI5+ skill package using only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "eli5-plus"
SKILL_FILE = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter delimited by ---")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        key, separator, raw_value = line.partition(":")
        if not separator:
            fail(f"invalid frontmatter line: {line!r}")
        values[key.strip()] = raw_value.strip().strip('"').strip("'")
    return values


def validate() -> None:
    for required in (SKILL_FILE, OPENAI_YAML, REPO_ROOT / "README.md", REPO_ROOT / "LICENSE"):
        if not required.is_file() or required.stat().st_size == 0:
            fail(f"missing or empty required file: {required.relative_to(REPO_ROOT)}")

    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter.get("name") != SKILL_DIR.name:
        fail("frontmatter name must match the skill directory name")
    if not frontmatter.get("description"):
        fail("frontmatter description must be non-empty")
    if len(frontmatter["description"]) > 1024:
        fail("frontmatter description is unexpectedly long")

    metadata_text = OPENAI_YAML.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if not re.search(rf"^\s{{2}}{key}:\s+\"[^\n]+\"\s*$", metadata_text, re.MULTILINE):
            fail(f"agents/openai.yaml is missing a quoted {key}")
    if "$eli5-plus" not in metadata_text:
        fail("default_prompt must mention $eli5-plus explicitly")

    debris = sorted(
        path.relative_to(REPO_ROOT)
        for path in REPO_ROOT.rglob("*")
        if path.name == ".DS_Store" or path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"}
    )
    if debris:
        fail("repository contains generated debris: " + ", ".join(map(str, debris)))

    print("ELI5+ skill package is valid.")


if __name__ == "__main__":
    validate()
