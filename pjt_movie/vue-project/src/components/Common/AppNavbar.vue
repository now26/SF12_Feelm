<script setup>

import LogoutButton from '@/components/LogoutButton.vue';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'

const useStore = useCounterStore()


</script>


<template>
  <!-- 로그인 O -->
  <div v-if="useStore.isLogin === true">
    <nav class="navMain">
      <!-- navbar css는 src/assets/navbar.css에서 관리중 -> assets만들고 main.js에 등록하기! -->
      <RouterLink :to="{name: 'HomeView'}">Home</RouterLink> | 
      <RouterLink :to="{name: 'MovieView'}">Movies</RouterLink> | 
      <RouterLink :to="{name: 'MovieTmdbView'}">TMDB</RouterLink> | 
      <RouterLink :to="{name: 'ArticleView'}">Articles</RouterLink> | 
      <RouterLink :to="{name: 'MyPageView'}">My Page</RouterLink>
      <LogoutButton  class="inline-button"></LogoutButton>
    </nav>
  </div>

  <!-- 로그인 X -->
  <div v-if="useStore.isLogin === false">
    <nav class="navMain">
      <RouterLink :to="{name: 'HomeView'}">Home</RouterLink> | 
      <RouterLink :to="{name: 'MovieView'}">Movies</RouterLink> | 
      <RouterLink :to="{name: 'ArticleView'}">Articles</RouterLink> | 
      <RouterLink :to="{name: 'SignUpView'}">Sign Up</RouterLink> | 
      <RouterLink :to="{name: 'LogInView'}">Log In</RouterLink>
    </nav>
  </div>
  

</template>


<style scoped>

.inline-button {
  display: inline-block;
  margin-left: 10px;
}
</style>
