<script setup>
import { defineEmits } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { useContentStore } from '@/stores/contents';

const emit = defineEmits()
const useStore = useCounterStore()
const contentStore = useContentStore()

defineProps({
  diary:Object
})

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
}

const deleteDiary = (diary_id) => {
  console.log('일기삭제 버튼') // 디버깅

  axios({
    method: 'delete',
    url: `${useStore.API_URL}/accounts/mypage/diary/${diary_id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    console.log(res, '일기삭제 성공')
    alert('일기삭제 성공')
    emit('deleteDiary', diary_id)
  })
  .catch((err) => {
    console.log(err)
  })
}


</script>


<template>
  <div>
    <ul>
      <!-- {{ diary }} -->
      <!-- <RouterLink :to="{ name: 'MovieDetailView', params:{ id: diary.movie.tmdb_id }}"> -->
        <img :src="getPosterUrl(diary.movie.poster_path, 'w300')" alt="poster_img">
      <!-- </RouterLink> -->
      <p>Movie : {{ diary.movie.title }}</p>
      <p>Contents : {{ diary.content }}</p>
      <!-- <p>Ratings : {{ diary.rating }}</p> -->
      <button @click.prevent="deleteDiary(diary.id)" class="btn">일기 삭제</button>
      <router-link :to="{name : 'DiaryUpdateView', params : { diary_id : diary.id}}" class="btn" >일기 수정</router-link>
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
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 10px;
}

.btn:hover {
  background-color: #0056b3;
}
</style>
