<script setup>
// 导入 Vue 组件
import IndexPage from './pages/IndexPage.vue'
import BriefPage from './pages/BriefPage.vue'
// 导入 Python 函数与 Python 响应式变量
import { pyfuncs, pyvars } from 'jianmu'

const { header_index } = pyvars
const { handle_header_select } = pyfuncs
</script>

<template>
  <div id="app">
    <el-container>
      <el-header>
        <el-menu
          :default-active="header_index"
          mode="horizontal"
          @select="handle_header_select"
        >
          <el-menu-item index="jianmu-template">Jianmu Template</el-menu-item>
          <el-menu-item index="brief">简介</el-menu-item>
        </el-menu>
      </el-header>
      <!-- 用 v-if 控制导入的页面组件的显示 -->
      <index-page v-if="header_index == 'jianmu-template'" />
      <brief-page v-else-if="header_index == 'brief'" />
    </el-container>
  </div>
</template>

<style scoped></style>
