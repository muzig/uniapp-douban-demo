<template>
  <view class="container">
    <button @click="handleNavToIndex">主页</button>
    <span>数字: {{ count }}</span>
    <button @click="handleIncrement">加</button>
    <div v-for="(v, k) in src" :key="k">{{ v }}</div>
    <div>
      <span>{{ girls[0].title }}</span>
      <image mode="aspectFit" :src="girls[0].images[0]"></image>
      <image mode="aspectFit" :src="girls[0].images[0]"></image>
      <image mode="aspectFit" :src="girls[0].images[0]"></image>
    </div>
  </view>
</template>

<script>
import { getGirls, getIndex } from "../../api/index";

export default {
  data() {
    return {
      src: [],
      girls: [],
    };
  },
  computed: {
    count() {
      return this.$store.state.count;
    },
  },
  created() {},
  onLoad() {
    getIndex((res) => {
      this.src = res.data;
    });

    getGirls((res) => {
      this.girls = res.data.data;
    });
  },
  methods: {
    handleIncrement() {
      this.$store.commit("increment");
    },
    handleNavToIndex() {
      uni.navigateTo({
        url: "detail",
        success: () => {
          console.log("navigate to index success");
        },
        fail: () => {
          console.log("navigate to index fail");
        },
      });
    },
  },
};
</script>

<style>
.container {
  padding: 20px;
  font-size: 14px;
  line-height: 24px;
}
</style>
