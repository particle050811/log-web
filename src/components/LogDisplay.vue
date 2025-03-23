<template>
  <div class="log-display">
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else>
      <div v-if="error" class="log-entry error">
        <span class="timestamp">-</span>
        <span class="level">ERROR</span>
        <span class="content">{{ error }}</span>
      </div>
      <div v-else>
        <div class="log-header">
          <span>时间戳</span>
          <span>日志级别</span>
          <span>内容</span>
        </div>
        <div 
          v-for="(entry, index) in entries" 
          :key="index"
          class="log-entry"
          :class="entry.level.toLowerCase()"
        >
          <span class="timestamp">{{ entry.timestamp }}</span>
          <span class="level">{{ entry.level }}</span>
          <span class="content">{{ entry.content }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    entries: Array,
    loading: Boolean,
    error: String
  }
}
</script>

<style scoped>
.log-display {
  margin: 20px auto;
  max-width: 600px;
}

.log-header {
  display: grid;
  grid-template-columns: 120px 70px 1fr;
  gap: 8px;
  padding: 8px;
  font-weight: bold;
  border-bottom: 2px solid #42b983;
}

.log-entry {
  display: grid;
  grid-template-columns: 120px 70px 1fr;
  gap: 8px;
  padding: 8px;
  border-bottom: 1px solid #eee;
}

.log-entry:hover {
  background-color: #f8f8f8;
}

.level {
  text-transform: uppercase;
  font-weight: bold;
}

.error-message {
  color: #ff4757;
  text-align: center;
  padding: 10px;
}

.loading {
  text-align: center;
  padding: 15px;
  color: #42b983;
}

.info { color: #2c3e50; }
.debug { color: #3498db; }
.warning { color: #f1c40f; }
.error { color: #ff4757; }
</style>