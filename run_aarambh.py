"""
Project Aarambh (आरम्भ) — Master Enterprise Suite Launcher.
Starts the FastAPI backend and launches the Claymorphic / Neumorphic Glass UI.
Supports both Web Browser mode and Native Edge WebView2 Desktop mode.
"""
import argparse
import os
import sys
import threading
import time
import webbrowser
from pathlib import Path

# Ground paths
APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))
sys.path.insert(0, str(APP_DIR / "studio"))
sys.path.insert(0, str(APP_DIR.parent))
sys.path.insert(0, str(APP_DIR.parent / "lib"))

import uvicorn

def main():
    parser = argparse.ArgumentParser(description="Aarambh (आरम्भ) AI Enterprise Suite")
    parser.add_argument("--host", default="127.0.0.1", help="Server host IP")
    parser.add_argument("--port", type=int, default=8501, help="Server port (default: 8501)")
    parser.add_argument("--desktop", action="store_true", help="Launch in native Edge WebView2 window")
    args = parser.parse_args()

    url = f"http://{args.host}:{args.port}"
    print("=" * 70)
    print("🚀  Starting Project Aarambh (आरम्भ) AI Enterprise Suite v2.0")
    print(f"🌐  Local URL: {url}")
    print("🎨  Design: Gamma Hive 10 Master Studios & 40 Categories")
    print("⚡  Features: Zero-Refresh Colab Workbench & Async Connectivity Ping")
    print("=" * 70)

    def open_browser():
        time.sleep(1.2)
        if not args.desktop:
            print(f"✨ Opening browser at {url}...")
            webbrowser.open(url)

    threading.Thread(target=open_browser, daemon=True).start()

    if args.desktop:
        try:
            import webview
            def run_server():
                uvicorn.run("studio.server:app", host=args.host, port=args.port, log_level="warning")

            threading.Thread(target=run_server, daemon=True).start()
            time.sleep(1.5)
            print("🖥️  Launching Native Edge WebView2 desktop container...")
            webview.create_window(
                title="Aarambh (आरम्भ) AI Enterprise Suite",
                url=url,
                width=1480,
                height=920,
                confirm_close=True,
            )
            webview.start()
            return
        except Exception as e:
            print(f"⚠️  PyWebView desktop launch notice: {e}. Falling back to standard browser mode.")

    from studio.server import app
    uvicorn.run(app, host=args.host, port=args.port)

if __name__ == "__main__":
    main()
