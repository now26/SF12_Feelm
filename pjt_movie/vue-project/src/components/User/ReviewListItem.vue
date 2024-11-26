<script setup>
import { defineEmits } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const emit = defineEmits()
const useStore = useCounterStore()

defineProps({
  review:Object
})

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
}

const deleteReview = (tmdb_id, review_id) => {
  console.log('리뷰삭제 버튼') // 디버깅

  axios({
    method: 'delete',
    url: `${useStore.API_URL}/api/v1/movies/${tmdb_id}/${review_id}`,
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    console.log(res, '리뷰삭제 성공')
    alert('리뷰삭제 성공')
    emit('deleteReview', review_id)
  })
  .catch((err) => {
    console.log(err)
  })
}

</script>


<template>
  <div>
    <ul>
      <!-- {{ review }} -->
      <RouterLink :to="{ name: 'MovieDetailView', params:{ id: review.movie.tmdb_id }}">
        <img :src="getPosterUrl(review.movie.poster_path, 'w300')" alt="poster_img">
      </RouterLink>
      <p>Movie : {{ review.movie.title }}</p>
      <p>Contents : {{ review.content }}</p>
      <p>Ratings : {{ review.rating }}</p>
      <button @click.prevent="deleteReview(review.movie.tmdb_id, review.id)" class="btn">리뷰 삭제</button>
      <button class="btn">좋아요</button>
    </ul>
    <hr>
  </div>
</template>


<style scoped>

.btn {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  text-decoration-line: none;
  margin-left: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.btn:hover {
  background-color: #0056b3;
}
</style>
