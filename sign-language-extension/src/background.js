
// Router
chrome.runtime.onMessage.addListener((msg) => {
  if (!msg.action || !actions[msg.action]) {
    return;
  }
  actions[msg.action](msg);
});

const actions = {
  injectAudioScript,
  injectDescriptionScript,
};


// Functions

function injectAudioScript() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tab = tabs[0];
    if (!tab || !tab.id) return;

    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ["src/contentScriptAudio.js"]
    }).catch(err => {
      console.error("Audio script injection failed:", err);
    });
  });
}

function injectDescriptionScript() {
    console.log("TODO");
}
