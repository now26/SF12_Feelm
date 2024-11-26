<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users';
import ReviewListItem from '@/components/User/ReviewListItem.vue';

const userStore = useUserStore()
const userDB = userStore.userInfo


// 로컬에 리뷰 리스트를 복사해서 사용
const reviews = ref([...userDB.reviews])

// 삭제된 리뷰 처리 함수
const handleDeleteReview = (review_id) => {
  // 삭제된 review_id를 제외한 새로운 배열로 갱신
  reviews.value = reviews.value.filter(review => review.id !== review_id);
  userDB.reviews = reviews.value;
}

// defineProps({
//   reviews:Object
// })

</script>


<template>

  <div v-if="reviews && reviews.length > 0">
    <ReviewListItem 
      v-for="review in reviews"
      :key="review.user"
      :review="review"
      @deleteReview="handleDeleteReview"
    />
  </div>
  <div v-else>
    <p>아직 작성된 리뷰가 없습니다.</p>
  </div>
</template>


<style scoped>

</style>
