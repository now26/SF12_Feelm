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
    <header>
      <p>Top Rated Movies</p>
    </header>

    <div class="tmdb-container">
      <div>
        <RouterLink :to="{ name:'MovieTopRatedDetailView' }" class="detail">Detail</RouterLink>
      </div>
  
      <div class="content">
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

  </div>
</template>


<style scoped>
header {
  font-size: 1.6rem;
  font-weight: bold;
  padding-left: 20px;
}

b {
  display: flex;
  justify-content: center;
  padding-bottom: 10px;
}

.detail {
  display: flex;
  justify-content: flex-end;
  color: aliceblue;
  font-size: 1.2rem;
  padding-bottom: 10px;
  text-decoration: none;
  padding-right: 20px;
}

.detail:hover{
  color: rgb(0, 68, 255)
}

.tmdb-container{
  /* background-color: aqua; */
  /* min-width: 100%; */
  display: flex;
  flex-direction: column;
  overflow: hidden;
  /* min-height: 100dvh; */
  padding-bottom: 100px;
/* 
  white-space: nowrap;
  overflow-x: auto;
  */
}

.content {
  display: flex;
  /* background-color: bisque; */
  width: 100%;
  overflow: hidden;
  /* box-sizing: border-box; */
}

.movie-list {
  display: flex;
  /* background-color: aqua; */
  padding-left: 20px;
  white-space: nowrap;
  overflow-x: scroll;
  width: 100dvw;
  /* padding: 20px;  */
  gap: 10px;
}

/* Webkit 기반 브라우저 (Chrome, Safari 등) */
/* 스크롤바 디자인 */
.movie-list::-webkit-scrollbar {
  width: 10px; /* 스크롤바의 너비 */
}

.movie-list::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1); /* 스크롤바의 배경 색상 */
  border-radius: 10px; /* 트랙에 둥근 모서리 적용 */
}

.movie-list::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.5); /* 스크롤바의 thumb 색상 */
  border-radius: 10px; /* thumb에 둥근 모서리 적용 */
}

.movie-list::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.8); /* thumb에 hover 효과 적용 */
}

.movie-poster {
  flex-shrink: 1; 
  width: 200px;
  height: 300px;
  border-radius: 10px;
}
</style>
