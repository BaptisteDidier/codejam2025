<template>
  <div style="margin-bottom: 2rem;">
    <input type="file" @change="onFileSelected"/>
    <button @click="uploadFile">Upload</button>
    <p v-if="uploadMessage">{{ uploadMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return { 
      selectedFile: null,
      uploadMessage: ''
    }
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
      this.uploadMessage = '';
    },
    async uploadFile() {
      if (!this.selectedFile) {
        return alert("Select a file first!");
      }

      try {
        const formData = new FormData();
        formData.append('file', this.selectedFile);

        const response = await fetch('http://localhost:5173/upload', { // default port
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || 'Upload failed');
        }

        const data = await response.json();
        this.uploadMessage = `File uploaded! ID: ${data.id}`;
        this.$emit('file-uploaded', this.selectedFile);
        this.selectedFile = null;
      } catch (err) {
        this.uploadMessage = `Error: ${err.message}`;
      }
    }
  }
}
</script>
