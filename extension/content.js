// Aarambh Extension Bridge Content Script
(function() {
    console.log("[Aarambh Bridge] Content script injected into Aarambh Suite.");

    function notifyAarambh() {
        try {
            document.documentElement.setAttribute('data-aarambh-bridge-active', 'true');
            window.postMessage({
                source: "aarambh-extension",
                type: "AARAMBH_BRIDGE_READY",
                version: "1.0.0",
                features: ["colab_unframe", "civitai_unframe", "huggingface_unframe"]
            }, "*");
        } catch (e) {
            console.error("[Aarambh Bridge] Notify failed:", e);
        }
    }

    notifyAarambh();
    document.addEventListener("DOMContentLoaded", notifyAarambh);
    window.addEventListener("load", notifyAarambh);

    // Listen for frontend health-checks
    window.addEventListener("message", (event) => {
        if (event.data && event.data.type === "PING_AARAMBH_BRIDGE") {
            window.postMessage({
                source: "aarambh-extension",
                type: "PONG_AARAMBH_BRIDGE",
                status: "ACTIVE",
                version: "1.0.0"
            }, "*");
        }
    });
})();
