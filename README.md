<div style='text-align: center'>
    <h1>uniapp-douban-demo</h1>
</div>

## 概览

此项目的目的是为了通过实践的方式, 熟悉uni-app的相关组件, 也同时熟悉相关的接口的使用方法等练手项目.

- [概览](#概览)
- [开发路线](#开发路线)
- [前端](#前端)
  - [环境准备](#环境准备)
  - [知识点参考](#知识点参考)
    - [HTML/CSS/JS](#htmlcssjs)
    - [基础](#基础)
    - [网络](#网络)
    - [数据](#数据)
    - [框架](#框架)
    - [其他](#其他)
- [后端](#后端)
  - [环境准备](#环境准备-1)
  - [知识点参考](#知识点参考-1)
- [爬虫](#爬虫)
  - [环境准备](#环境准备-2)
  - [知识点参考](#知识点参考-2)
- [Q & A](#q--a)
- [参考来源](#参考来源)

## 开发路线

> 前端界面

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
    

> 后端数据

- [x] 首页数据
- [ ] 榜单数据
- [ ] 用户数据

## 前端

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

## 后端

Flask: 基于python的用于快速开发的web框架

1. 数据服务目录: [cmd/src/srv](cmd/src/srv)

### 环境准备

```bash
# 安装python web框架
pip3 install flask
```

### 知识点参考

- [Flask 文档说明](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)

## 爬虫


1. 数据爬取目录: [cmd/src/crawler](cmd/src/crawler)
2. 数据清洗目录: [cmd/src/srv/staic](cmd/src/srv/static)
3. 数据服务目录: [cmd/src/srv](cmd/src/srv)

提取的数据, 按照分类来生成文件,同时按照文件来实现接口, 统一方便

### 环境准备

```bash
# 安装用于解析网页的工具
pip3 install bs4
# 处理网络请求
pip3 install reqeusts
```

### 知识点参考

- [BeautifulSoup4 教学文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)

## Q & A

> 为什么选择豆瓣模仿?

打开手机, 看到豆瓣的app, 所以有这个想法, 同时电影作为一款学习demo, 也是相当不错的.

## 参考来源

- [uni-app 官网](https://uniapp.dcloud.io/resource)
- [uni-ui 文档](https://ext.dcloud.net.cn/plugin?name=uni-list)