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
import RcDetailView from './RcDetailView.vue';

const useStore = useCounterStore()
const movieStore = useMovieStore()
const contentStore = useContentStore()

const route = useRoute()
const router = useRouter()

const movieDetail = ref(null)
const isBookmarked = ref(null)

onMounted(() => {
  // console.log("토큰: ", useStore.token)

  axios({
    method: 'get', 
    // url: `${movieStore.DB_BASE_URL}/api/v1/movies/${route.params.id}/`,
    url: `${movieStore.DB_BASE_URL}/api/v1/movies/1184918/`,
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
  <h1>Recommend Movies</h1>
  <div class="tmdb-container">      
      <div>
        <RouterLink :to="{ name:'MoviePopularDetailView' }" class="detail"> Detail </RouterLink>
      </div>

      <div class="content">
        <div v-if="movieDetail.movie_detail">
          <div class="movie-list">
            <div 
              v-for="movie in movies"
              :key="movie.id"
              class="movie-card"
            >
              <RouterLink :to="{ name: 'MovieDetailView', params:{ id: movie.tmdb_id }}">
                <img :src="getPosterUrl(movie.poster_url, 'w300')" alt="Movie Poster" class="movie-poster">
              </RouterLink>
              <p><b>{{ movie.title }}</b></p>
    
            </div>
          </div>
        </div>
  
        <div v-else>
          <p>No Movies</p>
        </div>

    </div>
</div>
  <!-- <div v-if="movieDetail && movieDetail.movie_recommend">
    <RcDetailView
        v-for="movie in movieDetail.movie_recommend"
        :key="movie.tmdb_id"
        :movie="movie"
    ></RcDetailView> -->
    <!-- <pre>
      {{ movieDetail.movie_recommend }}
    </pre> -->

</template>


<style scoped>
.img_Poster {
  /* max-width: 100%;  이미지가 화면을 넘어가지 않도록 */
  min-width: 150px;
  max-width: 20%;
  height: auto;  /* 비율을 유지하면서 높이 자동 조정 */
}
</style>
