<template>
  <div>
    <app-in-menu></app-in-menu>
    <div class="container">
      <div v-if="isServerRun">
        <div class="row">
          <div class="col-md-11 col-sm-11 col-xs-8">
            <h4>{{ topic.title }}</h4>
          </div>
          <div class="col-md-1 col-sm-1 col-xs-4">
            <topic-button></topic-button>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-md-8 col-sm-9 col-xs-12">
            <ta-view :ta="topic"></ta-view>
            <div class="row" v-if="answers.length > 0">
              <h4>Answers <span>{{ answers.length }}</span></h4>
            </div>
            <hr>
            <ta-view v-for="answer in answers" :key="answer.id" :ta="answer"></ta-view>
          </div>
          <div class="col-md-3 col-md-offset-1 col-sm-2 col-sm-offset-1 col-xs-10 col-xs-offset-1">
            <ta-view-right :date="topic.submitted_at"
                           :viewed="topic.viewed"
                           :right="topic.right"></ta-view-right>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>


<script>
  import {clientKey} from '@/env';
  import {taViewUrl} from '@/config';
  import {auth} from '@/auth/Auth';
  import InMenu from '@/components/InMenu';
  import TAView from '@/components/TAView';
  import TAViewRightCol from '@/components/TAViewRightCol';
  import TopicButton from '@/components/TopicButton';

  export default{
      name:'PageView',
      components: {
          'app-in-menu': InMenu,
          'taView': TAView,
          'taViewRight': TAViewRightCol,
          'topicButton': TopicButton
      },
      data(){
        return{
          topic_id: this.$route.params.topic_id,
          topic: Object,
          answers: [],
          isServerRun: false
        }
    },
    methods: {
           getTa: function(){

               const data = {
                  topic_id: this.topic_id,
                  client_key: clientKey,
                  access_token: auth.getAccessToken()
               };

              this.$http.post(taViewUrl, data)
                .then( (response) => {
                    if(response.status == 200){
                        var body = response.body;
                        this.isServerRun = true;
                        if(body.is_ok){
                          this.topic = body.topic;
                          this.answers = body.answers;
                        }

                    }
                });
          }
    },
    created(){
        this.getTa();

    }
  }
</script>

<style>

  h4{
    color: #464643;
    font-size: 22px;
  }
</style>


