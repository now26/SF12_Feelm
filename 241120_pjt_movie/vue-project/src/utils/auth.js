// auth.js - 인증 관련 설정만 컨트롤

import api from '@/axios'; // axios 설정을 가져옴 (src/axios.js)

// export const : 모듈을 내보내는 방법

// 로그인 함수
export const loginUser = async (username, password) => {
  try {
    // const response = await api.post('token/', {
    //   username: username,
    //   password: password,
    // });

    const response = await api.post('accounts/login/', {
      username: username,
      password: password,
    });


    // 토큰을 로컬 스토리지에 저장
    localStorage.setItem('access_token', response.data.access_token);
    localStorage.setItem('refresh_token', response.data.refresh_token);

    return true;  // 로그인 성공
  } catch (error) {
    console.error('Login error:', error);
    return false;  // 로그인 실패
  }
};


// 로그아웃 함수
export const logoutUser = () => {
  localStorage.removeItem('access_token');  // 로컬 스토리지에서 액세스 토큰 삭제
  localStorage.removeItem('refresh_token');  // 로컬 스토리지에서 리프레시 토큰 삭제
};