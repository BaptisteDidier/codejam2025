const msg = document.getElementById('msg');
let selectedOptions = new Set();


chrome.storage.local.get(['selectedOptions'], (result) => {
  const saved = result.selectedOptions || [];
  selectedOptions = new Set(saved);


  saved.forEach(value => {
    const btn = document.querySelector(`.option-btn[data-value="${value}"]`);
    if (btn) {
        btn.classList.add("selected");
    } 
  });
});

document.addEventListener("click", (e) => {
  const btn = e.target.closest(".option-btn");
  if (!btn) {
    return;
  }

  const value = btn.dataset.value;
  toggleOption(value, btn);

  chrome.storage.local.set({ selectedOptions: [...selectedOptions] });
});


// Functions

function toggleOption(value, btn) {
  const isSelected = selectedOptions.has(value);

  if (isSelected) {
    selectedOptions.delete(value);
    btn.classList.remove("selected");
  
} else {
    selectedOptions.add(value);
    btn.classList.add("selected");
    handleAction(value);
  }
}

function handleAction(value) {
  const map = {
    "1": "injectDescriptionScript",
    "2": "injectAudioScript"
  };

  const action = map[value];
  if (action) {
    chrome.runtime.sendMessage({ action });
  }
}

