<script setup>
import { useRouter } from 'vue-router'
// 데이터 가져오기
import { useCartStore } from '@/stores/carts';
const cartStore = useCartStore()

const router = useRouter()

const goDetail = (product) => {
  // router.push(`/cart/${product.id}`) // URL 경로로 이동하는 방식
  router.push({ name: 'CartDetailView', params:{ product_id : product.id }}) // 이름 기반 라우터 이동 (네이밍된 라우트 사용)
}

const deleteToCart = (product) => {
  cartStore.deleteToCart(product.id)
}

</script>


<template>
  <div>
    <h1>장바구니</h1>
    <div v-if="cartStore.carts.length > 0">

      <div class="product-list">
        <!-- {{ cartStore.products }} -->
      
        <!-- flex로 묶어주기 위해 div로 묶음 -->
        <!-- v-for를 쓸 때는 항상 key값을 함께 써주기 -->
        <div 
          v-for="product in cartStore.carts"
          :key='product.id'
          class="product-card"
        > 
          <!-- img :(v-bind)를 통해 바인딩 시키기 -->
          <img :src="product.image" alt="product_image" class="product-image">
          <div class="product-details">
            <h3> {{ product.title }}</h3>
            <p>Price : ${{ product.price }}</p>
            <button @click="goDetail(product)">Detail</button>&nbsp;
            <button @click="deleteToCart(product)">Delete</button>
          </div>
        </div>
        
      </div>
      
    </div>
    <div v-else>
      <p>장바구니가 비어있습니다.</p>
    </div>
  </div>
</template>


<style scoped>
.product-list{
  /* display: flex; -> 요소 가로로 위치 */
  display: flex;
  /* flex-wrap: wrap; -> 화면 내려가면 밑으로 내림 */
  flex-wrap: wrap;
  gap: 20px;
}

.product-card {
  border: 1px solid #000;
  width: 200px;
  padding: 15px;
}

.product-image {
  width: 100%;
}

.product-details {
  text-align: center;
}
</style>

