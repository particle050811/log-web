<template>
  <div class="log-display">
    <div v-if="loading" class="loading">加载中...</div>
    <template v-else>
      <div v-if="error" class="error-message">
        <span class="level">ERROR</span>
        <span class="content">{{ error }}</span>
      </div>
      <div v-else class="log-table-container">
        <table class="log-table">
          <thead>
            <tr>
              <th class="timestamp-header">时间戳</th>
              <th class="content-header">内容</th>
            </tr>
          </thead>
          <tbody ref="logBody">
            <tr
              v-for="(entry, index) in entries"
              :key="index"
              class="log-entry"
            >
              <td class="timestamp">{{ entry.timestamp }}</td>
              <td class="content">{{ entry.content }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  props: {
    entries: Array,
    loading: Boolean,
    error: String
  },
  mounted() {
    this.scrollToBottom();
  },
  watch: {
    entries() {
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    }
  },
  methods: {
    scrollToBottom() {
      if (this.$refs.logBody) {
        this.$refs.logBody.scrollIntoView({ block: 'end' });
      }
    }
  }
}
</script>

<style scoped>
.log-display {
  --header-height: 60px; /* 顶部日期选择器高度 */
  height: 100%;
  display: flex;
  flex-direction: column;
}

.log-table-container {
  flex: 1;
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.log-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  display: block;
  overflow-y: auto;
  max-height: calc(100vh - var(--header-height) - 120px); /* 留出更多边距 */
  margin-bottom: 0;
}

.log-table thead {
  position: sticky;
  top: 0;
  background: white;
}

.log-table tbody {
  flex-grow: 1;
  overflow-y: auto;
}

.timestamp-header {
  width: 120px;
  text-align: left;
  padding: 8px;
  border-bottom: 2px solid #42b983;
}

.content-header {
  text-align: left;
  padding: 8px;
  border-bottom: 2px solid #42b983;
}

.log-entry {
  border-bottom: 1px solid #eee;
}

.log-entry:hover {
  background-color: #f8f8f8;
}

.timestamp {
  width: 120px;
  padding: 8px;
  vertical-align: top;
}

.content {
  padding: 8px;
  white-space: pre-wrap;
  word-break: break-word;
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

@media (max-width: 768px) {
  .log-display {
    margin: 0 !important;
    padding: 10px !important;
  }
  
  .timestamp-header,
  .timestamp {
    width: 80px;
  }
}
</style>