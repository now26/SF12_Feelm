<script setup>
import { ref, computed } from 'vue'
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movies';

// Pinia store에서 상태와 함수를 가져오기.
const movieStore = useMovieStore()

// 페이지 이동 ========================================

// 앞으로 1페이지 이동
const prev1Page = () => {
  if (movieStore.tr_currentPage > 1){
    movieStore.getMovieTopRated(movieStore.tr_currentPage - 1) // API 호출
  } else {
    alert('첫 번째 페이지 입니다.')
  }
}

// 뒤로 1페이지 이동
const next1Page = () => {
  if (movieStore.tr_currentPage < movieStore.tr_totalPages){
    movieStore.getMovieTopRated(movieStore.tr_currentPage + 1)
  } else {
    alert('마지막 페이지 입니다.')
  }
}


// 특정 페이지로 이동
const goToPage = (pageNum) => {
  if (pageNum !== movieStore.tr_currentPage) {
    movieStore.getMovieTopRated(pageNum);
  }
};

// 앞으로 5페이지 이동
const prevPage = () => {
  if (movieStore.tr_currentPage > 1){
    if (movieStore.tr_currentPage - 5 > 1){
      movieStore.getMovieTopRated(movieStore.tr_currentPage - 5) // API 호출
    } else{
      movieStore.tr_currentPage = 1
      movieStore.getMovieTopRated(movieStore.tr_currentPage)
    }
  } else {
    alert('첫 번째 페이지 입니다.')
  }
}

// 뒤로 5페이지 이동
const nextPage = () => {
  if (movieStore.tr_currentPage < movieStore.tr_totalPages){
    if (movieStore.tr_currentPage + 5 < movieStore.tr_totalPages){
      movieStore.getMovieTopRated(movieStore.tr_currentPage + 5)
    } else{
      movieStore.tr_currentPage = movieStore.tr_totalPages
      movieStore.getMovieTopRated(movieStore.tr_currentPage)
    }
  } else {
    alert('마지막 페이지 입니다.')
  }
}

// 페이지 번호 목록 생성
const pageNumbers = computed(() => {
  const pages = [];
  let startPage = movieStore.tr_currentPage - 5
  let endPage = movieStore.tr_currentPage + 5

  // 첫 페이지가 1보다 작은 경우 조정
  if (startPage < 1){
    startPage = 1
    endPage = Math.min(10, movieStore.tr_totalPages)
  }
  
  // 마지막 페이지가 totalPages보다 큰 경우 조정
  if (endPage > movieStore.tr_totalPages){
    endPage = movieStore.tr_totalPages
    endPage = Math.max(1, movieStore.tr_totalPages - 9)
  }
  
  for (let i = startPage; i <= endPage; i++){
    pages.push(i)
  }

  return pages

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

      <!-- 앞 뒤 1페이지씩 이동할 때 -->
      <!-- <div>
        <button @click="prev1Page" :disabled="currentPage === 1">Previous</button>
        <span Page>&nbsp; {{ currentPage }} of {{ totalPages }} &nbsp;</span>
        <button @click="next1Page" :disabled="currentPage === totalPages">Next</button>
      </div> -->

      <!-- 페이지 내비게이션 -->
      <div>
        <button @click="prevPage" :disabled="currentPage === 1"><<</button>&nbsp;
        <button @click="prev1Page" :disabled="currentPage === 1"><</button>&nbsp;
        
        <!-- 페이지 숫자 목록 -->
        <span v-for="pageNum in pageNumbers" :key="pageNum">
          <button
            @click="goToPage(pageNum)"
            :class="{ active: pageNum === currentPage }"
          >
            {{ pageNum }}
          </button>
        </span>

        <span Page>&nbsp; {{ currentPage }} of {{ totalPages }} &nbsp;</span>

        &nbsp;<button @click="next1Page" :disabled="currentPage === totalPages">></button>
        &nbsp;<button @click="nextPage" :disabled="currentPage === totalPages">>></button>
      </div>

    </div>

  </div>
</template>


<style scoped>
.movie-list {
  /* display: flex; -> 요소 가로로 위치 */
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.movie-card {
  /* border: 1px solid #fff; */
  border: 1px none;
  width: 200px;
  padding: 5px;

}

.movie-poster {
  width: 100%;
  height: auto;
}


button:disabled {
  background-color: #ccc;
  
  cursor: not-allowed;
}

button.active {
  background-color: #007bff;
  color: white;
}
</style>
