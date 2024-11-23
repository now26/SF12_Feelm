<script setup>
import { useCartStore } from '@/stores/carts';
import { useRoute } from 'vue-router'
// 전달받은 것으로 부터 세부사항을 꺼내오기 위해 useRoute(받을 때 사용) 사용
const route = useRoute() 

const cartStore = useCartStore()

const productId = route.params.product_id
const product = cartStore.getProductById(productId)
// console.log("product in component = ", product)


</script>


<template>
  <h1>상세 페이지</h1>

  <div>
    <div v-if="product !== null">
      <img :src="product.image" alt="product_image" width="200px">
      <h3>{{ product.title }}</h3>
      <p>가격: {{ product.price }}</p>
      <p>카테고리: {{ product.category }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>

    </div>
  </div>
</template>


<style scoped>

</style>
