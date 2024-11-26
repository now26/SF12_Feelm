<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { loginUser } from '@/utils/auth.js' // auth.js에서 로그인 함수 가져오기

const router = useRouter()
const useStore = useCounterStore()

const username = ref('')
const password = ref('')


// 로그인 함수
const logIn = async () => {
  // console.log(username.value, password.value)
  const success = await loginUser(username.value, password.value)
  if (success){
    console.log('로그인 성공')
    useStore.token = localStorage.getItem('access_token')
    router.push({ name: 'HomeView' })
  } else{
    alert('아이디와 비밀번호를 확인해주세요.')
  }
}

</script>


<template>
  <div class="login-container">
    <div class="content">
      <header>
        <h1>Log In</h1>
      </header>

      <form @submit.prevent="logIn">
        <div class="input-group">
          <label for="username">Username : </label>
          <input type="text" id="username" v-model.trim="username" placeholder="Username" class="inputform" required />
        </div>
  
        <div class="input-group">
          <label for="password">Password : </label>
          <input type="password" id="password" v-model.trim="password" placeholder="Password" class="inputform" required />
        </div>
  
        <input type="submit" value="Log In" class="inputbtn">
      </form>

      <div class="extra-links">
        <!-- <a href="/forgot-password">비밀번호를 잊으셨나요?</a> -->
        <router-link :to="{name:'SignUpView'}">회원가입</router-link>
      </div>

    </div>
  </div>
</template>


<style scoped>

.login-container {
  /* background-color: aquamarine; */
  min-height: 100dvh;
  
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

.content {
  background-color: #d8f2ff;
  padding: 3rem;
  /* font-size: 2rem; */
  border-radius: 1rem;
  height: 400px;
  width: 300px;
}

/* 로그인 폼 스타일 */
form {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 400px; 
  margin-bottom: 20px;
  /* 
  width: 100%;
  */
}

/* 헤더 스타일 */
header {
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  font-size: 2rem;
  font-family: Arial, sans-serif;
  font-weight: bold;
  color: rgb(7, 8, 42);
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: 1rem;
  color: rgb(7, 8, 42);
}

.inputform {
  width: 92%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #333;
  border-radius: 5px; 
}

.input-group {
  margin-bottom: 15px;
}

.inputbtn {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  cursor: pointer;
}

.inputbtn:hover {
  background-color: #0056b3;
}

.extra-links {
  display: flex;
  /* justify-content: space-between; */
  justify-content: space-evenly;
  margin-top: 20px;
}

.extra-links a {
  font-size: 0.9rem;
  /* color: #007bff; */
  color: #0026ff;
  text-decoration: none;
}

.extra-links a:hover {
  text-decoration: underline;
}





/* 가운데 정렬 참고 */

/* .wrapper { */
  /* background-color: white;
  min-height: 100dvh; */

  /* grid 사용 */
  /* display: grid;
  place-items: center; */

  /* flexbox 관련 css 속성 */
  /* display: flex;
  justify-content: center;
  align-items: center; */
/* } */


</style>
