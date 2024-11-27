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
      url: `${DB_BASE_URL}/accounts/mypage/recom2/`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${useStore.token}`,
      },
    });

    console.log("API response:", response.data);  // 응답을 확인

    // 응답 받은 데이터를 배열에 바로 할당
    rc_bookmark_movies.value = response.data || []
    rc_review_movies.value = response.data || []

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
      <!-- <div>
        <RouterLink :to="{ name:'RcUserDetailView' }" class="detail"> Detail </RouterLink>
      </div> -->
      
      <!-- 로딩 상태 처리 -->
      <div v-if="isLoading">
        <p>Loading...</p>
      </div>

        <header>
          리뷰 기반의 영화 추천
        </header>
        <div class="content"></div>
        <!-- 리뷰 추천 영화 목록 -->
        <div v-if="!isLoading && rc_review_movies.length > 0">
          <div class="movie-list">
            <RcUserRT 
                v-for="movie in rc_review_movies"
                :key="movie.tmdb_id"
                :movie="movie"
                class="movie-card"
            />
            </div>
        </div>

        <!-- 리뷰 추천 영화가 없을 경우 -->
        <div v-else-if="!isLoading && rc_review_movies.length === 0">
          <p>No Review Movies</p>
        </div>
      </div>
    </div>

</template>


<style scoped>
header {
  display: flex;
  justify-content: center;
  font-size: 1.6rem;
  font-weight: bold;
  padding-left: 20px;
  padding-bottom: 40px;
}

h1 {
  font-weight: bold;
  font-size: 2.5rem;
  padding-bottom: 50px;
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

</style>
