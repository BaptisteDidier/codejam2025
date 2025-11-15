<template>
  <table border="1" cellspacing="0" cellpadding="5" style="margin-top: 2rem; width: 100%;">
    <thead>
      <tr>
        <th>Filename</th>
        <th>MIME Type</th>
        <th>Size (bytes)</th>
        <th>Uploaded At</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in history" :key="item.id">
        <td>{{ item.filename }}</td>
        <td>{{ item.mimetype }}</td>
        <td>{{ item.size }}</td>
        <td>{{ formatDate(item.uploaded_at) }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ['history'],
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString)
      return date.toLocaleString()
    }
  }
}
</script>
