<template>
  <div class="row">
    <div class="row">
      <p><span class="info">asked</span> <submitted-at :date="date"></submitted-at></p>
    </div>
    <div class="row">
      <p><span class="info">viewed</span> <span>{{ viewed }}</span> times</p>
    </div>
    <div class="row" v-if="linkedUrls.length > 0">
      <h3>Linked</h3>
      <p v-for="linkedUrl in linkedUrls"><a :href="linkedUrl.href">{{ linkedUrl.title }}</a></p>
    </div>
    <div class="row">
      <h3>Related</h3>
      <p v-if="relatedUrls.length == 0">There is no related topic url</p>
      <p v-for="relatedUrl in relatedUrls"><a :href="relatedUrl.href">{{ relatedUrl.title }}</a></p>
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
      props:{date:{ type: String, default:''}, viewed:{type: Number, default:0} ,linkedUrls:{ type: Array, default:[]}, relatedUrls: {type: Array, default: []}}
  }
</script>

<style>
  .info {
    color: #8f8c91;
  }
</style>
