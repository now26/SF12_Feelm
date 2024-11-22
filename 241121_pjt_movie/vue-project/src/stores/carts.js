import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

import { useCounterStore } from './counter'


export const useCartStore = defineStore('cart', () => {

    let products = ref([])
    let carts = ref([])

    const getProducts = () => {

      axios.get('https://fakestoreapi.com/products')
      .then((res) => {
        console.log(res)
        products.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }

    const getProductById = (id) => {
      const product = products.value.find((el) => {
        return el.id == id
      })
      // console.log("product = ", product)
      return product
    }


    const addToCart = (product) => {
      const index = carts.value.findIndex((el) => el.id === product.id)

      if (index === -1) {
        alert('장바구니 페이지로 이동합니다.')
        carts.value.push(product)
      } else{
        alert('이미 추가된 상품입니다.')
      }
    }

    const deleteToCart = (productId) => {
      const index = carts.value.findIndex((el) => el.id === productId)


      if (index !== -1){
        carts.value.splice(index, 1);
      }
    }


  return {
    products,
    carts,
    getProducts,
    getProductById,
    addToCart,
    deleteToCart
  }

}, { persist: true })