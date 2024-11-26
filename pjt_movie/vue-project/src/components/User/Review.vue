<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';

import ReviewList from '@/components/User/ReviewList.vue';

const userStore = useUserStore()
const userDB = userStore.userInfo


</script>


<template>
  <div>
    <header>
      <h1>
        Review
      </h1>
    </header>

    <!-- <ReviewList :reviews="userDB.reviews"/> -->
    <ReviewList />
  </div>
</template>


<style scoped>

</style>
