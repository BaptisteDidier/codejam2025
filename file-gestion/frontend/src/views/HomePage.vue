<script setup>
import Navbar from "@/components/Navbar.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useFileStore } from "@/stores/fileStore";

const router = useRouter();
const fileStore = useFileStore();

const selectedFileName = ref("Not selected file");
const fileInput = ref(null);

const triggerFile = () => {
  fileInput.value.click();
};

const handleFile = (event) => {
  const file = event.target.files[0];
  if (!file) return;

  selectedFileName.value = file.name;

  // Read CSV client-side
  const reader = new FileReader();
  reader.onload = (e) => {
    const text = e.target.result;
    const lines = text.split("\n").map(line => line.split(","));
    fileStore.setFile(file.name);
    fileStore.setCsvDataFromBackend({
      headers: lines[0],
      rows: lines.slice(1),
    });
    router.push({ name: "Editor" });
  };
  reader.readAsText(file);
};
</script>

<template>
  <div class="page">
    <header class="header">
      <Navbar />
    </header>

    <div class="content-wrapper">
      <main class="main-content">
        <h1 class="title">Welcome</h1>

        <!-- Upload Card -->
        <div class="upload-card">
          <div class="upload-header" @click="triggerFile">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M7 10V9C7 6.23858 9.23858 4 12 4C14.7614 4 17 6.23858 17 9V10C19.2091 10 21 11.7909 21 14C21 15.4806 20.1956 16.8084 19 17.5M7 10C4.79086 10 3 11.7909 3 14C3 15.4806 3.8044 16.8084 5 17.5M7 10C7.43285 10 7.84965 10.0688 8.24006 10.1959M12 12V21M12 12L15 15M12 12L9 15" stroke="#ef4444" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <p>Browse File to upload!</p>
          </div>

          <label for="file" class="upload-footer">
            <p>{{ selectedFileName }}</p>
          </label>

          <input id="file" type="file" ref="fileInput" accept=".csv" @change="handleFile" />
        </div>

      </main>
    </div>
  </div>
</template>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
}

.header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 20px;
  background: #222;
  width: 100vw;
}

.content-wrapper {
  flex: 1;
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  background: #19171a;
  width: 100%;
  height: 100%;
}

.title {
  font-size: 2.5rem;
  color: #e9e9e9;
  font-weight: bold;
}

/* Upload Card Styling */
.upload-card {
  width: 300px;
  height: 300px;
  border-radius: 10px;
  background-color: #1f1f1f; /* dark card */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  gap: 10px;
  border: 2px dashed #ef4444; /* red dashed border */
}

.upload-header {
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.upload-header svg {
  height: 100px;
}

.upload-header p {
  margin-top: 10px;
  color: #e9e9e9;
  text-align: center;
}

.upload-footer {
  width: 100%;
  height: 40px;
  background-color: #2a2a2a;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  cursor: pointer;
  color: #e9e9e9;
  font-weight: bold;
}

#file {
  display: none;
}
</style>
