<template>
  <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="/">app</a>
      </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="navbar">
        <ul class="nav navbar-nav">
          <li ><router-link to="/" tag="a">hot</router-link></li>
          <li ><router-link to="" tag="a">new</router-link></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="" @click="logout">logout</a></li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
  </nav>
</template>

<script>
  import {auth} from '@/auth/Auth';

  export default{
    name:'Menu',
    data: function () {
      return{
      }
    },
    methods: {
      logout: function () {
        auth.destroyAuthendication();
        this.$router.push({name:'Login'});

      }
    }

  }

</script>
