import { defineStore } from "pinia";

export const useFileStore = defineStore("fileStore", {
  state: () => ({
    fileName: null,
    headers: [],
    rows: [],
  }),
  actions: {
    setFile(fileName) {
      this.fileName = fileName;
    },
    setCsvDataFromBackend(data) {
      // data = { headers: [...], rows: [[...],[...]] }
      this.headers = data.headers || [];
      this.rows = data.rows || [];
    },
    clear() {
      this.fileName = null;
      this.headers = [];
      this.rows = [];
    },
  },
});
