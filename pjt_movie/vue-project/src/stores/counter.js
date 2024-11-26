import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

// auth.js에서 로그인, 로그아웃 함수 가져오기
import { loginUser, logoutUser } from '@/utils/auth'
import { useUserStore } from '@/stores/users'

export const useCounterStore = defineStore('counter', () => {
  // const userStore = useUserStore()
  const router = useRouter()

  const API_URL = 'http://127.0.0.1:8000'
  const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY

  // const token = ref(null)
  const token = ref(localStorage.getItem('access_token'))  // 초기값으로 localStorage에서 토큰을 가져옴

  // userinfo를 localStorage에서 가져올 때는 JSON.parse로 객체로 변환
  const userinfo = ref(localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null);


  // JWT 토큰이 있으면 로그인 상태
  const isLogin = computed(() => !!token.value) 

  const signUp = async (requestData) => {
    try {
      const response = await axios.post(`${API_URL}/accounts/signup/`, requestData, {
        headers: {
          // 'Content-Type': 'application/json',
          'Content-Type': 'multipart/form-data',
        },
      });

      console.log('회원가입 성공:', response.data);
      localStorage.setItem('access_token', response.data.token);
      token.value = response.data.token;  // 토큰 저장
      alert('회원가입 성공')
      localStorage.removeItem('access_token', response.data.token);

      router.push({ name: 'LogInView' });  // 로그인 화면으로 이동
    } catch (error) {
      console.error('회원가입 실패:', error.response ? error.response.data : error.message);
      throw new Error('회원가입 실패');
    }
  };

  const logIn = async (username, password) => {
    const success = await loginUser(username, password)
    if (success) {
      // window.location.href = '/';  // 로그인 성공 시 홈 화면으로 이동
      // userStore.getUserInfo()

      console.log('로그인 성공')
      router.push({name: 'HomeView'})
    }
  }

  const logOut = () => {

    // 로그아웃 시작 시 window.isLoggingOut을 true로 설정
    window.isLoggingOut = true;

    logoutUser();  // 로컬 스토리지에서 토큰 삭제
    token.value = null; // Pinia 상태에서 token 초기화
    userinfo.value = null

    console.log('로그아웃 성공');
    alert('로그아웃 성공')
    // 로그아웃 후에는 다시 window.isLoggingOut을 false로 설정
    window.isLoggingOut = false;

    router.push({ name: 'LogInView' });  // 로그인 페이지로 리디렉션
  };


  const tests = ref([])

  const getArticles = function() {

    axios({
      method:'get',
      url:`${API_URL}/api/v1/articles/`,
      headers: {
        // 토큰 전달
        // Authorization: `Token ${token.value}` 
        Authorization: `Bearer ${token.value}` 
      }
    })
    .then((res) => {
      tests.value = res.data
      // console.log(res)
      })
    .catch((err) => console.log(err))
  }

  return { 
    API_URL,
    tests,
    token,
    isLogin,
    signUp,
    logIn,
    logOut,
    getArticles,
  }
}, { persist: true })
