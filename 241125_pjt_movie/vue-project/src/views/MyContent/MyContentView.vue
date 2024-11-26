<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue';
import { onBeforeRouteLeave } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router'

import MyContentTabs from '@/components/Content/MyContentTabs.vue';

onBeforeRouteLeave((to, from, next) => {
  // console.log('MyComponent 컴포넌트에서 떠날 때');
  localStorage.removeItem('currentTab')
  next();
})

const userStore = useUserStore()

onMounted(() => {
  if (localStorage.user) {
    userStore.getUserInfo();
  }
  // if (userStore.token) {
  //   userStore.getUserInfo();
  // }
})

</script>


<template>
  <div>
    <div>
      <MyContentTabs />
      <!-- <div v-if="userStore.isLoading">Loading...</div> -->
      <!-- <div v-if="userStore.error">{{ userStore.error }}</div> -->
      <!-- <div v-else> -->
        <!-- 유저 정보가 정상적으로 로딩되었을 때 표시 -->
        <!-- <p>User Info: {{ userStore.userInfo }}</p> -->
      <!-- </div> -->
    </div>

  </div>
</template>


<style scoped>

</style>
