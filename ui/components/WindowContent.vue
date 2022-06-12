<script setup lang="ts">
import { ref } from 'vue'
import { api } from 'jianmu'

const msg = ref('点击下面的按钮试试')

async function getMsg() {
  msg.value = await api.invokePython('hello', 'World')
}
</script>

<template>
  <div class="window-content">
    <p>{{ msg }}</p>
    <el-button type="primary" @click="getMsg()">我是按钮</el-button>
  </div>
</template>

<style lang="scss" scoped>
.window-content {
  padding: 20px;
}
</style>
