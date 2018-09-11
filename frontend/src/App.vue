<template>
  <div id="app" class="container">
    <h1>Vue+Django Twitter clone</h1>
    <div class="row">
      <TweetForm v-bind:tweets="tweets" v-bind:addTweet="addTweet"/>
    </div>
    <br/>
    <div class="row">
      <TweetTable v-bind:tweets="tweets"/>
    </div>
  </div>
</template>

<script>
import TweetTable from "./components/TweetTable";
import TweetForm from "./components/TweetForm";
import "bootstrap/dist/css/bootstrap.css";

export default {
  name: "App",
  data() {
    return {
      tweets: []
    };
  },
  components: {
    TweetTable,
    TweetForm
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch("http://localhost:8000/api/v1/tweets/")
        .then(response => {
          response.json().then(tweets => (this.tweets = tweets));
        })
        .catch(() =>
          alert("Error loading tweets. Is the backend receiving requests?")
        );
    },
    addTweet(tweet) {
      this.tweets.push(tweet);
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  padding-bottom: 1em;
}
</style>
