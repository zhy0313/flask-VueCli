<template>
  <div>
    <div class="row">
      <div class="col-lg-2  col-md-2 col-xs-2"> <!-- rank and voting-->
        <div class="text-center">
          <div class="row">
                <div class="col-md-6 col-xs-5 col-xs-offset-1">
                    <div class="row">
                        <span class="rating-answer">{{ topic.vote }}</span>
                    </div>
                    <div class="row">
                        <span class="rating-answer">
                            Votes
                        </span>
                    </div>
                </div>
                <div class="col-md-6 col-xs-5 col-xs-offset-1">
                    <div class="row">
                        <span class="rating-answer">{{ topic.answer }}</span>
                    </div>
                    <div class="row">
                        <span class="rating-answer">
                            Answers
                        </span>
                    </div>
                </div>
          </div>
        </div>
      </div>
      <div class="col-lg-10 col-md-10 col-xs-10">
        <div class="row">
          <div class="col-md-12 col-pull-left">
            <router-link :to="{ path: 'ta/' + topic.id}" class="title">{{ topic.title }}</router-link>
            <div class="row">
              <div class="col-md-12 col-xs-12">
                  <p class="submit-info pull-right">submitted <span>{{ topic.submitted_at | moment('from', 'now') }}</span> by <a href="">{{ topic.submitted_by }}</a></p>
              </div>
            </div>


            <!-- tags -->
            <div class="">
                <a href="#" v-for="tag in topic.tags">
                    <span class="badge">{{ tag }}</span>
                </a>
            </div>
            <!-- end tags -->
          </div>
        </div>

      </div>
    </div>

    <hr>

  </div>
</template>


<script>
  export default{
    name: 'TopicPreview',
    props:{ 'topic':{ type:Object, default: null}},
    data(){
      return{
       }
    },
    methods:{
    }

  }


</script>

<style>


.rating-answer{
  color: #8f8c91;
  font-size: 14px;
}
.title{
    color: #913f44;
    font-size: 19px;
}
.col-pull-left{
 }
 .col-push-right{
     padding-right: 15px;
 }
.submit-info{
    padding-top: -10px;
    color: #8f8c91;
}
hr{
     padding-top: 0px;
     padding-bottom: 0px;
}
</style>
