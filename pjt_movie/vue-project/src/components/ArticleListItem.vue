<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  test: Object
})
</script>


<template>
  <div class="arti">
    <!-- <h5>ArticleListItem</h5> -->
    <div class="textItem">{{ test.id }}. {{ test.title }}</div>
    <RouterLink :to="{ name:'ArticleDetailView', params:{ id : test.id }}">상세보기</RouterLink>
    <!-- <hr> -->
  </div>
</template>


<style scoped>
.arti{
  margin-bottom: 20px;
  display: flex;
  justify-content: space-around;
}

.textItem {
  color: #333;
  font-size: 20px;
  margin-bottom: 10px;
}
</style>
