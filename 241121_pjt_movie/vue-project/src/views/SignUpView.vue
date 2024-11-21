<script setup>
import { ref } from 'vue'
import axios from 'axios';

import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()


const username = ref('')
const password1 = ref('')
const password2 = ref('')

const nickname = ref('')
const age = ref('')
const gender = ref('')
const profile_image = ref(null)

const errorMessage = ref('')

const signUp = async function() {

  if (password1.value !== password2.value){
    errorMessage.value = 'Password do not match!'
    return
  }

  const formData = new FormData()
  formData.append('username', username.value)
  formData.append('password1', password1.value)
  formData.append('password2', password2.value)
  formData.append('nickname', nickname.value)
  formData.append('age', age.value)
  formData.append('gender', gender.value)

  if (profile_image.value){
    formData.append('profile_image', profile_image.value)
  }

  try{
    await useStore.signUp(formData)
  } catch (err) {
    console.error(err)
    errorMessage.value = 'An error occurred during signup. Please try again.'
  }
}

</script>


<template>
  <div>
    <h1>Sign Up</h1>
    <!-- 필수 : username, nickname, age -->
    <!-- 필수 : gender -->
    <!-- 선택 : profile_image-->

    <div v-if="errorMessage" style="color: red; font-weight: bold;">
      {{ errorMessage }}
    </div>

    <!-- 미입력 : is_activate, is_staff, created_at -->
    <form @submit.prevent="signUp">
      <div>
        <label for="username">Username : </label>
        <input type="text" id="username" v-model.trim="username">
      </div>
      
      <div>
        <label for="password1">Password : </label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>
      
      <div>
        <label for="password2">Password Confirmation : </label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>
      
      <div>
        <label for="nickname">Nickname : </label>
        <input type="text" id="nickname" v-model.trim="nickname">
      </div>

      <div>
        <label for="age">Age : </label>
        <input type="number" id="age" v-model.trim="age" min="1">
      </div>

      <div>
        <label for="gender">Gender : </label>
        <!-- <input type="select" id="gender" v-model.trim="gender"> -->
        <select id="gender" v-model="gender">
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="N">Prefer not to say</option>
        </select>
      </div>

      <div>
        <label for="profile_image">Profile Image : </label>
        <input type="file" id="profile_image" @change="e => profile_image.value = e.target.files[0]">

      </div>

      <input type="submit" value="Sign Up">

    </form>
  </div>
</template>


<style scoped>

</style>
