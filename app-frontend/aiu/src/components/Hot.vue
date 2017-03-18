<template>
    <div>
      <app-in-menu></app-in-menu>
      <div class="navbar-hot">
        <div class="container">
          <div class="row">
            <div class="col-md-12 col-xs-12">
              <div class="pull-right">
                <topic-button></topic-button>
              </div>
            </div>
          </div>
          <hr>
          <h3 v-if="!isServerRun">Server is not responsing</h3>
          <preview v-if="isServerRun" :topic="topic" v-for="topic in topics" :key="topic.id"></preview>

        </div>
      </div>
    </div>
</template>

<script>
  import {clientKey} from '@/env';
  import {auth} from '@/auth/Auth'
  import {hotUrl} from '@/config';
  import InMenu from '@/components/InMenu';
  import TAPreview from  '@/components/TAPreview';
  import TopicButton from '@/components/TopicButton';

  export default{
      name:'Hot',
      components: {
          'preview': TAPreview,
          'topicButton': TopicButton,
          'app-in-menu': InMenu
      },
      data(){
          return{
              topics: [],
              isServerRun: false,
              intervalId: 0
          }
      },
      methods:{
          fetchTopics: function () {
              var data = {
                  access_token: auth.getAccessToken(),
                  client_key: clientKey
              }
              this.$http.post(hotUrl, data)
                .then((response)=>{
                    if(response.status == 200){
                      this.isServerRun = true;
                      var body = response.body;
                      if(body.is_ok){
                          this.topics = body.topics;

                      }
                    }
                })
          }
      },
      created() {

          this.fetchTopics();

      },
      mounted: function () {
          this.fetchTopics();
      }

  }

</script>


<style>
  .btn-topic{
    background-color: #0082ff;
    color: #ffffff;
  }

</style>
