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
    <ReviewList :reviews="userDB.reviews"/>
  </div>
</template>


<style scoped>

</style>
