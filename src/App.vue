<template>
  <div class="app-container">
    <h1>日志查看器</h1>
    <TimeInput @fetch-logs="handleFetchLogs" />
    <LogDisplay 
      :entries="logEntries"
      :loading="isLoading"
      :error="errorMessage"
    />
  </div>
</template>

<script>
import TimeInput from './components/TimeInput.vue'
import LogDisplay from './components/LogDisplay.vue'
import axios from 'axios'
const host = window.location.hostname;
export default {
  name: 'App',
  components: {
    TimeInput,
    LogDisplay
  },
  data() {
    return {
      logEntries: [],
      isLoading: false,
      errorMessage: ''
    }
  },
  mounted() {
    const today = new Date();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    this.handleFetchLogs({ month, day });
  },
  methods: {
    async handleFetchLogs({ month, day }) {
      this.isLoading = true
      this.errorMessage = ''
      try {
        const response = await axios.get(`http://${host}:5000/logs/${month}/${day}`)
        this.logEntries = response.data.entries
      } catch (error) {
        this.errorMessage = error.response?.data?.description || '获取日志失败'
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style>
.app-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
}

@media (max-width: 768px) {
  .app-container {
    padding: 0;
  }
}

h1 {
  color: #2c3e50;
  margin-bottom: 20px;
  font-size: 24px;
}
</style>
