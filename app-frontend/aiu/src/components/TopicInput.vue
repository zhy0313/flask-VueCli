<template>
  <div>
    <h3>New Topic</h3>
    <hr>
    <form>
      <div class="row">
        <div class="col-md-8 col-md-offset-2 col col-xs-12">
          <div class="form-group">
            <quill-editor id="editor"
                          ref="myTextEditor"
                          v-model="content">
            </quill-editor>

          </div>

          <div class="form-group">
            <input type="text" class="form-control" placeholder="Tags">
            <span><b>**</b> use comma for splitting tags</span>
          </div>


          <button class="btn btn-success btn-block">Post</button>
        </div>
      </div>

    </form>
  </div>

</template>


<script>
  export default{
      name: 'TopicInput',
      props:{
          postLink:{type: String, defualt:''}
      },
      components:{
      },
      data(){
          return{
            content:'',
          }
      }

  }
</script>

<style>
  #editor{
    height: 200px;
  }
</style>
