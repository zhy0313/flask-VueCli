<template>
  <div>
    <app-menu></app-menu>
    <div class="container">
      <div id="logo-form-space">
        <form action="index.html" method="post">
          <div class="row">
            <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
              <div class="form-group">
                <input type="email" class="form-control" placeholder="E-Mail" v-model="user.email">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
              <div class="form-group">
                <input type="password" class="form-control"  placeholder="Password" v-model="user.password">
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
              <button type="button" class="btn btn-success btn-block" @click="login">Login</button>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
              <router-link to="forgot-password" href="" class="">Forgot password</router-link>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>

</template>

<script>
  import Menu from '@/components/Menu';
  import toastr from "toastr";
  import {loginUrl} from '@/config';
  import {clientKey} from '@/env';
  import {auth} from '@/auth/Auth';

  export default{
      name: 'login',
      components:{
      'app-menu': Menu
    },
      data() {
          return{
            user: {
              email: '',
              password: ''
            }
          }
      },
      methods: {
          login: function () {
              const data = {
                  email: this.user.email,
                  password: this.user.password,
                  client_key: clientKey
              };

              this.$http.post(loginUrl, data)
                .then( (response) => {
                    if(response.status == 200){
                      var body = response.body;
                      if(!body.is_ok){
                        toastr.error(body.error_message, 'Login Error');
                      }
                      else {
                        auth.setAuthendicated(body.access_token);
                        toastr.success('', 'Logged In');
                        this.$router.push({name:'Hot'});
                      }
                    }
                });
          }
      },

  }
</script>

<style>
  #top-space{
    padding-top: 50px;
  }
  #logo{
    width: 200px;
  }
  #logo-form-space{
      padding-top: 200px;

  }
</style>
