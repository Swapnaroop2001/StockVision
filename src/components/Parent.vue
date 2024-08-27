<!-- src/Parent.vue -->

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import StockSearch from './StockSearch.vue';
</script>

<template>
  <div class="container">
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/home">Home</RouterLink>
          <RouterLink to="/about">News</RouterLink>
          <RouterLink to="/stockcharts">Stock Charts</RouterLink>
        </nav>
      </div>
    </header>
    <main class="content">
      <router-view />
    </main>
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
  width: 100%;
  text-align: center;
  display: flex;
  justify-content: center;
  margin-top: 10px;
  margin-bottom: 20px;
}

nav {
  width: 100%;
  font-size: 1rem;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  text-decoration: none;
  color: rgb(43, 216, 0);
}

nav a:first-of-type {
  border: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  font-size: 1.5rem;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

.content {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}
</style>
