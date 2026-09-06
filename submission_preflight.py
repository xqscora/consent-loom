"""Check the local Consent Loom pitch package before a CSH submission."""
from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import struct


ROOT = Path(__file__).resolve().parent
REQUIRED = [
    ROOT / "SUBMISSION_PACK.md",
    ROOT / "README.md",
    ROOT / "DEVPOST_OPERATOR_CARD.md",
    ROOT / "DEVPOST_FIELD_PAYLOAD.json",
    ROOT / "pitch.html",
    ROOT / "pitch.png",
    ROOT / "prototype.html",
]
SCREENSHOTS = [ROOT / "demo" / name for name in ("consent_loom_draft.png", "consent_loom_proposed.png", "consent_loom_shared.png")]


class StructureParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.headings: list[str] = []
        self._in_title = False
        self._in_heading = False
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self._in_title = True
        if tag in {"h1", "h2"}:
            self._in_heading = True
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._in_title or self._in_heading:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._in_title:
            self.title = " ".join("".join(self._buffer).split())
            self._in_title = False
            self._buffer = []
        if tag in {"h1", "h2"} and self._in_heading:
            heading = " ".join("".join(self._buffer).split())
            if heading:
                self.headings.append(heading)
            self._in_heading = False
            self._buffer = []


def main() -> None:
    missing = [str(path.name) for path in REQUIRED if not path.exists()]
    if missing:
        raise SystemExit(f"missing required files: {', '.join(missing)}")

    pitch = (ROOT / "pitch.html").read_text(encoding="utf-8")
    parser = StructureParser()
    parser.feed(pitch)
    required_headings = {"Consent Loom", "The problem", "The technical thesis", "From language to consent"}
    if parser.title != "Consent Loom | CSH Social Impact Ideathon":
        raise SystemExit(f"unexpected title: {parser.title!r}")
    if not required_headings.issubset(parser.headings):
        missing_headings = sorted(required_headings.difference(parser.headings))
        raise SystemExit(f"missing pitch headings: {', '.join(missing_headings)}")
    for forbidden in ("diagnosis", "permanent profile", "hidden sharing"):
        if forbidden not in pitch.lower():
            raise SystemExit(f"missing boundary statement: {forbidden}")
    prototype = (ROOT / "prototype.html").read_text(encoding="utf-8").lower().replace(" ", "")
    for marker in ("proposefields", "confirmlocally", "shareminimumview", "revokesharedview", "externaldata:false"):
        if marker not in prototype:
            raise SystemExit(f"missing prototype marker: {marker}")
    image = (ROOT / "pitch.png").read_bytes()
    if image[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("pitch.png is not a PNG")
    width, height = struct.unpack(">II", image[16:24])
    if width < 1000 or height < 700:
        raise SystemExit(f"pitch.png is too small: {width}x{height}")
    for screenshot in SCREENSHOTS:
        if not screenshot.exists() or screenshot.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            raise SystemExit(f"invalid local prototype screenshot: {screenshot.name}")
    payload = json.loads((ROOT / "DEVPOST_FIELD_PAYLOAD.json").read_text(encoding="utf-8"))
    required_payload_keys = {
        "project_name", "track", "tagline", "problem_statement", "proposed_solution",
        "technology_component", "beneficiaries", "potential_impact", "feasibility_plan",
        "challenges_limitations", "supporting_material", "ai_use_disclosure",
    }
    if not required_payload_keys.issubset(payload):
        missing_payload = sorted(required_payload_keys.difference(payload))
        raise SystemExit(f"missing payload fields: {', '.join(missing_payload)}")
    evidence = [ROOT / payload["prototype_local_path"], ROOT / payload["video_local_path"]]
    evidence.extend(ROOT / item for item in payload["screenshots"])
    missing_evidence = [str(path.relative_to(ROOT)) for path in evidence if not path.is_file() or path.stat().st_size == 0]
    if missing_evidence:
        raise SystemExit(f"missing local evidence: {', '.join(missing_evidence)}")
    print(f"CSH Consent Loom submission preflight: OK ({len(evidence)} local evidence files)")


if __name__ == "__main__":
    main()
