<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useContentStore } from '@/stores/contents'
import { useCounterStore } from '@/stores/counter';
import RcUserBM from './RcUserBM.vue';
import RcUserRT from './RcUserRT.vue';

const useStore = useCounterStore()

// Pinia store에서 상태와 함수를 가져오기.
const contentStore = useContentStore()
const DB_BASE_URL = 'http://127.0.0.1:8000'

// 데이터를 저장할 배열 선언
const rc_bookmark_movies = ref([])
const rc_review_movies = ref([])

// 컴포넌트가 마운트될 때 영화 목록을 불러오기.
onMounted(async () => {
  try {
    // API 요청을 보내고, 응답 받은 데이터 바로 배열에 할당
    const response = await axios({
      method: 'get',
      url: `${DB_BASE_URL}/accounts/mypage/recom/`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${useStore.token}`,
      },
    });

    console.log("API response:", response.data);  // 응답을 확인

    // 응답 받은 데이터를 배열에 바로 할당
    rc_bookmark_movies.value = response.data?.bookmark_reccomendations || []
    rc_review_movies.value = response.data?.review_recommendations || []

  } catch (err) {
    console.error('Error fetching recommendations:', err)
  }
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
  <div id="page">
    <header>
      <!-- <p>Content Based</p> -->
    </header>
    <div class="tmdb-container">
      <div>
        <RouterLink :to="{ name:'RcContDetailView' }" class="detail"> Detail </RouterLink>
      </div>
      
      <!-- 로딩 상태 처리 -->
      <div v-if="isLoading">
        <p>Loading...</p>
      </div>
      
      <!-- <h1>RcUserBookMark</h1> -->
      <header>
        북마크 기반의 영화 추천
      </header>
      <div class="content">
        <!-- 북마크 추천 영화 목록 -->
        <div v-if="!isLoading && rc_bookmark_movies.length > 0">
          <div class="movie-list">
            <RcUserBM 
                v-for="movie in rc_bookmark_movies"
                :key="movie.tmdb_id"
                :movie="movie"
                class="movie-card"
            />
          </div>
        </div>
        
        <!-- 북마크 추천 영화가 없을 경우 -->
        <div v-else-if="!isLoading && rc_bookmark_movies.length === 0">
          <p>No Bookmark Movies</p>
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
  padding-bottom: 40px;
}

header2 {
  font-size: 1.6rem;
  font-weight: bold;
  padding-left: 20px;
  /* padding-top: 120px; */
  /* padding-bottom: 40px; */
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
  /* padding-bottom: 10px; */
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
  /* padding-bottom: 100px; */
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
