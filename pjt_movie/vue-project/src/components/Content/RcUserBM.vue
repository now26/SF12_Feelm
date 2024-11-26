<script setup>

import MovieDetailView from '@/views/MovieDetailView.vue';
defineProps({
    movie:Object
})

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
}

const getBackDrop = (backDropPath, imageSize) => {
  if (backDropPath) {
    return `${BASE_IMAGE_URL}${imageSize}${backDropPath}`
  }
}

</script>



<template>
  <div>
    <!-- <header>
        <h1>
            RcUserBookMark
        </h1>
    </header> -->
    <!-- <div>
      <MovieDetailView />
    </div> -->

    <div>
        <!-- {{ movie }} -->
        <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.tmdb_id }}">
        <img :src="getPosterUrl(movie.poster_url, 'w300')" alt="Movie Poster" class="movie-poster">
        </RouterLink>
        <p><b>{{ movie.title }}</b></p>
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
