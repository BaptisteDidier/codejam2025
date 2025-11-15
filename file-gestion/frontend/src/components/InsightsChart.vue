<template>
  <div>
    <h2>File Insights</h2>
    <p>Number of rows: {{ insights["Number of rows"] }}</p>
    <p>Rows: {{ insights["Rows"] }}</p>
    <p>Number of columns: {{ insights["Number of columns"] }}</p>
    <p>Columns: {{ insights["Columns"] }}</p>
    <p>Number of missing values: {{ insights["Number of missing values"] }}</p>
    <p>Missing values locations: {{ insights["Missing values locations"] }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  props: ["fileId"],
  setup(props) {
    const insights = ref({});

    onMounted(async () => {
      try {
        const res = await axios.get(`/api/insights/${props.fileId}`);
        insights.value = res.data;
      } catch (err) {
        console.error("Error fetching insights:", err);
      }
    });

    return { insights };
  },
};
</script>
