<template>
  <div class="">
    <div class="col-md-12 mb-5" v-if="createNew">
      <CreateVideo @updated="updateVideo()" />
    </div>
    <form @submit="createdNewVideo()">
      <input
        class="btn-sm btn-primary mb-3 btn-center"
        id="cretedVideo"
        type="submit"
        value="Create New Video"
      />
    </form>

    <div class="row">
      <div class="col-md-5 text-center nicefont">
        <h1>{{ msg }}</h1>
        <button v-on:click="getvideos()">Check videos</button>
        <br />
        <div v-bind:key="video.id" v-for="(video, val) in video_list">
          {{ val + 1 + ":" + "\t" + video.title }}
          <br />
          <p>Rating : {{ video.rating_average }}</p>
          <p>Comments : {{ video.comments_list }}</p>

          <button
            class="btn btn-primary mt-2 mb-3"
            v-on:click="sendVideoDetail(video)"
          >
            Details
          </button>
        </div>
      </div>
      <div class="col-md-6">
        <VideoDetails :msg="video_detail" v-on:updated="updateVideo()" />
      </div>
    </div>
  </div>
</template> 

<script>
import axios from "axios";
import VideoDetails from "./VideoDetails.vue";
import CreateVideo from "./CreateVideo.vue";
export default {
  name: "ListVideos",
  components: {
    VideoDetails,
    CreateVideo,
  },
  props: {
    msg: Object,
  },
  data() {
    return {
      video_list: [],
      video_detail: Object,
      createNew: "",
    };
  },
  methods: {
    getvideos() {
      axios
        .get(" http://127.0.0.1:8000/api/videos/")
        .then((result) => (this.video_list = result.data))
        .catch((err) => console.log(err));
    },
    createdNewVideo() {
      this.createNew = !this.createNew;
    },
    sendVideoDetail(video) {
      this.video_detail = video;
    },
    updateVideo(video) {
      this.timer = setTimeout(() => {
        axios
          .get(" http://127.0.0.1:8000/api/videos/")
          .then((res) => (this.video_list = res.data))
          .catch((err) => console.log(err));
      }, 600);
    },
  },
  // before the html is created we will have all our variable or opertions under the creation will be executed and ready to be used
  created() {
    this.getvideos();
    this.createNew = false;
  },
};
</script>

<style >
@import url("https://fonts.googleapis.com/css2?family=Slabo+27px&display=swap");
.nicefont {
  font-size: 1.5rem;
  font-family: "Slabo ", serif;
}
</style>