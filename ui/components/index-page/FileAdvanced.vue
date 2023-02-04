<script setup>
// 导入 Python 函数与 Python 响应式变量
import { pyfuncs, pyvars } from 'jianmu'

const { file_list, file_content_list } = pyvars
const { clear_file } = pyfuncs
</script>

<template>
  <div>
    <el-upload v-model:file-list="file_list" drag multiple :auto-upload="false">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">
        只能上传jpg/png文件，且不超过500kb
      </div>
    </el-upload>
    <div>
      <el-button @click="clear_file">清空文件</el-button>
    </div>
    <div>
      <pre v-for="file_content in file_content_list" :key="file_content">
        {{ file_content }}
      </pre>
    </div>
  </div>
</template>

<style scoped></style>
