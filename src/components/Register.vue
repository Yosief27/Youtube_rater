<template>
  <div class="">
    <h1>User Registration</h1>
    <form id="formvideo" @submit.prevent="CreateUser">
      <p>
        <label for="username">User Name </label>
        <input
          class="ml-2"
          type="text"
          name="username"
          id="username"
          v-model="username"
        />
      </p>
      <p>
        <label for="password">Pass Word</label>
        <input
          type="password"
          class="ml-2"
          name="password"
          id="password"
          v-model="password"
        />
      </p>
      <p>
        <input type="submit" value="Submit" />
      </p>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "resgiter",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    CreateUser() {
      axios
        .post("http://127.0.0.1:8000/api/users/", {
          username: this.username,
          password: this.password,
        })
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
      // redirecting the user into the main page which is in our case the home vue
      this.$router.push("/");
    },
  },
};
</script>

<style>
</style>