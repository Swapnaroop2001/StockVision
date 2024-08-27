<template>
    <div>
      <!-- Display chart and StockSearch only if there's data -->
      <StockSearch @search="fetchStockInfo" />
      <div v-if="chartSeries.length > 0">
        <h2 class="chart-title">Stock Prices Candlestick Chart</h2>
        <apexchart type="candlestick" :options="chartOptions" :series="chartSeries" class="chart" height="400" width="600"></apexchart>
      </div>
      
      <!-- Display message if there's no data -->
      <div v-else>
        <p>"Enter the stock ticker to view Charts."</p>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import axios from 'axios'
  import StockSearch from './StockSearch.vue'
  
  // Data to be displayed in the candlestick chart
  const chartSeries = ref<any[]>([])
  
  // Chart options configuration
  const chartOptions = {
    chart: {
      type: 'candlestick',
      height: 500,
      toolbar: {
        show: true
      }
    },
    xaxis: {
      type: 'datetime',
      labels: {
        style: {
          colors: '#9e9e9e',
          fontSize: '12px'
        }
      }
    },
    yaxis: {
      labels: {
        formatter: function (value: number) {
          return value.toFixed(2)
        }
      }
    },
    title: {
      text: 'Stock Prices Candlestick Chart',
      align: 'left',
      style: {
        fontSize: '16px',
        fontWeight: 'bold',
        color: '#333'
      }
    },
    tooltip: {
      theme: 'dark',
      x: {
        format: 'dd MMM'
      }
    },
    plotOptions: {
      candlestick: {
        colors: {
          upward: '#00e396',
          downward: '#ff4560'
        }
      }
    },
    grid: {
      borderColor: '#e0e0e0',
      strokeDashArray: 4
    }
  }
  
  // Fetch stock data and update the chart series
  const fetchStockInfo = async (ticker: string) => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/api/stock/${ticker}/history`)
      chartSeries.value = formatStockData(response.data)
    } catch (error) {
      console.error('Error fetching stock data:', error)
      chartSeries.value = []
    }
  }
  
  // Function to format the stock data for the chart
  const formatStockData = (data: any) => {
    return [
      {
        name: 'Stock Prices',
        data: Object.entries(data['Open']).map(([timestamp, open]) => ({
          x: new Date(parseInt(timestamp)).toISOString().split('T')[0], // Date in 'YYYY-MM-DD' format
          y: [
            open,
            data['High'][timestamp],
            data['Low'][timestamp],
            data['Close'][timestamp]
          ]
        }))
      }
    ]
  }
  </script>
  
  <style scoped>
  .chart-container {
    width: 100%;
    max-width: 60000px; /* Increased maximum width */
    margin: 0 auto;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .chart-title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .chart {
    width: 100%; /* Full width */
  }
  </style>
  