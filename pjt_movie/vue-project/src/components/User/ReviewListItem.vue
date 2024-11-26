<script setup>
import { RouterLink } from 'vue-router';

defineProps({
  review:Object
})

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
}

</script>


<template>
  <div>
    <ul>
      <RouterLink :to="{ name: 'MovieDetailView', params:{ id: review.movie.tmdb_id }}">
        <img :src="getPosterUrl(review.movie.poster_path, 'w300')" alt="poster_img">
      </RouterLink>
      <p>Movie : {{ review.movie.title }}</p>
      <p>Contents : {{ review.content }}</p>
      <p>Ratings : {{ review.rating }}</p>
    </ul>
    <hr>
  </div>
</template>


<style scoped>

</style>
