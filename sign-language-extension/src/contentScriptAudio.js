console.log("Audio subtitles content script loaded");

// 1️⃣ Inject floating subtitle box if not exists
let subtitleBox = document.getElementById("subtitle-box");
if (!subtitleBox) {
  subtitleBox = document.createElement("div");
  Object.assign(subtitleBox.style, {
    position: "fixed",
    bottom: "80px",
    left: "50%",
    transform: "translateX(-50%)",
    padding: "15px 20px",
    background: "rgba(0,0,0,0.7)",
    color: "white",
    borderRadius: "8px",
    fontSize: "18px",
    zIndex: 99999,
    maxWidth: "80%",
    textAlign: "center"
  });
  subtitleBox.id = "subtitle-box";
  subtitleBox.textContent = "Waiting for audio...";
  document.body.appendChild(subtitleBox);
}

// 2️⃣ Start audio transcription only once
if (!window.audioRecognition) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert("Your browser does not support SpeechRecognition API");
  } else {
    const recognition = new SpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "en-US";

    recognition.onresult = (event) => {
      let transcript = "";
      for (let i = event.resultIndex; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
      }
      subtitleBox.textContent = transcript;
    };

    recognition.onerror = (event) => console.error("Speech recognition error:", event.error);

    recognition.onend = () => {
      recognition.start(); // auto-restart
    };

    recognition.start();
    window.audioRecognition = recognition; // global reference to avoid duplicates
    console.log("Speech recognition started");
  }
}

