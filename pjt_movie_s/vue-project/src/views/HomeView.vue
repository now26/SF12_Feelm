<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';

const movieStore = useMovieStore()

const top20Movies = ref([])
const randomMovies = ref([])
const movie_backdrop_image = ref([])

onMounted(() => {
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
    .slice(0, count) // 처음 20개 항목을 선택
}

// 랜덤으로 n개 항목을 뽑는 함수
function getRandomMovies(movies, count) {
  // 배열을 섞은 후, 처음 n개 항목을 리턴
  return movies
    .sort(() => Math.random() - 0.5) // movieStore.movies_db 배열 섞기
    .slice(0, count) // 처음 10개 항목을 선택
}

// 배너 자동 슬라이드
let currentIndex = 0

function startAutoSlide() {
  setInterval(() => {
    currentIndex = (currentIndex + 1) % randomMovies.value.length
    const slider = document.querySelector('.banner-slider')
    slider.style.transform = `translateX(-${currentIndex * 100}%)`
  }, 5000) // 5초마다 슬라이드
}

// 슬라이드 버튼 이동
function moveSlide(direction){
  if (direction === 'prev'){
    currentIndex = (currentIndex - 1 + randomMovies.value.length) % randomMovies.value.length
  } else if (direction === 'next'){
    currentIndex = (currentIndex + 1) % randomMovies.value.length
  }
  const slider = document.querySelector('.banner-slider')
  slider.style.transform = `translate(-${currentIndex * 100}%)`
}


</script>


<template>
  <div>
    <!-- <h1>Home</h1> -->
    <div>
      <!-- Banner Section -->
      <section class="banner">
        <div class="banner-slider">
          <!-- 슬라이더 이미지 동적 생성 -->
          <img 
            v-for="(movie, index) in randomMovies"
            :key="movie.id"
            :src="movie.backdrop_url"
            :alt="'Banner' + (index + 1)"
            class="banner-image"
          />
        </div>
      </section>
  
      <!-- 슬라이드 수동 이동 버튼 -->
      <button @click="moveSlide('prev')" class="prev-button"> < </button>
      <button @click="moveSlide('next')" class="next-button"> > </button>
    </div>

    <div>
      Top 20 영화
    </div>

    <div>
      if - 로그인 시,
      사용자 정보 기반 추천 영화
    </div>

    <div>
      if - 로그인 시,
      사용자 정보 기반 북마크 영화
    </div>

    <div>
      <hr>
      메뉴바 구성
      - Home (배너와 영화 상세 정보 페이지 연결)
      - Movie (장르 기반 필터링 기능 구현, 영화 카드 디자인, 페이지네이션 기능)
      - BookMarks (Mypage 내부 Bookmark 상세 페이지 연결)
      - Review (Mypage 내부 review 상세 페이지 연결)
      
      - (가능하면 영화 검색 기능 구현)
      - Mypage (각 세부페이지 들어가기)
      - Logout
    </div>
    
    <div>
      <hr>
      - 영화 추천 detail 페이지 구현
      - vue에서 생성한 user가 db에서 보이지 않는 에러 해결 필요
    </div>



  </div>
</template>


<style scoped>
.banner {
  display: grid;
  place-content: center;
  width: 100%;
  height: 530px;
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
  top: 50%;
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
