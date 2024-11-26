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
const content = ref('')
const rating = ref(0)
const movie = movieDB

// console.log(typeof movieDB.tmdb_id)

// 평점 옵션 (0.0부터 5.0까지)
// const ratingOptions = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
const ratingOptions = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

const createReview = () => {
    
  // 평점과 내용이 모두 입력되었는지 확인
  if (!rating || !content.value) {
    alert('평점과 내용을 모두 입력해주세요');
    return;
  }

  // rating을 명시적으로 숫자로 변환
  const ratingValue = parseFloat(rating.value.toFixed(1));  // 숫자로 변환  
  // console.log(ratingValue)
  // console.log(typeof ratingValue)

  axios({
      method: 'post',
      url: `${userStore.DB_BASE_URL}/api/v1/movies/${movieDB.tmdb_id}/`,
      data: {
          // movie: movie,
          content: content.value,
          // rating: parseFloat(rating.value) // 실수형으로 변환
          rating: ratingValue
      },
      headers: {
          Authorization: `Bearer ${useStore.token}`
      }
  })
  .then((res) => {
      console.log(res)
      // router.push({name : 'ReviewDetailView'}) //DetailView 보내는 건 고민해보기 (ReviewList 라도)
  })
  .catch((err) => {
      console.log(err)
  })
}


</script>



<template>
  
  <div id="page">
    <h1>ReviewCreateView</h1>
    
      <div>
        <form @submit.prevent="createReview">
          <div>
            <label for="content">Content</label>
            <textarea
              id="content"
              v-model.trim="content"
              placeholder="리뷰를 작성해주세요..."
            >
            </textarea>
          </div>

          <div>
            <label for="rating">Rating</label>
            <select id="rating" v-model="rating">
              <option v-for="option in ratingOptions" :key="option" :value="option">
                {{ option }}
              </option>
            </select>
          </div>

          <!-- <div>
            <p>선택한 평점: {{ rating }}</p>
          </div> -->

          <button type="submit">submit</button>
        </form>


    <br><hr><br>

    Movie DB : 
    <pre>
        {{ movieDB }}
    </pre>
    </div>

  </div>
</template>



<style scoped>


</style>