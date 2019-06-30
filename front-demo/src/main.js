import Vue from 'vue'
import App from './App.vue'
import 'vue-g2'
import VueRouter from 'vue-router'
import routes from '@/router/index.js'
import axios from '@/util/http.js'

Vue.use(VueRouter)

const router = new VueRouter({
	routes,
})


Vue.config.productionTip = false
Vue.prototype.axios = axios

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
