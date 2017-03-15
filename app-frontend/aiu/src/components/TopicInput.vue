<template>
  <div>
    <h3>New Topic</h3>
    <hr>
      <div class="row">
        <div class="col-md-8 col-md-offset-2 col col-xs-12">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Title" v-model="topic.title">
          </div>
          <div class="form-group">
            <quill-editor id="editor"
                          ref="myTextEditor"
                          v-model="topic.content">
            </quill-editor>

          </div>

          <div class="form-group">
            <input type="text" class="form-control" placeholder="Tags">
            <span><b>**</b> use comma for splitting tags</span>
          </div>


          <button class="btn btn-success btn-block" @click="post">Post</button>
        </div>
      </div>
  </div>

</template>


<script>
  import {auth} from '@/auth/Auth';
  import {clientKey} from '@/env';
  import {newTopicUrl} from '@/config';
  import toastr from 'toastr';
  export default{
      name: 'TopicInput',
      props:{
          postLink:{type: String, defualt:''}
      },
      components:{
      },
      data(){
          return{
            topic: {
                    title: '',
                    content: '',
                    tags: ''
              }
          }
      },
      methods:{
          post: function () {
            const data = {
                title: this.topic.title,
                content: this.topic.content,
                tags: this.topic.tags,
                access_token: auth.getAccessToken(),
                client_key: clientKey
            };
            this.$http.post(newTopicUrl, data)
              .then( (response) => {
                  if(response.status == 200){
                      var body = response.body;
                      console.log(body);
                      if(body.is_ok){
                          toastr.success('Topic is successfully created', 'Success');
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
