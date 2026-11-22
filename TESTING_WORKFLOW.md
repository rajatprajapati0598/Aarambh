# Project Aarambh (आरम्भ) — Enterprise Testing & QA Workflow

> **Standard Operating Procedure (SOP) & Testing Architecture**  
> *10 Master Studios | 40 Sub-Categories | Dual T4 30GB VRAM Matrix | Zero-Leak Security Shield*

---

## 1. Overview & Testing Philosophy

Project Aarambh is a multi-tier AI orchestrator combining generative media, deep reasoning, real-time audio, and autonomous agent studios running on dual hardware profiles (**Google Colab 15GB T4** & **Kaggle 30GB Dual T4**). 

To ensure stability across high-compute AI models and complex web frontends, Aarambh adopts an **Automated Defense-in-Depth QA Workflow** based on standard **Software Testing Life Cycle (STLC)** principles used across top tech organizations.

```
+---------------------------------------------------------------------------------+
|                        AARAMBH QA DEFENSE-IN-DEPTH PIPELINE                     |
+---------------------------------------------------------------------------------+
|                                                                                 |
|  [ LAYER 1 ] Security & Zero-Leak Shield                                         |
|              -> Scans code for API keys, tokens (ghp_, HF, Kaggle), .gitignore  |
|                                                                                 |
|  [ LAYER 2 ] AI Models Manifest & VRAM Matrix                                   |
|              -> Verifies 40+ models, quantization formats & 15GB/30GB VRAM fit  |
|                                                                                 |
|  [ LAYER 3 ] Backend Gateway & API Integration                                  |
|              -> Tests FastAPI endpoints, MCP status, telemetry, proxy & logs    |
|                                                                                 |
|  [ LAYER 4 ] Real-Browser Headless E2E UI Journey                               |
|              -> Automated Edge/Chrome Playwright: 10 Studios, 40 Categories,    |
|                 Error Drawer 6-filter tabs, 1-Click Copy & Zero Console Errors  |
+---------------------------------------------------------------------------------+
```

---

## 2. Software Testing Life Cycle (STLC) in Aarambh

| STLC Phase | Aarambh Implementation | Tooling / Artifact |
| :--- | :--- | :--- |
| **1. Requirement Analysis** | Validates hardware profiles (Colab 15GB vs Kaggle 30GB) and studio specs | `models_manifest.py` |
| **2. Test Planning** | Defines test coverage across Security, Models, APIs, and UI UX | `TESTING_WORKFLOW.md` |
| **3. Test Case Design** | Parameterized test suites covering nominal, boundary, and edge conditions | `tests/test_*.py` |
| **4. Test Environment** | Python 3.12 venv, Playwright headless Chrome/Edge, FastAPI local server | `run_aarambh.py` |
| **5. Test Execution** | Master unified CLI runner with instant pass/fail telemetry | `run_tests.py`, `run_tests.bat` |
| **6. Defect Logging** | System error drawer with 6 categorical filters & JSON audit reports | `tests/latest_test_report.json` |
| **7. Release Sign-off** | 100% test pass requirement before any GitHub commit/push | GitHub pre-push protocol |

---

## 3. The 4 Core Testing Layers

### 🛡️ Layer 1: Security & Zero-Leak Audit
- **Test File**: `tests/test_security_audit.py`
- **Objective**: Prevent accidental leakage of credentials, tokens, or PII into public git repositories or client-facing browsers.
- **Checks Performed**:
  - Scans all `.html`, `.js`, `.py`, `.json`, and `.md` files for regex token patterns (`ghp_`, `github_pat_`, `KGAT_`, `hf_`, AWS access keys).
  - Validates `.gitignore` enforcement for sensitive folders (`.secrets/`, `__pycache__/`, `.env`).
  - Verifies zero hardcoded private paths in client-facing bundles.

### 🧠 Layer 2: AI Models Manifest & VRAM Budget Matrix
- **Test File**: `tests/test_models_integration.py`
- **Objective**: Ensure that all models configured in Aarambh are mathematically bound to the supported GPU VRAM limits.
- **Checks Performed**:
  - Verifies all 40+ model declarations across the 10 studios.
  - Ensures quantization formats (4-bit AWQ, 8-bit FP8, 16-bit BF16) match target VRAM budgets:
    - **Colab Mode**: Up to 15 GB VRAM (T4 Single).
    - **Kaggle Ultra Mode**: Up to 30 GB VRAM (Dual T4 2x15GB).
  - Validates metadata integrity: `studio_id`, `category_id`, `preferred_engine`, and inference parameters.

### ⚡ Layer 3: Backend Gateway & API Services
- **Test File**: `tests/test_aarambh_ui_server.py`
- **Objective**: Ensure backend server stability, endpoint responsiveness, and real-time telemetry streaming.
- **Checks Performed**:
  - `GET /` — Serves main Aarambh workspace frontend with HTTP 200.
  - `GET /static/{file}` — Validates static CSS, JS, and asset routing.
  - `GET /api/mcp/status` — Checks active MCP cluster health (Kaggle, Colab, HuggingFace).
  - `GET /api/tunnel_hud` — Validates tunneling bridge status.
  - `GET /api/check_gateway` — Verifies external routing reachability.
  - Log ingestion & retrieval endpoint lifecycle.

### 🌐 Layer 4: Real-Browser Headless E2E UI Journey
- **Test File**: `tests/test_e2e_ui_real_browser.py`
- **Objective**: Simulate real user actions in an actual browser engine (Chrome / Edge) using Playwright.
- **Checks Performed**:
  - **Hardware Profile Switches**: Clicks `Colab 15GB` and `Kaggle 30GB Ultra` buttons and verifies CSS class binding and state persistence.
  - **10 Master Studios**: Sequentially activates Studio 01 through Studio 10, asserting category cards and model selectors render properly.
  - **40 Sub-Categories**: Confirms each studio loads its respective subcategory filters without layout breaks.
  - **Error Logs Drawer**: Opens sliding drawer and tests all **6 Filter Tabs**:
    - `ALL` (complete log buffer)
    - `🚨 ERRORS` (isolated critical issues)
    - `⚠️ WARNINGS` (memory or rate warnings)
    - `✅ SUCCESS` (completed inferences & mounts)
    - `ℹ️ INFO` (status telemetry)
    - `⚙️ SYSTEM` (MCP daemon & core events)
  - **1-Click Copy**: Verifies individual log row copy buttons with dynamic `✅ Copied!` clipboard confirmation.
  - **Zero-Error Invariant**: Asserts zero unhandled JavaScript page errors and zero runtime exceptions in the browser console.

---

## 4. How to Execute the QA Suite

### Option A: Using Windows 1-Click Launcher (Batch)
Double-click `run_tests.bat` or run from terminal:
```cmd
.\run_tests.bat
```
Interactive menu options:
1. `Run Complete QA Suite (Security + Models + APIs + Browser E2E)`
2. `Fast Health Check (Security + Models + APIs)`
3. `Security & Secret Leak Audit Only`
4. `AI Model Manifest & VRAM Budget Matrix Only`
5. `Backend Gateway & API Services Only`
6. `Real-Browser Headless E2E UI Audit Only`
7. `View Latest Diagnostic Report (JSON)`

### Option B: Using Python CLI

```powershell
# 1. Run Complete QA Suite (all 4 layers including Real-Browser E2E)
python run_tests.py --all

# 2. Fast Pre-Commit Smoke Check (< 3 seconds)
python run_tests.py

# 3. Layer-Specific Testing
python run_tests.py --security   # Security and secret leak audit
python run_tests.py --models     # AI Models manifest & VRAM budget
python run_tests.py --api        # Backend FastAPI server endpoints
python run_tests.py --e2e        # Playwright Real-Browser UI Journey
```

---

## 5. Defect Severity & Classification Guide

When a test fails, classify the defect according to industry standards:

| Severity | Category | Example in Aarambh | Action Required |
| :--- | :--- | :--- | :--- |
| **P0 - Blocker** | Security / Crash | Secret token detected in code, or server fails to boot | Immediate halt. Do not push to git. |
| **P1 - Critical** | Model / OOM | Model requires 34GB on a 30GB Kaggle budget | Adjust model quantization or VRAM limit. |
| **P2 - Major** | UI / Routing | Studio card click doesn't display subcategories | Fix event listener or DOM selector. |
| **P3 - Minor** | Telemetry / Copy | Copy button clipboard tooltip delay | Styling or timing adjustment. |

---

## 6. Pre-Push Verification Invariant

Before any code is committed or pushed to GitHub:
1. Ensure the background Aarambh server is alive: `http://127.0.0.1:8501`.
2. Run `python run_tests.py --all`.
3. Verify that **Overall Pass Rate is 100.0%**.
4. Commit with descriptive semantic tags:
   - `feat(studio-name): add model XYZ with 4-bit AWQ`
   - `fix(error-drawer): resolve filter tab selector mismatch`
   - `test(e2e): update playwright browser resilient launcher`
5. Push to `main` branch.
