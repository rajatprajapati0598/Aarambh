#!/usr/bin/env python3
"""
Project Aarambh (आरम्भ) — Master Unified Enterprise Test Runner & QA Auditor.

Orchestrates all 4 testing suites:
1. Security & Leak Audit (Zero tokens/credentials leak, .gitignore compliance)
2. Models Manifest & VRAM Tiers (40+ models, Colab 15GB vs Kaggle 30GB)
3. API Gateway & Backend Services (FastAPI routes, telemetry, proxy, logging)
4. Real-Browser Headless E2E UI Journey (10 Studios, 40 Categories, Drawer, Toggles)
"""
import sys
import time
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
PYTHON_EXE = sys.executable

# Terminal Colors
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"
C_YELLOW = "\033[93m"
C_CYAN = "\033[96m"
C_BLUE = "\033[94m"

def print_banner():
    print(f"""{C_CYAN}{C_BOLD}
======================================================================
  PROJECT AARAMBH (आरम्भ) — ENTERPRISE QA & TEST SUITE RUNNER
  10 Master Studios | 40 Sub-Categories | Dual T4 & Zero-Leak Shield
======================================================================{C_RESET}""")

def run_suite(suite_name: str, icon: str, script_path: Path, args=None):
    print(f"\n{C_BOLD}{icon} Running Suite: {suite_name}...{C_RESET}")
    start = time.time()
    cmd = [PYTHON_EXE, str(script_path)] + (args or [])
    
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(BASE_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=120
        )
        duration = round(time.time() - start, 3)
        success = (proc.returncode == 0)
        
        if success:
            print(f"   {C_GREEN}✔ PASS{C_RESET} ({duration}s)")
            return {
                "suite": suite_name,
                "status": "PASS",
                "duration_seconds": duration,
                "output": proc.stdout[-500:] if proc.stdout else ""
            }
        else:
            print(f"   {C_RED}✖ FAIL{C_RESET} ({duration}s)")
            print(f"{C_YELLOW}--- Failure Traceback ---{C_RESET}")
            print(proc.stdout)
            print(f"{C_YELLOW}-------------------------{C_RESET}")
            return {
                "suite": suite_name,
                "status": "FAIL",
                "duration_seconds": duration,
                "output": proc.stdout
            }
    except Exception as e:
        duration = round(time.time() - start, 3)
        print(f"   {C_RED}✖ ERROR{C_RESET} ({duration}s): {e}")
        return {
            "suite": suite_name,
            "status": "ERROR",
            "duration_seconds": duration,
            "output": str(e)
        }

def main():
    parser = argparse.ArgumentParser(description="Aarambh Unified QA Runner")
    parser.add_argument("--all", action="store_true", help="Run all 4 suites including heavy real-browser E2E")
    parser.add_argument("--security", action="store_true", help="Run only Security & Secret Leakage Audit")
    parser.add_argument("--models", action="store_true", help="Run only Models Manifest & VRAM Matrix")
    parser.add_argument("--api", action="store_true", help="Run only API Gateway & Backend Services")
    parser.add_argument("--e2e", action="store_true", help="Run only Real-Browser Headless E2E UI Journey")
    args = parser.parse_args()

    print_banner()
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🕒 Execution Started at: {timestamp_str}")
    print(f"🐍 Python Interpreter: {PYTHON_EXE}")

    suites_to_run = []
    
    # Selective flags or default
    if args.security:
        suites_to_run.append(("Security & Zero-Leak Audit", "🛡️", BASE_DIR / "tests" / "test_security_audit.py", []))
    elif args.models:
        suites_to_run.append(("Models Manifest & VRAM Matrix", "🧠", BASE_DIR / "tests" / "test_models_integration.py", []))
    elif args.api:
        suites_to_run.append(("Backend Gateway & API Services", "⚡", BASE_DIR / "tests" / "test_aarambh_ui_server.py", []))
    elif args.e2e:
        suites_to_run.append(("Real-Browser Headless E2E UI Journey", "🌐", BASE_DIR / "tests" / "test_e2e_ui_real_browser.py", []))
    else:
        # Default run: Security, Models, Backend APIs
        suites_to_run.append(("Security & Zero-Leak Audit", "🛡️", BASE_DIR / "tests" / "test_security_audit.py", []))
        suites_to_run.append(("Models Manifest & VRAM Matrix", "🧠", BASE_DIR / "tests" / "test_models_integration.py", []))
        suites_to_run.append(("Backend Gateway & API Services", "⚡", BASE_DIR / "tests" / "test_aarambh_ui_server.py", []))
        if args.all:
            suites_to_run.append(("Real-Browser Headless E2E UI Journey", "🌐", BASE_DIR / "tests" / "test_e2e_ui_real_browser.py", []))

    total_start = time.time()
    results = []

    for name, icon, path, cmd_args in suites_to_run:
        res = run_suite(name, icon, path, cmd_args)
        results.append(res)

    total_duration = round(time.time() - total_start, 3)
    passed_count = sum(1 for r in results if r["status"] == "PASS")
    total_count = len(results)
    pass_pct = round((passed_count / total_count) * 100, 1) if total_count > 0 else 0

    print(f"""
======================================================================
  AARAMBH QA AUDIT SUMMARY REPORT
======================================================================
  Total Suites Executed : {total_count}
  Passed Suites         : {C_GREEN}{passed_count}{C_RESET}
  Failed Suites         : {C_RED if (total_count - passed_count) > 0 else C_GREEN}{total_count - passed_count}{C_RESET}
  Overall Pass Rate     : {C_GREEN if pass_pct == 100 else C_YELLOW}{pass_pct}%{C_RESET}
  Total Execution Time  : {total_duration}s
=====================================================================""")

    # Generate persistent JSON report
    report_file = BASE_DIR / "tests" / "latest_test_report.json"
    report_data = {
        "timestamp": timestamp_str,
        "total_suites": total_count,
        "passed_suites": passed_count,
        "failed_suites": total_count - passed_count,
        "pass_rate_pct": pass_pct,
        "duration_seconds": total_duration,
        "suites": results
    }
    report_file.write_text(json.dumps(report_data, indent=2), encoding="utf-8")
    print(f"📄 Full Diagnostic Report Saved to: {report_file.resolve()}\n")

    if pass_pct == 100:
        print(f"{C_GREEN}{C_BOLD}🎉 100% PRODUCTION READY: All Quality Invariants & Security Gates Verified!{C_RESET}\n")
        sys.exit(0)
    else:
        print(f"{C_RED}{C_BOLD}⚠️ QA DEFECTS DETECTED: Fix issues before production deployment.{C_RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
