<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';

import { useRoute } from 'vue-router';
import { RouterLink } from 'vue-router'

// 날짜 형식 변경
import { format } from 'date-fns'
import { ko } from 'date-fns/locale'

const useStore = useCounterStore()
const movieStore = useMovieStore()
const route = useRoute()

const movieDetail = ref('')

onMounted(() => {
  // console.log("토큰: ", useStore.token)

  axios({
    method: 'get', 
    url: `${movieStore.DB_BASE_URL}/api/v1/movies/${route.params.id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`
    }
  })
  .then((res) => {
    movieDetail.value = res.data
    // console.log(res.data.movie_detail)
  })
  .catch((err) => {
    console.log(err)
  })
})

const formateDate = (dateString) => {
  const date = new Date(dateString)
  return format(date, 'yyyy년 MM월 dd일', { locale: ko }) // 한국 날짜 형식으로 변환
}

</script>


<template>
  <!-- 
  <pre>
    {{ movieDetail }}
  </pre> 
  -->
 
  <!-- {{ movieDetail }} -->
  <!-- {{ movieDetail !== null }} -->
  <!-- {{ movieDetail.movie_recommend }} -->

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
        <!-- <p>release_date : {{ formateDate(movieDetail.movie_detail.release_date) }} KST</p> -->
        <p>release_date : {{ movieDetail.movie_detail.release_date ? formateDate(movieDetail.movie_detail.release_date) : 'Loading...' }} KST</p> 
        <p>runtime : {{ movieDetail.movie_detail.runtime }}</p>
        <p>status : {{ movieDetail.movie_detail.status }}</p>
        <p>vote_avg : {{ movieDetail.movie_detail.vote_avg }}</p>
        <p>vote_count : {{ movieDetail.movie_detail.vote_count }}</p>
      </div>
    </div>
  </div>

  <br>
  <h1>Reviews</h1>
  <div  v-if="movieDetail && movieDetail.movie_detail">
    <div>
      <router-link 
        :to="{name: 'ReviewCreateView', query: {movie_db: JSON.stringify(movieDetail.movie_detail)}}">
        Create
      </router-link>
    </div>

    <p>review : 
      <pre>
        {{ movieDetail.movie_detail.reviews }}
      </pre>
    </p>
  </div>

  <br>
  <h1>Recommend Movies</h1>
  <div v-if="movieDetail && movieDetail.movie_recommend">
    <pre>
      {{ movieDetail.movie_recommend }}
    </pre>
  </div>
</template>


<style scoped>
.img_Poster {
  /* max-width: 100%;  이미지가 화면을 넘어가지 않도록 */
  min-width: 150px;
  max-width: 20%;
  height: auto;  /* 비율을 유지하면서 높이 자동 조정 */
}
</style>
