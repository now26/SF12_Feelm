<script setup>
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import axios from 'axios';
import { onMounted, ref } from 'vue'

import { useRoute, useRouter } from 'vue-router';
const route = useRoute()
const router = useRouter()

// const articledetail = ref([])
const diaryDetail = ref(null)
const diary_id = route.params.diary_id
console.log(diary_id)

onMounted(() => {

  axios({
    method: 'get',
    url: `${useStore.API_URL}/accounts/mypage/diary/${diary_id}/`,
    headers: {
        Authorization: `Bearer ${useStore.token}` 
    }
  })
  .then((res) => {
    diaryDetail.value = res.data
    // console.log(res.data)
  })
  .catch((err) => {console.log(err)})
})

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
    router.push({name : 'DiaryView'})
  })
  .catch((err) => {
    console.log(err)
  })
}


</script>


<template>
  <div>
    <h1>Diary Detail View</h1>
    <div v-if="diaryDetail !== null">
      <p>게시글 번호 : {{ diaryDetail.id }}</p>
      <p>제목 : {{ diaryDetail.title }}</p>
      <p>내용 : {{ diaryDetail.content }}</p>
      <p>작성일 : {{ diaryDetail.created_at }}</p>
      <p>수정일 : {{ diaryDetail.updated_at }}</p>
    </div>
  </div>
  <button @click.prevent="deleteDiary(diary_id)">일기 삭제</button>
  <router-link :to="{name : 'DiaryUpdateView', params : { diary_id : diary_id}}" >일기 수정</router-link>
</template>


<style scoped>

</style>
