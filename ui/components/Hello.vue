<script setup lang="ts">
import { invokePython } from 'jianmu'
import { ref } from 'vue'

import jianmuImgUrl from 'assets/jianmu.png'

const target = ref('World')
const result = ref('')

async function onClick() {
  result.value = await invokePython('say_hello', target.value)
}
</script>

<template>
  <div class="hello">
    <p>
      <img :src="jianmuImgUrl" height="320" />
    </p>
    <h2>欢迎使用 Jianmu（建木）开发框架！</h2>
    <p>点击下面的按钮，就可以调用 src/app.py 中的 say_hello 函数。</p>
    <p>打开 src 目录下的 app.py，便可以看到 say_hello 函数的定义。</p>
    <p>您可以在下面的输入框中，输入被 say_hello 函数调用的参数。</p>
    <el-input
      class="input"
      v-model="target"
      placeholder="请输入 say_hello 的参数"
      clearable
    />
    <p>
      <el-button type="primary" @click="onClick()">
        调用 Python 函数 say_hello
      </el-button>
    </p>
    <p>say_hello 函数返回值为：</p>
    <pre>{{ result }}</pre>
  </div>
</template>

<style lang="scss" scoped>
.hello {
  text-align: center;
  .input {
    width: 480px;
  }
}
</style>
