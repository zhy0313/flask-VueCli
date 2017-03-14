<template>
  <div>
    <app-in-menu></app-in-menu>
    <div class="container">
      <div v-if="isServerRun">
        <div class="row">
          <div class="col-md-11 col-sm-11 col-xs-8">
            <h4>{{ topic.topic.title }}</h4>
          </div>
          <div class="col-md-1 col-sm-1 col-xs-4">
            <topic-button></topic-button>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-md-8 col-sm-9 col-xs-12">
            <ta-view :ta="topic.topic"></ta-view>
            <div class="row" v-if="topic.answers.length > 0">
              <h4>Answers <span>{{ topic.answers.length }}</span></h4>
            </div>
            <hr>
            <ta-view v-for="answer in topic.answers" :key="answer.id" :ta="answer"></ta-view>
          </div>
          <div class="col-md-3 col-md-offset-1 col-sm-2 col-sm-offset-1 col-xs-10 col-xs-offset-1">
            <ta-view-right :date="topic.topic.submitted_at"
                           :viewed="topic.topic.viewed"
                           :right="topic.right"></ta-view-right>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>


<script>
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
          isServerRun: false
        }
    },
    methods: {
           getTa: function(){
//            this.$http.get(Config.WEB_LINK + '/api/detail/' + this.topic_id)
//              .then( (response) => {
//                  if(response.status == 200){
//                      this.topic = response.body;
//                      this.isServerRun = true;
//                  }
//              });
          }
    },
    created(){
        //this.getTa();
    }
  }
</script>

<style>

  h4{
    color: #464643;
    font-size: 22px;
  }
</style>


