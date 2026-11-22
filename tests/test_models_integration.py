"""
Unit & Integration Test Suite for Aarambh Model Pipelines & Manifests.
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "src"))

from models_manifest import MODELS_MANIFEST, get_models_by_studio


def test_manifest_integrity():
    assert len(MODELS_MANIFEST) > 0, "Manifest must not be empty"
    for key, model in MODELS_MANIFEST.items():
        assert "studio_id" in model, f"Model {key} missing studio_id"
        assert "category_id" in model, f"Model {key} missing category_id"
        assert "name" in model, f"Model {key} missing name"
        assert "preferred_engine" in model, f"Model {key} missing preferred_engine"
        assert model["preferred_engine"] in ["kaggle", "huggingface"], f"Invalid engine for {key}"
        assert model["vram_required_gb"] > 0, f"Invalid VRAM for {key}"


def test_studio_filtering():
    studio_1_models = get_models_by_studio(1)
    assert len(studio_1_models) >= 10, "Studio 1 should have generative visual models"
    studio_2_models = get_models_by_studio(2)
    assert len(studio_2_models) >= 4, "Studio 2 should have audio models"


if __name__ == "__main__":
    test_manifest_integrity()
    test_studio_filtering()
    print("✅ All Model Manifest Integration Tests Passed Successfully!")
