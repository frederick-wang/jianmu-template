<script setup>
// 导入 Plot Demo 组件
import PlotDemo from '../components/index-page/PlotDemo.vue'
// 导入 FileAdvanced 组件
import FileAdvanced from '../components/index-page/FileAdvanced.vue'
// 导入图标
import { Document, Location, Setting } from '@element-plus/icons-vue'
// 导入 Python 函数与 Python 响应式变量
import { pyfuncs, pyvars } from 'jianmu'

const { name, result, sentence, sent_split, aside_index, test_file_path } =
  pyvars
const {
  add_count,
  handle_aside_select,
  test_message_box,
  test_error_box,
  test_beep,
  test_open_dialog,
  test_save_dialog,
  test_show_item_in_folder,
  test_open_path,
  test_open_external,
  test_trash_item
} = pyfuncs
</script>

<template>
  <el-container>
    <el-aside width="200px">
      <el-menu :default-active="aside_index" @select="handle_aside_select">
        <el-menu-item index="1">
          <el-icon><document /></el-icon>
          <span>测试 1</span>
        </el-menu-item>
        <el-menu-item index="2">
          <el-icon><setting /></el-icon>
          <span>测试 2</span>
        </el-menu-item>
        <el-menu-item index="3">
          <el-icon><location /></el-icon>
          <span>画图</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><location /></el-icon>
          <span>反馈</span>
        </el-menu-item>
        <el-menu-item index="5">
          <el-icon><location /></el-icon>
          <span>文件（基本）</span>
        </el-menu-item>
        <el-menu-item index="6">
          <el-icon><location /></el-icon>
          <span>文件（进阶）</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-main>
        <!-- 侧边栏的第一个功能 -->
        <div v-if="aside_index == '1'">
          <p>
            name:
            <input v-model="name" placeholder="请输入 name 的值" clearable />
          </p>
          <p>
            <button @click="add_count()">调用 add_count()</button>
          </p>
          <p>result 的值为：</p>
          <pre>{{ result }}</pre>
        </div>
        <!-- 侧边栏的第二个功能 -->
        <div v-if="aside_index == '2'">
          <p>
            原句：<input
              v-model="sentence"
              placeholder="请输入 name 的值"
              clearable
            />
          </p>
          <p>按字切分结果为：</p>
          <pre>{{ sent_split }}</pre>
        </div>
        <!-- 侧边栏的第三个功能 -->
        <!-- 加载一个封装好的 Vue 组件 -->
        <plot-demo v-if="aside_index == '3'" />
        <div v-if="aside_index == '4'">
          <button @click="test_message_box()">test_message_box</button>
          <button @click="test_error_box()">test_error_box</button>
          <button @click="test_beep()">test_beep</button>
          <button @click="test_open_external()">test_open_external</button>
        </div>
        <div v-if="aside_index == '5'">
          <button @click="test_save_dialog()">test_save_dialog</button>
          <p>test_file_path: {{ test_file_path }}</p>
          <button @click="test_open_dialog()">test_open_dialog</button>
          <button @click="test_show_item_in_folder()">
            test_show_item_in_folder
          </button>
          <button @click="test_open_path()">test_open_path</button>
          <button @click="test_trash_item()">test_trash_item</button>
        </div>
        <file-advanced v-if="aside_index == '6'" />
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped></style>
