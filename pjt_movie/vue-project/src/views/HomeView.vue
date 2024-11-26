<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';
import { RouterLink } from 'vue-router'

import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';
import { useUserStore } from '@/stores/users';
const userStore = useUserStore()

import MoviePopular from '@/components/Movie_tmdb/MoviePopular.vue'
import RcUserDetail from '@/components/Content/RcUserDetail.vue';

const movieStore = useMovieStore()

const top20Movies = ref([])
const randomMovies = ref([])
const movie_backdrop_image = ref([])

onMounted(() => {
  // if (!localStorage.getItem('user')) {
  //   userStore.getUserInfo();
  // }
  userStore.getUserInfo()

  movieStore.getMovies()

  // movieStore.movies_db 에서 상위 40개 영화 자르기
  if (movieStore.movies_db && movieStore.movies_db.length > 0){
    top20Movies.value = getSliceMovies(movieStore.movies_db, 40)
  }
  // console.log(top20Movies.value)
  

  // top20Movies.value 에서 10개 랜덤으로 선택
  if (top20Movies.value && top20Movies.value.length > 0){
    randomMovies.value = getRandomMovies(top20Movies.value, 10)
  }
  // console.log(randomMovies.value)
  startAutoSlide()
})

function getSliceMovies(movies, count) {
  return movies
    .slice(0, count) // 처음 40개 항목을 선택
}

// 랜덤으로 n개 항목을 뽑는 함수
function getRandomMovies(movies, count) {
  // 배열을 섞은 후, 처음 n개 항목을 리턴
  return movies
    .sort(() => Math.random() - 0.5) // movieStore.movies_db 배열 섞기
    .slice(0, count) // 처음 10개 항목을 선택
}


let currentIndex = 0

// 배너 자동 슬라이드 // 캐러셀
function startAutoSlide() {
  setInterval(() => {
    currentIndex = (currentIndex + 1) % randomMovies.value.length
    const slider = document.querySelector('.banner-slider')
    slider.style.transform = `translateX(-${currentIndex * 100}%)`
  }, 8000) // 8초마다 슬라이드
}


// 슬라이드 버튼 이동
function moveSlide(direction){
  if (direction === 'prev'){
    currentIndex = (currentIndex - 1 + randomMovies.value.length) % randomMovies.value.length
  } else if (direction === 'next'){
    currentIndex = (currentIndex + 1) % randomMovies.value.length
  }
  const slider = document.querySelector('.banner-slider')
  slider.style.transform = `translateX(-${currentIndex * 100}%)`
}

</script>


<template>
  <div id="page">

    <!-- <h1>Home</h1> -->
    <div class="bannerSection">

      <!-- Banner Section -->
      <section class="banner">

        <!-- 슬라이더 이미지 동적 생성 -->
        <div class="banner-slider">
          <img 
            v-for="(movie, index) in randomMovies"
            :key="movie.tmdb_id"
            :src="movie.backdrop_url"
            :alt="'Banner' + (index + 1)"
            class="banner-image"
          />
        </div>


        <!-- 슬라이드 수동 이동 버튼 -->
        <button @click="moveSlide('prev')" class="prev-button"> < </button>
        <button @click="moveSlide('next')" class="next-button"> > </button>
      </section>
    </div>

    <MoviePopular/>

    <RcUserDetail/> 
    

  </div>
</template>


<style scoped>
.bannerSection {
  padding-bottom: 30px;
}

.banner {
  display: grid;
  place-content: center;
  width: 100%;
  height: 530px;
  border-radius: 10px;
  overflow: hidden; /* 슬라이더 영역 밖으로 나가지 않도록 */
}

.banner-slider {
  display: flex; /* 이미지들을 가로로 배열 */
  transition: transform 0.5s ease; /* 슬라이드 효과 */
}

.banner-image {
  width: 100%; /* 배너 이미지를 화면 전체 너비로 맞춤 */
  height: 100%; /* 배너 높이에 맞게 이미지 크기 맞춤 */
  /* object-fit: cover; 이미지가 비율을 맞춰서 잘리도록 */
  object-fit: scale-down;
}

/* 버튼 스타일 */
.prev-button,
.next-button {
  position: absolute;
  top: 430px;
  transform: translateY(50%);
  background-color: rgba(0, 0, 0, 0);
  color: white;
  border: none;
  font-size: 1.5rem;
  padding: 10px;
  cursor: pointer;
  z-index: 10;
}

.prev-button {
  left: 10px;
}

.next-button {
  right: 10px;
}

</style>
