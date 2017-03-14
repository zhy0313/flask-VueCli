<template>
  <div>
    <app-menu></app-menu>
    <div class="container">
    <div id="logo-form-space">
      <form action="index.html" method="post">

        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <input type="email" class="form-control"  placeholder="E-Mail">
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <div class="form-group">
              <button type="button" name="button" class="btn btn-success btn-block" v-on:click="send">Submit</button>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4 col-md-offset-4 col-xs-10 col-xs-offset-1">
            <router-link to="login" tag="a" class="pull-left">Redirect to login page</router-link>
          </div>
        </div>
      </form>
    </div>

  </div>
  </div>
</template>

<script>
  import toastr from "toastr";
  import Menu from '@/components/Menu';
  export default{
    name: 'register',
    components:{
        'app-menu': Menu
    },
    data() {
      return{
        newUser: {
          email: '',
          password: '',
          nick: ''
        },
        is_error_exist: true,
        error_message: 'this is fucking error'
      }
    },
    methods: {
      send: function () {
          toastr.success('Check your inbox','Mail is sent');
          this.$router.push('/login');
      }
    }
  }
</script>

<style>

  #logo{
    width: 200px;
  }
  #logo-form-space{  }
</style>
