<script setup>
import { ref, computed } from 'vue'
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movies';
import MovieNowPlayingDetailView from '@/views/Movie_tmdb/MovieNowPlayingDetailView.vue';

const movieStore = useMovieStore()

// const eventName = 'MovieNowPlayingDetailView-date-range-changed'
// const dateRange = ref({ startDate: '', endDate: ''})

// const updateDateRange = (newDateRange) => {
//   dateRange.value = newDateRange.detail
//   console.log(dateRange)
//   console.log('newDate: ', newDateRange)
// }


onMounted(() => {
  // window.addEventListener(eventName, updateDateRange)
  movieStore.getMovieNowPlaying(movieStore.np_currentPage)
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

const movies = computed(() => movieStore.movie_nowPlaying)
const currentPage = computed(() => movieStore.np_currentPage)
const totalPages = computed(() => movieStore.np_totalPages)
// console.log(movies)

</script>


<template>
  <div>
    <h3>Now Playing Movies</h3>
    <RouterLink :to="{ name:'MovieNowPlayingDetailView' }">Detail</RouterLink>

    <!-- 날짜 범위 선택 컴포넌트 -->
    <!-- <MovieNowPlayingDetailView @date-range-changed="updateDateRange" /> -->

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
