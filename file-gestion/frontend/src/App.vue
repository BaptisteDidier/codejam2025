<template>
  <div id="app">
    <!-- Navigation bar -->
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <router-link to="/history">History</router-link>
      <router-link to="/insights">Insights</router-link>
    </nav>

    <!-- Pages will render here -->
    <router-view />
  </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
.navbar {
  display: flex;
  justify-content: center;
  gap: 2rem;
  background-color: #3498db;
  padding: 1rem 0;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
}

.navbar a.router-link-active {
  text-decoration: underline;
}

/* Optional: keep general page styles */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  max-width: 900px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  border-radius: 12px;
}
</style>
