<script>
export default {
  onLaunch: function () {
    uni.request({
      url: "https://www.baidu.com",
      success: (res) => {
        console.log(res);
      },
    });
  },
  onShow: function () {
    console.log("App Show");
  },
  onHide: function () {
    console.log("App Hide");
  },
};
</script>

<style>
/*每个页面公共css */
</style>
