const optionButtons = document.querySelectorAll('.option-btn');
const applyBtn = document.getElementById('apply-btn');
const msg = document.getElementById('msg');

const selectedOptions = new Set();

optionButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.value;

    if (selectedOptions.has(value)) {
      selectedOptions.delete(value);
      btn.classList.remove('selected');
    } else {
      if (selectedOptions.size < 2) {
        selectedOptions.add(value);
        btn.classList.add('selected');
      } else {
        msg.textContent = "You can select at most 2 options";
        setTimeout(() => msg.textContent = "", 2000);
      }
    }
  });
});

applyBtn.addEventListener('click', () => {
  const optionsArray = Array.from(selectedOptions);
  chrome.runtime.sendMessage({ action: 'setOptions', options: optionsArray });
  msg.textContent = optionsArray.length
    ? "Options applied: " + optionsArray.join(", ")
    : "No options selected";
});
