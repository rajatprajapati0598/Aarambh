# Project Aarambh (आरम्भ) — Master Studio Models Directory & Tracker

> **Persistent Blueprint for Step-by-Step Model Implementation**  
> *10 Master Studios | 51 Sovereign Models | Dual T4 30GB VRAM Matrix | Google Drive Sync*

---

## 🧭 Modular Conversation Protocol (मॉड्यूलर बातचीत का नियम)

यह फाइल हर एक नए कन्वर्सेशन के लिए **सिंगल सोर्स ऑफ ट्रुथ (Source of Truth)** है:
1. **एक कन्वर्सेशन = एक मॉडल (One Conversation = One Model)**:
   - हर नए चैट सेशन में केवल एक विशिष्ट मॉडल को लिया जाएगा ताकि मेमोरी, कोड और लॉग्स पूरी तरह सेपरेट और क्लीन रहें।
2. **4-फेज इम्प्लीमेंटेशन साइकिल**:
   - **Phase 1 (Kaggle CUDA Check):** GPU VRAM और आवश्यक लाइब्रेरीज़ का सत्यापन।
   - **Phase 2 (Inference Test):** टेस्ट प्रॉम्प्ट/इनपुट के साथ मॉडल रन और आउटपुट जनरेशन।
   - **Phase 3 (Google Drive Verification):** मॉडल आउटपुट और वेट्स का ड्राइव सिंक/बैकअप।
   - **Phase 4 (Aarambh UI & Git Sync):** Aarambh बैकएंड में लाइव कनेक्शन और गिट कमिट।
3. **प्रोग्रेस ट्रैकिंग**: मॉडल पूरा होते ही नीचे दी गई चेकलिस्ट में `[ ]` को `[x]` मार्क करें।

---

## 📋 Complete Studio-Wise Model Implementation Checklist (51 Models)

### 🏛️ Studio 01: Visual & Generative Media (19 Models)
- [ ] **Model 01:** `flux_schnell` | **Category 1.1 Text-to-Image** | FLUX.1 Schnell (Fast DiT) | `black-forest-labs/FLUX.1-schnell` | VRAM: 12 GB | Target: Colab / Kaggle
- [ ] **Model 02:** `flux_dev_fp8` | **Category 1.1 Text-to-Image** | FLUX.1-Dev (FP8 / Multi-LoRA) | `black-forest-labs/FLUX.1-dev` | VRAM: 20 GB | Target: Kaggle Ultra
- [ ] **Model 03:** `dreamshaper_8` | **Category 1.1 Text-to-Image** | DreamShaper 8 (Cyberpunk & 3D) | `Lykon/DreamShaper` | VRAM: 8 GB | Target: Colab / Kaggle
- [ ] **Model 04:** `juggernaut_xl_v9` | **Category 1.1 Text-to-Image** | Juggernaut XL v9 (Cinematic Photoreal) | `RunDiffusion/Juggernaut-XL-v9` | VRAM: 12 GB | Target: Colab / Kaggle
- [ ] **Model 05:** `sdxl_base_refiner` | **Category 1.1 Text-to-Image** | SDXL 1.0 (Full Base + Refiner) | `stabilityai/stable-diffusion-xl-base-1.0` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 06:** `kolors_2_7b` | **Category 1.1 Text-to-Image** | Kolors 2.7B (Bilingual Photoreal) | `Kwai-Kolors/Kolors` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 07:** `ltx_video_2_5` | **Category 1.2 Video Gen** | LTX-Video 2.5 DiT (High-Speed) | `Lightricks/LTX-Video` | VRAM: 14 GB | Target: Colab / Kaggle
- [ ] **Model 08:** `wan_2_1_14b` | **Category 1.2 Video Gen** | Wan 2.1 (14B DiT Cinematic FP8) | `Wan-AI/Wan2.1-T2V-14B` | VRAM: 26 GB | Target: Kaggle Ultra
- [ ] **Model 09:** `cogvideox_5b` | **Category 1.2 Video Gen** | CogVideoX-5B (DiT Temporal) | `THUDM/CogVideoX-5b` | VRAM: 18 GB | Target: Kaggle Ultra
- [ ] **Model 10:** `svd_xt` | **Category 1.2 Video Gen** | Stable Video Diffusion (SVD-XT) | `stabilityai/stable-video-diffusion-img2vid-xt-1-1` | VRAM: 15 GB | Target: Colab / Kaggle
- [ ] **Model 11:** `animatediff_v3` | **Category 1.3 Animation** | AnimateDiff v3 (Motion Module) | `guoyww/animatediff` | VRAM: 10 GB | Target: Colab / Kaggle
- [ ] **Model 12:** `live_portrait` | **Category 1.3 Face Retarget** | LivePortrait (Facial Retargeting) | `KwaiVGI/LivePortrait` | VRAM: 8 GB | Target: Colab / Kaggle
- [ ] **Model 13:** `hallo_2` | **Category 1.3 Audio Avatar** | Hallo 2 (4K Long-Duration Avatar) | `fudan-generative-ai/hallo2` | VRAM: 18 GB | Target: Kaggle Ultra
- [ ] **Model 14:** `hunyuan3d_2` | **Category 1.4 3D Mesh** | Hunyuan3D-2 (Dense Mesh Stage 1+2) | `tencent/Hunyuan3D-2` | VRAM: 22 GB | Target: Kaggle Ultra
- [ ] **Model 15:** `triposr` | **Category 1.4 3D Mesh** | TripoSR (Fast OBJ/GLB 3D) | `stabilityai/TripoSR` | VRAM: 6 GB | Target: Colab / Kaggle
- [ ] **Model 16:** `supir_upscaler` | **Category 1.6 Upscaler** | SUPIR (Photoreal Diffusion Upscaler) | `Fanghua-Yu/SUPIR` | VRAM: 22 GB | Target: Kaggle Ultra
- [ ] **Model 17:** `real_esrgan_4x` | **Category 1.6 Upscaler** | Real-ESRGAN (4x+ Upscaler) | `xinntao/Real-ESRGAN` | VRAM: 4 GB | Target: Colab / Kaggle
- [ ] **Model 18:** `codeformer` | **Category 1.6 Face Restore** | CodeFormer (Face Restoration) | `sczhou/CodeFormer` | VRAM: 4 GB | Target: Colab / Kaggle
- [ ] **Model 19:** `sam_2_large` | **Category 1.7 Segmentation** | Meta SAM 2.1 Large (Segment Anything) | `facebook/sam2.1-hiera-large` | VRAM: 8 GB | Target: Colab / Kaggle

---

### 🎙️ Studio 02: Audio, Voice & Music Studio (7 Models)
- [ ] **Model 20:** `chat_tts` | **Category 2.1 TTS** | ChatTTS (Conversational Humanlike) | `2noise/ChatTTS` | VRAM: 8 GB | Target: Colab / Kaggle
- [ ] **Model 21:** `cosyvoice_2` | **Category 2.1 TTS** | CosyVoice 2 (0.5B Multilingual Stream) | `FunAudioLLM/CosyVoice2-0.5B` | VRAM: 12 GB | Target: Colab / Kaggle
- [ ] **Model 22:** `f5_tts` | **Category 2.1 Voice Clone** | F5-TTS (Zero-Shot Voice Clone) | `SWivid/F5-TTS` | VRAM: 6 GB | Target: Colab / Kaggle
- [ ] **Model 23:** `whisper_large_v3_turbo` | **Category 2.2 Speech-to-Text** | Whisper-large-v3-turbo (Ultra-Fast) | `openai/whisper-large-v3-turbo` | VRAM: 4 GB | Target: Colab / Kaggle
- [ ] **Model 24:** `whisper_large_v3_fp16` | **Category 2.2 Speech-to-Text** | Whisper-Large-v3 (Full FP16 Ensemble) | `openai/whisper-large-v3` | VRAM: 10 GB | Target: Kaggle Ultra
- [ ] **Model 25:** `musicgen_large` | **Category 2.3 Music Gen** | Meta MusicGen Large (3.3B Stereo) | `facebook/musicgen-large` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 26:** `demucs_v4_6stem` | **Category 2.4 Stem Splitter** | Demucs v4 (HTDemucs-FT 6-Stem) | `facebook/demucs` | VRAM: 8 GB | Target: Colab / Kaggle

---

### 🧠 Studio 03: HiveMind Cognitive Lab (10 Models)
- [ ] **Model 27:** `deepseek_r1_32b_gguf` | **Category 3.1 Deep Reasoning** | DeepSeek-R1-Distill-Qwen-32B (Q4_K_M) | `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B-GGUF` | VRAM: 20 GB | Target: Kaggle Ultra
- [ ] **Model 28:** `qwq_32b_preview` | **Category 3.1 Deep Reasoning** | QwQ-32B-Preview (Math & Logic AWQ) | `Qwen/QwQ-32B-Preview-AWQ` | VRAM: 22 GB | Target: Kaggle Ultra
- [ ] **Model 29:** `deepseek_r1_14b` | **Category 3.1 Deep Reasoning** | DeepSeek-R1-Distill-Qwen-14B (Q4_K_M) | `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B-GGUF` | VRAM: 10 GB | Target: Colab / Kaggle
- [ ] **Model 30:** `mixtral_8x7b_gguf` | **Category 3.1 MoE Reasoning** | Mixtral 8x7B Instruct (47B MoE Q4) | `TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF` | VRAM: 26 GB | Target: Kaggle Ultra
- [ ] **Model 31:** `qwen_2_5_14b_instruct` | **Category 3.2 Long Synthesis** | Qwen 2.5 14B Instruct (FP16) | `Qwen/Qwen2.5-14B-Instruct` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 32:** `qwen_2_5_32b_instruct` | **Category 3.2 Long Synthesis** | Qwen 2.5 32B Instruct (AWQ 128k) | `Qwen/Qwen2.5-32B-Instruct-AWQ` | VRAM: 20 GB | Target: Kaggle Ultra
- [ ] **Model 33:** `llama_3_3_70b_gguf` | **Category 3.2 Long Synthesis** | Meta Llama 3.3 70B (IQ2_XXS Dual-T4) | `bartowski/Llama-3.3-70B-Instruct-GGUF` | VRAM: 24 GB | Target: Kaggle Ultra
- [ ] **Model 34:** `qwen_2_5_72b_gguf` | **Category 3.2 Long Synthesis** | Qwen 2.5 72B Instruct (IQ3_M Split) | `Qwen/Qwen2.5-72B-Instruct-GGUF` | VRAM: 28 GB | Target: Kaggle Ultra
- [ ] **Model 35:** `bge_m3_hybrid` | **Category 3.3 Hybrid RAG** | BGE-M3 (Dense + Sparse + ColBERT 8k) | `BAAI/bge-m3` | VRAM: 6 GB | Target: Colab / Kaggle
- [ ] **Model 36:** `seamless_m4t_v2` | **Category 3.4 Translation** | SeamlessM4T-v2-Large (2.3B Speech/Text) | `facebook/seamless-m4t-v2-large` | VRAM: 12 GB | Target: Colab / Kaggle

---

### 💻 Studio 04: Software Engineering (4 Models)
- [ ] **Model 37:** `qwen_2_5_coder_32b` | **Category 4.1 Code Gen** | Qwen 2.5 Coder 32B (AWQ / SOTA SWE) | `Qwen/Qwen2.5-Coder-32B-Instruct-AWQ` | VRAM: 20 GB | Target: Kaggle Ultra
- [ ] **Model 38:** `deepseek_coder_v2_lite` | **Category 4.1 Code Gen** | DeepSeek-Coder-V2 Lite (16B MoE 128k) | `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct` | VRAM: 12 GB | Target: Colab / Kaggle
- [ ] **Model 39:** `defog_sqlcoder_34b` | **Category 4.4 SQL Schema** | Defog SQLCoder (34B Alpha) | `defog/sqlcoder-34b-alpha` | VRAM: 22 GB | Target: Kaggle Ultra
- [ ] **Model 40:** `granite_20b_code` | **Category 4.5 IaC / DevOps** | IBM Granite 20B Code (K8s & Cloud IaC) | `ibm-granite/granite-20b-code-instruct` | VRAM: 16 GB | Target: Kaggle Ultra

---

### 🤖 Studio 05: Autonomous Agents & Physical AI (2 Models)
- [ ] **Model 41:** `ui_tars_7b` | **Category 5.2 GUI Agent** | UI-TARS 7B (Vision-to-Action OS) | `ByteDance/UI-TARS-7B-DPO` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 42:** `openvla_7b` | **Category 5.3 Robotics VLA** | OpenVLA 7B (Vision-Language-Action) | `openvla/openvla-7b` | VRAM: 16 GB | Target: Kaggle Ultra

---

### 🛡️ Studio 06: Cyber Security & Threat Intelligence (1 Model)
- [ ] **Model 43:** `codellama_34b_security` | **Category 6.2 SAST Audit** | CodeLlama-34B-Security (SAST Vulnerability) | `TheBloke/CodeLlama-34B-Instruct-GGUF` | VRAM: 22 GB | Target: Kaggle Ultra

---

### 📈 Studio 07: Enterprise Finance & Ledger (1 Model)
- [ ] **Model 44:** `fingpt_14b` | **Category 7.1 Quant Analysis** | FinGPT (14B Quant Factor & Sentiment) | `FinGPT/fingpt-forecaster_qwen2-7b_lora` | VRAM: 10 GB | Target: Colab / Kaggle

---

### 👁️ Studio 08: Vision & Document OCR (3 Models)
- [ ] **Model 45:** `qwen_2_5_vl_7b` | **Category 8.2 Multimodal VLM** | Qwen2.5-VL-7B-Instruct (Video & BBox) | `Qwen/Qwen2.5-VL-7B-Instruct` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 46:** `internvl_2_5_8b` | **Category 8.2 Multimodal VLM** | InternVL-2.5-8B (High-Res Multimodal) | `OpenGVLab/InternVL2_5-8B` | VRAM: 18 GB | Target: Kaggle Ultra
- [ ] **Model 47:** `mineru_enterprise` | **Category 8.1 Document OCR** | MinerU (PDF-Extract-Kit LaTeX & Tables) | `opendatalab/PDF-Extract-Kit` | VRAM: 8 GB | Target: Colab / Kaggle

---

### 🔬 Studio 09: Deep Science & Discovery (2 Models)
- [ ] **Model 48:** `esmfold_3b` | **Category 9.1 Protein Folding** | Meta ESMFold (3B Single-Sequence Fold) | `facebook/esmfold_v1` | VRAM: 16 GB | Target: Kaggle Ultra
- [ ] **Model 49:** `med_sam_2` | **Category 9.2 Medical Imaging** | Med-SAM-2 (Volumetric 3D CT/MRI Segment) | `bowang-lab/MedSAM` | VRAM: 10 GB | Target: Colab / Kaggle

---

### 🏭 Studio 10: Model Foundry & Hyper Runtime (2 Models)
- [ ] **Model 50:** `unsloth_qlora_32b` | **Category 10.1 Fine-Tuning** | Unsloth 5x QLoRA Trainer (14B–32B Dual-T4) | `unsloth/Qwen2.5-32B-Instruct-bnb-4bit` | VRAM: 22 GB | Target: Kaggle Ultra
- [ ] **Model 51:** `vllm_tensor_parallel` | **Category 10.2 Edge Serving** | vLLM Dual-T4 Engine (PagedAttention TP=2) | `vllm/vllm` | VRAM: 28 GB | Target: Kaggle Ultra

---

## 🚀 नए कन्वर्सेशन के लिए रेडी प्रॉम्प्ट टेम्पलेट (Starter Prompt)

जब आप नए कन्वर्सेशन में जाएं, तो बस यह प्रॉम्प्ट पेस्ट करें:

```
load persistence learning

हम Project Aarambh (आरम्भ) के मॉडल्स को एक-एक करके इम्प्लीमेंट और टेस्ट कर रहे हैं। 
कृपया D:\workspace\Aarambh\MODELS_STUDIO_DIRECTORY.md को लोड करो और आज के सेशन में हम 
Model #01: FLUX.1 Schnell (Fast DiT) - Category 1.1 Text-to-Image पर काम करेंगे। 
Kaggle पर टेस्ट रन करके आउटपुट वेरीफाई करो और फिर Drive पर सिंक करो।
```
