<template>
<p> {{ name }}</p>
</template>

<script>

export default {
  props: {
    jsonData: {
      type: Object
    },
    name:{
        type: String
    },
  }
};
</script>