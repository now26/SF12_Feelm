import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

import { useCounterStore } from './counter'


export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'

  const reviews = ref([])
  const getReviews = () => {
    axios({
      method:'get',
      url:``
    })
  }

  return {
  }

}, { persist: true })