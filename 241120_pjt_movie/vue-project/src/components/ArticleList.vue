<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue';
import { useCounterStore } from '@/stores/counter'
const useStore = useCounterStore()

</script>


<template>
  <div>
    <h3>Article List</h3>

    <ArticleListItem
      v-for="test in useStore.tests"
      :key="test.id"
      :test="test"
    />
  </div>
</template>


<style scoped>

</style>
