<template>
  <span>{{ submittedAt }}</span>
</template>

<script>

  export default{
    name: 'DynamicSubmittedAt',
    props: {date:{ type: '', default: null}},
    data(){
      return{
        submittedAt: this.$moment(this.date).fromNow(),
        intervalId: null
      }
    },
    methods: {
      dynamicSubmitDate: function () {
        this.submittedAt =  this.$moment(this.date).fromNow();
      }
    },
    mounted() {
      this.intervalId = setInterval(this.dynamicSubmitDate, 60 * 1000);
    },
    beforeDestroy(){
      clearInterval(this.intervalId)
    }

  }

</script>
