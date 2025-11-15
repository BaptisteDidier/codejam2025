<template>
  <div class="history-container">
    <h1>Upload History</h1>
    <UploadHistory :history="history"/>
  </div>
</template>

<script>
import UploadHistory from '../components/UploadHistory.vue'
import { fetchHistory } from '../services/api.js'

export default {
  components: { UploadHistory },
  data() {
    return {
      history: []
    }
  },
  async mounted() {
    this.history = await fetchHistory()
  }
}
</script>
