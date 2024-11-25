import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

import { useCounterStore } from './counter'


export const useUserStore = defineStore('user', () => {
  const useStore = useCounterStore()
  const router = useRouter()

  const token = useStore.token
  const DB_BASE_URL = 'http://127.0.0.1:8000'

  const userInfo = ref([])
  const getUserInfo = () => {
    axios({
      method:'get',
      url: `${DB_BASE_URL}/accounts/mypage/`,
      headers: {
        Authorization: `Bearer ${token}` 
      }
    })
    .then((res) => {
      userInfo.value = res.data
      // console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  // const reviews = ref([])
  // const getReviews = () => {
  //   axios({
  //     method:'get',
  //     url:``
  //   })
  // }

  return {
    userInfo,
    getUserInfo
  }

}, { persist: true })