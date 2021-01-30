<template>
  <div>
    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-bod">
            <form id="formvideo" @submit.prevent="checkFrom()">
              <p>
                <label for="title">Title</label>
                <input
                  class="ml-2"
                  type="text"
                  name="title"
                  id="title"
                  v-model="title"
                />
              </p>
              <p>
                <label for="description">Description</label>
                <input
                  class="ml-2"
                  type="textarea"
                  name="description"
                  id="description"
                  v-model="description"
                />
              </p>
              <p>
                <label for="url">Url</label>
                <input
                  class="ml-2"
                  type="text"
                  name="url"
                  id="url"
                  v-model="url"
                />
              </p>
              <p>
                <label for="category">Category</label>
                <select
                  class="ml-2"
                  type="text"
                  name="category"
                  id="category"
                  v-model="category"
                >
                  <option>Web_development</option>
                  <option>Programming</option>
                  <option>Desgining</option>
                </select>
              </p>
              <p>
                <label for="subcategory">Subcategory</label>
                <input
                  class="ml-2"
                  type="text"
                  name="subcategory"
                  id="subcategory"
                  v-model="subcategory"
                />
              </p>

              <p>
                <label for="author">Author</label>
                <input
                  class="ml-2"
                  type="text"
                  name="author"
                  id="author"
                  v-model="author"
                />
              </p>
              <p>
                <input type="submit" value="Submit" @click="$emit('updated')" />
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// an axios  need http post request to backend django
import axios from "axios";
export default {
  name: "CreateVideo",
  components: {},
  data() {
    return {
      title: null,
      description: null,
      category: null,
      url: null,
      subcategory: null,
      author: null,
    };
  },
  methods: {
    checkFrom() {
      axios
        .post("http://127.0.0.1:8000/api/videos/", {
          title: this.title,
          description: this.description,
          url: this.url,
          category: this.category,
          subcategory: this.subcategory,
          author: this.author,
        })
        .then((res) => console.log(res))
        .catch((res) => console.log(res));
    },
  },
};
</script>

<style>
</style>