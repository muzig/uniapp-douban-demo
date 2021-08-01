<script>
export default {
  onLaunch: function () {
    console.log("App Launch");

    this.handleRequest();
  },
  onShow: function () {
    console.log("App Show");
  },
  onHide: function () {
    console.log("App Hide");
  },

  methods: {
    handleRequest() {
      uni.addInterceptor("request", {
        invoke(args) {
          args.url = "http://127.0.0.1:5000" + args.url;
          args.headers = Object.assign(
            {
              "User-Agent":
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            },
            args.headers
          );
        },
        success(args) {},
        fail(err) {
          console.log(err);
        },
        complete(res) {},
      });
    },
  },
};
</script>

<style>
/*每个页面公共css */
</style>
