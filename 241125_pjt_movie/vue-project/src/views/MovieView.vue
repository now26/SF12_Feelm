<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movies';
import { onBeforeRouteLeave } from 'vue-router'
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router';
import MovieList from '@/components/MovieList.vue'

const movieStore = useMovieStore()
const selectedGenre = ref(null)

onMounted(() => {
  movieStore.setSelectedGenre(selectedGenre.value)
  movieStore.getMovies()
  movieStore.getGenres()
})

onBeforeRouteLeave((to, from, next) => {
  selectedGenre.value = null
  next()
})

// console.log(selectedGenre.value)

const handleGenreChange = (event) => {
  selectedGenre.value = event.target.value;
}

const handleSearch = () => {
  movieStore.setSelectedGenre(selectedGenre.value); // 선택된 장르를 Pinia 상태에 저장
  movieStore.getMovies(); // 필터링된 영화 목록을 가져오기
}

// 페이지 변경 함수
const changePage = (pageNum) => {
  if (pageNum < 1 || pageNum > movieStore.db_totalPages) return; // 유효하지 않은 페이지 번호는 무시
  movieStore.changePage(pageNum); // 새로운 페이지 번호로 영화 목록 가져오기
}

</script>


<template>
  <header>
    <h1>Movies</h1>
  </header>

  <div class="selectForm">
    <label for="genre" class="selectTxt">Select Genre :</label>&nbsp;
    <select id="genre" v-model="selectedGenre" @change="handleGenreChange" class="inputItem">
      <option value="">All</option>
      <option v-for="genre in movieStore.genres" :key="genre.id" :value="genre.name">{{ genre.name }}</option>
    </select>&nbsp;
    <button @click="handleSearch" class="btn">검색</button>
  </div>

  <div id="page">
    <!-- <MovieList /> -->

    <!-- 현재 페이지에 맞는 영화 목록을 MovieList로 전달 -->
    <MovieList :movies="movieStore.getMoviesForCurrentPage()" />
  </div>


  <!-- 페이지네이션 버튼 -->
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


</template>


<style scoped>
header {
  display: flex;
  justify-content: center;
}

h1 {
  font-weight: bold;
  font-size: 2.5rem;
}

.selectForm {
  padding-top: 50px;
  padding-bottom: 20px;
  display: flex;
  justify-content: flex-end;
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
  width: 50px;
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

</style>
