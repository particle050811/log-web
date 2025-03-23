<template>
  <div class="time-input">
    <form @submit.prevent="fetchLogs">
      <div class="input-group">
        <input 
          v-model="month" 
          type="number"
          min="1" 
          max="12"
          placeholder="MM"
          class="input-field"
          required
        >
        <span class="separator">/</span>
        <input
          v-model="day"
          type="number"
          min="1" 
          max="31"
          placeholder="DD"
          class="input-field"
          required
        >
      </div>
      <button type="submit" class="submit-btn">查询日志</button>
    </form>
    <div v-if="error" class="error-msg">{{ error }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      month: '',
      day: '',
      error: ''
    }
  },
  mounted() {
    const now = new Date()
    this.month = String(now.getMonth() + 1)
    this.day = String(now.getDate())
    this.fetchLogs()
  },
  methods: {
    async fetchLogs() {
      try {
        this.error = ''
        this.$emit('fetch-logs', { 
          month: String(this.month).padStart(2, '0'), 
          day: String(this.day).padStart(2, '0')
        })
      } catch (err) {
        this.error = '请输入有效的日期格式（MM/DD）'
      }
    }
  }
}
</script>

<style scoped>
.time-input {
  margin: 20px 0;
}

.input-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.input-field {
  width: 60px;
  padding: 6px;
  border: 1px solid #42b983;
  border-radius: 4px;
  font-size: 14px;
}

.separator {
  color: #2c3e50;
  margin: 0 4px;
}

.submit-btn {
  margin-top: 8px;
  padding: 6px 16px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}

.error-msg {
  color: #ff4757;
  margin-top: 10px;
}
</style>