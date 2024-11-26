<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  movie:Object
})
// console.log(props)
</script>


<template>
  
  <div>
    <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.tmdb_id }}">
      <img 
        class="movie-poster" 
        :src="movie.poster_url" 
        alt="img_Poster" 
        v-if="movie.poster_url"
      >
    </RouterLink>
    <p class="movieInfo">{{ movie.title }}</p>
  </div>

</template>


<style scoped>





/* .movie-card { */
  /* border: 1px solid #fff; */
  /* border: 1px none; */
  /* padding: 5px; */
/* } */


 .movie-poster {
  flex-shrink: 1;
  width: 200px;
  height: 300px;
  border-radius: 10px;
} 

.movieInfo {
  width: 200px;
  white-space: normal;
  display: flex;
  justify-content: center;
}




/* .title {
  font-weight: bold;
  font-size: clamp(0.5rem, 5vw, 1.5rem);
}

.img_Backdrop {
  min-width: 20%;
  max-width: 600px; 
  height: auto; 
} */

</style>
