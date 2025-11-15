<template>
  <div class="insights-container">
    <h1>Data Insights</h1>
    <InsightsChart :insights="insights"/>
  </div>
</template>

<script>
import InsightsChart from '../components/InsightsChart.vue'
import { fetchHistory, fetchInsights } from '../services/api.js'

export default {
  components: { InsightsChart },
  data() {
    return {
      insights: []
    }
  },
  async mounted() {
    const history = await fetchHistory()
    if(history.length > 0){
      this.insights = await fetchInsights(history[0].id)
    }
  }
}
</script>
