<template>
    <main class="form-signin w-100 m-auto">
  <form @submit.prevent="submit">
    <img class="mb-4" src="@/assets/dhaba.jpeg" alt="" width="150" height="75">
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <div class="form-floating">
      <input v-model="data.email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
  </form>
</main>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
    export default {
        name: 'LoginPage',
        setup() {
          const data = reactive ({
            
            email: '',
            password: ''
            
          })
          
          const router = useRouter();
          const submit = async () => {
            const response = await axios.post('login', data, {
              withCredentials: true
            });

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