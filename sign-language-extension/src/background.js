chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg.action === "injectAudioScript") {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (!tabs[0].id) return;
  
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          files: ["src/contentScriptAudio.js"]
        }).catch(err => {
          console.error("Injection failed:", err);
        });
      });
    }
  });
  
  