<template>
  <table border="1" cellspacing="0" cellpadding="5" style="margin-top: 2rem; width: 100%;">
    <thead>
      <tr>
        <th>Filename</th>
        <th>Status</th>
        <th>Uploaded At</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in history" :key="item.id">
        <td>{{ item.filename }}</td>
        <td>{{ item.status }}</td>
        <td>{{ item.uploadTime }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ['history']
}
</script>
