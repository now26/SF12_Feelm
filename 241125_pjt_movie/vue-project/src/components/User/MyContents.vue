<script setup>
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router';

const userStore = useUserStore()
const userDB = userStore.userInfo

</script>


<template>
  <div>
    <div>
  
      <div>
        <p>like_movies : {{ userDB.like_movies }}</p>
        <p>like_reviews : {{ userDB.like_reviews }}</p>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
