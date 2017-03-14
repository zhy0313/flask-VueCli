<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>


  export default {
    name: 'app',
    data: function(){
        return {

        }
    },

    methods: {
      loginControl: function (){
        this.$.menu.loginControl();
      }
    }

}


</script>

<style>
  @import "../static/css/font-awesome.min.css";

.container{
  padding-top: 80px;
}

</style>
