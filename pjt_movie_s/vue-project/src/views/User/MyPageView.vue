<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue';
import { onBeforeRouteLeave } from 'vue-router';
import { RouterLink, RouterView } from 'vue-router'

import MyPageNavbar from '@/components/Common/MyPageNavbar.vue';

import MyPageTabs from '@/components/User/MyPageTabs.vue';

onBeforeRouteLeave((to, from, next) => {
  // console.log('MyComponent 컴포넌트에서 떠날 때');
  localStorage.removeItem('currentTab')
  next();
})

const userStore = useUserStore()
onMounted(() => {
  userStore.getUserInfo()
})

</script>


<template>
  <div>
    <!-- <h1>My Page</h1> -->
    <MyPageTabs />
    <!-- <TabsView /> -->
    <!-- <UserInfo />
    <MyPageNavbar />
    <UserInfoView /> -->
    <!-- <Review /> -->
  </div>
</template>


<style scoped>

</style>
