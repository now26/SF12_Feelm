<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  test: Object
})
</script>


<template>
  <div>
    <!-- <h5>ArticleListItem</h5> -->
    <div>{{ test.id }}. {{ test.title }}</div>
    <RouterLink :to="{ name:'ArticleDetailView', params:{ id : test.id }}">상세보기</RouterLink>
    <hr>
  </div>
</template>


<style scoped>

</style>
