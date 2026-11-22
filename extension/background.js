// Aarambh Extension Bridge Service Worker (Manifest V3)
console.log("[Aarambh Bridge] Service Worker registered.");

chrome.runtime.onInstalled.addListener((details) => {
    console.log("[Aarambh Bridge] Extension installed/updated:", details.reason);
    if (chrome.declarativeNetRequest && chrome.declarativeNetRequest.getDynamicRules) {
        chrome.declarativeNetRequest.getMatchedRules?.({}, (matched) => {
            console.log("[Aarambh Bridge] Active rules loaded.");
        });
    }
});
