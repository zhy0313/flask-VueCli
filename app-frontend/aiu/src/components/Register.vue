<template>
  <div>
    <app-menu></app-menu>
    <div class="container">
    <div id="logo-form-space">
      <form action="index.html" method="post">

        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <input type="email" class="form-control"  placeholder="E-Mail" v-model="user.email">
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <input type="password" class="form-control" placeholder="Password" v-model="user.password">
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Nick" v-model="user.nick">
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <button type="button" name="button" class="btn btn-success btn-block" @click="register">Sign up</button>
            </div>
          </div>
        </div>
      </form>
    </div>

  </div>
  </div>
</template>

<script>
  import {registerUrl} from '@/config';
  import {clientKey} from '@/env';
  import Menu from '@/components/Menu';
  import toastr from "toastr"

  export default{
    name: 'register',
    components:{
        'app-menu':Menu
    },
    data() {
      return{
        user: {
            email: '',
            password: '',
            nick: ''
        },
        is_error_exist: true,
        error_message: 'this is fucking error'
      }
    },
    methods: {
        register: function () {
            const data = {
                email: this.user.email,
                password: this.user.password,
                nick: this.user.nick,
                client_key: clientKey
            };

            this.$http.post(registerUrl, data)
              .then( (response) => {
                  if(response.status == 200){
                      var body = response.body;
                      if(body.is_ok){
                          toastr.success("","Registered Successfully");
                          this.$router.push({name: 'Login'})
                      }
                      else{
                          toastr.error(body.error_message);
                      }
                  }


            });
        }
    }
  }
</script>

<style>

</style>
