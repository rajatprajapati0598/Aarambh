"""
Unit & Integration Test Suite for Aarambh UI Server & Gamma Hive API Gateway.
Built with standard library unittest and Starlette/FastAPI TestClient.
"""
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "studio"))
sys.path.insert(0, str(BASE_DIR.parent / "lib"))

from fastapi.testclient import TestClient
from studio.server import app


class TestAarambhUIServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_index_page_serves_html(self):
        """Verify that root URL serves the Gamma Hive HTML dashboard."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("GAMMA HIVE", response.text)
        self.assertIn("01 Visual & Generative Media", response.text)
        self.assertIn("10 Model Foundry & Hyper Runtime", response.text)

    def test_static_assets_serve_correctly(self):
        """Verify that CSS and JS assets are accessible."""
        css_resp = self.client.get("/static/css/style.css")
        self.assertEqual(css_resp.status_code, 200)
        self.assertIn("--surface-clay", css_resp.text)

        js_resp = self.client.get("/static/js/app.js")
        self.assertEqual(js_resp.status_code, 200)
        self.assertIn("checkGoogleConnectivity", js_resp.text)

    def test_10_master_studios_present(self):
        """Verify all 10 Master Studios from the Blueprint are present in the DOM."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        studios = [
            "01 Visual & Generative Media",
            "02 Audio, Voice & Music",
            "03 HiveMind Cognitive Lab",
            "04 Software Engineering",
            "05 Autonomous Agents & Physical AI",
            "06 Cyber Security & Threat Intelligence",
            "07 Enterprise Finance & Ledger",
            "08 Vision & Document OCR",
            "09 Deep Science & Discovery",
            "10 Model Foundry & Hyper Runtime",
        ]
        for s in studios:
            self.assertIn(s, response.text, f"Missing studio: {s}")

    def test_vram_toggle_and_error_console_elements(self):
        """Verify that VRAM Hardware Toggle and Error Console elements are in HTML."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("btnProfileColab", response.text)
        self.assertIn("btnProfileKaggle", response.text)
        self.assertIn("btnHeaderLogs", response.text)
        self.assertIn("errorDrawer", response.text)
        self.assertIn("drawerLogsList", response.text)

    def test_mcp_status_endpoint(self):
        """Verify that /api/mcp/status returns valid JSON structure."""
        resp = self.client.get("/api/mcp/status")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data.get("status"), "success")
        self.assertIn("providers", data)
        self.assertIn("kaggle", data["providers"])
        self.assertIn("colab", data["providers"])
        self.assertIn("huggingface", data["providers"])

    def test_tunnel_hud_telemetry_endpoint(self):
        """Verify that /api/tunnel_hud returns GPU and telemetry specs."""
        resp = self.client.get("/api/tunnel_hud")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data.get("status"), "success")
        self.assertIn("data", data)
        self.assertIn("connected", data["data"])

    def test_log_endpoints_lifecycle(self):
        """Verify logging API endpoints lifecycle: POST, GET, DELETE."""
        # 1. Post log
        post_resp = self.client.post("/api/logs", json={
            "message": "Automated pipeline lifecycle test",
            "level": "SUCCESS",
            "details": "Telemetry verified",
            "section": "TestRunner"
        })
        self.assertEqual(post_resp.status_code, 200)
        self.assertEqual(post_resp.json()["status"], "ok")

        # 2. Get logs
        get_resp = self.client.get("/api/logs")
        self.assertEqual(get_resp.status_code, 200)
        logs = get_resp.json()["logs"]
        self.assertTrue(any("Automated pipeline lifecycle test" in l["message"] for l in logs))

        # 3. Clear logs
        del_resp = self.client.delete("/api/logs")
        self.assertEqual(del_resp.status_code, 200)
        self.assertEqual(del_resp.json()["status"], "cleared")

    def test_check_gateway_standby_on_empty_url(self):
        """Verify that check_gateway returns standby for unconfigured/empty URL."""
        resp = self.client.post("/api/check_gateway", json={
            "gateway_url": ""
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status"], "standby")
        self.assertFalse(data["connected"])


if __name__ == "__main__":
    unittest.main()
