<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'
import MovieReviewsList from './MovieReviewsList.vue';

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
      url: `${userStore.DB_BASE_URL}/api/v1/movies/${props.movie_tmdb_id}/`,
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
      userDB.reviews.push(res.data)
      
      content.value = '' // 입력 필드 초기화
      rating.value = 0   // 평점 초기화
      // router.push({name : 'ReviewDetailView'}) //DetailView 보내는 건 고민해보기 (ReviewList 라도)
      loadReviews()
  })
  .catch((err) => {
      console.log(err)
  })
}

// const userStore = useUserStore()
const userDB = userStore.userInfo

const props = defineProps({
  movie_reviews : Array,
  movie_tmdb_id : Number
})

// 로컬에 리뷰 리스트를 복사해서 사용
const reviews = ref([...userDB.reviews])

// 삭제된 리뷰 처리 함수
const handleDeleteReview = (review_id) => {
  axios({
    method: 'delete',
    url: `${userStore.DB_BASE_URL}/api/v1/movies/${props.movie_tmdb_id}/${review_id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`,
    }
  })
  .then((res) => {
    console.log(res, '리뷰삭제 성공')
    alert('리뷰 삭제 성공')

    // 서버에서 최신 리뷰 목록을 가져와서 갱신
    loadReviews()

  })
  .catch((err) => {
    console.log(err)
  })
}

// 리뷰 목록을 서버에서 가져오는 함수
const loadReviews = () => {
  axios({
    method: 'get',
    url: `${userStore.DB_BASE_URL}/api/v1/movies/${props.movie_tmdb_id}/`,
    headers: {
      Authorization: `Bearer ${useStore.token}`
    }
  })
  .then((res) => {
    reviews.value = res.data.movie_detail.reviews || []  // 최신 리뷰 목록 반영
    userDB.reviews = res.data.movie_detail.reviews  // 서버에서 받은 최신 리뷰 목록 업데이트
  })
  .catch((err) => {
    console.error(err)
  })
}


</script>



<template>
  
  <div id="page">
    <h2>MovieReviews</h2>
    
      <div>
        <form @submit.prevent="createReview" class="form">
          <div class="list">
            <label for="content" id="cd" >Content</label>
            <textarea
              id="content"
              v-model.trim="content"
              placeholder="리뷰를 작성해주세요..."
            >
            </textarea>
          </div>

          <div  class="list">
            <label for="rating" id="button">Rating</label>
            <select id="rating" v-model="rating">
              <option v-for="option in ratingOptions" :key="option" :value="option">
                {{ option }}
              </option>
            </select>
          </div>

          <!-- <div>
            <p>선택한 평점: {{ rating }}</p>
          </div> -->

          <button type="submit" class="list" id="button">submit</button>
        </form>
      </div>

    <br><br>
    <!-- ================================================ -->
    <!-- <pre>
      {{ movie_reviews }}
    </pre> -->
    <div v-if="movie_reviews && movie_reviews.length > 0">
      <MovieReviewsList
        v-for="review in movie_reviews"
        :key="review.id"
        :review="review"
        :movie_id="movie_tmdb_id"
        @deleteReview="handleDeleteReview"
      />
    </div>
    <div v-else>
      아직 작성된 리뷰가 없습니다.
    </div>
    ================================================
  </div>
</template>


<style scoped>
.form {
  align-items: center;
  margin-bottom: 20px;
}
.li-contain{
  display: flex;
  justify-content: center;
}
.list {
  display: flex;
  float:left;
  gap:10px;
  justify-content: center;
}

#button {
  margin-left: 30px;
}

#cd{
  margin-left: 40px;
}
</style>
