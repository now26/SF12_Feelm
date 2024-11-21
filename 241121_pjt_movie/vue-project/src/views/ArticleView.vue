<script setup>
import { useCounterStore } from '@/stores/counter.js'
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/ArticleList.vue';

const useStore = useCounterStore()


onMounted(()=>{
  useStore.getArticles()
  // console.log(useStore.tests)
})
</script>


<template>
  <h1>Articles</h1>
  
  <div>
    <nav>
      <RouterLink :to="{name: 'ArticleCreateView'}">Create</RouterLink>
    </nav>
  </div>

  <div>
    <ArticleList/>
  </div>

</template>


<style scoped>

</style>
