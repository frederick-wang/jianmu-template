<script setup lang="ts">
import Titlebar from './components/Titlebar.vue'
import WindowContainer from './components/WindowContainer.vue'
</script>

<template>
  <div class="main-view">
    <Titlebar />
    <WindowContainer />
  </div>
</template>

<style lang="scss">
@import './global.scss';

.main-view {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>
