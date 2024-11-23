<script setup>
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import { logoutUser } from '@/utils/auth';
import { useRouter } from 'vue-router';
const router = useRouter()


const logout = () => {
  useStore.logOut()
};

</script>


<template>
  <div>
    <button @click="logout">Logout</button>
  </div>
</template>


<style scoped>

</style>
