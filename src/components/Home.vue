<script setup lang="ts">
import { onMounted, ref } from 'vue'
import api from '@/api'

const welcomeMessage = ref(null)

onMounted(async () => {
  try {
    const response = await api.get('/welcome')
    welcomeMessage.value = response.data.message
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div>
    <div v-if="welcomeMessage">
      {{ welcomeMessage }}
    </div>
  </div>
</template>
