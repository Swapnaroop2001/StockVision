import './assets/main.css'
import ApexCharts from 'vue3-apexcharts';
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';

import App from './App.vue'
import router from './router'



const app = createApp(App)
app.use(Toast);

app.use(ApexCharts);
app.component('apexchart', ApexCharts);

app.use(createPinia())
app.use(router)

app.mount('#app')
