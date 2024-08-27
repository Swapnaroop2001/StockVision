declare module 'vue-chartjs' {
    import { Component } from 'vue';
    import { Chart as ChartJS, ChartData, ChartOptions } from 'chart.js';
  
    // Declare the component exports
    export const Line: Component;
    export const Bar: Component;
    export const Doughnut: Component;
    export const Pie: Component;
  
    // Declare the ChartProps interface for chart components
    export interface ChartProps<TType extends keyof ChartJS> {
      data: ChartData<TType>;
      options?: ChartOptions<TType>;
    }
  }
  