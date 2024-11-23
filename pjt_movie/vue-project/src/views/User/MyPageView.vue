<script setup>
import { RouterLink, RouterView } from 'vue-router'

import MyPageNavbar from '@/components/Common/MyPageNavbar.vue';

import UserInfo from '@/components/User/UserInfo.vue';
import UserInfoView from './UserInfoView.vue';
import Review from '@/components/User/Review.vue';
</script>


<template>
  <div>
    <h1>My Page</h1>
    <UserInfo />
    <MyPageNavbar />
    <UserInfoView />
    <!-- <Review /> -->
  </div>
</template>


<style scoped>

</style>
