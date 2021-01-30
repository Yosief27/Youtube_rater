<template>
  <div class="">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand class="text-white" href="#">Youtube Rater</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"> </b-navbar-toggle>

      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit.prevent="login" v-if="token == null">
          <b-form-input
            id="username"
            size="sm"
            class="mr-sm-2"
            v-model="username"
            placeholder="username"
            name="username"
          ></b-form-input>
          <b-form-input
            id="password"
            size="sm"
            class="mr-sm-2"
            placeholder="password"
            type="password"
            v-model="password"
            name="password"
          ></b-form-input>

          <b-button size="sm" class="my-2 my-sm-0" type="submit"
            >Login</b-button
          >
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button type="submit" size="sm" class="my-2 ml-2"> Logout</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="register" v-if="token === null">
          <b-button
            :to="{ name: 'register' }"
            type="submit"
            size="sm"
            class="my-2 ml-2"
          >
            Register</b-button
          >
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
      token: null,
    };
  },
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/auth/", {
          username: this.username,
          password: this.password,
        })
        .then((res) => {
          this.token = res.data.token;
          localStorage.setItem("user-token", res.data.token);
          console.log(res.data.token);
        })
        .catch((err) => {
          localStorage.removeItem("user-token");
        });
    },
    logout() {
      localStorage.removeItem("user-token");
      this.token = null;
      this.username = "";
      this.password = "";
    },
  },
  register() {},
  created() {
    this.token = TokenService.getToken() || null;
  },
};
</script>

<style>
</style>