// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import resource from 'vue-resource'
import moment from 'vue-moment'
import VueQuillEditor from 'vue-quill-editor'
import {auth} from '@/auth/Auth'

Vue.use(resource)
Vue.use(moment)
Vue.use(VueQuillEditor)


router.beforeEach((to, from, next) => {
  console.log('test')
  if (to.meta.requiresAuth) {
      if (!auth.isAuhthendicated()){
        next({
          name: 'Login'
        })
      }
      else{
        next();
      }
  }
  else if(to.meta.requiresNoAuth){
    if (auth.isAuhthendicated()){
      next({
        name: 'Hot'
      })
    }
    else{
      next();
    }
  }
  else{
    next();
  }

});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
