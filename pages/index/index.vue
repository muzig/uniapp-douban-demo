<template>
  <view class="container">
    <button @click="handleNavToIndex">主页</button>
    <span>数字: {{ count }}</span>
    <button @click="handleIncrement">加</button>
  </view>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    count() {
      return this.$store.state.count;
    },
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
