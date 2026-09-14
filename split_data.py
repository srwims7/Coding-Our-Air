"""
split_data.py

Run this once against your CURRENT Philadelphia_Air_Emissions_Map.html
(the one already in your repo). It pulls the giant embedded `ALL_DATA`
JS array out of the HTML and writes it to small, per-year JSON files
instead — so the browser only has to download the year the user is
actually looking at, not all 14 years at once.

Usage (from the repo root, in VS Code's terminal):
    python scripts/split_data.py

Output:
    data/manifest.json      -> list of available years, e.g. [2010, 2011, ...]
    data/2010.json          -> just 2010's records
    data/2011.json          -> just 2011's records
    ...
"""

import re
import json
from pathlib import Path
from collections import defaultdict

SRC = Path("Philadelphia_Air_Emissions_Map.html")
OUT_DIR = Path("data")


def extract_all_data(html_text: str) -> list[dict]:
    match = re.search(r"var ALL_DATA\s*=\s*(\[.*?\]);", html_text, re.DOTALL)
    if not match:
        raise SystemExit(
            "Couldn't find `var ALL_DATA = [...]` in the HTML. "
            "Open the file and confirm the variable name matches, "
            "or update the regex above."
        )
    return json.loads(match.group(1))


def main() -> None:
    if not SRC.exists():
        raise SystemExit(
            f"Expected to find {SRC} in the current folder. "
            "Run this script from your repo root."
        )

    OUT_DIR.mkdir(exist_ok=True)
    records = extract_all_data(SRC.read_text(encoding="utf-8"))

    by_year: dict[int, list[dict]] = defaultdict(list)
    for r in records:
        r["tons"] = round(r["tons"], 2)  # trims float noise, shrinks file size
        by_year[r["year"]].append(r)

    years = sorted(by_year.keys())
    total_before = SRC.stat().st_size

    for year, rows in by_year.items():
        out_path = OUT_DIR / f"{year}.json"
        out_path.write_text(json.dumps(rows, separators=(",", ":")), encoding="utf-8")
        print(f"  wrote {out_path}  ({len(rows)} records, {out_path.stat().st_size / 1024:.1f} KB)")

    (OUT_DIR / "manifest.json").write_text(json.dumps(years), encoding="utf-8")

    total_after = sum((OUT_DIR / f"{y}.json").stat().st_size for y in years)
    print(f"\nOriginal HTML: {total_before / 1024:.0f} KB (all years, loaded on every page view)")
    print(f"Largest single year now: {max((OUT_DIR / f'{y}.json').stat().st_size for y in years) / 1024:.1f} KB")
    print(f"(that's the most any single visit now has to download for the map data)")


if __name__ == "__main__":
    main()
