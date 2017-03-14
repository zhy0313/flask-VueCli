<template>
  <div class="row">
    <div class="row">
      <p><span class="info">asked</span> <submitted-at :date="date"></submitted-at></p>
    </div>
    <div class="row">
      <p><span class="info">viewed</span> <span>{{ viewed }}</span> times</p>
    </div>
    <div class="row">
      <h3>Linked</h3>
      <p v-for="linked in right.linkeds"><a :href="linked.href">{{ linked.title }}</a></p>


    </div>
    <div class="row">
      <h3>Related</h3>
      <p v-for="related in right.relateds"><a :href="related.href">{{ related.title }}</a></p>
    </div>
  </div>
</template>

<script>
  import DynamicSubmittedAt from '@/components/DynamicSubmittedAt';
  export default{
      name: "TAViewRightCol",
      components:{
          'submittedAt': DynamicSubmittedAt
      },
      props:{date:{ type: String, default:''}, viewed:{type: Number, default:0} ,right:{ type: Object, default:null}}
  }
</script>

<style>
  .info {
    color: #8f8c91;
  }
</style>
