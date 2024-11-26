<script setup>
import { ref, computed } from 'vue'
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movies';
import MovieTopRatedDetailView from '@/views/Movie_tmdb/MovieTopRatedDetailView.vue';

const movieStore = useMovieStore()

onMounted(() => {
  // window.addEventListener(eventName, updateDateRange)
  movieStore.getMovieTopRated(movieStore.tr_currentPage)
})

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
//   else {
//     return `${BASE_IMAGE_URL}/default-image.jpg`; // 기본 이미지 경로
//   }
}

const getBackDrop = (backDropPath, imageSize) => {
  if (backDropPath) {
    return `${BASE_IMAGE_URL}${imageSize}${backDropPath}`
  }
//   else {
//     return `${BASE_IMAGE_URL}/default-image.jpg`; // 기본 이미지 경로
//   }
}

const movies = computed(() => movieStore.movie_topRated)
const currentPage = computed(() => movieStore.tr_currentPage)
const totalPages = computed(() => movieStore.tr_totalPages)
// console.log(movies)

</script>


<template>
  <div>
    <h3>Top Rated Movies</h3>
    <RouterLink :to="{ name:'MovieTopRatedDetailView' }">Detail</RouterLink>

    <div>
      <div v-if="movies.length !== null">
        <div class="movie-list">
          <div 
            v-for="movie in movies"
            :key="movie.id"
            class="movie-card"
          >
            <img :src="getPosterUrl(movie.poster_path, 'original')" alt="Movie Poster" class="movie-poster">
            <p><b>{{ movie.title }}</b></p>
  
          </div>
        </div>
      </div>

      <div v-else>
        <p>No Movies</p>
      </div>
    </div>

  </div>
</template>


<style scoped>
.movie-list {
  display: flex;
  gap: 10px;
  width: 80%;
  overflow-x: auto;
  white-space: nowrap;
  padding-bottom: 10px; 
  padding: 20px;
}

.movie-card {
  width: 200px; 
  flex-shrink: 0; 
  padding: 5px;
  box-sizing: border-box;
}

.movie-poster {
  width: 100%;
  height: auto;
}

</style>
