<script setup>
import { ref, computed } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
// import { error } from 'cypress/types/jquery';
const useStore = useCounterStore()


const username = ref('')
const password1 = ref('')
const password2 = ref('')

const nickname = ref('')
const age = ref('')
const gender = ref('')
const profile_image = ref(null)

const errorMessage = ref('')
const passwordErrorMessage1 = ref('')
const passwordErrorMessage2 = ref('')
const usernameError = ref('')

const handleFileChange = (el) => {
  const file = el.target.files ? el.target.files[0] : null
  if (file) {
    profile_image.value = file

    // // 파일을 base64로 변환
    // const reader = new FileReader()
    // reader.onloadend = () => {
    //   profile_image.value = reader.result
    // }
    // reader.readAsDataURL(file)

  } else {
    profile_image.value = null
  }
}

// 비밀번호 일치 여부를 실시간으로 확인
const passwordsMatch = computed(() => password1.value === password2.value)

const checkPasswordLength = () => {
  // console.log(password1.value.length)
  if (password1.value.length < 8 || password2.value.length < 8) {
    passwordErrorMessage1.value = '비밀번호는 8자리 이상이어야 합니다.'
  } else {
    passwordErrorMessage1.value = ''
  }
}

const checkPasswordsMatch = () => {
  // console.log('psw2')
  if (password1.value !== password2.value) {
    passwordErrorMessage2.value = '비밀번호가 일치하지 않습니다.'
  } else {
    passwordErrorMessage2.value = '' // 비밀번호 일치하면 에러 메시지 초기화
  }
}

const handlePassword = () => {
  checkPasswordLength()
  checkPasswordsMatch()
}

// username 중복 검사 함수
const checkUsernameAvailability = async () => {
  // console.log("blur 이벤트 호출됨"); // 디버깅을 위한 로그 추가
  // console.log(username.value)

  try {
    // 서버 측 회원가입 엔드포인트 작성 -> 서버에username만 전송하여 중복 여부 확인
    const response = await axios.post('/accounts/check-username/', {
      username: username.value || 'undefined',  // null이면 undefined로 대체
    })

    // 중복되지 않으면 usernameError를 빈 문자열로 초기화
    if (response.status === 200) {
      if (response.data.exists === true){
        // console.log('있음')
        usernameError.value = '이미 존재하는 username 입니다.'
      } else {
        // console.log('없음')
        usernameError.value = ''
      }
      // if (response)
    }
  } catch (error) {
    // 서버에서 중복된 username에 대해 에러를 반환하면 해당 에러 메시지 처리
    console.log(error)
    if (error.response && error.response.data.username){
      usernameError.value = error.response.data.username[0]
    }
  }
}


const signUp = async function() {

  if (!passwordsMatch.value){
    errorMessage.value = '비밀번호가 일치하지 않습니다.'
    return
  }

  if (usernameError.value){
    console.log(usernameError)
    errorMessage.value = '이미 존재하는 username 입니다.'
    return
  }

  // const requestData = {
  //   username: username.value,
  //   password1: password1.value,
  //   password2: password2.value,
  //   nickname: nickname.value,
  //   age: age.value,
  //   gender: gender.value,
    
  //   profile_image: profile_image.value || null,
  // }

  // if (profile_image.value) {
  //   // 이미지 업로드는 별도로 처리
  //   requestData.profile_image = profile_image.value // 파일을 별도로 전송
  // }


  const formData = new FormData();
  formData.append('username', username.value);
  formData.append('password1', password1.value);
  formData.append('password2', password2.value);
  formData.append('nickname', nickname.value);
  formData.append('age', age.value);
  formData.append('gender', gender.value);

  if (profile_image.value) {
    formData.append('profile_image', profile_image.value);  // 파일이 있을 경우 전송
  }

  try{
    // await useStore.signUp(requestData)
    await useStore.signUp(formData);  // signUp 함수가 FormData를 처리한다고 가정
  } catch (err) {
    console.error(err)
    errorMessage.value = '회원가입을 다시 시도해주세요.'
    // errorMessage.value = 'An error occurred during signup. Please try again.'
  }
}

</script>


<template>
  <div class="signup-container">
    <div class="content">
      <header>
        <h1>Sign Up</h1>
      </header>

      <!-- 필수 : username, nickname, age -->
      <!-- 필수 : gender -->
      <!-- 선택 : profile_image-->
  
      <div v-if="errorMessage" style="color: red; font-weight: bold;">
        {{ errorMessage }}
      </div>
  
      <!-- 미입력 : is_activate, is_staff, created_at -->
      <form @submit.prevent="signUp">
        <div>
          <div class="input-group">
            <label for="username">Username<b class="required">*</b> : </label>
            <input 
              type="text" 
              id="username" 
              v-model.trim="username"
              placeholder="Username"
              class="inputform"
              required
              @blur="checkUsernameAvailability"
            >
            <div v-if="usernameError" class="error">
              {{ usernameError }}
            </div>
          </div>
          
        </div>
        
        <div class="input-group">
          <label for="nickname">Nickname : </label>
          <input type="text" id="nickname" v-model.trim="nickname" placeholder="Nickname" class="inputform">
        </div>

        <div class="input-group">
          <label for="password1">Password<b class="required">*</b> : </label>
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
        
        <div>
          <div class="input-group">
            <label for="password2">Password Confirmation<b class="required">*</b> : </label>
            <input 
              type="password" 
              id="password2" 
              v-model.trim="password2"
              placeholder="Password confirmation"
              required
              @blur="handlePassword"
              class="inputform"
            >
            <div v-if="password1.length < 8" class="error">
              {{ passwordErrorMessage1 }}
            </div>
            <div v-if="!passwordsMatch" class="error">
              {{ passwordErrorMessage2 }}
            </div>
          </div>

        </div>
        
        <div class="input-group">
          <label for="age">Age<b class="required">*</b> : </label>
          <input type="number" id="age" v-model.trim="age" min="1" placeholder="20" class="inputform" required>
        </div>
  
        <div class="input-group">
          <label for="gender">Gender<b class="required">*</b> : </label>
          <!-- <input type="select" id="gender" v-model.trim="gender"> -->
          <select id="gender" v-model="gender" class="inputform" required>
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
          value="Sign Up" 
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

.signup-container {
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
