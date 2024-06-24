<template>
     <header class="p-3 text-bg-dark">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
          <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"/></svg>
        </a>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
         
          <li><router-link to="/"  class="nav-link px-2 text-white">Home</router-link></li>
        </ul>



        <div class="text-end" v-if="!auth">
          <router-link to="/login"  class="btn btn-outline-light me-2">Login</router-link>
          <router-link to="/register"  class="btn btn-outline-light me-2">Register</router-link>
        </div>
        <div class="text-end" v-if="auth">
          <router-link to="/"  class="btn btn-outline-light me-2" @click="logout">Logout</router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
     
  import { computed } from "vue";
   import axios from 'axios';
   import { useStore } from "vuex";
    export default {
      name: 'NavBar',
      setup(){
      const store = useStore()
        const auth = computed(() => store.state.auth)
    
          const logout = async () => {
            await axios.post('logout', {}, {withCredential: true})
            axios.defaults.headers.common['Authorization'] = ``
            await store.dispatch('setAuth', false)
          }
          return ({
            auth, logout
          })
      }
    }
   
</script>

<style scoped>

</style>