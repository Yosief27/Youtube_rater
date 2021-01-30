<template>
  <div class="" v-if="msg.title != null">
    <div class="row">
      <div class="col-md-10">
        <p class="mb-3">Title: {{ msg.title }}</p>

        <p>Description: {{ msg.description }}</p>

        <p>Rating: {{ msg.rating_average }}</p>

        <p>Comments: {{ msg.comments_list }}</p>

        <p>
          <iframe
            width="400"
            height="300"
            :src="msg.url"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </p>
        <p>Category: {{ msg.category }}</p>
        <form @submit.prevent="addRating(msg)" @submit="$emit('updated')">
          <p>
            <lable for="stars">Ratings</lable>
            <input type="text" class="ml-2" id="stars" v-model="stars" />
          </p>
          <p>
            <lable for="comments">Comments</lable>
            <input type="text" class="ml-2" id="comments" v-model="comments" />
          </p>
          <p>
            <input class="btn-primary" type="submit" value="Submit Rating" />
          </p>
        </form>
        <button
          v-on:click="deleteVideo(msg)"
          @click="$emit('updated')"
          class="btn-sm btn-danger mt-2 mb-2"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { TokenService } from "../storage/service";
import axios from "axios";
export default {
  name: "VideoDetails",
  props: {
    msg: Object,
  },
  data() {
    return {
      stars: 0,
      comments: "",
    };
  },
  methods: {
    deleteVideo(video_delete) {
      // the data to be deleted
      let postdata = {
        video: video_delete.id,
      };
      // user identfier token
      let axiosconfig = {
        headers: { Authorization: "Token " + this.token },
      };

      axios
        .delete(
          `http://127.0.0.1:8000/api/videos/${video_delete.id}`,
          axiosconfig
        )
        .then((res) => console.log(res.data))
        .catch((err) => console.log(err));
    },
    addRating(video) {
      this.token = TokenService.getToken();
      console.log(this.token);
      console.log(this.stars);
      console.log(this.comments);
      let axiosconfig = {
        headers: { Authorization: "Token " + this.token },
      };
      var postData = {
        stars: this.stars,
        comments: this.comments,
      };
      axios
        .post(
          `http://127.0.0.1:8000/api/videos/${video.id}/rate_video/`,
          postData,
          axiosconfig
        )
        .then((res) => console.log(res.data))
        .catch((err) => console.log(err));
    },
  },
  created() {
    let token;
    this.token = TokenService.getToken();
  },
};
</script>

<style>
</style>