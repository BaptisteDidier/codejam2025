<script setup>
import { useRouter } from "vue-router";
defineProps({
  tabs: Array,
  activeTab: String
});
const router = useRouter();

const handleClick = () => {
  if (router.currentRoute.value.name === "Editor") {
    if (confirm("Are you sure you want to leave your work?")) {
      router.push({ name: "Home" });
    }
  } else {
    router.push({ name: "Home" });
  }
};

const updateTab = (tabName) => {
  // Emit event to parent for active tab change
  // Only if tabs are passed
  if (typeof __props.updateActiveTab === "function") {
    __props.updateActiveTab(tabName);
  }
};
</script>

<template>
  <nav class="navbar">
    <div class="header-content">
      <!-- Logo / Title -->
      <div class="logo-title" @click="handleClick">
        <h1 class="logo-text">CVSzy</h1>
      </div>

      <!-- Tabs (optional, only if provided) -->
      <div v-if="tabs && tabs.length" class="tabs">
        <button
          v-for="tab in tabs"
          :key="tab.name"
          :class="{ active: activeTab === tab.name }"
          @click="$emit('update:activeTab', tab.name)"
        >
          {{ tab.label.toUpperCase() }}
        </button>
      </div>
    </div>
  </nav>
</template>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  color: #e9e9e9;
}

.navbar {
  width: 100vw;
  background: #1f1f1f;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 50;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 22px;
  border-bottom: 1px solid #444;
}

.logo-title {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: bold;
  color: #ef4444;
}

.tabs {
  display: flex;
  align-items: center;
  gap: 20px;
}

.tabs button {
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  color: #ef4444;
  padding: 6px 12px;
  transition: all 0.2s;
}

.tabs button:hover {
  color: #dc2626;
  font-weight: bold;
  text-decoration: underline;
}

.tabs button.active {
  color: #dc2626;
  font-weight: bold;
  text-decoration: underline;
}
</style>
