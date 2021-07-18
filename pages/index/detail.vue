<template>
  <view>
    <button @click="handleNavToIndex">细节</button>
  </view>
</template>

<script>
export default {
  name: "detail",
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
