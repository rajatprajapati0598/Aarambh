"""
LTX-Video 2.5 Pipeline for Colab T4 GPU (Free-Tier Compliant).
Enforces Rule 13: 480p/768p bounds, KSampler euler/normal, zero OOM.
"""
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger("aarambh.video_pipeline")

WORKFLOW_PATH = Path(__file__).parent.parent / "workflows" / "video_ltx_t4.json"


class VideoPipeline:
    """Executes LTX-Video 2.5 text-to-video / img-to-video generation on remote T4 GPU."""

    def __init__(self, bridge=None, ws_bridge=None):
        self.bridge = bridge
        self.ws_bridge = ws_bridge

    def load_workflow_template(self) -> Dict[str, Any]:
        """Loads and grounds workflow from disk to prevent Node ID hallucination."""
        if not WORKFLOW_PATH.exists():
            raise FileNotFoundError(f"Workflow template missing on disk: {WORKFLOW_PATH}")
        with open(WORKFLOW_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def run(
        self,
        prompt: str,
        negative_prompt: str = "blurry, low quality, deformed, jitter, watermark",
        seed: int = 42,
        steps: int = 20,
        length: int = 25,
        on_progress=None,
        on_node_change=None,
    ) -> Dict[str, Any]:
        """Runs the video generation workflow on remote GPU."""
        workflow = self.load_workflow_template()

        # Grounded node parameter injection
        workflow["2"]["inputs"]["text"] = prompt
        workflow["3"]["inputs"]["text"] = negative_prompt
        workflow["4"]["inputs"]["length"] = min(length, 49)  # Bound to T4 limits
        workflow["5"]["inputs"]["seed"] = seed
        workflow["5"]["inputs"]["steps"] = min(steps, 30)

        logger.info(f"Dispatching LTX-Video pipeline: '{prompt[:40]}...' (Seed: {seed}, Steps: {steps})")

        if self.ws_bridge:
            prompt_id, outputs = self.ws_bridge.stream_execution(
                prompt_workflow=workflow,
                on_progress=on_progress,
                on_node_change=on_node_change,
            )
            return {
                "status": "success",
                "pipeline": "ltx_video_2.5",
                "prompt_id": prompt_id,
                "outputs": outputs,
            }
        elif self.bridge:
            return self.bridge.dispatch_workflow(workflow)
        else:
            return {
                "status": "prepared",
                "workflow": workflow,
            }
