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
  <div>
    <div>
      <!-- nickname이 없으면 username을 사용 -->
      <h3>{{ userDB.nickname || userDB.username }}님 안녕하세요!</h3>
    </div>


    <div class="grid-container">
      <div>
        <!-- 이미지가 없으면 defaultImage로 대체 -->
        <img :src="profileImageUrl" alt="profile_image" class="profile_image">

        <!-- <img :src="userDB.profile_image || defaultImage_chick" alt="profile_image" class="profile_image"> -->
      </div>
  
      <div>
        <p>username : {{ userDB.username }}</p>
        <p>nickname : {{ userDB.nickname }}</p>
        <p>age : {{ userDB.age }}</p>
        <p>gender : {{ userDB.gender }}</p>
      
      </div>
    </div>
    
    <!-- <UserInfo /> -->
  </div>
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
  /* gap: 10px; 각 아이템 사이에 10px 간격 추가 */
}

</style>
