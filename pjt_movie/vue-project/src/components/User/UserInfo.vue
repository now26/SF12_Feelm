<script setup>3
import { computed } from 'vue';
import { useUserStore } from '@/stores/users';
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router';

const userStore = useUserStore()
const userDB = userStore.userInfo

// profile_image
import defaultImage from '@/assets/FeeLM_image/FeeLM_color.png'
import defaultImage_chick from '@/assets/profile_image_default/chick.png'

const profileImageUrl = computed(() => {
  console.log(`http://127.0.0.1:8000${userDB.profile_image}`)
  if(userDB.profile_image) {
    
    // profile_image가 전체 URL이면 그대로 사용
    if(userDB.profile_image.startsWith('http')){
      return userDB.value.profile_image
    }
    // 상대 URL이면 Django media URL을 붙여서 반환
    return `http://localhost:8000${userDB.profile_image}`
  }
  // 프로필 이미지가 없으면 기본 이미지로 대체
  return defaultImage_chick;
})

</script>


<template>
  <div class="info-container">
    <div class="content">
      <header>
        <!-- nickname이 없으면 username을 사용 -->
        <h3> <b class="name">{{ userDB.nickname || userDB.username }}</b> 님 안녕하세요!</h3>
      </header>

      <div class="grid-container">
        <div>
          <!-- 이미지가 없으면 defaultImage로 대체 -->
          <img :src="profileImageUrl" alt="profile_image" class="profile_image">
  
          <!-- <img :src="userDB.profile_image || defaultImage_chick" alt="profile_image" class="profile_image"> -->
        </div>
    
        <div>
          <p class="info">username : {{ userDB.username }}</p>
          <p class="info">nickname : {{ userDB.nickname }}</p>
          <p class="info">age : {{ userDB.age }}</p>
          <p class="info">gender : {{ userDB.gender }}</p>
        
          <router-link >회원정보 변경</router-link>
        </div>
      </div>


    </div>
  </div>
  
  <!-- <UserInfo /> -->
</template>


<style scoped>
.profile_image {
  min-width: 200px;
  max-width: 30%;
  height: auto;
}

.grid-container {
  display: grid;
  grid-template-columns: 50% 50%;
  justify-content: center;
  align-items: center;
  /* gap: 10px; 각 아이템 사이에 10px 간격 추가 */
}

.info-container {
  /* background-color: aqua; */
  min-height: 100dvh;

  display: flex;
  justify-content: center;
}

/* 헤더 스타일 */
header {
  text-align: center;
  margin-bottom: 40px;
  font-size: 1.2rem;
}

.name {
  font-weight: bolder;
}

.info {
  font-size: 1.1rem;
  margin-bottom: 20px;
}

</style>
