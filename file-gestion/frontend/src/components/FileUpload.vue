<template>
  <div style="margin-bottom: 2rem;">
    <input type="file" @change="onFileSelected"/>
    <button @click="uploadFile">Upload</button>
  </div>
</template>

<script>
export default {
  data() {
    return { selectedFile: null }
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      if (!this.selectedFile) return alert("Select a file first!");
      this.$emit('file-uploaded', this.selectedFile);
      this.selectedFile = null;
    }
  }
}
</script>

