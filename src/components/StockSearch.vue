<template>
    <div>
      <input v-model="ticker" placeholder="Enter stock ticker" />
      <button @click="searchStock">Search</button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineEmits } from 'vue';
  
  const ticker = ref('');
  const emit = defineEmits<{ (event: 'search', ticker: string): void }>();
  
  const searchStock = () => {
    emit('search', ticker.value);
  };
  </script>
  
 