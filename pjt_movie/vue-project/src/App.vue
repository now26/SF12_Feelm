<script setup>
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import { onMounted, reactive } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router';

import AppNavbar from '@/components/Common/AppNavbar.vue'
import CartNavbar from '@/components/Common/CartNavbar.vue'

import { useUserStore } from './stores/users';
const userStore = useUserStore()


// 로그인 상태를 반응형으로 관리
const state = reactive({
  isLoggedIn: false,
});

// 로그인 상태 확인 로직 추가
import { checkLogin } from '@/utils/auth.js'

onMounted(async () => {
  // 앱 시작 시 로그인 상태 확인
  const isLoggedIn = await checkLogin();
  state.isLoggedIn = isLoggedIn; // 로그인 상태 업데이트

  if (isLoggedIn) {
    console.log('로그인 상태 유지');
  } else {
    console.log('로그인 상태 아님');
    useStore.logOut()
  }
});

const router = useRouter()

const goToHome = () => {
  router.push({ name : 'HomeView' })
}


</script>

<template>
  <!-- <CartNavbar /> -->
  <div id="wrapper">
    <!-- Header Section -->
    <header class="header">
      <img 
        alt="FeeLM_logo" 
        class="FeeLM_logo" 
        src="@/assets/FeeLM_image/FeeLM_logo.png" 
        @click="goToHome"
      />
      <AppNavbar />
    </header>

    <!-- <div id="app">
    </div> -->

  
    <RouterView />
  </div>

  
  
  


  <!-- Footer Section -->
  <footer class="footer">
    <div class="footer-content">
      <p>&copy; FeeLM. All rights reserved.</p>
      <ul class="footer-links">
      </ul>
    </div>
  </footer>

</template>

<style scoped>

.header {
  /* display: flex; */
  display: grid;
  grid-template-columns: auto 1fr;
}

.FeeLM_logo {
  width: auto;
  height: 150px;
  margin: 0 auto 2rem;
  margin-left: 5px;
  /* display: block; */
  /* margin-right: 50px; */
  cursor: pointer; /* 클릭할 수 있는 이미지로 변경 */
}

#wrapper {
  /* height: auto; */
  position: relative;
  min-height: calc(100vh - 30px); /* 화면 전체에서 footer 높이를 제외한 높이를 설정 */
  padding-bottom: 60px;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%
}

.footer {
  position: relative;
  /* background-color: #3C516D; */
  /* padding: 20px 0; */
  text-align: center;
  color: #FFF7D6;
  width: 100%;
  height: 20px;
}

.footer-content {
  /* display: flex; */
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  padding: 0 20px;
  text-align: center;
}


</style>
