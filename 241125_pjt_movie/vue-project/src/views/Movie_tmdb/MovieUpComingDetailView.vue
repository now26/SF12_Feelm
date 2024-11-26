<script setup>
import { ref, computed } from 'vue'
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movies';

// Pinia store에서 상태와 함수를 가져오기.
const movieStore = useMovieStore()

// 날짜 선택 부분
const startDate = ref('')
const endDate = ref('')

const sendDateRange = () => {
  movieStore.getMovieUpComing(1, startDate.value, endDate.value)
}

const resetRange = () => {
  startDate.value = null
  endDate.value = null
  movieStore.getMovieUpComing(1)
}

// 날짜를 'YYYY-MM-DD' 형식으로 변환
const formatDate = (date) => {
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const day = date.getDate().toString().padStart(2, '0')

  // console.log(`${year}-${month}-${day}`)
  return `${year}-${month}-${day}`
}

// 컴포넌트가 마운트될 때 영화 목록을 불러오기.
onMounted(() => {
  const today = new Date()
  const nearFuture = new Date(today)
  const future = new Date(today)
  nearFuture.setDate(today.getDate() + 7) // 7일 후
  future.setMonth(today.getMonth() + 1)

  // 날짜를 'YYYY-MM-DD' 형식으로 변환
  startDate.value = formatDate(nearFuture)
  endDate.value = formatDate(future)

  movieStore.getMovieUpComing(movieStore.up_currentPage)
})



// 페이지 이동 ========================================

// 앞으로 1페이지 이동
const prev1Page = () => {
  if (movieStore.up_currentPage > 1){
    movieStore.getMovieUpComing(movieStore.up_currentPage - 1) // API 호출
  } else {
    alert('첫 번째 페이지 입니다.')
  }
}

// 뒤로 1페이지 이동
const next1Page = () => {
  if (movieStore.up_currentPage < movieStore.up_totalPages){
    movieStore.getMovieUpComing(movieStore.up_currentPage + 1)
  } else {
    alert('마지막 페이지 입니다.')
  }
}


// 특정 페이지로 이동
const goToPage = (pageNum) => {
  if (pageNum !== movieStore.up_currentPage) {
    movieStore.getMovieUpComing(pageNum);
  }
};

// 앞으로 5페이지 이동
const prevPage = () => {
  if (movieStore.up_currentPage > 1){
    if (movieStore.up_currentPage - 5 > 1){
      movieStore.getMovieUpComing(movieStore.up_currentPage - 5) // API 호출
    } else{
      movieStore.up_currentPage = 1
      movieStore.getMovieUpComing(movieStore.up_currentPage)
    }
  } else {
    alert('첫 번째 페이지 입니다.')
  }
}

// 뒤로 5페이지 이동
const nextPage = () => {
  if (movieStore.up_currentPage < movieStore.up_totalPages){
    if (movieStore.up_currentPage + 5 < movieStore.up_totalPages){
      movieStore.getMovieUpComing(movieStore.up_currentPage + 5)
    } else{
      movieStore.up_currentPage = movieStore.up_totalPages
      movieStore.getMovieUpComing(movieStore.up_currentPage)
    }
  } else {
    alert('마지막 페이지 입니다.')
  }
}

// 페이지 번호 목록 생성
const pageNumbers = computed(() => {
  const pages = [];
  let startPage = movieStore.up_currentPage - 5
  let endPage = movieStore.up_currentPage + 5

  // 첫 페이지가 1보다 작은 경우 조정
  if (startPage < 1){
    startPage = 1
    endPage = Math.min(10, movieStore.up_totalPages)
  }
  
  // 마지막 페이지가 totalPages보다 큰 경우 조정
  if (endPage > movieStore.up_totalPages){
    endPage = movieStore.up_totalPages
    endPage = Math.max(1, movieStore.up_totalPages - 9)
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

const movies = computed(() => movieStore.movie_upComing)
const currentPage = computed(() => movieStore.up_currentPage)
const totalPages = computed(() => movieStore.up_totalPages)
// console.log(movies)



</script>


<template>
  <div>
    <header>
      <h1>Upcoming Movies</h1>
    </header>

    <div id="page">
      
      <div class="selectForm">
        <span class="selectTxt">검색기간 </span>&nbsp;&nbsp;
        <input type="date" id="startDate" v-model="startDate" class="inputItem">&nbsp;
        <label for="startDate" class="selectTxt">~</label>&nbsp;
  
        <input type="date" id="endDate" v-model="endDate" class="inputItem">&nbsp;
        <label for="endDate"></label>
        <button @click.prevent="sendDateRange" class="btn">검색</button>&nbsp;
        <button @click.prevent="resetRange" class="btn">초기화</button>
      </div>
  
  
      <div>
        <div v-if="movies.length !== null">
          <div class="movie-list">
            <div 
              v-for="movie in movies"
              :key="movie.id"
              class="movie-card"
            >
            <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.id }}">
              <img :src="getPosterUrl(movie.poster_path, 'w300')" alt="Movie Poster" class="movie-poster">
            </RouterLink>
            <p class="movieInfo"><b>{{ movie.title }}</b></p>
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
        <div class="pageCnt">
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

  </div>
</template>


<style scoped>
header {
  display: flex;
  justify-content: center;
}

h1 {
  font-weight: bold;
  font-size: 2.5rem;
  padding-bottom: 20px;
}

.selectForm {
  padding-top: 50px;
  padding-right: 120px;
  padding-bottom: 20px;
  display: flex;
  justify-content: flex-end;
  gap: 3px;
}

.selectTxt {
  font-size: 1.2rem;
}

.inputItem{
  padding: 5px;
  font-size: 1rem;
  border: 1px solid #333;
  border-radius: 5px; 
}

.btn {
  width: auto;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 15px;
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3;
}

.movie-list {
  /* display: flex; -> 요소 가로로 위치 */
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-left: 1rem;
  justify-content: center;
}

.movie-card {
  /* border: 1px solid #fff; */
  border: 1px none;
  padding: 5px;

}

.movie-poster {
  flex-shrink: 1;
  width: 200px;
  height: 300px;
  border-radius: 10px;

}

.movieInfo {
  width: 200px;
  white-space: normal;
  display: flex;
  justify-content: center;
}

.pageCnt {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  padding-top: 20px;
  gap: 2px;
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
