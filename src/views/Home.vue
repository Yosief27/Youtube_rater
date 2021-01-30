<template>
  <div class="home">
    <ListVideos msg="Your List of Videos " />
  </div>
</template>

<script>
import ListVideos from "@/components/ListVideos.vue";

export default {
  name: "Home",
  components: {
    ListVideos,
  },
};
</script>
