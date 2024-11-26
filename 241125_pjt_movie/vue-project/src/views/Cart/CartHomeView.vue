<script setup>
// Router를 이동하기 위해 사용 (컴포넌트 이동)
import { useRouter, useRoute } from 'vue-router'
// useRouter : 보낼 때 사용
// useRoute : 받을 때 사용

import { onMounted } from 'vue'
import { useCartStore } from '@/stores/carts';

const cartStore = useCartStore()
const router = useRouter()

// <'onMounted' 를 권장하는 이유>
// API로 데이터를 다운로드 받는 것 -> setup에서 일반 호출하는 게 맞을까? (답-> 아니다.)
// 이때 발생할 수 있는 문제점 -> 
    // 1. setup은 기본적으로 DOM(template 부분)이 그려진 후에 호출이 된다. 
    // 2. 그래서 setup에서 데이터를 그냥 다운 받으면, DOM은 (화면)렌더링(DOM 그리기)을 해야 하는데 그려야할 데이터를 못 받아오는 상태가 된다.
    // 3. 없는 데이터를 자꾸 받아오려고 하다보니까 오류가 발생한다.
// 따라서 데이터 다운로드는 DOM이 그려지기 전에 가져오는 것을 권장한다.
// 그래서 활용되는 것이 'onMounted' 이다. (데이터를 받는 부분을 onMounted의 콜백함수로 넣어주어 DOM이 그려지기 전에 데이터를 받아오기 위함.)

onMounted(() => {
  cartStore.getProducts()
})

const goDetail = (product) => {
  // router.push(`/cart/${product.id}`) // URL 경로로 이동하는 방식
  router.push({ name: 'CartDetailView', params:{ product_id : product.id }}) // 이름 기반 라우터 이동 (네이밍된 라우트 사용)
}

const addToCart = (product) => {
  cartStore.addToCart(product)
  // router.push(`/cart`)
  router.push({ name: 'CartView' })
}

</script>


<template>
  <h1>상품 목록 리스트</h1>

  <div class="product-list">
    <!-- {{ cartStore.products }} -->

    <!-- flex로 묶어주기 위해 div로 묶음 -->
    <!-- v-for를 쓸 때는 항상 key값을 함께 써주기 -->
    <div 
      v-for="product in cartStore.products"
      :key='product.id'
      class="product-card"
    > 
      <!-- img :(v-bind)를 통해 바인딩 시키기 -->
      <img :src="product.image" alt="product_image" class="product-image">
      <div class="product-details">
        <h3> {{ product.title }}</h3>
        <p>Price : ${{ product.price }}</p>
        <p>Category : {{ product.category }}</p>
        <p>Description : {{ product.description }}</p>
        <button @click="goDetail(product)">Detail</button>&nbsp;
        <button @click="addToCart(product)">Cart</button>
      </div>
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
