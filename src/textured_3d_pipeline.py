"""
Hunyuan3D-2 & Kijai Wrapper Textured 3D Pipeline.
Enforces Rule 13: Shape-to-CPU offload, BPT texture baking, zero 404 git cloning.
"""
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional

logger = logging.getLogger("aarambh.textured_3d_pipeline")

WORKFLOW_PATH = Path(__file__).parent.parent / "workflows" / "3d_textured_hunyuan.json"


class Textured3DPipeline:
    """Executes full textured 3D mesh generation on remote T4 GPU."""

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
        image_name: str = "input_object.png",
        seed: int = 42,
        steps: int = 30,
        guidance_scale: float = 5.5,
        texture_size: int = 1024,
        on_progress=None,
        on_node_change=None,
    ) -> Dict[str, Any]:
        """Runs the textured 3D mesh workflow on remote GPU."""
        workflow = self.load_workflow_template()

        # Grounded node parameter injection
        workflow["1"]["inputs"]["image"] = image_name
        workflow["5"]["inputs"]["seed"] = seed
        workflow["5"]["inputs"]["steps"] = min(steps, 50)
        workflow["5"]["inputs"]["guidance_scale"] = guidance_scale
        workflow["8"]["inputs"]["texture_size"] = min(texture_size, 1024)

        logger.info(f"Dispatching Hunyuan3D-2 Textured 3D pipeline for '{image_name}' (Seed: {seed})")

        if self.ws_bridge:
            prompt_id, outputs = self.ws_bridge.stream_execution(
                prompt_workflow=workflow,
                on_progress=on_progress,
                on_node_change=on_node_change,
            )
            return {
                "status": "success",
                "pipeline": "hunyuan3d_textured_3d",
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
