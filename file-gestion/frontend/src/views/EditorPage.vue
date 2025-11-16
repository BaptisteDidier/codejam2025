<script setup>
import Navbar from "@/components/Navbar.vue";
import { useFileStore } from "@/stores/fileStore";
import { ref } from "vue";
import { useRouter } from "vue-router";

const fileStore = useFileStore();
const router = useRouter();
const tabs = ref(["Tab 1", "Tab 2", "Tab 3"]);
const currentTab = ref(0);
const zoom = ref(1);

// Apply button: download CSV and navigate to Final page
const applyChanges = () => {
  const csvText = [fileStore.headers.join(","), ...fileStore.rows.map(r => r.join(","))].join("\n");
  const blob = new Blob([csvText], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = fileStore.fileName || "file.csv";
  a.click();
  URL.revokeObjectURL(url);

  router.push({ name: "Final" });
};

// Trackpad zoom
const handleWheel = (e) => {
  if (e.ctrlKey) {
    e.preventDefault();
    zoom.value = Math.min(2, Math.max(0.5, zoom.value + (e.deltaY > 0 ? -0.1 : 0.1)));
  }
};

// Example action buttons
const performAction = (i) => alert(`Action ${i + 1}`);
</script>

<template>
  <div class="page">
    <header class="header">
      <Navbar />
    </header>

    <div class="content-wrapper">
      <main class="main-content editor-main">
        <!-- Left panel -->
        <div class="editor-left">
          <!-- Horizontal Tabs -->
          <div class="editor-tabs-horizontal">
            <div
              v-for="(tab, index) in tabs"
              :key="index"
              :class="['editor-tab', { active: currentTab === index }]"
              @click="currentTab = index"
            >
              {{ tab }}
            </div>
          </div>

          <!-- 6 action buttons -->
          <div class="grid grid-cols-3 gap-4 mt-4">
            <button
              v-for="i in 6"
              :key="i"
              class="button-primary"
              @click="performAction(i)"
            >
              Action {{ i }}
            </button>
          </div>

          <!-- Apply button -->
          <button class="button-apply mt-auto" @click="applyChanges">
            Apply
          </button>
        </div>

        <!-- Right panel CSV preview -->
        <div
          class="editor-preview"
          ref="previewContainer"
          @wheel.prevent="handleWheel"
        >
          <table :style="{ transform: `scale(${zoom})`, transformOrigin: 'top left' }">
            <thead>
              <tr>
                <th v-for="(h, i) in fileStore.headers" :key="i">
                  {{ h }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, r) in fileStore.rows" :key="r">
                <td v-for="(cell, c) in row" :key="c">{{ cell }}</td>
              </tr>
            </tbody>
          </table>
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
  padding: 10px 22px;
  background: #222;
  width: 100vw;
}

.content-wrapper {
  flex: 1;
  display: flex;
  width: 100%;
}

.main-content.editor-main {
  flex: 1;
  display: flex;
  padding: 22px;
  gap: 1.5rem;
  background: #19171a;
}

/* Left panel */
.editor-left {
  width: 250px;
  background-color: #1f1f1f;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
}

/* Horizontal Tabs */
.editor-tabs-horizontal {
  display: flex;
  gap: 10px;
  margin-bottom: 1rem;
}

.editor-tab {
  color: #ef4444;
  cursor: pointer;
  padding: 6px 12px;
  transition: all 0.2s;
}
.editor-tab:hover {
  color: #dc2626;
  font-weight: bold;
  text-decoration: underline;
}
.editor-tab.active {
  color: #dc2626;
  font-weight: bold;
  text-decoration: underline;
}

/* Buttons */
.button-primary {
  padding: 0.5rem 1rem;
  background-color: #ef4444;
  color: white;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
}
.button-primary:hover {
  background-color: #dc2626;
}

/* Apply button */
.button-apply {
  margin-top: auto;
  padding: 0.75rem 1rem;
  background-color: #dc2626;
  color: white;
  border-radius: 0.5rem;
  border: none;
  cursor: pointer;
}
.button-apply:hover {
  background-color: #b91c1c;
}

/* Right panel CSV preview */
.editor-preview {
  flex: 1;
  overflow: auto;
  background-color: white; /* always white */
  color: black; /* text readable */
  padding: 1rem;
}

.editor-preview table {
  border-collapse: collapse;
  width: max-content;
}

.editor-preview th,
.editor-preview td {
  border: 1px solid #444;
  padding: 4px 8px;
  text-align: left;
}

.editor-preview thead th {
  position: sticky;
  top: 0;
  background-color: #f1f1f1;
  z-index: 1;
}
</style>
