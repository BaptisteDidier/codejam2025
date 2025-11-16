<script setup>
import { ref } from 'vue';
import Navbar from "@/components/Navbar.vue";
import DownloadButton from "@/components/DownloadButton.vue";
import { useRouter } from 'vue-router';

const router = useRouter();
const fileInput = ref(null);

const triggerFile = () => {
  fileInput.value.click();
};

const handleFile = (event) => {
  const file = event.target.files[0];
  if (file) {
    router.push({ name: "Editor", query: { file: file.name } });
  }
};

const downloadDemo = () => {
  alert("Download triggered!");
};
</script>

<template>
  <div class="page">
    <!-- Header -->
    <header class="header">
      <Navbar />
    </header>

    <!-- Main content wrapper -->
    <div class="content-wrapper">
      <main class="main-content">
        <h1 class="title">Welcome</h1>

        <button class="button-primary" @click="triggerFile">
          Choose File
        </button>

        <DownloadButton @download="downloadDemo" />

        <input
          ref="fileInput"
          type="file"
          class="hidden"
          accept=".csv"
          @change="handleFile"
        />
      </main>
    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
  padding: 0;
  color: #e9e9e9;
}

.page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
}

.header {
  display: flex;
  justify-content: flex-start; /* left-aligned logo */
  align-items: center;
  padding: 10px 20px;
  background: #222;
  width: 100vw;
}

.content-wrapper {
  flex: 1;
  display: flex;
  width: 100%;
}

.main-content {
  flex: 1;
  padding: 22px; /* spacing same as example */
  text-align: center;
  background: #19171a;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem; /* spacing between buttons and title */
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
}

.button-primary {
  padding: 0.75rem 1.5rem;
  background-color: #ef4444;
  color: white;
  border-radius: 0.75rem;
  border: none;
  cursor: pointer;
}

.button-primary:hover {
  background-color: #dc2626;
}
</style>
