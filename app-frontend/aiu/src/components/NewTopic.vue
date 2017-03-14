<template>
  <div>
    <app-in-menu></app-in-menu>
    <div class="container">
      <topic-input></topic-input>
    </div>
  </div>
</template>

<script>
  import InMenu from '@/components/InMenu';
  import TopicInput from '@/components/TopicInput'
  export default{
    name: 'NewTopic',
    components:{
        'topicInput': TopicInput,
        'app-in-menu': InMenu
    }
  }

</script>
