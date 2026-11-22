"""
Project Aarambh (आरम्भ) — Master Models Manifest.
Comprehensive directory mapping generative, cognitive & sovereign models
across all 10 Studios for Kaggle Dual-T4 (30GB VRAM) and Hugging Face ZeroGPU runners.
Supports dynamic filtering by VRAM Profile (Colab 15GB Baseline vs Kaggle 30GB Ultra).
"""
from typing import Dict, Any, List

MODELS_MANIFEST: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # STUDIO 01: VISUAL & GENERATIVE MEDIA
    # =========================================================================
    # 1.1 Text-to-Image
    "flux_schnell": {
        "studio_id": 1,
        "category_id": "1.1",
        "name": "FLUX.1 Schnell (Fast DiT)",
        "hf_repo_id": "black-forest-labs/FLUX.1-schnell",
        "file_name": "flux1-schnell.safetensors",
        "target_dir": "models/diffusion_models",
        "vram_required_gb": 12.0,
        "tier": "colab",
        "preferred_engine": "huggingface",  # ZeroGPU Serverless A100
        "task": "text-to-image"
    },
    "flux_dev_fp8": {
        "studio_id": 1,
        "category_id": "1.1",
        "name": "FLUX.1-Dev (FP8 / Multi-LoRA)",
        "hf_repo_id": "black-forest-labs/FLUX.1-dev",
        "file_name": "flux1-dev-fp8.safetensors",
        "target_dir": "models/diffusion_models",
        "vram_required_gb": 20.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",  # Dual T4 30GB
        "task": "text-to-image"
    },
    "dreamshaper_8": {
        "studio_id": 1,
        "category_id": "1.1",
        "name": "DreamShaper 8 (Cyberpunk & 3D)",
        "hf_repo_id": "Lykon/DreamShaper",
        "file_name": "DreamShaper_8_pruned.safetensors",
        "target_dir": "models/checkpoints",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "text-to-image"
    },
    "juggernaut_xl_v9": {
        "studio_id": 1,
        "category_id": "1.1",
        "name": "Juggernaut XL v9 (Cinematic)",
        "hf_repo_id": "RunDiffusion/Juggernaut-XL-v9",
        "file_name": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
        "target_dir": "models/checkpoints",
        "vram_required_gb": 12.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "text-to-image"
    },
    "kolors_2_7b": {
        "studio_id": 1,
        "category_id": "1.1",
        "name": "Kolors 2.7B (Bilingual Photoreal)",
        "hf_repo_id": "Kwai-Kolors/Kolors",
        "file_name": "kolors-text-to-image.safetensors",
        "target_dir": "models/checkpoints",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "text-to-image"
    },
    # 1.2 Video Generation
    "ltx_video_2_5": {
        "studio_id": 1,
        "category_id": "1.2",
        "name": "LTX-Video 2.5 DiT (High-Speed)",
        "hf_repo_id": "Lightricks/LTX-Video",
        "file_name": "ltx-video-2b-v0.9.1.safetensors",
        "target_dir": "models/checkpoints",
        "vram_required_gb": 14.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "text-to-video"
    },
    "wan_2_1_14b": {
        "studio_id": 1,
        "category_id": "1.2",
        "name": "Wan 2.1 (14B DiT Cinematic)",
        "hf_repo_id": "Wan-AI/Wan2.1-T2V-14B",
        "file_name": "wan2.1_t2v_14b_fp8.safetensors",
        "target_dir": "models/video_models",
        "vram_required_gb": 26.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",  # Dual T4 Device Map
        "task": "text-to-video"
    },
    "cogvideox_5b": {
        "studio_id": 1,
        "category_id": "1.2",
        "name": "CogVideoX-5B (DiT Temporal)",
        "hf_repo_id": "THUDM/CogVideoX-5b",
        "file_name": "cogvideox_5b.safetensors",
        "target_dir": "models/video_models",
        "vram_required_gb": 18.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "text-to-video"
    },
    "svd_xt": {
        "studio_id": 1,
        "category_id": "1.2",
        "name": "Stable Video Diffusion (SVD-XT)",
        "hf_repo_id": "stabilityai/stable-video-diffusion-img2vid-xt-1-1",
        "file_name": "svd_xt_1_1.safetensors",
        "target_dir": "models/checkpoints",
        "vram_required_gb": 15.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "image-to-video"
    },
    # 1.3 Motion & Animation
    "animatediff_v3": {
        "studio_id": 1,
        "category_id": "1.3",
        "name": "AnimateDiff v3 (Motion Module)",
        "hf_repo_id": "guoyww/animatediff",
        "file_name": "v3_sd15_mm.ckpt",
        "target_dir": "models/animatediff_models",
        "vram_required_gb": 10.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "motion-animation"
    },
    "live_portrait": {
        "studio_id": 1,
        "category_id": "1.3",
        "name": "LivePortrait (Facial Retargeting)",
        "hf_repo_id": "KwaiVGI/LivePortrait",
        "file_name": "base_models.tar",
        "target_dir": "models/liveportrait",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "facial-retargeting"
    },
    "hallo_2": {
        "studio_id": 1,
        "category_id": "1.3",
        "name": "Hallo 2 (4K Long-Duration Audio Avatar)",
        "hf_repo_id": "fudan-generative-ai/hallo2",
        "file_name": "hallo2_model.safetensors",
        "target_dir": "models/liveportrait",
        "vram_required_gb": 18.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "facial-retargeting"
    },
    # 1.4 3D Mesh Synthesis
    "hunyuan3d_2": {
        "studio_id": 1,
        "category_id": "1.4",
        "name": "Hunyuan3D-2 (Dense Mesh Stage 1+2)",
        "hf_repo_id": "tencent/Hunyuan3D-2",
        "file_name": "hunyuan3d-dit-v2-0.safetensors",
        "target_dir": "models/3d_models",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "mesh-3d"
    },
    "triposr": {
        "studio_id": 1,
        "category_id": "1.4",
        "name": "TripoSR (Fast OBJ/GLB)",
        "hf_repo_id": "stabilityai/TripoSR",
        "file_name": "model.ckpt",
        "target_dir": "models/3d_models",
        "vram_required_gb": 6.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "mesh-3d"
    },
    # 1.6 Super-Resolution
    "supir_upscaler": {
        "studio_id": 1,
        "category_id": "1.6",
        "name": "SUPIR (Photoreal Diffusion Upscaler)",
        "hf_repo_id": "Fanghua-Yu/SUPIR",
        "file_name": "SUPIR-v0Q.ckpt",
        "target_dir": "models/upscale_models",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "super-resolution"
    },
    "real_esrgan_4x": {
        "studio_id": 1,
        "category_id": "1.6",
        "name": "Real-ESRGAN (4x+ Upscaler)",
        "hf_repo_id": "xinntao/Real-ESRGAN",
        "file_name": "RealESRGAN_x4plus.pth",
        "target_dir": "models/upscale_models",
        "vram_required_gb": 4.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "super-resolution"
    },
    "codeformer": {
        "studio_id": 1,
        "category_id": "1.6",
        "name": "CodeFormer (Face Restoration)",
        "hf_repo_id": "sczhou/CodeFormer",
        "file_name": "codeformer.pth",
        "target_dir": "models/facerestore_models",
        "vram_required_gb": 4.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "face-restoration"
    },
    # 1.7 Segmentation
    "sam_2_large": {
        "studio_id": 1,
        "category_id": "1.7",
        "name": "Meta SAM 2.1 (Segment Anything 2.1 Large)",
        "hf_repo_id": "facebook/sam2.1-hiera-large",
        "file_name": "sam2.1_hiera_large.pt",
        "target_dir": "models/sams",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "segmentation"
    },

    # =========================================================================
    # STUDIO 02: AUDIO, VOICE & MUSIC STUDIO
    # =========================================================================
    "chat_tts": {
        "studio_id": 2,
        "category_id": "2.1",
        "name": "ChatTTS (Conversational Humanlike)",
        "hf_repo_id": "2noise/ChatTTS",
        "file_name": "model.safetensors",
        "target_dir": "models/tts",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "voice-cloning"
    },
    "cosyvoice_2": {
        "studio_id": 2,
        "category_id": "2.1",
        "name": "CosyVoice 2 (0.5B Multilingual Stream)",
        "hf_repo_id": "FunAudioLLM/CosyVoice2-0.5B",
        "file_name": "cosyvoice2.safetensors",
        "target_dir": "models/tts",
        "vram_required_gb": 12.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "voice-cloning"
    },
    "f5_tts": {
        "studio_id": 2,
        "category_id": "2.1",
        "name": "F5-TTS (Zero-Shot Voice Clone)",
        "hf_repo_id": "SWivid/F5-TTS",
        "file_name": "model_1200000.safetensors",
        "target_dir": "models/tts",
        "vram_required_gb": 6.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "voice-cloning"
    },
    "whisper_large_v3_turbo": {
        "studio_id": 2,
        "category_id": "2.2",
        "name": "Whisper-large-v3-turbo (Ultra-Fast ASR)",
        "hf_repo_id": "openai/whisper-large-v3-turbo",
        "file_name": "model.safetensors",
        "target_dir": "models/asr",
        "vram_required_gb": 4.0,
        "tier": "colab",
        "preferred_engine": "huggingface",
        "task": "speech-to-text"
    },
    "musicgen_large": {
        "studio_id": 2,
        "category_id": "2.3",
        "name": "Meta MusicGen Large (3.3B Stereo)",
        "hf_repo_id": "facebook/musicgen-large",
        "file_name": "model.safetensors",
        "target_dir": "models/audio",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "music-generation"
    },
    "demucs_v4_6stem": {
        "studio_id": 2,
        "category_id": "2.4",
        "name": "Demucs v4 (HTDemucs-FT 6-Stem Splitter)",
        "hf_repo_id": "facebook/demucs",
        "file_name": "htdemucs_ft.th",
        "target_dir": "models/audio",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "stem-separation"
    },

    # =========================================================================
    # STUDIO 03: HIVEMIND COGNITIVE LAB
    # =========================================================================
    "deepseek_r1_32b_gguf": {
        "studio_id": 3,
        "category_id": "3.1",
        "name": "DeepSeek-R1-Distill-Qwen-32B (Q4_K_M CoT)",
        "hf_repo_id": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B-GGUF",
        "file_name": "DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf",
        "target_dir": "models/llm",
        "vram_required_gb": 20.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "deep-reasoning"
    },
    "qwq_32b_preview": {
        "studio_id": 3,
        "category_id": "3.1",
        "name": "QwQ-32B-Preview (Deliberate Math & Architecture)",
        "hf_repo_id": "Qwen/QwQ-32B-Preview-AWQ",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "deep-reasoning"
    },
    "deepseek_r1_14b": {
        "studio_id": 3,
        "category_id": "3.1",
        "name": "DeepSeek-R1-Distill-Qwen-14B",
        "hf_repo_id": "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B-GGUF",
        "file_name": "DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf",
        "target_dir": "models/llm",
        "vram_required_gb": 10.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "deep-reasoning"
    },
    "qwen_2_5_32b_instruct": {
        "studio_id": 3,
        "category_id": "3.2",
        "name": "Qwen 2.5 (32B Instruct AWQ / 128k)",
        "hf_repo_id": "Qwen/Qwen2.5-32B-Instruct-AWQ",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 20.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "long-synthesis"
    },
    "bge_m3_hybrid": {
        "studio_id": 3,
        "category_id": "3.3",
        "name": "BGE-M3 (Dense + Sparse + ColBERT 8k)",
        "hf_repo_id": "BAAI/bge-m3",
        "file_name": "model.safetensors",
        "target_dir": "models/embeddings",
        "vram_required_gb": 6.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "hybrid-rag"
    },
    "seamless_m4t_v2": {
        "studio_id": 3,
        "category_id": "3.4",
        "name": "SeamlessM4T-v2-Large (2.3B Multilingual)",
        "hf_repo_id": "facebook/seamless-m4t-v2-large",
        "file_name": "model.safetensors",
        "target_dir": "models/translation",
        "vram_required_gb": 12.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "translation"
    },

    # =========================================================================
    # STUDIO 04: SOFTWARE ENGINEERING
    # =========================================================================
    "qwen_2_5_coder_32b": {
        "studio_id": 4,
        "category_id": "4.1",
        "name": "Qwen 2.5 Coder (32B AWQ / SOTA SWE)",
        "hf_repo_id": "Qwen/Qwen2.5-Coder-32B-Instruct-AWQ",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 20.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "code-synthesis"
    },
    "deepseek_coder_v2_lite": {
        "studio_id": 4,
        "category_id": "4.1",
        "name": "DeepSeek-Coder-V2 (16B MoE / 128k)",
        "hf_repo_id": "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 12.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "code-synthesis"
    },
    "defog_sqlcoder_34b": {
        "studio_id": 4,
        "category_id": "4.4",
        "name": "Defog SQLCoder (34B Schema Architect)",
        "hf_repo_id": "defog/sqlcoder-34b-alpha",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "sql-generation"
    },
    "granite_20b_code": {
        "studio_id": 4,
        "category_id": "4.5",
        "name": "Granite 20B Code (Cloud IaC & K8s)",
        "hf_repo_id": "ibm-granite/granite-20b-code-instruct",
        "file_name": "model.safetensors",
        "target_dir": "models/llm",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "iac-devops"
    },

    # =========================================================================
    # STUDIO 05: AUTONOMOUS AGENTS & PHYSICAL AI
    # =========================================================================
    "ui_tars_7b": {
        "studio_id": 5,
        "category_id": "5.2",
        "name": "UI-TARS 7B (Vision-to-Action GUI)",
        "hf_repo_id": "ByteDance/UI-TARS-7B-DPO",
        "file_name": "model.safetensors",
        "target_dir": "models/vlm",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "gui-action"
    },
    "openvla_7b": {
        "studio_id": 5,
        "category_id": "5.3",
        "name": "OpenVLA (7B Vision-Language-Action Robotics)",
        "hf_repo_id": "openvla/openvla-7b",
        "file_name": "model.safetensors",
        "target_dir": "models/vlm",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "robotics-control"
    },

    # =========================================================================
    # STUDIO 06: CYBER SECURITY & THREAT INTELLIGENCE
    # =========================================================================
    "codellama_34b_security": {
        "studio_id": 6,
        "category_id": "6.2",
        "name": "CodeLlama-34B-Security (SAST Vulnerability Audit)",
        "hf_repo_id": "TheBloke/CodeLlama-34B-Instruct-GGUF",
        "file_name": "codellama-34b-instruct.Q4_K_M.gguf",
        "target_dir": "models/llm",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "vulnerability-audit"
    },

    # =========================================================================
    # STUDIO 07: ENTERPRISE FINANCE & LEDGER
    # =========================================================================
    "fingpt_14b": {
        "studio_id": 7,
        "category_id": "7.1",
        "name": "FinGPT (14B Quant Factor & Sentiment)",
        "hf_repo_id": "FinGPT/fingpt-forecaster_qwen2-7b_lora",
        "file_name": "adapter_model.bin",
        "target_dir": "models/llm",
        "vram_required_gb": 10.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "quant-finance"
    },

    # =========================================================================
    # STUDIO 08: VISION & DOCUMENT OCR
    # =========================================================================
    "qwen_2_5_vl_7b": {
        "studio_id": 8,
        "category_id": "8.2",
        "name": "Qwen2.5-VL-7B-Instruct (Multimodal Video & BBox)",
        "hf_repo_id": "Qwen/Qwen2.5-VL-7B-Instruct",
        "file_name": "model.safetensors",
        "target_dir": "models/vlm",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "multimodal-vision"
    },
    "internvl_2_5_8b": {
        "studio_id": 8,
        "category_id": "8.2",
        "name": "InternVL-2.5-8B (High-Res Multimodal)",
        "hf_repo_id": "OpenGVLab/InternVL2_5-8B",
        "file_name": "model.safetensors",
        "target_dir": "models/vlm",
        "vram_required_gb": 18.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "multimodal-vision"
    },
    "mineru_enterprise": {
        "studio_id": 8,
        "category_id": "8.1",
        "name": "MinerU (PDF-Extract-Kit LaTeX & Tables)",
        "hf_repo_id": "opendatalab/PDF-Extract-Kit",
        "file_name": "models.tar",
        "target_dir": "models/ocr",
        "vram_required_gb": 8.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "document-ocr"
    },

    # =========================================================================
    # STUDIO 09: DEEP SCIENCE & DISCOVERY
    # =========================================================================
    "esmfold_3b": {
        "studio_id": 9,
        "category_id": "9.1",
        "name": "Meta ESMFold (3B Single-Sequence Folding)",
        "hf_repo_id": "facebook/esmfold_v1",
        "file_name": "esmfold.pt",
        "target_dir": "models/science",
        "vram_required_gb": 16.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "protein-folding"
    },
    "med_sam_2": {
        "studio_id": 9,
        "category_id": "9.2",
        "name": "Med-SAM-2 (Volumetric 3D CT/MRI Segmenter)",
        "hf_repo_id": "bowang-lab/MedSAM",
        "file_name": "medsam_vit_b.pth",
        "target_dir": "models/science",
        "vram_required_gb": 10.0,
        "tier": "colab",
        "preferred_engine": "kaggle",
        "task": "medical-segmentation"
    },

    # =========================================================================
    # STUDIO 10: MODEL FOUNDRY & HYPER RUNTIME
    # =========================================================================
    "unsloth_qlora_32b": {
        "studio_id": 10,
        "category_id": "10.1",
        "name": "Unsloth 5x QLoRA Trainer (14B–32B Dual-T4)",
        "hf_repo_id": "unsloth/Qwen2.5-32B-Instruct-bnb-4bit",
        "file_name": "model.safetensors",
        "target_dir": "models/foundry",
        "vram_required_gb": 22.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "fine-tuning"
    },
    "vllm_tensor_parallel": {
        "studio_id": 10,
        "category_id": "10.2",
        "name": "vLLM Dual-T4 Engine (PagedAttention TP=2)",
        "hf_repo_id": "vllm/vllm",
        "file_name": "engine_config.json",
        "target_dir": "models/foundry",
        "vram_required_gb": 28.0,
        "tier": "kaggle_ultra",
        "preferred_engine": "kaggle",
        "task": "edge-serving"
    }
}

def get_models_by_studio(studio_id: int, tier: str = None) -> List[Dict[str, Any]]:
    """Returns models belonging to a specific studio, optionally filtered by tier."""
    results = [m for m in MODELS_MANIFEST.values() if m["studio_id"] == studio_id]
    if tier == "colab":
        return [m for m in results if m.get("tier", "colab") == "colab"]
    return results

def get_models_by_category(category_id: str, tier: str = None) -> List[Dict[str, Any]]:
    """Returns models belonging to a subcategory, optionally filtered by tier."""
    results = [m for m in MODELS_MANIFEST.values() if m["category_id"] == category_id]
    if tier == "colab":
        return [m for m in results if m.get("tier", "colab") == "colab"]
    return results
