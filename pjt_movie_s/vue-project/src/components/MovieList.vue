<script setup>
import MovieListItem from '@/components/MovieListItem.vue';
import { useMovieStore } from '@/stores/movies';
const movieStore = useMovieStore()

</script>


<template>
  <div>
    <h3>MovieList</h3>
    <MovieListItem 
      v-for="movie in movieStore.movies_db"
      :key="movie.tmdb_id"
      :movie="movie"
    />

  </div>
</template>


<style scoped>

</style>
