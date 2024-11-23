<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  movie:Object
})
// console.log(props)
</script>


<template>
  <div>

    <p class="title">{{ movie.title }}</p>
    
    <div>
      <!-- 배경 이미지 표시 -->
      <img class="img_Backdrop" :src="movie.backdrop_url" alt="img_Backdrop" v-if="movie.backdrop_url">
    </div>

    <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.tmdb_id }}">상세보기</RouterLink>
        
    <hr>
  </div>
</template>


<style scoped>
.title {
  font-weight: bold;
  font-size: clamp(0.5rem, 5vw, 1.5rem);
}

.img_Backdrop {

  min-width: 20%;
  max-width: 600px; 
  height: auto; 
}

</style>
