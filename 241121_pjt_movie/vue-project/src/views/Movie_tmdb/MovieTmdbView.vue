<script setup>
import { useMovieStore } from '@/stores/movies';
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router';

import MovieNowPlaying from '@/components/Movie_tmdb/MovieNowPlaying.vue';
import MoviePopular from '@/components/Movie_tmdb/MoviePopular.vue';
import MovieTopRated from '@/components/Movie_tmdb/MovieTopRated.vue';

const movieStore = useMovieStore()


</script>


<template>
  <div>
    <h1>TMDB</h1>
    <MoviePopular />
    <MovieNowPlaying />
    <!-- <MovieTopRated /> -->

  </div>
</template>


<style scoped>

</style>
