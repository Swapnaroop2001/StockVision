
import type DividendchartVue from './Dividendchart.vue';
<template>
  <div>
  <StockSearch @search="fetchStockInfo" />
  </div>
  <StockInfo :stock="stockData" />
  <DividendchartVue/>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import StockSearch from '../components/StockSearch.vue'
import StockInfo from '../components/StockInfo.vue'
import axios from 'axios'

const stockData = ref<any>(null)

const fetchStockInfo = async (ticker: string) => {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/stock/${ticker}`)
    stockData.value = response.data
  } catch (error) {
    console.error('Error fetching stock data:', error)
    stockData.value = null
  }
}
</script>
