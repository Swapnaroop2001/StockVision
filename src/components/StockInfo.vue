<template>
    <div v-if="stock" class="stock-info">
      <div class="info-container">
        <div class="stock-details">
          <h2 class="stock-title">{{ stock.name }}</h2>
          <div class="detail-item">
            <span class="label">Symbol:</span>
            <span class="value">{{ stock.symbol }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Percentage Change:</span>
            <span :class="percentageChangeClass">{{ percentageChange.toFixed(2) }}%</span>
          </div>
          <div class="detail-item">
            <span class="label">Sector:</span>
            <span class="value">{{ stock.sector }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Current Price:</span>
            <span class="value">${{ stock.currentPrice.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Open Price:</span>
            <span class="value">${{ stock.open.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Day High:</span>
            <span class="value">${{ stock.dayHigh.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Day Low:</span>
            <span class="value">${{ stock.dayLow.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Volume:</span>
            <span class="value">{{ stock.volume.toLocaleString() }}</span>
          </div>
          <div class="detail-item">
            <span class="label">Previous Close:</span>
            <span class="value">${{ stock.previousClose.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">52 Week High:</span>
            <span class="value">${{ stock.fiftyTwoWeekHigh.toFixed(2) }}</span>
          </div>
          <div class="detail-item">
            <span class="label">52 Week Low:</span>
            <span class="value">${{ stock.fiftyTwoWeekLow.toFixed(2) }}</span>
          </div>
        </div>
  
        <div class="stock-summary">
          <h2><b>Business Summary</b></h2>
          <p>{{ stock.longBusinessSummary }}</p>
        </div>
      </div>
    </div>
    <div v-else class="no-data">
      <p>No stock information available.</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { defineProps, computed } from 'vue';
  
  interface Stock {
    name: string;
    sector: string;
    symbol: string;
    longBusinessSummary: string;
    currentPrice: number;
    open: number;
    fiftyTwoWeekHigh: number;
    fiftyTwoWeekLow: number;
    previousClose: number;
    dayLow: number;
    dayHigh: number;
    volume: number;
  }
  
  const props = defineProps<{ stock: Stock | null }>();
  
  const percentageChange = computed(() => {
    if (props.stock) {
      return ((props.stock.currentPrice - props.stock.previousClose) / props.stock.previousClose) * 100;
    }
    return 0;
  });
  
  const percentageChangeClass = computed(() => {
    if (percentageChange.value > 0) return 'positive';
    if (percentageChange.value < 0) return 'negative';
    return 'neutral';
  });
  </script>
  
  <style scoped>
  .stock-info {
    max-width: 1200px;
    margin: auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .info-container {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .stock-details, .stock-summary {
    flex: 1;
    min-width: 300px;
  }
  
  .stock-title {
    font-size: 1.8rem;
    margin-bottom: 20px;
    color: #333;
  }
  
  .detail-item {
    display: flex;
    justify-content: space-between;
    padding: 12px;
    border-radius: 6px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
  }
  
  .label {
    font-weight: bold;
    color: #555;
  }
  
  .value {
    font-size: 1rem;
    color: #333;
  }
  
  .stock-summary {
    background-color: #fff;
    padding: 20px;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .stock-summary h3 {
    margin-top: 0;
  }
  
  .positive {
    color: #4caf50; 
  }
  
  .negative {
    color: #f44336;
  }
  
  .neutral {
    color: #000; 
  }
  
  .no-data {
    text-align: center;
    padding: 20px;
    color: #888;
  }
  </style>
  