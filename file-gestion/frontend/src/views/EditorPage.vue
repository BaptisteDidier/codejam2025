<template>
  <div class="relative w-full h-full">

    <!-- Tabs -->
    <div class="absolute top-0 w-full flex justify-center mt-4 gap-4">
      <button
        v-for="(tab, index) in tabs"
        :key="index"
        @click="currentTab = index"
        class="px-4 py-2 rounded-xl"
        :class="currentTab === index ? 'bg-blue-600' : 'bg-gray-700 hover:bg-gray-600'"
      >
        {{ tab }}
      </button>
    </div>

    <!-- Main 6 buttons on top half -->
    <div class="w-full pt-20 flex flex-col">
      <div class="grid grid-cols-3 gap-4 p-4 h-1/2">
        <button
          v-for="i in 6"
          :key="i"
          class="bg-gray-700 hover:bg-gray-600 rounded-xl p-4"
          @click="performAction(i)"
        >
          Action {{ i }}
        </button>
      </div>

      <!-- Bottom: "top of page preview" placeholder -->
      <div class="h-1/2 bg-gray-900 p-6 overflow-auto">
        <p class="opacity-50">Preview of the top of the page (placeholder)</p>
      </div>
    </div>

    <!-- Download Button -->
    <button
      @click="goFinal"
      class="absolute bottom-8 right-8 bg-green-600 hover:bg-green-700 px-6 py-3 rounded-xl shadow"
    >
      Download File
    </button>

  </div>
</template>

<script>
export default {
  data() {
    return {
      tabs: ["Tab 1", "Tab 2", "Tab 3"],
      currentTab: 0
    };
  },
  methods: {
    performAction(i) {
      console.log("Performed action", i);
    },
    goFinal() {
      this.$router.push({ name: "Final" });
    }
  }
};
</script>
