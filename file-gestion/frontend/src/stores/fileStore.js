import { defineStore } from "pinia";

export const useFileStore = defineStore("fileStore", {
  state: () => ({
    file: null,
    csvData: null,
    headers: []
  }),

  actions: {
    setFile(file) {
      this.file = file;
    },

    setCsvData(data) {
      this.csvData = data;
    },

    setHeaders(headers) {
      this.headers = headers;
    }
  }
});
