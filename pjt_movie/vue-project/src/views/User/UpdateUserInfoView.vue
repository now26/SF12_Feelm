<script setup>
import { ref, computed } from 'vue'
import axios from 'axios';

import { useUserStore } from '@/stores/users';
// import { error } from 'cypress/types/jquery';
const userStore = useUserStore()


const username = ref('')
const password1 = ref('') // 기존 비밀번호
const password2 = ref('') // 신규 비밀번호
const password3 = ref('') // 신규 비밀번호 확인

const nickname = ref('')
const age = ref('')
const gender = ref('')
const profile_image = ref(null)

const errorMessage = ref('')
const passwordErrorMessage1 = ref('')
const passwordErrorMessage2 = ref('')
const usernameError = ref('')

// 에러 메시지 가져오기
const errorMessage2 = ref(null);

const handleFileChange = (el) => {
  const file = el.target.files ? el.target.files[0] : null
  if (file) {
    profile_image.value = file
  } else {
    profile_image.value = null
  }
}

// 비밀번호 일치 여부를 실시간으로 확인
const passwordsMatch = computed(() => password2.value === password3.value)

const checkPasswordLength = () => {
  // console.log(password2.value.length)
  if(password2.value || password3.value){
    if (password2.value.length < 8 || password3.value.length < 8) {
      passwordErrorMessage1.value = '비밀번호는 8자리 이상이어야 합니다.'
    } else {
      passwordErrorMessage1.value = ''
    }
  }
}

const checkPasswordsMatch = () => {
  // console.log('psw2')
  if (password2.value !== password3.value) {
    passwordErrorMessage2.value = '비밀번호가 일치하지 않습니다.'
  } else {
    passwordErrorMessage2.value = '' // 비밀번호 일치하면 에러 메시지 초기화
  }
}

const handlePassword = () => {
  checkPasswordLength()
  checkPasswordsMatch()
}

const updateUserInfo = async function() {

  if (!passwordsMatch.value){
    errorMessage.value = '비밀번호가 일치하지 않습니다.'
    return
  }

  if (usernameError.value){
    console.log(usernameError)
    errorMessage.value = '이미 존재하는 username 입니다.'
    return
  }

  const formData = new FormData();
  formData.append('username', username.value);
  formData.append('password1', password1.value);
  formData.append('nickname', nickname.value);
  formData.append('age', age.value);
  formData.append('gender', gender.value);
  
  if (password2.value && password3.value){
    formData.append('password2', password2.value);
    formData.append('password3', password3.value);
  }

  if (profile_image.value) {
    formData.append('profile_image', profile_image.value);  // 파일이 있을 경우 전송
  }

  try{
    await userStore.updateUserInfo(formData); 
  } catch (err) {
    console.error(err)
    errorMessage2.value = userStore.errorMessage
    // errorMessage.value = 'An error occurred during signup. Please try again.'
  }
}

</script>


<template>
  <div class="update-container">
    <div class="content">
      <header>
        <h1>회원정보 수정</h1>
      </header>
  
      <div v-if="errorMessage" style="color: red; font-weight: bold;">
        {{ errorMessage }}
      </div>
      <div v-if="errorMessage2" style="color: red; font-weight: bold;">
        {{ errorMessage2 }}
      </div>
  
      <!-- 미입력 : is_activate, is_staff, created_at -->
      <form @submit.prevent="updateUserInfo">

        <div class="input-group">
          <label for="nickname">Nickname : </label>
          <input type="text" id="nickname" v-model.trim="nickname" placeholder="Nickname" class="inputform">
        </div>

        <div class="input-group">
          <label for="password1">Password <b class="required">*</b> : </label>
          <input 
            type="password" 
            id="password1" 
            v-model.trim="password1"
            @blur="handlePassword"
            placeholder="Password"
            required
            class="inputform"
          >
        </div>


        <div class="input-group">
          <label for="password2">New Password : </label>
          <input 
            type="password" 
            id="password2" 
            v-model.trim="password2"
            @blur="handlePassword"
            placeholder="Password"
            class="inputform"
          >
        </div>
        
        <div>
          <div class="input-group">
            <label for="password3">New Password Confirmation : </label>
            <input 
              type="password" 
              id="password3" 
              v-model.trim="password3"
              placeholder="Password confirmation"
              @blur="handlePassword"
              class="inputform"
            >
            <div v-if="password2.length < 8" class="error">
              {{ passwordErrorMessage1 }}
            </div>
            <div v-if="!passwordsMatch" class="error">
              {{ passwordErrorMessage2 }}
            </div>
          </div>

        </div>
        
        <div class="input-group">
          <label for="age">Age : </label>
          <input type="number" id="age" v-model.trim="age" min="1" placeholder="20" class="inputform">
        </div>
  
        <div class="input-group">
          <label for="gender">Gender : </label>
          <!-- <input type="select" id="gender" v-model.trim="gender"> -->
          <select id="gender" v-model="gender" class="inputform">
            <option value="M">Male</option>
            <option value="F">Female</option>
            <option value="N">Prefer not to say</option>
          </select>
        </div>
  
        <div class="input-group">
          <label for="profile_image">Profile Image : </label>
          <input 
            type="file" 
            id="profile_image" 
            @change="handleFileChange" 
            class="selectimg">

          <!-- <div v-if="profile_image" class="selectimg">
            선택한 파일: {{ profile_image }}
          </div> -->
  
        </div>
  
        <input 
          type="submit" 
          value="Update" 
          class="inputbtn"
        >
  
      </form>
    </div>

  </div>
</template>


<style scoped>
.required {
  color: red;
}

.error {
  color: red;
  font-weight: bold;
}

.update-container {
  /* background-color: aqua; */
  min-height: 100dvh;
  
  display: flex;
  justify-content: center;
}

.content {
  background-color: #d8f2ff;
  padding: 3rem;
  border-radius: 1rem;
  height: 750px;
  width: 450px;
}

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
  padding: 8px;
  font-size: 1rem;
  border: 1px solid #333;
  border-radius: 5px; 
}

.input-group {
  margin-bottom: 15px;
}

.selectimg{
  color: #333;
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

</style>
