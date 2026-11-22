# 📦 Project Aarambh — Technical Manifest v2.0

| Component | Path | Status | Target Runtime | Description |
|---|---|---|---|---|
| **Gamma Hive Enterprise UI** | `studio/static/index.html` | ✅ Production Ready | Web / Localhost (:8501) | Claymorphic/Neumorphic frosted glass UI with 10 Master Studios & 40 Categories matching GIF specifications |
| **Aarambh API Gateway Server** | `studio/server.py` | ✅ Production Ready | FastAPI / Uvicorn (:8501) | High-performance backend with async Colab connectivity check, log console, and reverse proxy |
| **Suite Launcher** | `run_aarambh.py` | ✅ Verified | Python CLI | Auto-launches server, browser, and optional PyWebView native Edge WebView2 container |
| **Inbuilt Cloud Workbench** | `studio/static/js/app.js` | ✅ Production Ready | Browser Client (SPA) | Persistent zero-refresh embedded browser for Google Colab, HuggingFace, Kaggle, Civitai |
| **Universal Error Console** | `studio/static/js/app.js` | ✅ Production Ready | All Pages & Sections | Global slide-out diagnostic drawer + inline section error triggers with open/close/copy |
| **Colab Gateway** | `colab/ComfyUI_Streaming_Gateway.ipynb` | ✅ Production Ready | Colab Tesla T4 | Automated aria2c checkpoint downloads, ComfyUI, 120s timeout, dual Ngrok/Cloudflared tunnels |
| **Video Pipeline** | `src/video_pipeline.py` | ✅ Verified | Colab / Workstation | LTX-Video 2.5 DiT + T5 fp8 text encoder streaming pipeline |
| **3D Mesh Pipeline** | `src/textured_3d_pipeline.py` | ✅ Verified | Colab / Workstation | Hunyuan3D-2 shape DiT + CPU offloading + texture baking pipeline |
| **SDXL Streaming Graph** | `workflows/image_sdxl_streaming.json` | ✅ Verified | ComfyUI Engine | SDXL/DreamShaper/Realistic Vision/Juggernaut XL pipeline |
| **Video Workflow Graph** | `workflows/video_ltx_t4.json` | ✅ Verified | ComfyUI Engine | LTX-Video 2.5 graph with Node 8 CLIPLoader |
| **3D Mesh Workflow Graph** | `workflows/3d_textured_hunyuan.json` | ✅ Verified | ComfyUI Engine | Hunyuan3D-2 graph with Hy3DOffloadToCPU |
| **WebSocket Bridge** | `D:\workspace\lib\comfy_ws_bridge.py` | ✅ Verified (48/48 Tests) | Local Shared Lib | Real-time WebSocket streaming with `out[8:]` frame slicing & `/free` flush |
| **Legacy Streamlit UI** | `studio/app.py` | ✅ Maintained | Local Streamlit (:8501) | Multi-page creative interface with dynamic VRAM flush & mutex locking |
