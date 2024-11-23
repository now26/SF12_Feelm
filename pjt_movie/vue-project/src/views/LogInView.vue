<script setup>
// import { useCounterStore } from '@/stores/counter';
// const useStore = useCounterStore()

// const logIn = () => {
//   const payload = {
//     username : username.value,
//     password : password.value
//   }
//   // useStore.logIn(payload, router)
//   useStore.logIn(payload)
// }

import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { loginUser } from '@/utils/auth.js' // auth.js에서 로그인 함수 가져오기

const router = useRouter()
const useStore = useCounterStore()

const username = ref(null)
const password = ref(null)


// 로그인 함수
const logIn = async () => {
  const success = await loginUser(username.value, password.value)
  if (success){
    console.log('로그인 성공')
    useStore.token = localStorage.getItem('access_token')
    router.push({ name: 'HomeView' })
  } else{
    alert('Login failed!')
  }
}


</script>


<template>
  <div>
    <h1>Log In</h1>

    <form @submit.prevent="logIn">
      <div>
        <label for="username">Username : </label>
        <input type="text" id="username" v-model.trim="username" placeholder="Username" />
      </div>

      <div>
        <label for="password">Password : </label>
        <input type="password" id="password" v-model.trim="password" placeholder="Password" />
      </div>

      <input type="submit" value="Log In">
    </form>
  </div>
</template>


<style scoped>

</style>
