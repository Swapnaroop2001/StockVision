<template>
  <div class="centered-container">
    <h2>Stock Search</h2>
  </div>
  <div class="centered-container search-container">
    <input v-model="ticker" class="search-input" placeholder="Enter stock ticker" />
    <button @click="searchStock" class="search-button">Search</button>
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

<style scoped>
.centered-container {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.search-container {
  position: relative;
  display: flex;
  align-items: center;
}

.search-input {
  width: 250px;
  padding: 12px 20px;
  border: 2px solid #ccc;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  outline: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.search-input:focus {
  border-color: #001015;
  box-shadow: 0 4px 12px rgba(39, 39, 39, 0.4);
  width: 300px;
}

.search-input::placeholder {
  color: #888;
  transition: color 0.3s ease;
}

.search-input:focus::placeholder {
  color: #555;
}

.search-button {
  padding: 12px 20px;
  margin-left: 10px;
  background: linear-gradient(45deg, #387d00, hsl(143, 100%, 31%));
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.search-button:hover {
  background: linear-gradient(45deg, #009c3c, #2c8300);
  transform: translateY(-2px);
}

.search-button:active {
  transform: translateY(0);
}
</style>
