"""Render scene.html to entry.png at 1024x1024 via Playwright (Chromium).

Deterministic: fixed viewport, no network, no animation, one screenshot.
Usage: python3 render.py [scene.html] [entry.png]
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
SCENE = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "scene.html"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "entry.png"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1024, "height": 1024},
                                device_scale_factor=1)
        page.goto(SCENE.as_uri())
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT))
        browser.close()
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
