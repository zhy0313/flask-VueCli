<template>
  <div>
    <h4>Your Answer</h4>
    <hr>
      <div class="row">
        <div class="col-md-12 col-sm-12 col-xs-12">
          <div class="form-group">
            <quill-editor id="editor"
                          ref="myTextEditor"
                          v-model="answer.content">
            </quill-editor>

          </div>
          <button class="btn btn-success btn-block" @click="post">Post</button>
        </div>
      </div>
  </div>

</template>


<script>
  import {auth} from '@/auth/Auth';
  import {clientKey} from '@/env';
  import {newAnswerUrl} from '@/config';
  import toastr from 'toastr';

  export default{
      name: 'AnswerInput',
      props:{
      },
      components:{
      },
      data(){
          return{
            answer: {
                    content: '',
              }
          }
      },
      methods:{
          post: function () {
            const data = {
                topic_id: this.$route.params.topic_id,
                content: this.answer.content,
                access_token: auth.getAccessToken(),
                client_key: clientKey
            };
            this.$http.post(newAnswerUrl, data)
              .then( (response) => {
                  if(response.status == 200){
                      var body = response.body;
                      console.log(body);
                      if(body.is_ok){
                          toastr.success('answer is successfully created', 'Success');
                          this.$router.push({ path: 'ta/' + body.topic_id})

                      }
                      else{
                          toastr.error(body.error_message, 'Error');
                      }
                  }
                  else{
                    toastr.error(body.error_message, 'Error');
                  }
              });

          }
      }

  }
</script>

<style>
  #editor{
    height: 200px;
  }
</style>
