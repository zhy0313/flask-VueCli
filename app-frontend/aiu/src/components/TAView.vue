<template>
  <div class="row topic">
    <div class="col-md-1 col-sm-1 col-xs-2">
      <div class="row text-center">
        <a href="" @click="vote('UP', $event)" v-if="!ta.is_up_voted"><i class="fa fa-angle-up fa-3x up-down"></i></a>
        <a href="" @click="vote('UP', $event)" v-if="ta.is_up_voted"><i class="fa fa-angle-up fa-3x uped-downed"></i></a>
      </div>
      <div class="row text-center">
          <div class="">
            <span class="rating">{{ ta.vote }}</span>
          </div>
      </div>
      <div class="row text-center">
        <a href="" @click="vote('DOWN', $event)" v-if="!ta.is_down_voted"><i class="fa fa-angle-down fa-3x up-down"></i></a>
        <a href="" @click="vote('DOWN', $event)" v-if="ta.is_down_voted"><i class="fa fa-angle-down fa-3x uped-downed"></i></a>
      </div>
      <div v-if="ta.is_topic" class="row text-center">
        <a v-if="!ta.is_stared" href="" @click="star($event)"><i class="fa fa-star-o fa-2x star"></i></a>
        <a v-if="ta.is_stared" href="" @click="star($event)"><i class="fa fa-star fa-2x stared"></i></a>
      </div>
    </div>
    <div class="col-md-11 col-sm-11 col-xs-10">
        <p v-html="ta.content"></p>
        <div class="" v-if="ta.is_topic">
          <a href="" v-for="tag in ta.tags">
          <span class="badge">{{ tag }}</span>
          </a>
        </div>
        <div v-else="ta.is_topic" class="author-space"></div>
    </div>

    <div class="col-md-12 col-sm-12 col-xs-12 author">
      <p class="submit-info pull-right">submitted <submitted-at :date="ta.submitted_at"></submitted-at> by <a href="">{{ ta.submitted_by }}</a></p>
    </div>
  </div>
</template>

<script>
  import {auth} from '@/auth/Auth';
  import {clientKey} from '@/env';
  import {voteTopicUrl, starTopicUrl} from '@/config';
  import DynamicSubmittedAt from '@/components/DynamicSubmittedAt';
  import toastr from 'toastr';

  export default{
    name: '',
    props: {ta:{ type: Object, default: null}},
    data(){
        return{
            intervalId: null
        }
    },
    components:{
        'submittedAt': DynamicSubmittedAt
    },
    methods: {
        vote: function (voteDirection, event) {
            event.preventDefault();
            var data = {
              topic_id: this.ta.id,
              vote: voteDirection,
              client_key: clientKey,
              access_token: auth.getAccessToken()
            };
           if (this.ta.is_topic){
                this.$http.post(voteTopicUrl, data)
                  .then( (response) => {
                      if(response.status == 200){
                          var body = response.body;
                          console.log(body);
                          if(body.is_ok){
                              location.reload();
                          }
                          else{
                              toastr.error(body.error_message, 'Fail')
                          }
                      }
                  })
            }
            else{
                // for answwer vote
            }
        },
        star: function (event) {
            event.preventDefault();
          var data = {
            topic_id: this.ta.id,
            client_key: clientKey,
            access_token: auth.getAccessToken()
          };

          this.$http.post(starTopicUrl, data)
            .then( (response) => {
                if(response.status == 200){
                    var body = response.body;
                    console.log(body)
                    if(body.is_ok){
                        location.reload();
                    }
                    else{
                      toastr.error('Topic is not stared','Fail');
                    }
                }
            });
        }


    },
    mounted() {
        console.log(this.ta.is_stared)
    },
    beforeDestroy(){
    }

  }

</script>



<style>
  .up-down{
    color: #464348;
  }
  .uped-downed{
    color: #ff5f33;
  }
  .star{
    color: #93939a;
  }
  .stared{
    color: #ff9658;
  }
  .rating{
    color: #464348;
    font-size: 16px;
  }
  .author-space{
    padding-top: 10px;
  }
  .author{
    position: absolute;
    bottom: -20px;
  }

  .topic{
    witdh: 100%;
    position: relative;

  }

</style>

