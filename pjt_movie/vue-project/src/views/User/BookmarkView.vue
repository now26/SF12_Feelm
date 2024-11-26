<script setup>
// Router를 이동하기 위해 사용 (컴포넌트 이동)
import { useRouter, useRoute } from 'vue-router'
// useRouter : 보낼 때 사용
// useRoute : 받을 때 사용

import { onMounted } from 'vue'

const cartStore = useCartStore()
const router = useRouter()

onMounted(() => {

})

const goDetail = (movie) => {

}



</script>


<template>
  <div>
    <h1>Bookmark View</h1>
  </div>
</template>


<style scoped>

</style>
