<script setup>
import { useMovieStore } from '@/stores/movies';
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router';

import MoviePopular from '@/components/Movie_tmdb/MoviePopular.vue';
import MovieUpComing from '@/components/Movie_tmdb/MovieUpComing.vue';
import MovieTopRated from '@/components/Movie_tmdb/MovieTopRated.vue';
import MovieNowPlaying from '@/components/Movie_tmdb/MovieNowPlaying.vue';

const movieStore = useMovieStore()


</script>


<template>
  <div>
    <h1>TMDB</h1>
    <MoviePopular />
    <MovieUpComing />
    <MovieTopRated />
    <!-- <MovieNowPlaying /> -->

  </div>
</template>


<style scoped>

</style>
