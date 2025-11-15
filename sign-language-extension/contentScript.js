console.log("Content script loaded"); // check if injected

function injectButton() {
  if (document.getElementById("camera-btn")) return;

  const btn = document.createElement("button");
  btn.id = "camera-btn";
  btn.textContent = "Checking camera...";
  Object.assign(btn.style, {
    position: "fixed",
    bottom: "20px",
    right: "20px",
    zIndex: 9999,
    padding: "12px",
    fontSize: "14px",
    backgroundColor: "red",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "not-allowed"
  });

  document.body.appendChild(btn);

  // Periodically check if camera can be accessed
  setInterval(async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      stream.getTracks().forEach(track => track.stop());
      btn.disabled = false;
      btn.style.cursor = "pointer";
      btn.textContent = "Camera active!";
    } catch (err) {
      btn.disabled = true;
      btn.style.cursor = "not-allowed";
      btn.textContent = "Camera not in use";
    }
  }, 2000);

  btn.addEventListener("click", () => {
    if (!btn.disabled) alert("Button clicked — camera active!");
  });
}

// Inject when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", injectButton);
} else {
  injectButton();
}
