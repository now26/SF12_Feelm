<script setup>
import { useUserStore } from '@/stores/users';
const userStore = useUserStore()

import ReviewListItem from '@/components/User/ReviewListItem.vue';

defineProps({
  reviews:Object
})

</script>


<template>
  <div>
    <p>
      <b>Review</b>
    </p>
    <ReviewListItem 
      v-for="review in reviews"
      :key="review.user"
      :review="review"
    />

  </div>
</template>


<style scoped>

</style>
