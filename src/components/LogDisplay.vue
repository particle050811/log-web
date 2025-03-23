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
          <span>内容</span>
        </div>
        <div 
          v-for="(entry, index) in entries" 
          :key="index"
          class="log-entry"
        >
          <span class="timestamp">{{ entry.timestamp }}</span>
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
  max-width: 1200px;
  overflow-y: auto;
}

.log-header {
  display: grid;
  grid-template-columns: minmax(80px, 0.12fr) 1fr;
  gap: clamp(1px, 0.3vw, 3px);
  padding: 4px 6px;
  font-weight: bold;
  border-bottom: 2px solid #42b983;
  position: sticky;
  top: 0;
  background: white;
}

.log-entry {
  display: grid;
  grid-template-columns: minmax(80px, 0.12fr) 1fr;
  gap: clamp(1px, 0.3vw, 3px);
  padding: 4px 6px;
  border-bottom: 1px solid #eee;
}

.log-entry:hover {
  background-color: #f8f8f8;
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

.content {
  white-space: pre-wrap;
  word-break: break-word;
  min-height: 20px;
}
</style>