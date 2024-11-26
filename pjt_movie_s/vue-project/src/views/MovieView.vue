<script setup>
import { useMovieStore } from '@/stores/movies';
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router';
import MovieList from '@/components/MovieList.vue'

const movieStore = useMovieStore()

onMounted(() => {
  movieStore.getMovies()
})
</script>


<template>
  <h1>Movies</h1>

  <div>
    <MovieList />
  </div>
</template>


<style scoped>

</style>
