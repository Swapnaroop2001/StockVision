<!-- src/components/AppLayout.vue -->
<template>
    <div class="container">
      <header>
        <div class="wrapper">
          <h1>StockVision</h1>
          <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
          </nav>
        </div>
        <StockSearch @search="updateTicker" />
      </header>
  
      <div class="content">
        <RouterView :ticker="ticker" />
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import { RouterLink, RouterView } from 'vue-router'
  import StockSearch from './StockSearch.vue'
  
  const ticker = ref<string>('')
  
  const updateTicker = (searchTicker: string) => {
    ticker.value = searchTicker
  }
  </script>
  
  <style scoped>
  /* Your existing styles */
  </style>
  