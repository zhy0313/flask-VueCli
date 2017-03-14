import Vue from 'vue'
import Router from 'vue-router'
import Hot from '@/components/Hot'
import Login from '@/components/Login'
import Register from '@/components/Register'
import ForgotPassword from "@/components/Forgot-Password"
import PageView from '@/components/PageView'
import NewTopic from '@/components/NewTopic'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Hot',
      component: Hot,
      meta: {requiresAuth: true}
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {requiresNoAuth: true}
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: {requiresNoAuth: true}
    },
    {
      path: '/forgot-password',
      name: 'ForgotPassword',
      component: ForgotPassword,
      meta: {requiresNoAuth: true}

    },
    {
      path: '/ta/:topic_id',
      name: 'PageView',
      component: PageView,
      meta: {requiresAuth: true}
    },
    {
      path: '/open-topic',
      name: 'OpenTopic',
      component: NewTopic,
      meta: {requiresAuth: true}
    }

  ]
})
