<div style='text-align: center'>
    <h1>uniapp-douban-demo</h1>
</div>

## 概览

此项目的目的是为了通过实践的方式, 熟悉uni-app的相关组件, 也同时熟悉相关的接口的使用方法等练手项目.

## 开发路线

参考资源图: [/docs/imgs](docs/imgs)

- 首页
  - [ ] 主页
  - [ ] 详细列表
- 榜单
  - [ ] 主页
  - [ ] Top榜单
- 用户
  - [ ] 主页
  - [ ] 用户观影界面
  - [ ] 用户详情界面
  

## 前端界面

### 环境准备

- XBuild
- WebStorm
- WeChat Development Tool
- Git

```bash
# 下载代码
git clone https://github.com/muzig/uniapp-douban-demo

# 准备环境
npm i prettier --save-dev
npm i vue
npm i @dcloudio/uni-ui
npm i @dcloudio/types --save-dev
```

### 知识点参考

#### HTML/CSS/JS

- [SCSS](https://www.sass.hk/guide/)

#### 基础

- [基础](https://uniapp.dcloud.io/api/log)
- [组件](https://uniapp.dcloud.io/component/README)
- [界面交互](https://uniapp.dcloud.io/api/ui/prompt)
- [路由与页面跳转](https://uniapp.dcloud.io/api/router?id=navigateto)

#### 网络

- [网络API](https://uniapp.dcloud.io/api/request/request)
- [微信小程序网络限制说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)

#### 数据

- [数据缓存](https://uniapp.dcloud.io/api/storage/storage?id=setstorage)
- [文件](https://uniapp.dcloud.io/api/file/file?id=savefile)
- [Vuex 全局数据管理](https://uniapp.dcloud.io/vue-vuex)

#### 框架

- [指导文档](https://uniapp.dcloud.io/collocation/pages)

#### 其他

- [地理](https://uniapp.dcloud.io/api/location/location)
- [媒体](https://uniapp.dcloud.io/api/media/image)
- [设备](https://uniapp.dcloud.io/api/system/info)
- [广告](https://uniapp.dcloud.io/api/a-d/rewarded-video)
- [第三方服务](https://uniapp.dcloud.io/api/plugins/provider)
- [其他](https://uniapp.dcloud.io/api/other/authorize)

## 后端界面

### 环境准备

- Flask: 基于python的用于快速开发的web框架

```bash
# 安装python web框架
pip3 install flask
```

### 知识点参考

- [Flask使用说明](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)


## Q & A

> 为什么选择豆瓣模仿?

打开手机, 看到豆瓣的app, 所以有这个想法, 同时电影作为一款学习demo, 也是相当不错的.

## 参考来源

- [uni-app 官网](https://uniapp.dcloud.io/resource)
- [uni-ui 文档](https://ext.dcloud.net.cn/plugin?name=uni-list)