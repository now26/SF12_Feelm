<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue';
import { useCounterStore } from '@/stores/counter'
const useStore = useCounterStore()

</script>


<template>
  <div>
    <header>
      <p>Article List</p>
    </header>

    <ArticleListItem
      v-for="test in useStore.tests"
      :key="test.id"
      :test="test"
    />
  </div>
</template>


<style scoped>
p {
  font-size: 1.5rem;
  color:rgb(16, 16, 77);
  font-weight: bolder;
  padding-bottom: 30px;
}

</style>
