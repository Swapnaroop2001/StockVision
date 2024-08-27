// src/plugins/apexcharts.ts
import { App } from 'vue';
import VueApexCharts from 'vue3-apexcharts';

export default {
  install(app: App) {
    app.use(VueApexCharts);
    app.component('apexchart', VueApexCharts);
  }
};
