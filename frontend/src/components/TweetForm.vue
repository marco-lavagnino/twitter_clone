<template>
<div class="well">
  
  <form class="form-inline" v-on:submit.prevent="submitTweet($event)">
      <label class="sr-only" for="inlineFormInputGroupUsername">Username</label>
      <div class="input-group mb-2 mr-sm-2">
        <div class="input-group-prepend">
          <div class="input-group-text">@</div>
        </div>
        <input type="text" maxlength="50" required class="form-control" id="inlineFormInputGroupUsername" placeholder="Username" v-model="name">
      </div>

      <label class="sr-only" for="inlineFormInputGroup">Tweet Content</label>
      <div class="input-group mb-2 mr-sm-2">
        <input type="text"  maxlength="50" required class="form-control" id="inlineFormInputGroup" placeholder="Write your tweet here" v-model="content">
      </div>

      <button type="submit" class="btn btn-primary mb-2">Tweet</button>
  </form>
</div>
</template>

<script>
export default {
  name: "TweetForm",
  data() {
    return {
      name: "",
      content: ""
    };
  },
  props: ["tweets", "addTweet"],
  methods: {
    submitTweet(event) {
      fetch("http://localhost:8000/api/v1/tweets/", {
        method: "POST",
        body: JSON.stringify({ name: this.name, content: this.content }),
        headers: { "Content-Type": "application/json" }
      })
        .then(response => {
          response.json().then(tweet => this.addTweet(tweet));
        })
        .catch(() =>
          alert("Error uploading tweet. Is the backend receiving requests?")
        );

      this.name = "";
      this.content = "";
    }
  }
};
</script>


<style scoped>
</style>
