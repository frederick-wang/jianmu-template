<script setup>
import { pyfuncs, pyvars } from 'jianmu'

const {
  name,
  result,
  sentence,
  sent_split,
  fig_b64,
  apple_count,
  plot_title,
  file_list,
  file_content_list
} = pyvars
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
      Plot Title:
      <el-input
        style="width: 50%"
        v-model="plot_title"
        placeholder="Please input plot title"
        clearable
      />
    </p>
    <p>
      apple_count:
      <el-input-number v-model="apple_count" :min="1" :max="100" />
    </p>
    <p><img :src="fig_b64" /></p>
    <el-upload v-model:file-list="file_list" drag multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">
        只能上传jpg/png文件，且不超过500kb
      </div>
    </el-upload>
    <div>
      <p v-for="v in file_content_list" :key="v">
        <pre>{{ v }}</pre>
      </p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#app {
  padding: 20px;
}
</style>
