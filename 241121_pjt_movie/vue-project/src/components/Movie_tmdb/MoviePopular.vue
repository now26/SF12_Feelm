<script setup>
import { ref, computed } from 'vue'
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movies';
import MoviePopularDetailView from '@/views/Movie_tmdb/MoviePopularDetailView.vue';

// Pinia store에서 상태와 함수를 가져오기.
const movieStore = useMovieStore()

// 컴포넌트가 마운트될 때 영화 목록을 불러오기.
onMounted(() => {
  movieStore.getMoviePopular(movieStore.po_currentPage)
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

const movies = computed(() => movieStore.movie_popular)
const currentPage = computed(() => movieStore.po_currentPage)
const totalPages = computed(() => movieStore.po_totalPages)
// console.log(movies)

</script>


<template>
  <div>
    <h3>Popular Movies</h3>
    <RouterLink :to="{ name:'MoviePopularDetailView' }">Detail</RouterLink>

    <div>
      <div v-if="movies.length !== null">
        <div class="movie-list">
          <div 
            v-for="movie in movies"
            :key="movie.id"
            class="movie-card"
          >
            <img :src="getPosterUrl(movie.poster_path, 'w300')" alt="Movie Poster" class="movie-poster">
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
