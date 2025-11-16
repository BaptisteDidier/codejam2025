<script setup>
import Navbar from "@/components/Navbar.vue";
import { useFileStore } from "@/stores/fileStore";

const fileStore = useFileStore();
</script>

<template>
  <div class="page">
    <header class="header">
      <Navbar />
    </header>

    <div class="final-preview">
      <table>
        <thead>
          <tr>
            <th v-for="(h, i) in fileStore.headers" :key="i">{{ h }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, r) in fileStore.rows" :key="r">
            <td v-for="(cell, c) in row" :key="c">{{ cell }}</td>
          </tr>
        </tbody>
      </table>
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
  z-index: 2;
}

.final-preview {
  flex: 1;
  overflow: auto;
  width: 100%;
  height: calc(100vh - 60px); /* full space under header */
  background-color: white; /* always white */
  color: black; /* text readable */
  padding: 1rem;
}

.final-preview table {
  border-collapse: collapse;
  width: 100%;
  height: 100%;
}

.final-preview th,
.final-preview td {
  border: 1px solid #444;
  padding: 4px 8px;
  text-align: left;
}

.final-preview thead th {
  position: sticky;
  top: 0;
  background-color: #f1f1f1;
  z-index: 1;
}
</style>
