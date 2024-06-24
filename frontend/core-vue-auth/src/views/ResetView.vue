<template>
  <main class="form-signin w-100 m-auto">

   <form @submit.prevent="submit">
    <!-- <img class="mb-4" src="@/assets/dhaba.jpeg" alt="" width="150" height="75"> -->
    <h1 class="h3 mb-3 fw-normal">Reset Password</h1>

    <div class="form-floating">
      <input v-model="data.password"  type="password" class="form-control"   placeholder="Password">
      <label >Password</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password_confirm"  type="password" class="form-control"   placeholder="Confirm Password">
      <label >Confirm Password</label>
    </div>

    <button class="btn btn-primary w-100 py-2" type="submit">Submit</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
  </form>
  </main>
</template>

<script>
   

    import { reactive } from 'vue';
    import axios from 'axios';
    import { useRoute, useRouter } from 'vue-router';
    export default {
        name: "ResetView",
        setup(){
          const data = reactive ({

            password: '',
            password_confirm: ''
            
          })
          
          const route = useRoute();
          const router = useRouter()
          const submit = async () => {
            await axios.post('reset', {...data, token: route.params.token})
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