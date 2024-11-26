<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue';
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import { useUserStore } from '@/stores/users';
const userStore = useUserStore()

const router = useRouter()

// Review를 작성할 영화 DB 받아오기
const route = useRoute()
// const movieDB = JSON.parse(route.query.movie_db || '{}')

// content는 문자열로, rating은 숫자나 문자열로 초기화
const title = ref('')
const content = ref('')
const diary_id = ref(0)

// console.log(typeof movieDB.tmdb_id)

// 다이어리 데이터를 받아오는 함수
const fetchDiaryData = () => {
  axios({
    method: 'get',
    url: `${useStore.API_URL}/accounts/mypage/diary/${route.params.diary_id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    const diary = res.data
    title.value = diary.title
    content.value = diary.content
    diary_id.value = diary.id
  })
  .catch((err) => {
    console.log(err)
  })
}

const updateDiary = () => {
  console.log('일기수정 버튼') // 디버깅

  axios({
    method: 'put',
    url: `${useStore.API_URL}/accounts/mypage/diary/${route.params.diary_id}/`,
    data: {
        title: title.value,
        content: content.value,
    },
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    if (res.data && res.data.id) {
      diary_id.value = res.data.id; // 생성된 다이어리 ID 설정

      title.value = res.data.title
      content.value = res.data.content

      router.push({ name: 'DiaryDetailView', params: { diary_id: diary_id.value } }) // 다이어리 상세 페이지로 이동
    }
  })
  .catch((err) => {
    console.log(err)
  })
}

// 페이지가 마운트되면 기존 다이어리 데이터를 로드
onMounted(() => {
  fetchDiaryData()
})

</script>



<template>
  
  <div id="page">
    <h1>Diary Update View</h1>
    
      <div>
        <form @submit.prevent="updateDiary">
          <div>
            <label for="title">Title</label>
            <input type="text"
              id="title"
              v-model.trim="title"
            >
          </div>

          <div>
            <label for="content">Content</label>
            <textarea
              id="content"
              v-model.trim="content"
              placeholder="리뷰를 작성해주세요..."
            >
            </textarea>
          </div>

          <button type="submit">submit</button>
        </form>
    </div>

  </div>
</template>



<style scoped>


</style>