"""
Unit & Integration Test Suite for Aarambh UI Server & Gamma Hive API Gateway.
Built with standard library unittest and Starlette/FastAPI TestClient (httpx).
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
        """Verify all 10 Master Studios from the Blueprint and GIF are present in the DOM."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        studios = [
            "01 Visual & Generative Media",
            "02 Audio, Voice & Music",
            "03 HiveMind Cognitive Lab",
            "04 Software Engineering",
            "05 Autonomous Agents & Physical AI",
            "06 Cyber Security & Threat Intel",
            "07 Enterprise Finance & Ledger",
            "08 Vision & Document OCR",
            "09 Deep Science & Discovery",
            "10 Model Foundry & Hyper Runtime",
        ]
        for s in studios:
            self.assertIn(s, response.text, f"Missing studio: {s}")

    def test_google_connectivity_and_error_console_elements_present(self):
        """Verify that Google Connectivity check and Universal Error Log elements are in HTML."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("btnCheckColab", response.text)
        self.assertIn("btnHeaderLogs", response.text)
        self.assertIn("errorDrawer", response.text)
        self.assertIn("section-diagnostics-bar", response.text)
        self.assertIn("workbenchIframe", response.text)

    def test_log_endpoints(self):
        """Verify logging API endpoints: POST, GET, DELETE."""
        # Post log
        post_resp = self.client.post("/api/logs", json={
            "message": "Test error trigger",
            "level": "ERROR",
            "details": "Stack trace sample",
            "section": "TestRunner"
        })
        self.assertEqual(post_resp.status_code, 200)
        self.assertEqual(post_resp.json()["status"], "ok")

        # Get logs
        get_resp = self.client.get("/api/logs")
        self.assertEqual(get_resp.status_code, 200)
        logs = get_resp.json()["logs"]
        self.assertTrue(any(l["message"] == "Test error trigger" for l in logs))

        # Clear logs
        del_resp = self.client.delete("/api/logs")
        self.assertEqual(del_resp.status_code, 200)
        self.assertEqual(del_resp.json()["status"], "cleared")

    def test_check_gateway_validation(self):
        """Verify that check_gateway handles invalid URLs safely without crashing."""
        resp = self.client.post("/api/check_gateway", json={
            "gateway_url": "invalid-url-string"
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status"], "error")
        self.assertFalse(data["connected"])

    def test_browser_proxy_endpoint(self):
        """Verify browser proxy returns response without crashing."""
        from unittest.mock import patch, MagicMock
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.headers = {"Content-Type": "text/html"}
        mock_resp.read.return_value = b"<html><body>Proxied Content</body></html>"

        with patch("urllib.request.urlopen", return_value=mock_resp):
            resp = self.client.get("/api/browser_proxy?url=https://example.com")
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Proxied Content", resp.text)
            self.assertNotIn("X-Frame-Options", resp.headers)


if __name__ == "__main__":
    unittest.main()
