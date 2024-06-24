<template>
  <main class="form-signin w-100 m-auto">
    <form  @submit.prevent="submit">
    <!-- <img class="mb-4" src="../src/assets/logo.png" alt="" width="72" height="57"> -->
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input  v-model="data.email" type="email" class="form-control mt-3" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input  v-model="data.password" type="password" class="form-control mt-3" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>
    <div>
        <router-link to="/forgot">Forgot password?</router-link>
    </div>

   
    <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Sign in</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
  </form>
</main>
</template>

<script lang="ts">
import { reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
 export default {
    name: "LoginView",
    setup() {
          const data = reactive ({
            
            email: '',
            password: ''
            
          })
          
          const router = useRouter();
          const submit = async () => {
            console.log('submitting');
            const response = await axios.post('login', data, {
              withCredentials: true
            });
            console.log(response);
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`
            await router.push('/')
          }
          return ({
            data, submit
          })

        }
 }
</script>

<style scoped>

</style>