<template>
<div>
<p v-for="value in jsonData"
    v-bind:key="value"
>
{{ value }}
</p>
</div>
</template>

<script>
export default{
props: {
    jsonData:{
        type: Object,
    }
    },
}
</script>