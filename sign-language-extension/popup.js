const optionButtons = document.querySelectorAll('.option-btn');
const msg = document.getElementById('msg');

let selectedOptions = new Set();

// Load saved options from chrome.storage
chrome.storage.local.get(['selectedOptions'], (result) => {
  const saved = result.selectedOptions || [];
  selectedOptions = new Set(saved);

  optionButtons.forEach(btn => {
    if (selectedOptions.has(btn.dataset.value)) {
      btn.classList.add('selected');
    }
  });
});

// Handle clicks
optionButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.value;

    // Toggle selection
    if (selectedOptions.has(value)) {
        selectedOptions.delete(value);
        btn.classList.remove('selected');
    } else {
        selectedOptions.add(value);
        btn.classList.add('selected');

        // ✅ Instead of executing the script directly, send a message to background
      if (value === "2") { // Option 2 = Audio Subtitles
        chrome.runtime.sendMessage({ action: "injectAudioScript" }, (response) => {
          if (chrome.runtime.lastError) {
            console.error("Message failed:", chrome.runtime.lastError.message);
          } else {
            console.log("Message sent to background:", response);
          }
        });
      }
    }

    // Save immediately to chrome.storage
    chrome.storage.local.set({ selectedOptions: Array.from(selectedOptions) });

    // Optionally, notify background script
    //chrome.runtime.sendMessage({ action: 'setOptions', options: Array.from(selectedOptions) });
  });
});
