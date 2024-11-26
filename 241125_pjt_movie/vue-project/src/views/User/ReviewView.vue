<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';

import ReviewList from '@/components/User/ReviewList.vue';

const userStore = useUserStore()

onMounted(() => {
  userStore.getReviews()
  console.log(userStore.reviews)
})

</script>


<template>
  <div>

  </div>
</template>


<style scoped>

</style>
