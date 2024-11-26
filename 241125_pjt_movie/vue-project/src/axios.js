import axios from 'axios';

const api = axios.create({
  // baseURL: 'http://localhost:8000/api/',  // Django API의 기본 URL
  baseURL: 'http://localhost:8000/',  // Django API의 기본 URL
});

// 요청 인터셉터: 토큰을 자동으로 헤더에 추가
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;

