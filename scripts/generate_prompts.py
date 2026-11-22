import sys
from pathlib import Path

# Add src to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from models_manifest import MODELS_MANIFEST

STUDIO_NAMES = {
    1: "Studio 01: Visual & Generative Media",
    2: "Studio 02: Audio, Voice & Music Studio",
    3: "Studio 03: HiveMind Cognitive Lab",
    4: "Studio 04: Software Engineering",
    5: "Studio 05: Autonomous Agents & Physical AI",
    6: "Studio 06: Cyber Security & Threat Intelligence",
    7: "Studio 07: Enterprise Finance & Ledger",
    8: "Studio 08: Vision & Document OCR",
    9: "Studio 09: Deep Science & Discovery",
    10: "Studio 10: Model Foundry & Hyper Runtime"
}

CATEGORY_NAMES = {
    "1.1": "Text-to-Image Generation",
    "1.2": "Text-to-Video Generation",
    "1.3": "Motion & Animation / Facial Retargeting",
    "1.4": "3D Mesh & Asset Synthesis",
    "1.6": "Super-Resolution & Restoration",
    "1.7": "Segmentation & Masking",
    "2.1": "Conversational TTS & Voice Cloning",
    "2.2": "Speech-to-Text & Transcription",
    "2.3": "Music & Audio Synthesis",
    "2.4": "Audio Stem Separation",
    "3.1": "Deep Reasoning & CoT (Chain of Thought)",
    "3.2": "Long-Form Synthesis & Instruction",
    "3.3": "Hybrid RAG & Embedding",
    "3.4": "Multimodal Translation",
    "4.1": "Code Synthesis & Debugging",
    "4.4": "SQL & Schema Architecture",
    "4.5": "Cloud IaC & DevOps",
    "5.2": "Vision-to-Action OS & GUI Agent",
    "5.3": "Robotics & Physical VLA",
    "6.2": "SAST Vulnerability & Security Audit",
    "7.1": "Quantitative Finance & Sentiment",
    "8.1": "Complex Document & Table OCR",
    "8.2": "Multimodal Vision & Video Understanding",
    "9.1": "Single-Sequence Protein Folding",
    "9.2": "Volumetric 3D Medical Imaging",
    "10.1": "High-Efficiency QLoRA Fine-Tuning",
    "10.2": "Dual-T4 Tensor-Parallel Edge Serving"
}

lines = []
lines.append("# Project Aarambh (आरम्भ) — Master Starter Prompts Directory (51 Models)\n\n")
lines.append("> **100% REAL MODEL WEIGHTS DOWNLOAD & ZERO DUMMY CODE DIRECTIVE**  \n")
lines.append("> *Ready-to-Copy Starter Prompts for 1-Model-Per-Conversation Modular Architecture.*  \n")
lines.append("> *Every prompt explicitly enforces real weight downloading, real GPU inference, and Google Drive sync.*  \n\n")
lines.append("---\n\n")
lines.append("## 📌 Table of Contents (All 51 Models)\n\n")

# Table of contents
idx = 1
for key, m in MODELS_MANIFEST.items():
    name = m["name"]
    lines.append(f"- [Model {idx:02d}: {name}](#model-{idx:02d}-{key.replace('_', '-')})\n")
    idx += 1

lines.append("\n---\n\n")

model_idx = 1
current_studio = None

for key, m in MODELS_MANIFEST.items():
    s_id = m["studio_id"]
    if s_id != current_studio:
        current_studio = s_id
        studio_title = STUDIO_NAMES.get(s_id, f"Studio {s_id:02d}")
        lines.append(f"\n# 🏛️ {studio_title}\n\n")
    
    num_str = f"{model_idx:02d}"
    name = m["name"]
    cat = m["category_id"]
    cat_desc = CATEGORY_NAMES.get(cat, "AI Task")
    repo = m["hf_repo_id"]
    file_name = m.get("file_name", "model.safetensors")
    target_dir = m.get("target_dir", "models/checkpoints")
    vram = m["vram_required_gb"]
    tier_label = "Kaggle Ultra (Dual-T4 30GB)" if m.get("tier") == "kaggle_ultra" else "Colab 15GB / Kaggle 30GB"
    engine = m.get("preferred_engine", "kaggle")
    task = m.get("task", "inference")
    
    anchor_id = f"model-{num_str}-{key.replace('_', '-')}"
    lines.append(f"<a id=\"{anchor_id}\"></a>\n")
    lines.append(f"### 🏷️ Model {num_str}: {name}\n")
    lines.append(f"- **Studio:** {STUDIO_NAMES.get(s_id)}  \n")
    lines.append(f"- **Category:** {cat} ({cat_desc})  \n")
    lines.append(f"- **Model Key:** `{key}`  \n")
    lines.append(f"- **HuggingFace Repo:** [`{repo}`](https://huggingface.co/{repo})  \n")
    lines.append(f"- **Primary File:** `{file_name}`  \n")
    lines.append(f"- **Target Kaggle Path:** `/kaggle/working/{target_dir}/`  \n")
    lines.append(f"- **VRAM Required:** `{vram} GB` ({tier_label})  \n")
    lines.append(f"- **Engine & Task:** `{engine}` / `{task}`  \n\n")
    
    lines.append("**👇 Copy Prompt for New Conversation:**\n\n")
    lines.append("```markdown\n")
    lines.append("load persistence learning\n\n")
    lines.append("⚠️ STRICT MANDATE: ZERO DUMMY / NO SIMULATION / REAL WEIGHTS DOWNLOAD REQUIRED\n")
    lines.append("इस सत्र में कोई भी डमी (Mock/Fake/Dummy/Placeholder) कोड स्वीकार्य नहीं है। हमें Hugging Face से वास्तविक मॉडल फाइल्स/वेट्स डाउनलोड करने हैं, Kaggle Dual-T4 GPU पर वास्तविक इनफ्रेंस चलाना है, और जनरेटेड आउटपुट व मॉडल को Google Drive पर सिंक और वेरीफाई करना है।\n\n")
    lines.append("हम Project Aarambh (आरम्भ) के मॉडल्स को एक-एक करके लाइव टेस्ट और इंटीग्रेट कर रहे हैं। \n")
    lines.append("कृपया D:\\workspace\\Aarambh\\MODELS_STUDIO_DIRECTORY.md और D:\\workspace\\Aarambh\\MODEL_STARTER_PROMPTS.md को लोड करो। \n\n")
    lines.append(f"आज के इस नए कन्वर्सेशन में हम केवल और केवल Model #{num_str} पर काम करेंगे:\n")
    lines.append(f"- Model ID: {key}\n")
    lines.append(f"- Model Name: {name}\n")
    lines.append(f"- Studio: {STUDIO_NAMES.get(s_id)} — Category {cat} ({cat_desc})\n")
    lines.append(f"- HuggingFace Repo: {repo}\n")
    lines.append(f"- Primary File: {file_name}\n")
    lines.append(f"- Target Kaggle Directory: /kaggle/working/{target_dir}/\n")
    lines.append(f"- VRAM Budget: {vram} GB ({tier_label})\n")
    lines.append(f"- Preferred Engine: {engine} | Task: {task}\n\n")
    lines.append("📋 हमारा 4-स्टेप एग्जीक्यूशन वर्कफ्लो:\n")
    lines.append("1. [Kaggle GPU & Environment Check]: Kaggle Dual T4 (30GB VRAM) और PyTorch CUDA एनवायरनमेंट एक्टिवेशन की जांच करना।\n")
    lines.append(f"2. [REAL Weight Download]: huggingface_hub (hf_hub_download / snapshot_download) से '{repo}' के असली वेट्स ('{file_name}') को Kaggle डिस्क (/kaggle/working/{target_dir}/) पर वास्तविक डाउनलोड करना। (ZERO DUMMY!)\n")
    lines.append(f"3. [Real GPU Inference Test]: मॉडल को T4 GPU पर लोड करके वास्तविक इनपुट प्रॉम्प्ट देकर असली आउटपुट जनरेट करना और VRAM मेमोरी व लेटेंसी मापना।\n")
    lines.append("4. [Google Drive Sync & UI Connect]: जनरेटेड आउटपुट और आर्टिफैक्ट्स को Google Drive पर अपलोड/वेरीफाई करना और Aarambh बैकएंड को लाइव मार्क करना।\n\n")
    lines.append(f"बताओ Step 1 (GPU Check) और Step 2 ('{file_name}' का Real Download) शुरू करने के लिए Kaggle पर क्या कोड रन करना है?\n")
    lines.append("```\n\n")
    lines.append("---\n\n")
    
    model_idx += 1

out_path = BASE_DIR / "MODEL_STARTER_PROMPTS.md"
out_path.write_text("".join(lines), encoding="utf-8")
print(f"Generated {out_path} with {model_idx - 1} starter prompts successfully!")
