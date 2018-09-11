<template>
  <table class="table">
    <thead>
      <tr>
        <td>
          <a href="" v-bind:class="{ active: sort == 'name' }" v-on:click.prevent="sort = 'name'">Author</a>
        </td>
        <td>Tweet</td>
        <td>
          <a href="" v-bind:class="{ active: sort == 'timestamp' }" v-on:click.prevent="sort = 'timestamp'">Timestamp</a>
        </td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="tweet in orderedTweets" :key="tweet.id">
        <td>{{tweet.name}}</td>
        <td>{{tweet.content}}</td>
        <td>{{humanizeDate(tweet.timestamp)}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
function humanizeDuration(timeInMillisecond) {
  var result = "";
  if (timeInMillisecond) {
    if (
      (result = Math.round(
        timeInMillisecond / (1000 * 60 * 60 * 24 * 30 * 12)
      )) > 0
    ) {
      //year
      result = result === 1 ? result + " Year" : result + " Years";
    } else if (
      (result = Math.round(timeInMillisecond / (1000 * 60 * 60 * 24 * 30))) > 0
    ) {
      //months
      result = result === 1 ? result + " Month" : result + " Months";
    } else if (
      (result = Math.round(timeInMillisecond / (1000 * 60 * 60 * 24))) > 0
    ) {
      //days
      result = result === 1 ? result + " Day" : result + " Days";
    } else if (
      (result = Math.round(timeInMillisecond / (1000 * 60 * 60))) > 0
    ) {
      //Hours
      result = result === 1 ? result + " Hours" : result + " Hours";
    } else if ((result = Math.round(timeInMillisecond / (1000 * 60))) > 0) {
      //minute
      result = result === 1 ? result + " Minute" : result + " Minutes";
    } else if ((result = Math.round(timeInMillisecond / 1000)) > 0) {
      //second
      result = result === 1 ? result + " Second" : result + " Seconds";
    } else {
      result = timeInMillisecond + " Millisec";
    }
  }
  return result;
}

export default {
  name: "TweetTable",
  props: ["tweets"],
  data() {
    return {
      currentTime: new Date(),
      sort: "timestamp"
    };
  },
  created() {
    this.updateCurrentTime();
  },
  computed: {
    orderedTweets() {
      const tweets = this.tweets.slice();

      if (this.sort === "timestamp") {
        // sort by timestamp
        tweets.sort((a, b) => {
          return new Date(b.timestamp) - new Date(a.timestamp);
        });
      } else {
        // sort by username
        tweets.sort((a, b) => {
          if (a.name > b.name) {
            return 1;
          }
          if (a.name < b.name) {
            return -1;
          }
          return new Date(b.timestamp) - new Date(a.timestamp);
        });
      }

      return tweets;
    }
  },
  methods: {
    updateCurrentTime() {
      this.currentTime = new Date();

      setTimeout(this.updateCurrentTime, 5000);
    },
    humanizeDate(date_str) {
      return humanizeDuration(this.currentTime - new Date(date_str));
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
thead {
  font-weight: bold;
}
.active {
  color: indianred;
}
</style>
