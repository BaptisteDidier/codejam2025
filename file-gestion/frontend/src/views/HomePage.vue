<template>
  <div class="flex flex-col items-center justify-center h-screen bg-gray-900 text-white gap-6 text-center">
    <h1 class="text-4xl font-bold text-center">Welcome</h1>

    <button
      class="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl shadow"
      @click="triggerFile"
    >
      Choose a File
    </button>

    <DownloadButton @download="downloadDemo" />

    <input
      ref="fileInput"
      type="file"
      class="hidden"
      accept=".csv"
      @change="handleFile"
    />
  </div>
</template>

<script>
import DownloadButton from "@/components/DownloadButton.vue";

export default {
  components: { DownloadButton },

  methods: {
    triggerFile() {
      this.$refs.fileInput.click();
    },

    handleFile(event) {
      const file = event.target.files[0];
      if (file) {
        this.$router.push({
          name: "Editor",
          query: { file: file.name }
        });
      }
    },

    downloadDemo() {
      alert("Download triggered!");
    }
  }
};
</script>
