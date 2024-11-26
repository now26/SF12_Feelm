<script setup>

import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'

const useStore = useCounterStore()
const logout = () => {
  useStore.logOut()
};


</script>


<template>
  <!-- 로그인 O -->
  <div v-if="useStore.isLogin === true">
    <nav class="navMain">
      <span class="contentNav">
        <!-- navbar css는 src/assets/navbar.css에서 관리중 -> assets만들고 main.js에 등록하기! -->
        <RouterLink :to="{name: 'HomeView'}">Home</RouterLink>
        <RouterLink :to="{name: 'MovieView'}">Movies</RouterLink>
        <RouterLink :to="{name: 'MovieTmdbView'}">TMDB</RouterLink>
        <RouterLink :to="{name: 'RecommendView'}">Recommend</RouterLink>
        <RouterLink :to="{name: 'ArticleView'}">Articles</RouterLink>
        <RouterLink :to="{name: 'MyContentView'}">Contents</RouterLink>
      </span>
      <span class="userNav">
        <!-- <input type="text" placeholder="Search..." class="search-bar" /> -->
        <RouterLink :to="{name: 'MyPageView'}">My Page</RouterLink>
        <span class="logoutButton" @click="logout">Logout</span>
      </span>
    </nav>
  </div>

  <!-- 로그인 X -->
  <div v-if="useStore.isLogin === false">
    <nav class="navMain">
      <RouterLink :to="{name: 'HomeView'}">Home</RouterLink>
      <RouterLink :to="{name: 'MovieView'}">Movies</RouterLink>
      <!-- <RouterLink :to="{name: 'ArticleView'}">Articles</RouterLink> -->
      <RouterLink :to="{name: 'SignUpView'}">Sign Up</RouterLink>
      <RouterLink :to="{name: 'LogInView'}">Log In</RouterLink>
    </nav>
  </div>
  

</template>


<style scoped>

.navMain {
  width: 100%;
  font-size: 23px;
  display: flex;
  text-align: center;
  margin-top: 3rem;
  /* justify-content: space-between; */
  justify-content: space-evenly;
}

.navMain a{
  text-decoration: none;
  color: #F7F9FF;
  border-radius: 5px;
  margin-right: 20px;
  white-space: nowrap; /* 줄바꿈 방지 */
}

.logoutButton {
  cursor: pointer;
  border-radius: 5px;
}

.userNav {
  margin-top: 0.2rem;
  font-size: 20px;
}

/* .search-bar {
  padding: 5px;
  border: 1px solid #618CF6;
  border-radius: 4px;
} */


a:hover {
  color: #f1cf53;
  transition: 0.4s;
}

.logoutButton:hover {
  color: #f1cf53;
  transition: 0.4s;
}

</style>
