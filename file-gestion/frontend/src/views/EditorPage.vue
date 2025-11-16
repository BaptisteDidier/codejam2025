<template>
  <div class="page">
    <header class="header">
      <Navbar />
    </header>
    <div class="editor-main">
      <div class="editor-left">

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

        <div class="editor-buttons">
          <button v-for="i in 6" :key="i" class="button-primary" @click="performAction(i)">
            Action {{ i }}
          </button>
        </div>

        <button class="button-apply" @click="applyChanges">Apply</button>
      </div>

      <div class="editor-preview" ref="previewContainer" @wheel.prevent="handleWheel">
        <canvas ref="canvasRef"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import { useFileStore } from "@/stores/fileStore";
import { ref, onMounted, nextTick } from "vue";
import { useRouter } from "vue-router";

const fileStore = useFileStore();
const router = useRouter();

const tabs = ref(["Tab 1", "Tab 2", "Tab 3"]);
const currentTab = ref(0);
const zoom = ref(1);

const canvasRef = ref(null);
const previewContainerRef = ref(null);

const drawCanvas = () => {
  const canvas = canvasRef.value;
  const container = previewContainerRef.value;
  if (!canvas || !container) return;

  const ctx = canvas.getContext("2d");
  const headers = fileStore.headers || [];
  const rows = fileStore.rows || [];

  const cellWidth = 120 * zoom.value;
  const cellHeight = 24 * zoom.value;

  canvas.width = Math.max(container.clientWidth, headers.length * cellWidth);
  canvas.height = Math.max(container.clientHeight, (rows.length + 1) * cellHeight);

  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.font = `${14 * zoom.value}px Arial`;
  ctx.fillStyle = "black";
  ctx.textBaseline = "middle";

  headers.forEach((h, i) => {
    ctx.fillText(h, i * cellWidth + 5, cellHeight / 2);
    ctx.strokeRect(i * cellWidth, 0, cellWidth, cellHeight);
  });

  rows.forEach((row, r) => {
    row.forEach((cell, c) => {
      ctx.fillText(cell, c * cellWidth + 5, (r + 1) * cellHeight + cellHeight / 2);
      ctx.strokeRect(c * cellWidth, (r + 1) * cellHeight, cellWidth, cellHeight);
    });
  });
};

const handleWheel = (e) => {
  if (e.ctrlKey) {
    e.preventDefault();
    const delta = e.deltaY > 0 ? -0.1 : 0.1;
    zoom.value = Math.min(2, Math.max(0.5, zoom.value + delta));
    drawCanvas();
  }
};

const performAction = (i) => alert(`Action ${i + 1}`);

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

onMounted(() => {
  nextTick(() => drawCanvas());
  const container = previewContainerRef.value;
  new ResizeObserver(drawCanvas).observe(container);
});
</script>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
}

.header {
  height: 80px;
  width: 100vw;
  z-index: 10;
}

.editor-main {
  flex: 1;
  display: flex;
  background: #19171a;
}

.editor-left {
  width: 250px;
  background-color: #1f1f1f;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  position: sticky;
  top: 80px;
  height: calc(100vh - 80px);
  justify-content: space-between;
}

.editor-title-container {
  min-height: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1rem;
}

.editor-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #ef4444;
  text-align: center;
}

.editor-tabs-horizontal {
  display: flex;
  gap: 10px;
  margin-bottom: 1rem;
  justify-content: center;
}

.editor-tab {
  color: #ef4444;
  cursor: pointer;
  padding: 6px 12px;
  transition: all 0.2s;
}

.editor-tab:hover,
.editor-tab.active {
  color: #dc2626;
  font-weight: bold;
  text-decoration: underline;
}

.editor-buttons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  width: 100%;
}

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

.button-apply {
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

.editor-preview {
  flex: 1;
  overflow: auto;
  background-color: white;
  padding: 0;
  position: relative;
}

.editor-preview canvas {
  display: block;
  width: auto;
  height: auto;
}
</style>
