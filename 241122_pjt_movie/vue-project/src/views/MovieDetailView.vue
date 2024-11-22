<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
import { useMovieStore } from '@/stores/movies';

import { useRoute } from 'vue-router';

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
    console.log(res.data)
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
  <div v-if="movieDetail !== null">
    <!-- <h1>Movie Detail</h1> -->
    <h1>{{ movieDetail.title }}</h1>
    <div>
      <div>
        <!-- 포스터 이미지 표시 -->
        <img class="img_Poster" :src="movieDetail.poster_url" alt="img_Poster" v-if="movieDetail.poster_url">
      </div>
  
      <div>
        <p>genre : {{  movieDetail.genre }}</p>
        <p>tagline : {{ movieDetail.tagline }}</p>
        <p>overview : {{ movieDetail.overview }}</p>

        <!-- 날짜 포맷 변경 -->
        <!-- <p>release_date : {{ formateDate(movieDetail.release_date) }} KST</p> -->
        <p>release_date : {{ movieDetail.release_date ? formateDate(movieDetail.release_date) : 'Loading...' }} KST</p> 
        <p>runtime : {{ movieDetail.runtime }}</p>
        <p>status : {{ movieDetail.status }}</p>
        <p>vote_avg : {{ movieDetail.vote_avg }}</p>
        <p>vote_count : {{ movieDetail.vote_count }}</p>
        <p>review : {{ movieDetail.reviews }}</p>
        <!-- <p>{{ movie.poster_url }}</p>
        <p>{{ movie.backdrop_url }}</p> -->
      </div>

    </div>
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
