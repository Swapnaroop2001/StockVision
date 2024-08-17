<template>
  <div v-if="stock" class="stock-info">
    <div class="info-container">
      <div class="stock-details">
        <h1 class="stock-title">{{ stock.name }}</h1>

        <!-- Combined Stock Detail Card -->
        <div class="combined-detail-card">
          <h2 class="combined-card-title">Stock Overview</h2>
          <div class="combined-card-content">
            <div class="combined-detail">
              <span class="combined-label">Symbol:</span>
              <span class="combined-value">{{ stock.symbol }}</span>
            </div>
            <div class="combined-detail">
              <span class="combined-label">CEO:</span>
              <span class="combined-value">{{ stock.companyOfficers[0].name }}</span>
            </div>
            <div class="combined-detail">
              <span class="combined-label">Sector:</span>
              <span class="combined-value">{{ stock.sector }}</span>
            </div>
          </div>
        </div>

        <div class="detail-item" v-for="detail in stockDetails.slice(3)" :key="detail.label">
          <span class="label">{{ detail.label }}:</span>
          <span :class="detail.className || 'value'">{{ detail.value }}</span>
        </div>
      </div>

      <div class="stock-summary">
        <h2><b>Business Summary</b></h2>
        <p>{{ stock.longBusinessSummary }}</p>
      </div>
    </div>

    <div class="officer-cards">
      <h2>Top Company Officers</h2>
      <div class="officer-cards-container">
        <div class="officer-card" v-for="(officer, index) in topOfficers" :key="index">
          <h3>{{ officer.name }}</h3>
          <p><strong>Title:</strong> {{ officer.title }}</p>
          <p><strong>Age:</strong> {{ officer.age }}</p>
          <p><strong>Total Pay:</strong> ${{ officer.totalPay.toLocaleString() }}</p>
          <p><strong>Exercised Value:</strong> ${{ officer.exercisedValue.toLocaleString() }}</p>
          <p><strong>Unexercised Value:</strong> ${{ officer.unexercisedValue.toLocaleString() }}</p>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="no-data">
    <p>"Enter the stock ticker to view detailed information."</p>
  </div>
</template>



<script setup lang="ts">
import { defineProps, computed } from 'vue';

interface Stock {
  name: string;
  companyOfficers: CompanyOfficer[];
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

interface CompanyOfficer {
  name: string;
  age: number;
  title: string;
  totalPay: number;
  exercisedValue: number;
  unexercisedValue: number;
  fiscalYear: number;
  yearBorn: number;
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

const stockDetails = computed(() => {
  if (!props.stock) return [];
  return [
    { label: 'Symbol', value: props.stock.symbol },
    { label: 'CEO', value: props.stock.companyOfficers[0].name },
    { label: 'Sector', value: props.stock.sector },
    { label: 'Percentage Change', value: `${percentageChange.value.toFixed(2)}%`, className: percentageChangeClass.value },
    { label: 'Current Price', value: `$${props.stock.currentPrice.toFixed(2)}`, className: 'current-price' },
    { label: 'Open Price', value: `$${props.stock.open.toFixed(2)}` },
    { label: 'Day High', value: `$${props.stock.dayHigh.toFixed(2)}` },
    { label: 'Day Low', value: `$${props.stock.dayLow.toFixed(2)}` },
    { label: 'Volume', value: props.stock.volume.toLocaleString() },
    { label: 'Previous Close', value: `$${props.stock.previousClose.toFixed(2)}` },
    { label: '52 Week High', value: `$${props.stock.fiftyTwoWeekHigh.toFixed(2)}` },
    { label: '52 Week Low', value: `$${props.stock.fiftyTwoWeekLow.toFixed(2)}` }
  ];
});

const topOfficers = computed(() => {
  if (props.stock && props.stock.companyOfficers) {
    return props.stock.companyOfficers.slice(0, 4);
  }
  return [];
});
</script>

<style scoped>
.combined-detail-card {
  background: linear-gradient(to top left, #fff, #f9f9f9);
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  padding: 20px;
  margin-bottom: 30px;
}

.combined-card-title {
  margin: 0 0 15px 0;
  font-size: 1.8rem;
  color: #333;
}

.combined-card-content {
  display: flex;
  flex-direction: column;
}

.combined-detail {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #e0e0e0;
}

.combined-detail:last-child {
  border-bottom: none;
}

.combined-label {
  font-weight: bold;
  color: #666;
}

.combined-value {
  font-size: 1.2rem;
  color: #222;
}
.stock-info {
  max-width: 1200px;
  margin: 20px auto;
  padding: 30px;
  background-color: #f0f0f0;
  border-radius: 10px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.8s ease-out;
}

.info-container {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
  animation: slideIn 0.8s ease-out;
}

.stock-details, .stock-summary {
  flex: 1;
  min-width: 350px;
}

.stock-title {
  font-size: 2.4rem;
  color: #444;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  padding: 15px;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.detail-item:hover {
  transform: scale(1.03);
  background-color: #f9f9f9;
}

.label {
  font-weight: bold;
  color: #666;
}

.value {
  font-size: 1.1rem;
  color: #222;
}

.current-price {
  font-size: 1rem;
  font-weight: bold;
  color: #333;
}

.percentage-change {
  font-size: 1rem;
  font-weight: bold;
}

.stock-summary {
  background: linear-gradient(to top left, #ffffff, #f9f9f9);
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  padding: 25px;
  border: 1px solid #e0e0e0;
  margin-bottom: 30px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden; /* Ensure the circle does not overflow */
}

.stock-summary:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.stock-summary::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 30%;
  height: 25%;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 50%;
  transform: rotate(45deg);
  z-index: 0;
}

.stock-summary h2 {
  margin-top: 0;
  font-size: 1.8rem;
  color: #333;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 10px;
  font-weight: 600;
  position: relative;
  z-index: 1;
}

.stock-summary p {
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
  position: relative;
  z-index: 1;
}

.stock-summary p::first-line {
  font-weight: bold;
  color: #333;
}


@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateX(-50px); }
  to { transform: translateX(0); }
}

.officer-cards {
  margin-top: 30px;
}

.officer-cards-container {
  display: flex;
  gap: 20px;
  overflow-x: auto;
  padding: 10px 0;
}

.officer-card {
  background: linear-gradient(to top left, #fff, #f9f9f9);
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  padding: 20px;
  flex: 1;
  min-width: 250px;
  max-width: 300px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  overflow: hidden;
}

.officer-card::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 50%;
  height: 50%;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 50%;
  transform: rotate(45deg);
  z-index: 0;
}

.officer-card h3 {
  margin: 0 0 10px 0;
  font-size: 1.6rem;
  color: #444;
  z-index: 1;
  position: relative;
}

.officer-card p {
  margin: 5px 0;
  color: #666;
  z-index: 1;
  position: relative;
}

.officer-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.positive {
  font-size: 1rem;
  color: #4caf50;
  font-weight: bold;
}

.negative {
  font-size: 1rem;
  color: #f44336;
  font-weight: bold;
}

.neutral {
  color: #888;
}

.no-data {
  text-align: center;
  padding: 25px;
  color: #aaa;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateX(-50px); }
  to { transform: translateX(0); }
}
</style>


