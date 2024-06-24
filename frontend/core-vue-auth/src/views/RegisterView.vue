<template>
  <main class="form-signin w-100 m-auto">
   <form @submit.prevent="submit">
    <!-- <img class="mb-4" src="@/assets/dhaba.jpeg" alt="" width="150" height="75"> -->
    <h1 class="h3 mb-3 fw-normal">Register New User</h1>

    <div class="form-floating">
      <input v-model="data.first_name" class="form-control mt-3"   placeholder="First Name">
      <label>First Name</label>
    </div>
    <div class="form-floating">
      <input v-model="data.last_name"  class="form-control mt-3"   placeholder="Last Name">
      <label  >Last Name</label>
    </div>
    <div class="form-floating">
      <input v-model="data.email"  type="email" class="form-control mt-3"   placeholder="Email">
      <label  >Email address</label>
    </div>

    <div class="form-floating">
      <input v-model="data.password"  type="password" class="form-control mt-3"   placeholder="Password">
      <label >Password</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password_confirm"  type="password" class="form-control mt-3"   placeholder="Confirm Password">
      <label >Confirm Password</label>
    </div>

    <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Register</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
  </form>
  </main>
</template>

<script lang="ts">
   import { reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
    export default {
        name: "RegisterView",
        setup(){
          const data = reactive ({
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            password_confirm: ''
            
          })
          
          const router = useRouter();
          const submit = async () => {
            await axios.post('register', data)
            await router.push('/login')
          }
          return ({
            data, submit
          })
        }
    }
</script>

<style scoped>

</style>