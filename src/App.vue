<!-- src/App.vue -->
<script setup lang="ts">
import Parent from './components/Parent.vue';
</script>

<template>
  <div class="container">
    <header>
      <div class="wrapper">
        <h1>StockVision</h1>
        <Parent/>
      </div>
    </header>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  width: 100%;
  text-align: center;
  display: flex;
  justify-content: center;
  width: 100%;
  top: 0;
  margin-top: 10px;
  margin-bottom: 20px;
}

h1 {
  font-size: 3rem;
  font-weight: 600;
}

nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  font-size: 1.5rem;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-self: flex-start;
}
</style>
