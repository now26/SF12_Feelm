<script setup>
import MovieListItem from '@/components/MovieListItem.vue';
import { useMovieStore } from '@/stores/movies';
const movieStore = useMovieStore()

</script>


<template>

  <!-- <h3>MovieList</h3> -->

  <div class="movie-list">
    <MovieListItem 
      v-for="movie in movieStore.movies_db"
      :key="movie.tmdb_id"
      :movie="movie"
    />

  </div>
</template>


<style scoped>
.movie-list {
  /* display: flex; -> 요소 가로로 위치 */
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-left: 1rem;
  justify-content: center;
}
</style>
