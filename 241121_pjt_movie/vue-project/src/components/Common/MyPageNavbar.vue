<template>
  <nav class="navMyPage">
    <RouterLink :to="{ name: 'UserInfo' }">Home</RouterLink> | 
    <RouterLink :to="{ name: 'ReviewList' }">Review</RouterLink>
  </nav>
  
  <div>
    <button @click="currentComponent = 'UserInfoComponent'">Show User Info</button>
    <button @click="currentComponent = 'ReviewListComponent'">Show Reviews</button>
    
    <component :is="currentComponent" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import UserInfo from '@/components/User/UserInfo.vue'
import ReviewList from '@/components/User/ReviewList.vue'

const currentComponent = ref('UserInfoComponent'); // 기본적으로 UserInfoComponent를 보여줌
</script>

<style scoped>
/* 스타일을 여기에 작성하세요 */
</style>
