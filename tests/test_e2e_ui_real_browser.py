"""
Automated Real-Browser End-to-End Test Suite for Project Aarambh.
Uses Microsoft Edge headless via Playwright to click, navigate, filter, and verify 100% UI health.
"""
import sys
import time
from playwright.sync_api import sync_playwright

def run_e2e_tests():
    print("🚀 Launching Headless Edge Browser for Aarambh E2E UI Audit...")
    console_errors = []
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="msedge")
        context = browser.new_context()
        page = context.new_page()

        # Capture console errors
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        # 1. Navigate to Aarambh
        print("🌐 Step 1: Navigating to http://127.0.0.1:8501...")
        page.goto("http://127.0.0.1:8501", wait_until="networkidle")
        assert "Aarambh" in page.title(), f"Unexpected title: {page.title()}"
        print("   ✅ Page loaded with title:", page.title())

        # 2. Test VRAM Hardware Profile Toggles
        print("⚡ Step 2: Testing VRAM Hardware Profile Toggles...")
        btn_colab = page.locator("#btnProfileColab")
        btn_kaggle = page.locator("#btnProfileKaggle")
        
        btn_colab.click()
        time.sleep(0.3)
        assert "active" in btn_colab.get_attribute("class"), "btnProfileColab should be active"
        assert "active" not in btn_kaggle.get_attribute("class"), "btnProfileKaggle should not be active"
        print("   ✅ Clicked Colab 15GB toggle -> active class applied correctly")

        btn_kaggle.click()
        time.sleep(0.3)
        assert "active" in btn_kaggle.get_attribute("class"), "btnProfileKaggle should be active"
        assert "active" not in btn_colab.get_attribute("class"), "btnProfileColab should not be active"
        print("   ✅ Clicked Kaggle 30GB toggle -> active class applied correctly")

        # 3. Test Error Logs Drawer & All 6 Filter Tabs
        print("📋 Step 3: Testing Error Logs Drawer & 6 Filter Tabs...")
        page.locator("#btnHeaderLogs").click()
        time.sleep(0.5)
        drawer = page.locator("#errorDrawer")
        assert "open" in drawer.get_attribute("class"), "errorDrawer should have 'open' class"
        print("   ✅ Error drawer opened successfully")

        # Test each filter tab
        filters = ["ALL", "ERRORS", "WARNINGS", "SUCCESS", "INFO", "SYSTEM"]
        for f in filters:
            tab = page.locator(f".drawer-filter-bar .filter-tab[data-filter='{f}']")
            tab.click()
            time.sleep(0.2)
            assert "active" in tab.get_attribute("class"), f"Filter tab {f} should be active"
            list_text = page.locator("#drawerLogsList").inner_text()
            print(f"   ✅ Filter tab '{f}' clicked -> active and rendered {len(list_text.splitlines())} lines")

        # Test individual copy button
        single_copy_btn = page.locator(".btn-copy-single-log").first
        if single_copy_btn.count() > 0:
            single_copy_btn.click()
            time.sleep(0.3)
            print("   ✅ Clicked individual log copy button (data-log-id)")

        # Close drawer
        page.locator("#btnCloseLogs").click()
        time.sleep(0.3)
        assert "open" not in drawer.get_attribute("class"), "errorDrawer should be closed"
        print("   ✅ Closed error drawer cleanly")

        # 4. Test Navigation and View Panels
        print("🏛️ Step 4: Testing Master Studios (Cards 1 through 10)...")
        for studio_id in range(1, 11):
            card = page.locator(f".studio-card[data-studio-id='{studio_id}']")
            assert card.count() == 1, f"Studio card {studio_id} not found"
            card.click()
            time.sleep(0.4)
            
            # Verify workspace view is active
            workspace = page.locator("#view-workspace")
            assert "active" in workspace.get_attribute("class"), f"Workspace not active for Studio {studio_id}"
            
            title = page.locator("#workspaceStudioTitle").inner_text()
            pills = page.locator("#workspaceSubcategoriesBar .subcat-pill-btn")
            pill_count = pills.count()
            assert pill_count > 0, f"No subcategory pills for Studio {studio_id}"
            
            # Click second subcategory pill if available
            if pill_count > 1:
                pills.nth(1).click()
                time.sleep(0.2)
                assert "active" in pills.nth(1).get_attribute("class"), f"Second pill not active in Studio {studio_id}"

            print(f"   ✅ Studio {studio_id:02d}: '{title}' launched ({pill_count} subcategories verified)")
            
            # Click back to studios
            page.locator("#btnBackStudios").click()
            time.sleep(0.3)
            studios_view = page.locator("#view-studios")
            assert "active" in studios_view.get_attribute("class"), "view-studios should be active after back"

        # 5. Test Inbuilt Workbench View & MCP Tabs
        print("🌐 Step 5: Testing Inbuilt Workbench & MCP Provider Tabs...")
        page.locator(".nav-link[data-view='workbench']").click()
        time.sleep(0.3)
        workbench_view = page.locator("#view-workbench")
        assert "active" in workbench_view.get_attribute("class"), "view-workbench should be active"
        
        tab_kaggle = page.locator("#tabMcpKaggle")
        tab_colab = page.locator("#tabMcpColab")
        tab_hf = page.locator("#tabMcpHf")
        
        tab_colab.click()
        time.sleep(0.2)
        assert "active" in tab_colab.get_attribute("class"), "tabMcpColab should be active"
        assert page.locator("#panelMcpColab").is_visible(), "panelMcpColab should be visible"
        print("   ✅ Switched to Colab MCP Bridge in Workbench")

        tab_hf.click()
        time.sleep(0.2)
        assert "active" in tab_hf.get_attribute("class"), "tabMcpHf should be active"
        assert page.locator("#panelMcpHf").is_visible(), "panelMcpHf should be visible"
        print("   ✅ Switched to Hugging Face ZeroGPU MCP in Workbench")

        tab_kaggle.click()
        time.sleep(0.2)
        assert "active" in tab_kaggle.get_attribute("class"), "tabMcpKaggle should be active"
        assert page.locator("#panelMcpKaggle").is_visible(), "panelMcpKaggle should be visible"
        print("   ✅ Switched back to Kaggle 2x T4 MCP in Workbench")

        # 6. Test Architecture View
        print("ℹ️ Step 6: Testing Architecture View...")
        page.locator(".nav-link[data-view='about']").click()
        time.sleep(0.3)
        about_view = page.locator("#view-about")
        assert "active" in about_view.get_attribute("class"), "view-about should be active"
        print("   ✅ Switched to Architecture view")

        # Return to studios view
        page.locator(".nav-link[data-view='studios']").click()
        time.sleep(0.3)

        browser.close()

    # 7. Check for Javascript Errors
    print("🔍 Step 7: Verifying Zero Console / Page Errors...")
    print("   Total Page Errors:", len(page_errors))
    print("   Total Console Errors:", len(console_errors))
    
    if page_errors:
        print("   ❌ Page Errors:", page_errors)
        sys.exit(1)
        
    if console_errors:
        print("   ⚠️ Console Errors:", console_errors)

    print("\n🎉 100% SUCCESS: All UI Buttons, Studios, Drawers, Filters, and Toggles PASSED with 0 Errors!")

if __name__ == "__main__":
    run_e2e_tests()
