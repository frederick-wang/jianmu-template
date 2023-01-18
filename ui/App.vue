<script setup>
import { pyfuncs, pyvars } from 'jianmu'

const { name, result, sentence, sent_split, fig_b64, apple_count } = pyvars
const { add_count } = pyfuncs
</script>

<template>
  <div id="app">
    name: <input v-model="name" placeholder="请输入 name 的值" clearable />
    <p>
      <button @click="add_count()">调用 add_count()</button>
    </p>
    <p>result 的值为：</p>
    <pre>{{ result }}</pre>
    原句：<input v-model="sentence" placeholder="请输入 name 的值" clearable />
    <p>分词结果为：</p>
    <pre>{{ sent_split }}</pre>
    <h2>Plot</h2>
    <p>
      apple_count:
      <el-input-number v-model="apple_count" :min="1" :max="100" />
    </p>
    <p><img :src="fig_b64" /></p>
  </div>
</template>

<style lang="scss" scoped>
#app {
  padding: 20px;
}
</style>
