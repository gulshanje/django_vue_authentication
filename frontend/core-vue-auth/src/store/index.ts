import { ActionContext, createStore } from 'vuex'

export default createStore({
  state: {
    auth: false
  },
  getters: {

  },
  mutations: {
    setAuth(state: {auth: boolean}, auth: boolean) {
      state.auth = auth
    }
  },
  actions: {
    setAuth(context: ActionContext<any, any>, auth: boolean){
      context.commit('setAuth', auth)
    }
    
  },
  modules: {
  }
})
