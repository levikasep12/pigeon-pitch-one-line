# Pigeon Pitch, One Line — make.fun entry
# Writes the entry's single pitch line to /output/entry.txt.
# Deterministic: the same bytes on every run. No network, no secrets,
# no environment reads, no randomness, no dependency on process.cwd().
from pathlib import Path

LINE = (
    "We're monetizing the world's largest untapped rooftop real estate: "
    "every statue, ledge, and breadcrumb within a five-block radius — "
    "the birds are already onboard."
)

# The gate allows 1 to 200 characters: refuse to emit a line that would fail it.
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-200")

OUT_FILE = Path("/output/entry.txt")
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to {OUT_FILE}")
