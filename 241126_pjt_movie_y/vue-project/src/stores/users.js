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

  const userInfo = ref(null) // 초기값을 null로 설정하여 로딩 상태와 구별
  const isLoading = ref(true) // 로딩 상태를 관리할 변수
  const error = ref(null) // 에러 상태를 관리할 변수
  const errorMessage = ref('');

  const getUserInfo = async () => {
    if (!token) {
      // 토큰이 없다면 로그인 페이지로 리디렉션
      router.push('/login')
      return
    }

    try {
      isLoading.value = true
      const response = await axios.get(`${DB_BASE_URL}/accounts/mypage/`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      userInfo.value = response.data
    } catch (err) {
      console.error('Error fetching user info:', err)
      error.value = 'Failed to fetch user information.' // 에러 메시지 설정
    } finally {
      isLoading.value = false
    }
  }

  // 초기 로딩 시 호출
  if (token) {
    getUserInfo() // 컴포넌트가 마운트될 때 유저 정보 로드
  }


  const updateUserInfo = async (formData) => {
    try{
      const response = await axios ({
        method: 'patch',
        url: `${DB_BASE_URL}/accounts/update/`,
        data: formData,
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        },
      })

      console.log('유저정보 업데이트 성공:', response.data);
      router.push({name : 'MyPageView'})
    } catch (error) {
      // 에러가 axios response 객체를 포함하고 있는지 확인
      if (error.response && error.response.data && error.response.data.errors) {
        // 서버에서 반환한 에러 메시지를 상태에 저장
        errorMessage.value = error.response.data.errors[0];
      } else {
        // 네트워크 오류 또는 예상치 못한 오류 처리
        errorMessage.value = '정보 업데이트에 실패했습니다. 다시 시도해주세요.';
      }

      // 에러를 상위로 전달
      throw error;
    }
  }

  return {
    DB_BASE_URL,
    userInfo,
    isLoading,
    error,
    errorMessage,
    getUserInfo,
    updateUserInfo,
  }
}, { persist: true })
    



// ==========================================


//   const getUserInfo = async () => {
//     axios({
//       method:'get',
//       url: `${DB_BASE_URL}/accounts/mypage/`,
//       headers: {
//         Authorization: `Bearer ${token}` 
//       }
//     })
//     .then((res) => {
//       userInfo.value = res.data
//       // console.log(res)
//     })
//     .catch((err) => {
//       console.log(err)
//     })
//   }

//   // const reviews = ref([])
//   // const getReviews = () => {
//   //   axios({
//   //     method:'get',
//   //     url:``
//   //   })
//   // }

//   return {
//     DB_BASE_URL,
//     userInfo,
//     getUserInfo
//   }

// }, { persist: true })