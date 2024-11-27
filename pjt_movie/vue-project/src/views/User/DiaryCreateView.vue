<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'

import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import { useUserStore } from '@/stores/users';
const userStore = useUserStore()

const router = useRouter()

// Review를 작성할 영화 DB 받아오기
const route = useRoute()
const movieDB = JSON.parse(route.query.movie_db || '{}')

// content는 문자열로, rating은 숫자나 문자열로 초기화
const title = ref('')
const content = ref('')

const diary_id = ref(0)

const tmdb_id = movieDB.tmdb_id

// console.log(typeof movieDB.tmdb_id)


const createDiary = () => {
    
  // 평점과 내용이 모두 입력되었는지 확인
  if (!title.value || !content.value) {
    alert('제목과 내용을 모두 입력해주세요');
    return;
  }

  axios({
      method: 'post',
      url: `${userStore.DB_BASE_URL}/accounts/mypage/diary/`,
      data: {
          tmdb_id: tmdb_id,
          title: title.value,
          content: content.value,
      },
      headers: {
          Authorization: `Bearer ${useStore.token}`
      }
  })
  .then((res) => {
    if (res.data && res.data.id) {
      diary_id.value = res.data.id; // 생성된 다이어리 ID 설정
      router.push({ name: 'DiaryDetailView', params: { diary_id: diary_id.value } }) // 다이어리 상세 페이지로 이동
    }
  })
  .catch((err) => {
    // 에러 발생 시 사용자에게 알림
    console.error('다이어리 생성 오류:', err)
    alert('다이어리 생성에 실패했습니다. 다시 시도해주세요.')
  })
}
</script>



<template>
  
  <div id="page">
    <h1>DiaryCreateView</h1>
    
      <div>
        <form @submit.prevent="createDiary">
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


    <br><hr><br>
<!-- 
    Movie DB : 
    <pre>
        {{ movieDB }}
    </pre> -->
    </div>

  </div>
</template>



<style scoped>


</style>