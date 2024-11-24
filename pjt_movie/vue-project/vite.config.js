import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      'cypress': 'node_modules/cypress'
    },
  },
  server: {
    proxy: {
      '/accounts/check-username/': 'http://localhost:8000'

      // '/accounts/check-username/': {
      //   target: 'http://localhost:8000',  // 백엔드 서버 주소
      //   changeOrigin: true,
      //   // rewrite: (path) => path.replace(/^\/accounts/, '/accounts')  // 서버에서 올바른 경로로 요청 전달
      // },
    }
  },
})
