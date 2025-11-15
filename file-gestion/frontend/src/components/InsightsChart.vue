<template>
  <canvas id="chart" width="400" height="200"></canvas>
</template>

<script>
import { onMounted, watch } from 'vue'
import Chart from 'chart.js/auto'

export default {
  props: ['insights'],
  setup(props) {
    let chartInstance;

    onMounted(() => {
      const ctx = document.getElementById('chart').getContext('2d');
      chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: props.insights.map(i => i.label),
          datasets: [{
            label: 'Metrics',
            data: props.insights.map(i => i.value),
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    });

    watch(() => props.insights, (newVal) => {
      if(chartInstance) {
        chartInstance.data.labels = newVal.map(i => i.label);
        chartInstance.data.datasets[0].data = newVal.map(i => i.value);
        chartInstance.update();
      }
    });

    return {};
  }
}
</script>

