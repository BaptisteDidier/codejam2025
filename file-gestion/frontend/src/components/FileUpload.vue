<template>
  <div>
    <input type="file" @change="onFileSelected" />
    <button @click="uploadFile">Upload</button>
    <p>{{ uploadMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      uploadMessage: ""
    };
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },

    async uploadFile() {
      if (!this.selectedFile) return alert("Select a file first!");

      const formData = new FormData();
      formData.append("file", this.selectedFile);

      // <<< THIS IS THE SECOND SNIPPET START >>>
      try {
        const response = await fetch("http://localhost:8000/upload", {
          method: "POST",
          body: formData
        });

        const text = await response.text();
        console.log("Raw response text:", text);

        const data = JSON.parse(text); // <-- will throw if not valid JSON
        console.log("Parsed JSON:", data);

        this.uploadMessage = `File uploaded! ID: ${data.id}`;
      } catch (err) {
        console.error("Failed to upload or parse JSON:", err);
        this.uploadMessage = `Upload error: ${err.message}`;
      }
      this.selectedFile = null; // reset after upload
    }
  }
};
</script>
