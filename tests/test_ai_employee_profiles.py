from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / ".devspace" / "agents"
EXPECTED = {
    "ai-master",
    "ai-planner",
    "ai-developer",
    "ai-qa",
    "ai-marketer",
}


def _frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n")
    end = text.find("\n---\n", 4)
    assert end > 0
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, sep, value = line.partition(":")
        assert sep, f"invalid frontmatter line: {line!r}"
        result[key.strip()] = value.strip()
    return result


def test_ai_employee_profiles_match_devspace_schema_and_safety_boundary() -> None:
    files = sorted(PROFILE_DIR.glob("ai-*.md"))
    assert {path.stem for path in files} == EXPECTED

    for path in files:
        text = path.read_text(encoding="utf-8")
        meta = _frontmatter(text)
        assert meta["schema"] == "devspace-agent/v1"
        assert meta["name"] == path.stem
        assert meta["description"]
        assert meta["provider"] == "codex"
        assert re.fullmatch(r"[a-z0-9-]+", meta["name"])
        assert "deploy" in text.lower()
        assert "spend money" in text.lower()


def test_only_developer_profile_allows_repository_edits() -> None:
    for path in sorted(PROFILE_DIR.glob("ai-*.md")):
        body = path.read_text(encoding="utf-8").lower()
        if path.stem == "ai-developer":
            assert "may edit repository files" in body
        else:
            assert "read-only" in body
