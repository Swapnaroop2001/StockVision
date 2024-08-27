<template>
  <div>
    <StockSearch @search="fetchNews" />

    <div v-if="filteredNewsStories.length > 0" class="news-container">
      <div v-for="story in filteredNewsStories" :key="story.id" class="card-container">
        <!-- Date in top-right corner -->
        <div class="card-date">{{ formatDate(story.time) }}</div>
        <img :src="story.favicon_url || fallbackImage" alt="News Image" class="card-image" />
        <div class="card-content">
          <p class="card-site">{{ story.site }}</p>
          <h3 class="card-title">{{ story.title }}</h3>
          <p class="card-description">{{ story.description }}</p>
          <p class="card-time">{{ formatTimeAgo(story.time) }}</p>
          <a :href="story.url" class="card-link" target="_blank">Read more...</a>
        </div>
      </div>
    </div>
    <div v-else>
      <p>"Enter the stock ticker to view recent News."</p>
    </div>
  </div>
</template>
  
<script setup lang="ts">
import { ref, computed } from 'vue'
import StockSearch from './StockSearch.vue'

// Fallback image URL
const fallbackImage = 'src/assets/news.png'

// Reactive references for ticker and news stories
const ticker = ref('')
const newsStories = ref<any[]>([])

// Fetch news stories based on the provided ticker
const fetchNews = async (searchTicker: string) => {
  ticker.value = searchTicker; // Update ticker ref
  if (!searchTicker) {
    newsStories.value = []; // Clear news stories if no ticker
    return;
  }
  try {
    const response = await fetch(`https://api.tickertick.com/feed?q=tt:${searchTicker}&n=20`)
    const data = await response.json()
    console.log('API Response:', data)
    newsStories.value = data.stories
  } catch (error) {
    console.error('Error fetching news:', error)
    newsStories.value = []
  }
}

// Computed property to filter out stories without images
const filteredNewsStories = computed(() => {
  return newsStories.value.filter((story) => story.favicon_url)
})

// Function to format the time since the news was posted
const formatTimeAgo = (timestamp: number) => {
  const now = Date.now()
  const difference = now - timestamp
  const seconds = Math.floor(difference / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)

  if (days > 0) return `${days} day${days > 1 ? 's' : ''} ago`
  if (hours > 0) return `${hours} hour${hours > 1 ? 's' : ''} ago`
  if (minutes > 0) return `${minutes} minute${minutes > 1 ? 's' : ''} ago`
  return `${seconds} second${seconds > 1 ? 's' : ''} ago`
}

// Function to format the date
const formatDate = (timestamp: number) => {
  const date = new Date(timestamp)
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
}
</script>

  
<style scoped>
.header {
  font-size: 2rem;
  margin-bottom: 20px;
  text-align: center;
  color: #333;
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 250px;
}

.search-button {
  padding: 10px 20px;
  font-size: 1rem;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  margin-left: 10px;
}

.search-button:hover {
  background-color: #0056b3;
}

.news-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-container {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  overflow: hidden;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 10px;
  background-color: #fff;
  width: 100%; /* Adjusted width */
  max-width: 1000px; /* Adjusted max-width */
  position: relative;
}

.card-date {
  position: absolute;
  top: 5px;
  right: 5px;
  background-color: #fff;
  color: #555;
  font-size: 0.7rem; /* Smaller font size */
  padding: 3px 5px;
  border-radius: 4px;
}

.card-image {
  flex: 0 0 80px; /* Smaller width */
  height: 80px; /* Smaller height */
  object-fit: cover;
  border-radius: 6px;
  margin-right: 10px;
  justify-content: center;
  align-items: center;
}

.card-content {
  flex: 1;
}

.card-title {
  font-size: 1.2rem; /* Smaller font size */
  margin: 0 0 5px 0; /* Adjusted margin */
  color: #333;
}

.card-description {
  font-size: 0.8rem; /* Smaller font size */
  margin: 0;
  max-height: 3em; /* Adjusted height */
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* Limit to 2 lines */
  -webkit-box-orient: vertical;
  color: #555;
}

.card-site {
  font-size: 0.8rem; /* Smaller font size */
  color: #777;
  margin-top: 3px; /* Adjusted margin */
}

.card-link {
  text-decoration: none;
  color:#3c8500;
  font-weight: bold;
}

.card-link:hover {
  text-decoration: underline;
}

.card-time {
  font-size: 0.8rem; /* Smaller font size */
  color: #999;
  margin-top: 5px; /* Adjusted margin */
}

.no-news {
  text-align: center;
  font-size: 1.2rem;
  color: #777;
}
</style>
