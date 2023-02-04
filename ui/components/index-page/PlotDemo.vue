<script setup>
import { pyvars } from 'jianmu'

const { fig, plot_cnt, plot_title } = pyvars
</script>

<template>
  <div>
    <h2>Plot</h2>
    <p>
      plot_title:
      <el-input
        style="width: 50%"
        v-model="plot_title"
        placeholder="Please input plot title"
        clearable
      />
    </p>
    <p>
      plot_cnt:
      <el-input-number v-model="plot_cnt" :min="1" :max="100" />
    </p>
    <p><img :src="fig" /></p>
  </div>
</template>

<style scoped></style>
