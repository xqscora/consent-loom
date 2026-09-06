"""Render the CSH pitch visual to a local PNG for the supporting material."""
from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "pitch.png"
URL = "http://127.0.0.1:8791/pitch.html"


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.screenshot(path=str(TARGET), full_page=True)
        browser.close()
    print(f"saved {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
