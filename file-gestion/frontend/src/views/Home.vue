<template>
  <div class="home-container">
    <h1>Cloud File Processing</h1>
    <div class="upload-box">
      <FileUpload @file-uploaded="handleFileUploaded"/>
    </div>
    <InsightsChart :insights="insights"/>
  </div>
</template>

<script>
import FileUpload from '../components/FileUpload.vue'
import InsightsChart from '../components/InsightsChart.vue'
import { uploadFile } from '../services/api.js'

export default {
  components: { FileUpload, InsightsChart },
  data() {
    return {
      insights: []
    }
  },
  methods: {
    async handleFileUploaded(file) {
        const response = await uploadFile(file)
        this.insights = response.insights
    }
  }
}
</script>
