<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router';

import UserInfo from '@/components/User/UserInfo.vue';
import ReviewList from '@/components/User/ReviewList.vue';

const userStore = useUserStore()
onMounted(() => {
  userStore.getUserInfo()
})

const userDB = userStore.userInfo

</script>


<template>
  <div>
    <h3>User Info View</h3>
    <div>
      <div>
        <img :src="userDB.profile_image" alt="profile_image">
      </div>
  
      <div>
        <p>username : {{ userDB.username }}</p>
        <p>nickname : {{ userDB.nickname }}</p>
        <p>age : {{ userDB.age }}</p>
        <p>gender : {{ userDB.gender }}</p>
        <p>live_movies : {{ userDB.live_movies }}</p>
        <p>bookmark : {{ userDB.bookmark }}</p>
        <p>live_review : {{ userDB.live_review }}</p>
        
        <ReviewList :reviews="userDB.reviews"/>
      </div>
    </div>
    
    <!-- <UserInfo /> -->
  </div>
</template>


<style scoped>

</style>
