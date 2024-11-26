<script setup>
import { onMounted, ref, watch } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';
import { useContentStore } from '@/stores/contents';

import { useRoute, useRouter } from 'vue-router';
import { RouterLink } from 'vue-router'

// 날짜 형식 변경
import { format } from 'date-fns'
import { ko } from 'date-fns/locale'

import MovieReviews from '@/components/Movie_tmdb/MovieReviews.vue';

const useStore = useCounterStore()
const movieStore = useMovieStore()
const contentStore = useContentStore()

const route = useRoute()
const router = useRouter()

const movieDetail = ref(null)
const isBookmarked = ref(null)

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

onMounted(() => {
  // console.log("토큰: ", useStore.token)

  axios({
    method: 'get', 
    url: `${movieStore.DB_BASE_URL}/api/v1/movies/${route.params.id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    movieDetail.value = res.data
    checkBookmarkStatus(res.data.movie_detail.tmdb_id);  // 데이터 로딩 후 북마크 상태 확인
  })
  .catch((err) => {
    console.log(err)
  })

})

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return format(date, 'yyyy년 MM월 dd일', { locale: ko }) // 한국 날짜 형식으로 변환
}



// 해당 영화의 북마크 상태 추적
const checkBookmarkStatus = (movieId) => {
  // 북마크 리스트에서 해당 영화 ID가 있는지 확인
  isBookmarked.value = contentStore.bookmarkList.some(movie => movie.tmdb_id === movieId)
}

// 북마크 추가 또는 취소
const toggleBookmark = (movie) => {
  contentStore.addToBookmark(movie); // 북마크 추가
  checkBookmarkStatus(movie.tmdb_id); // 북마크 상태를 갱신
};


</script>


<template>
  <div id="page">
    <h1>Movie Detail</h1>
    
    <div v-if="movieDetail && movieDetail.movie_detail">
      <h1>{{ movieDetail.movie_detail.title }}</h1>
      <div>
        <div>
          <!-- 포스터 이미지 표시 -->
          <img class="img_Poster" :src="movieDetail.movie_detail.poster_url" alt="img_Poster" v-if="movieDetail.movie_detail.poster_url">
        </div>
        
        <div>
          <p>genre : {{ movieDetail.movie_detail.genre }}</p>
          <p>tagline : {{ movieDetail.movie_detail.tagline }}</p>
          <p>overview : {{ movieDetail.movie_detail.overview }}</p>
          
          <!-- 날짜 포맷 변경 -->
          <!-- <p>release_date : {{ formatDate(movieDetail.movie_detail.release_date) }} KST</p> -->
          <p>release_date : {{ movieDetail.movie_detail.release_date ? formatDate(movieDetail.movie_detail.release_date) : 'Loading...' }} KST</p> 
          <p>runtime : {{ movieDetail.movie_detail.runtime }}</p>
          <p>status : {{ movieDetail.movie_detail.status }}</p>
          <p>vote_avg : {{ movieDetail.movie_detail.vote_avg }}</p>
          <p>vote_count : {{ movieDetail.movie_detail.vote_count }}</p>
        </div>
      </div>
    </div>
    
    <div class="btns">
      <div v-if="movieDetail && movieDetail.movie_detail" >
        <button @click="toggleBookmark(movieDetail.movie_detail)" class="bookmark-btn">
          {{ contentStore.isBookmarked(movieDetail.movie_detail.tmdb_id) ? '북마크 취소' : '북마크 추가'}}
        </button>
      </div>
    
      <div v-if="movieDetail && movieDetail.movie_detail">
        <router-link 
          :to="{name: 'DiaryCreateView', query: {movie_db: JSON.stringify(movieDetail.movie_detail)}}" class="bookmark-btn2">
          일기쓰기
        </router-link>
      </div>
    </div>
    
    <br>
    <h1>Reviews</h1>
    <div  v-if="movieDetail && movieDetail.movie_detail" class="review">
      <!-- <MovieReviews :movie_db="JSON.stringify(movieDetail.movie_detail)" /> -->
      <MovieReviews 
        :movie_tmdb_id="movieDetail.movie_detail.tmdb_id"
        :movie_reviews="movieDetail.movie_detail.reviews" 
      />
    </div>
  
    <br>
    <h1>Recommend Movies</h1>
    <div v-if="movieDetail && movieDetail.movie_recommend">
      <div class="content">
        <div class="movie-list">
      <div v-for="movie in movieDetail.movie_recommend">
        <!-- {{ movie }} -->
  
        <div>
          <!-- {{ movie }} -->
          <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.tmdb_id }}">
            <img :src="getPosterUrl(movie.poster_url, 'w300')" alt="Movie Poster" class="movie-poster">
          </RouterLink>
          <p><b>{{ movie.title }}</b></p>
          </div>
        </div>
      </div>
        
  
      </div>
      <!-- <pre>
        {{ movieDetail.movie_recommend }}
      </pre> -->
    </div>

  </div>
</template>


<style scoped>
.btns{
  display: flex;
  justify-content: space-evenly;
  margin-top: 50px;
  margin-bottom: 50px;
}
.img_Poster {
  flex-shrink: 1; 
  width: 400px;
  height: 600px;
  border-radius: 10px;
  justify-content: center;
}

header {
  font-size: 1.6rem;
  font-weight: bold;
  padding-left: 20px;
  padding-bottom: 40px;
}

header2 {
  font-size: 1.6rem;
  font-weight: bold;
  padding-left: 20px;
  padding-top: 120px;
  padding-bottom: 40px;
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
  /* padding-top: 120px; */
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

.bookmark-btn {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  text-decoration-line: none;
}

.bookmark-btn:hover {
  background-color: #0056b3;
}
.bookmark-btn2 {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  margin-left: 150px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  text-decoration: none;
}

.bookmark-btn2:hover {
  background-color: #0056b3;
}
</style>
