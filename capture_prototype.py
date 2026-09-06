from pathlib import Path
import shutil

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "demo"
OUT.mkdir(exist_ok=True)


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            record_video_dir=str(OUT),
            record_video_size={"width": 1440, "height": 900},
        )
        page = context.new_page()
        page.goto("http://127.0.0.1:8792/prototype.html", wait_until="networkidle")
        page.wait_for_timeout(1800)
        page.screenshot(path=str(OUT / "consent_loom_draft.png"), full_page=False)
        page.get_by_role("button", name="Propose fields").click()
        page.wait_for_timeout(1600)
        page.screenshot(path=str(OUT / "consent_loom_proposed.png"), full_page=False)
        page.get_by_role("button", name="Confirm locally").click()
        page.get_by_role("button", name="Share minimum view").click()
        page.wait_for_timeout(1800)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "consent_loom_shared.png"), full_page=False)
        page.close()
        context.close()
        source = Path(page.video.path())
        target = OUT / "consent_loom_demo_2026-09-05.webm"
        if source != target:
            shutil.copyfile(source, target)
        browser.close()
    print(f"Captured {target}")


if __name__ == "__main__":
    main()
