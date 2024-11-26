<script setup>
import { defineEmits } from 'vue';
const emit = defineEmits(['deleteReview'])
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

defineProps({
    review:Object,
    movie_id:Number
})


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
    <!-- {{ review }} -->
    <!-- {{ movie_id }} -->
    <ul>
      <li class="li-contain">
        <div class="list">
          <p>User: {{ review.user }}</p>
          <p>Content: {{ review.content }}</p>
          <p>Rating: {{ review.rating }}</p>
          <button @click.prevent="deleteReview(movie_id, review.id)">리뷰 삭제</button>
        </div>
      </li>
    </ul>


  </div>
</template>



<style scoped>
.li-contain{
  display: flex;
  /* justify-content: center; */
}
.list {
  display: flex;
  float:left;
  gap:50px;
  justify-content: center;
}

</style>
