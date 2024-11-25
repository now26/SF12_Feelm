import api from '@/axios'; // axios 설정을 가져옴

// 액세스 토큰이 만료되었는지 확인하는 함수
const isTokenExpired = (token) => {
  if (!token) return true; // 토큰이 없으면 만료된 것으로 간주

  const payload = JSON.parse(atob(token.split('.')[1])); // 토큰의 페이로드 파싱
  const exp = payload.exp * 1000; // 만료 시간 (초 -> 밀리초 변환)
  return exp < Date.now(); // 현재 시간과 비교하여 만료 여부 확인
};

// 리프레시 토큰을 사용해 새로운 액세스 토큰을 받아오는 함수
const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem('refresh_token');
  if (!refreshToken) return false; // 리프레시 토큰이 없으면 실패

  try {
    const response = await api.post('accounts/refresh-token/', {
      refresh_token: refreshToken,
    });

    // 새로운 액세스 토큰을 로컬 스토리지에 저장
    localStorage.setItem('access_token', response.data.access_token);
    return true; // 갱신 성공
  } catch (error) {
    console.error('Refresh token error:', error);
    return false; // 갱신 실패
  }
};

// 로그인 상태 확인 함수
export const checkLogin = async () => {
  const accessToken = localStorage.getItem('access_token');

  // 액세스 토큰이 없거나 만료되었으면 리프레시 토큰으로 갱신 시도
  if (!accessToken || isTokenExpired(accessToken)) {
    const isRefreshed = await refreshAccessToken();
    if (!isRefreshed) {
      logoutUser(); // 리프레시 토큰 갱신 실패 시 로그아웃 처리
      return false; // 로그인 상태 아님
    }
  }

  return true; // 로그인 상태 유지
};

// 로그인 함수
export const loginUser = async (username, password) => {
  try {
    const response = await api.post('accounts/login/', {
      username: username,
      password: password,
    }, 
    // {
    //   headers: {
    //     'Content-Type': 'application/json',
    //   }
    // }
  );

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
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
};