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
        <p>bookmark : {{ userDB.bookmark }}</p>
      
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
