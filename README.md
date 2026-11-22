# 🚀 Project Aarambh (आरम्भ)

> **Next-Generation Open-Source Multi-Modal AI Enterprise Suite**  
> *Dedicated Multi-Studio Architecture | 40 Open-Source AI Domains Blueprint | Dynamic Zero-OOM VRAM Management*

---

## 🌟 Overview

**Aarambh (आरम्भ)** is an enterprise-grade, fully open-source AI studio environment designed to bridge local orchestration with remote/cloud compute engines (Google Colab Tesla T4 testbed and future high-VRAM personal workstations such as RTX 4090 / A100 / Dual-GPU rigs).

### 🏛️ Architecture Highlights:
- **Decoupled Gateway Protocol**: The UI and application logic connect via standard WebSocket (`ws://` / `wss://`) and REST endpoints (`POST /free`, `GET /system_stats`, `POST /prompt`), ensuring that migrating from Colab to a local workstation requires changing only the Gateway URL without modifying any code.
- **Dynamic VRAM Purge (`POST /free`)**: Ensures an automatic VRAM flush down to 0 MB baseline whenever switching between studios or models, guaranteeing that only one model occupies GPU memory at any given time.
- **Multi-Studio Layout**: Independent dedicated page views for creative, cognitive, developer, and scientific workflows.

---

## 📁 Repository Structure

```
D:\workspace\Aarambh\
├── colab\
│   └── ComfyUI_Streaming_Gateway.ipynb   # Colab notebook gateway with aria2c skips & tunnel
├── src\
│   ├── video_pipeline.py                 # LTX-Video 2.5 streaming pipeline
│   └── textured_3d_pipeline.py           # Hunyuan3D-2 CPU-offload 3D pipeline
├── studio\
│   └── app.py                            # Streamlit multi-page frontend
├── workflows\
│   ├── 3d_textured_hunyuan.json          # Hunyuan3D-2 ComfyUI execution graph
│   ├── image_sdxl_streaming.json         # SDXL / DreamShaper streaming graph
│   └── video_ltx_t4.json                 # LTX-Video 2.5 + T5 text encoder graph
├── docs\                                 # Architectural specifications & blueprints
├── README.md                             # Project overview & running instructions
└── MANIFEST.md                           # Component catalog & migration roadmap
```

---

## 🔌 Connection & Runtime Setup

### 1. Remote GPU Gateway (Google Colab)
Open `colab/ComfyUI_Streaming_Gateway.ipynb` in Google Colab (with Tesla T4 GPU enabled):
1. Execute **Runtime -> Run all** (`Ctrl+F9`).
2. Cell 5 will output the live **PUBLIC GATEWAY URL** (via Cloudflare tunnel or Ngrok).

### 2. Launching Aarambh Enterprise Suite (Gamma Hive UI v2.0)
Launch the Claymorphic / Neumorphic Glass UI with persistent Inbuilt Workbench and zero-reload Colab connectivity:
```powershell
& "D:\workspace\venv\Scripts\python.exe" "D:\workspace\Aarambh\run_aarambh.py"
```
Or launch as an isolated native Edge WebView2 desktop container:
```powershell
& "D:\workspace\venv\Scripts\python.exe" "D:\workspace\Aarambh\run_aarambh.py" --desktop
```

*(Legacy Streamlit frontend is still accessible via `& "D:\workspace\venv\Scripts\streamlit.exe" run "D:\workspace\Aarambh\studio\app.py"`)*

---

## 🗺️ Master Blueprint (40 Open-Source Categories Roadmap)

Aarambh is designed to incrementally integrate all 40 open-source AI categories:
1. **🎨 Visual & Generative Media** (Image, Video, Animation, 3D Mesh, 3DGS, Upscaling, SAM 2, PBR)
2. **🎙️ Audio, Voice & Music** (Zero-Shot TTS/F5-TTS, Whisper STT, MusicGen, Demucs)
3. **🧠 HiveMind & Cognition** (DeepSeek-R1, Qwen 2.5, Gemma 2, Llama 3.1, Hybrid RAG)
4. **💻 Software & Systems** (Qwen Coder, bolt.diy, Kotlin Android, SQLCoder, DevOps)
5. **🤖 Autonomous Agents & Physical AI** (AutoGen, UI-TARS Computer-Use, LeRobot)
6. **🛡️ Cyber Security & Forensics** (PentestGPT, Semgrep AI, Deepfake Detectors)
7. **📈 Enterprise & Quant Trading** (FinGPT, Microsoft Qlib, Fraud GNN)
8. **📄 Vision & Document Intelligence** (MinerU, Surya OCR, Florence-2)
9. **🧬 Deep Science & Discovery** (ESMFold, AlphaFold 2, GraphCast)
10. **⚙️ Model Foundry & Runtime** (Unsloth LoRA, llama.cpp GGUF, vLLM)
