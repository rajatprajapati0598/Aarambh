"""
Project Aarambh (आरम्भ) — Enterprise Security & Data Leakage Audit Suite.
Verifies zero hardcoded secrets, .gitignore invariants, and API credential masking.
"""
import re
import sys
import json
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "studio"))

class TestSecurityAudit(unittest.TestCase):

    def test_gitignore_enforces_zero_secrets(self):
        """Verify that .gitignore strictly ignores sensitive files and tokens."""
        gitignore_path = BASE_DIR / ".gitignore"
        self.assertTrue(gitignore_path.exists(), ".gitignore file must exist")
        
        content = gitignore_path.read_text(encoding="utf-8")
        required_patterns = [
            ".secrets/",
            "*.secret",
            "*.token",
            "*.key",
            "kaggle.json",
            "mcp_config.json",
            ".env"
        ]
        for pattern in required_patterns:
            self.assertIn(pattern, content, f"Missing critical security ignore pattern: {pattern}")

    def test_frontend_files_have_zero_secret_leakage(self):
        """Verify that frontend HTML, JS, and CSS files contain no leaked tokens or keys."""
        frontend_dirs = [BASE_DIR / "studio" / "static"]
        leak_patterns = [
            re.compile(r"ghp_[a-zA-Z0-9]{30,}", re.IGNORECASE),
            re.compile(r"github_pat_[a-zA-Z0-9_]{30,}", re.IGNORECASE),
            re.compile(r"KGAT_[a-zA-Z0-9_]{20,}", re.IGNORECASE),
            re.compile(r"hf_[a-zA-Z0-9]{25,}", re.IGNORECASE),
            re.compile(r"AKIA[0-9A-Z]{16}", re.IGNORECASE)
        ]

        scanned_files = 0
        for fdir in frontend_dirs:
            for ext in ["*.js", "*.html", "*.css"]:
                for file_path in fdir.rglob(ext):
                    scanned_files += 1
                    text = file_path.read_text(encoding="utf-8")
                    for pattern in leak_patterns:
                        matches = [m for m in pattern.findall(text) if "xxxx" not in m.lower()]
                        self.assertEqual(len(matches), 0, f"Potential secret leak detected in {file_path.name}: {matches}")
        
        self.assertGreater(scanned_files, 0, "At least one frontend file must be scanned")

    def test_api_status_masks_credentials(self):
        """Verify that the MCP status endpoint never exposes raw tokens or unmasked keys."""
        from fastapi.testclient import TestClient
        from studio.server import app

        client = TestClient(app)
        resp = client.get("/api/mcp/status")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        
        # Verify providers structure exists
        self.assertIn("providers", data)
        kaggle_info = data["providers"].get("kaggle", {})
        
        # Must not contain raw API key
        self.assertNotIn("key", kaggle_info, "Kaggle API key must never be sent in public status endpoint")
        self.assertNotIn("token", kaggle_info, "Kaggle token must never be sent in public status endpoint")

if __name__ == "__main__":
    unittest.main()
