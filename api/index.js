const apiMap = {
  Index: "/",
  Girls: "/hot/girls.json",
};

export function getIndex(succ, fail, header) {
  return uni.request({
    url: apiMap.Index,
    header: header,
    success: succ,
    fail: fail,
  });
}

export function getGirls(succ, fail) {
  return uni.request({
    url: apiMap.Girls,
    success: succ,
    fail: fail,
  });
}

export default {};
