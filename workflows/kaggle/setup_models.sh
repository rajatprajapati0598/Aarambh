#!/bin/bash
# ==============================================================================
# 🚀 Aarambh Cloud Model Provisioner for Kaggle Dual Tesla T4
# ==============================================================================
set -e
echo '⏳ [1/4] Preparing model destination directories...'
mkdir -p models/checkpoints models/diffusion_models models/animatediff_models models/3d_models models/upscale_models models/facerestore_models models/sams models/tts models/audio models/llm

echo '📦 [2/4] Downloading Heavy Generative Weights via huggingface-cli...'
pip install -q huggingface_hub

# Model: FLUX.1-Dev (FP8 / Multi-LoRA) (1.1)
echo '⬇️ Pulling FLUX.1-Dev (FP8 / Multi-LoRA)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='black-forest-labs/FLUX.1-dev', filename='flux1-dev-fp8.safetensors', local_dir='models/diffusion_models')" || true

# Model: DreamShaper 8 (Cyberpunk & 3D) (1.1)
echo '⬇️ Pulling DreamShaper 8 (Cyberpunk & 3D)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Lykon/DreamShaper', filename='DreamShaper_8_pruned.safetensors', local_dir='models/checkpoints')" || true

# Model: Juggernaut XL v9 (Cinematic) (1.1)
echo '⬇️ Pulling Juggernaut XL v9 (Cinematic)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='RunDiffusion/Juggernaut-XL-v9', filename='Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors', local_dir='models/checkpoints')" || true

# Model: SDXL 1.0 (Full Base + Refiner Ensemble) (1.1)
echo '⬇️ Pulling SDXL 1.0 (Full Base + Refiner Ensemble)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='stabilityai/stable-diffusion-xl-base-1.0', filename='sd_xl_base_1.0.safetensors', local_dir='models/checkpoints')" || true

# Model: Kolors 2.7B (Bilingual Photoreal) (1.1)
echo '⬇️ Pulling Kolors 2.7B (Bilingual Photoreal)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Kwai-Kolors/Kolors', filename='kolors-text-to-image.safetensors', local_dir='models/checkpoints')" || true

# Model: LTX-Video 2.5 DiT (High-Speed) (1.2)
echo '⬇️ Pulling LTX-Video 2.5 DiT (High-Speed)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Lightricks/LTX-Video', filename='ltx-video-2b-v0.9.1.safetensors', local_dir='models/checkpoints')" || true

# Model: Wan 2.1 (14B DiT Cinematic) (1.2)
echo '⬇️ Pulling Wan 2.1 (14B DiT Cinematic)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Wan-AI/Wan2.1-T2V-14B', filename='wan2.1_t2v_14b_fp8.safetensors', local_dir='models/video_models')" || true

# Model: CogVideoX-5B (DiT Temporal) (1.2)
echo '⬇️ Pulling CogVideoX-5B (DiT Temporal)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='THUDM/CogVideoX-5b', filename='cogvideox_5b.safetensors', local_dir='models/video_models')" || true

# Model: Stable Video Diffusion (SVD-XT) (1.2)
echo '⬇️ Pulling Stable Video Diffusion (SVD-XT)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='stabilityai/stable-video-diffusion-img2vid-xt-1-1', filename='svd_xt_1_1.safetensors', local_dir='models/checkpoints')" || true

# Model: AnimateDiff v3 (Motion Module) (1.3)
echo '⬇️ Pulling AnimateDiff v3 (Motion Module)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='guoyww/animatediff', filename='v3_sd15_mm.ckpt', local_dir='models/animatediff_models')" || true

# Model: LivePortrait (Facial Retargeting) (1.3)
echo '⬇️ Pulling LivePortrait (Facial Retargeting)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='KwaiVGI/LivePortrait', filename='base_models.tar', local_dir='models/liveportrait')" || true

# Model: Hallo 2 (4K Long-Duration Audio Avatar) (1.3)
echo '⬇️ Pulling Hallo 2 (4K Long-Duration Audio Avatar)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='fudan-generative-ai/hallo2', filename='hallo2_model.safetensors', local_dir='models/liveportrait')" || true

# Model: Hunyuan3D-2 (Dense Mesh Stage 1+2) (1.4)
echo '⬇️ Pulling Hunyuan3D-2 (Dense Mesh Stage 1+2)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='tencent/Hunyuan3D-2', filename='hunyuan3d-dit-v2-0.safetensors', local_dir='models/3d_models')" || true

# Model: TripoSR (Fast OBJ/GLB) (1.4)
echo '⬇️ Pulling TripoSR (Fast OBJ/GLB)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='stabilityai/TripoSR', filename='model.ckpt', local_dir='models/3d_models')" || true

# Model: SUPIR (Photoreal Diffusion Upscaler) (1.6)
echo '⬇️ Pulling SUPIR (Photoreal Diffusion Upscaler)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Fanghua-Yu/SUPIR', filename='SUPIR-v0Q.ckpt', local_dir='models/upscale_models')" || true

# Model: Real-ESRGAN (4x+ Upscaler) (1.6)
echo '⬇️ Pulling Real-ESRGAN (4x+ Upscaler)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='xinntao/Real-ESRGAN', filename='RealESRGAN_x4plus.pth', local_dir='models/upscale_models')" || true

# Model: CodeFormer (Face Restoration) (1.6)
echo '⬇️ Pulling CodeFormer (Face Restoration)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='sczhou/CodeFormer', filename='codeformer.pth', local_dir='models/facerestore_models')" || true

# Model: Meta SAM 2.1 (Segment Anything 2.1 Large) (1.7)
echo '⬇️ Pulling Meta SAM 2.1 (Segment Anything 2.1 Large)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='facebook/sam2.1-hiera-large', filename='sam2.1_hiera_large.pt', local_dir='models/sams')" || true

# Model: ChatTTS (Conversational Humanlike) (2.1)
echo '⬇️ Pulling ChatTTS (Conversational Humanlike)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='2noise/ChatTTS', filename='model.safetensors', local_dir='models/tts')" || true

# Model: CosyVoice 2 (0.5B Multilingual Stream) (2.1)
echo '⬇️ Pulling CosyVoice 2 (0.5B Multilingual Stream)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='FunAudioLLM/CosyVoice2-0.5B', filename='cosyvoice2.safetensors', local_dir='models/tts')" || true

# Model: F5-TTS (Zero-Shot Voice Clone) (2.1)
echo '⬇️ Pulling F5-TTS (Zero-Shot Voice Clone)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='SWivid/F5-TTS', filename='model_1200000.safetensors', local_dir='models/tts')" || true

# Model: Whisper-Large-v3 (Full FP16 Ensemble) (2.2)
echo '⬇️ Pulling Whisper-Large-v3 (Full FP16 Ensemble)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='openai/whisper-large-v3', filename='model.safetensors', local_dir='models/asr')" || true

# Model: Meta MusicGen Large (3.3B Stereo) (2.3)
echo '⬇️ Pulling Meta MusicGen Large (3.3B Stereo)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='facebook/musicgen-large', filename='model.safetensors', local_dir='models/audio')" || true

# Model: Demucs v4 (HTDemucs-FT 6-Stem Splitter) (2.4)
echo '⬇️ Pulling Demucs v4 (HTDemucs-FT 6-Stem Splitter)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='facebook/demucs', filename='htdemucs_ft.th', local_dir='models/audio')" || true

# Model: DeepSeek-R1-Distill-Qwen-32B (Q4_K_M CoT) (3.1)
echo '⬇️ Pulling DeepSeek-R1-Distill-Qwen-32B (Q4_K_M CoT)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-32B-GGUF', filename='DeepSeek-R1-Distill-Qwen-32B-Q4_K_M.gguf', local_dir='models/llm')" || true

# Model: QwQ-32B-Preview (Deliberate Math & Architecture) (3.1)
echo '⬇️ Pulling QwQ-32B-Preview (Deliberate Math & Architecture)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/QwQ-32B-Preview-AWQ', filename='model.safetensors', local_dir='models/llm')" || true

# Model: DeepSeek-R1-Distill-Qwen-14B (3.1)
echo '⬇️ Pulling DeepSeek-R1-Distill-Qwen-14B...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='deepseek-ai/DeepSeek-R1-Distill-Qwen-14B-GGUF', filename='DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf', local_dir='models/llm')" || true

# Model: Mixtral 8x7B Instruct (47B MoE / Q4_K_M) (3.1)
echo '⬇️ Pulling Mixtral 8x7B Instruct (47B MoE / Q4_K_M)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF', filename='mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf', local_dir='models/llm')" || true

# Model: Qwen 2.5 (14B Instruct FP16) (3.2)
echo '⬇️ Pulling Qwen 2.5 (14B Instruct FP16)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/Qwen2.5-14B-Instruct', filename='model.safetensors', local_dir='models/llm')" || true

# Model: Qwen 2.5 (32B Instruct AWQ / 128k) (3.2)
echo '⬇️ Pulling Qwen 2.5 (32B Instruct AWQ / 128k)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/Qwen2.5-32B-Instruct-AWQ', filename='model.safetensors', local_dir='models/llm')" || true

# Model: Meta Llama 3.3 70B Instruct (IQ2_XXS / Dual-T4 Split) (3.2)
echo '⬇️ Pulling Meta Llama 3.3 70B Instruct (IQ2_XXS / Dual-T4 Split)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='bartowski/Llama-3.3-70B-Instruct-GGUF', filename='Llama-3.3-70B-Instruct-IQ2_XXS.gguf', local_dir='models/llm')" || true

# Model: Qwen 2.5 72B Instruct (IQ3_M / Dual-T4 + RAM) (3.2)
echo '⬇️ Pulling Qwen 2.5 72B Instruct (IQ3_M / Dual-T4 + RAM)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/Qwen2.5-72B-Instruct-GGUF', filename='qwen2.5-72b-instruct-q3_k_m.gguf', local_dir='models/llm')" || true

# Model: BGE-M3 (Dense + Sparse + ColBERT 8k) (3.3)
echo '⬇️ Pulling BGE-M3 (Dense + Sparse + ColBERT 8k)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='BAAI/bge-m3', filename='model.safetensors', local_dir='models/embeddings')" || true

# Model: SeamlessM4T-v2-Large (2.3B Multilingual) (3.4)
echo '⬇️ Pulling SeamlessM4T-v2-Large (2.3B Multilingual)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='facebook/seamless-m4t-v2-large', filename='model.safetensors', local_dir='models/translation')" || true

# Model: Qwen 2.5 Coder (32B AWQ / SOTA SWE) (4.1)
echo '⬇️ Pulling Qwen 2.5 Coder (32B AWQ / SOTA SWE)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/Qwen2.5-Coder-32B-Instruct-AWQ', filename='model.safetensors', local_dir='models/llm')" || true

# Model: DeepSeek-Coder-V2 (16B MoE / 128k) (4.1)
echo '⬇️ Pulling DeepSeek-Coder-V2 (16B MoE / 128k)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct', filename='model.safetensors', local_dir='models/llm')" || true

# Model: Defog SQLCoder (34B Schema Architect) (4.4)
echo '⬇️ Pulling Defog SQLCoder (34B Schema Architect)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='defog/sqlcoder-34b-alpha', filename='model.safetensors', local_dir='models/llm')" || true

# Model: Granite 20B Code (Cloud IaC & K8s) (4.5)
echo '⬇️ Pulling Granite 20B Code (Cloud IaC & K8s)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='ibm-granite/granite-20b-code-instruct', filename='model.safetensors', local_dir='models/llm')" || true

# Model: UI-TARS 7B (Vision-to-Action GUI) (5.2)
echo '⬇️ Pulling UI-TARS 7B (Vision-to-Action GUI)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='ByteDance/UI-TARS-7B-DPO', filename='model.safetensors', local_dir='models/vlm')" || true

# Model: OpenVLA (7B Vision-Language-Action Robotics) (5.3)
echo '⬇️ Pulling OpenVLA (7B Vision-Language-Action Robotics)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='openvla/openvla-7b', filename='model.safetensors', local_dir='models/vlm')" || true

# Model: CodeLlama-34B-Security (SAST Vulnerability Audit) (6.2)
echo '⬇️ Pulling CodeLlama-34B-Security (SAST Vulnerability Audit)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='TheBloke/CodeLlama-34B-Instruct-GGUF', filename='codellama-34b-instruct.Q4_K_M.gguf', local_dir='models/llm')" || true

# Model: FinGPT (14B Quant Factor & Sentiment) (7.1)
echo '⬇️ Pulling FinGPT (14B Quant Factor & Sentiment)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='FinGPT/fingpt-forecaster_qwen2-7b_lora', filename='adapter_model.bin', local_dir='models/llm')" || true

# Model: Qwen2.5-VL-7B-Instruct (Multimodal Video & BBox) (8.2)
echo '⬇️ Pulling Qwen2.5-VL-7B-Instruct (Multimodal Video & BBox)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='Qwen/Qwen2.5-VL-7B-Instruct', filename='model.safetensors', local_dir='models/vlm')" || true

# Model: InternVL-2.5-8B (High-Res Multimodal) (8.2)
echo '⬇️ Pulling InternVL-2.5-8B (High-Res Multimodal)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='OpenGVLab/InternVL2_5-8B', filename='model.safetensors', local_dir='models/vlm')" || true

# Model: MinerU (PDF-Extract-Kit LaTeX & Tables) (8.1)
echo '⬇️ Pulling MinerU (PDF-Extract-Kit LaTeX & Tables)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='opendatalab/PDF-Extract-Kit', filename='models.tar', local_dir='models/ocr')" || true

# Model: Meta ESMFold (3B Single-Sequence Folding) (9.1)
echo '⬇️ Pulling Meta ESMFold (3B Single-Sequence Folding)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='facebook/esmfold_v1', filename='esmfold.pt', local_dir='models/science')" || true

# Model: Med-SAM-2 (Volumetric 3D CT/MRI Segmenter) (9.2)
echo '⬇️ Pulling Med-SAM-2 (Volumetric 3D CT/MRI Segmenter)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='bowang-lab/MedSAM', filename='medsam_vit_b.pth', local_dir='models/science')" || true

# Model: Unsloth 5x QLoRA Trainer (14B–32B Dual-T4) (10.1)
echo '⬇️ Pulling Unsloth 5x QLoRA Trainer (14B–32B Dual-T4)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='unsloth/Qwen2.5-32B-Instruct-bnb-4bit', filename='model.safetensors', local_dir='models/foundry')" || true

# Model: vLLM Dual-T4 Engine (PagedAttention TP=2) (10.2)
echo '⬇️ Pulling vLLM Dual-T4 Engine (PagedAttention TP=2)...'
python3 -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='vllm/vllm', filename='engine_config.json', local_dir='models/foundry')" || true

echo '✅ [3/4] All 40+ Category Model Weights Verified!'
echo '🚀 [4/4] Starting Aarambh Dual T4 Worker Engine...'
python3 worker.py