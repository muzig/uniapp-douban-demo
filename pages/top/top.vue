<template>
  <view>
    <h1>Top</h1>
    <button @click="handleNavToIndex"></button>
  </view>
</template>

<script>
export default {
  name: "top",
  methods: {
    handleNavToIndex() {
      uni.navigateTo({
        url: "index",
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

<style scoped></style>
