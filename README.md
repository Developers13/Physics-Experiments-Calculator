

# Calc8



<!-- PROJECT SHIELDS -->

![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Developers13/Physics-Experiments-Calculator?style=flat-square)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/Developers13/Physics-Experiments-Calculator?style=flat-square)
![GitHub License](https://img.shields.io/github/license/Developers13/Physics-Experiments-Calculator?style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Developers13/Physics-Experiments-Calculator?style=flat-square)
![Static Badge](https://img.shields.io/badge/Donation-Ethereum-%23ccccff?style=flat-square&logo=ethereum&link=https%3A%2F%2Fgoto.etherscan.com%2Faddress%2F0xe25926d3df559016ea45552780eb84c0430cbf97)



<!-- PROJECT LOGO -->
<p align='center'>
  <img src='./assets/images/calculator-one-svgrepo-com.svg' alt='logo' width=80 height=80 >
</p>
<br />

  <h3 align="center">大学物理实验八步法计算器</h3>
  <p align="center">
    A calculator for physics experiments and propagation of uncertainty.
    <br />
    <a href="https://github.com/Developers13/Physics-Experiments-Calculator"><strong>Github主页 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Developers13/Physics-Experiments-Calculator">开始使用</a>
    ·
    <a href="https://github.com/Developers13/Physics-Experiments-Calculator/issues">报告Bug</a>
    ·
    <a href="https://github.com/Developers13/Physics-Experiments-Calculator/issues">提出新特性</a>
  </p>

</p>

 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [如何参与开源项目](#如何参与开源项目)
- [作者](#作者)
- [捐赠](#donation)

### 上手指南

#### 静态网页
<a href="https://calc.cryste.site">Go>></a>


数据分布：选择平均分布或正态分布，该选项与实验过程和实验仪器有关


置信区间：3sigma:0.683 2sigma:0.95 一般情况使用0.683


仪器误差限：与实验仪器有关，请查阅资料。


数据：请用空格分开。


“数据分布”和“仪器误差限”会直接影响B类不确定度的结果。对于同一个实验B类不确定度应该是相同的，如果您不确定，可以在仪器误差限的输入框中输入0（但不能留空）


**一定记得选择分布和置信区间，且两个输入框均不能留空**


在网页的底端有一个通向v2版本的链接，点击即可进入不确定度传递计算页面


###### 开发前的配置要求

<details markdown='1'><summary>本项目使用了如下依赖</summary>
Pyscript 2024.5.2(No installation needed)

Tailwindcss 4.1.17
</details>

###### **安装步骤**

如果您要使用CLI版本：
`pip install sympy`

### 部署

静态网页使用了Vercel部署。

#### 文件结构说明

```
Physics-Experiments-Calculator/
├── index.html              # v1版本主页面
├── donate.html             # 捐赠页面
├── v1.main.py              # v1 Python主程序
├── stats.py                # 统计计算模块
├── LICENSE                 # 许可证文件
├── README.md               # 项目说明文档
├── package.json            # npm配置
├── package-lock.json       # npm依赖锁定
├── requirements.txt        # Python依赖
├── tests/                  # 测试文件目录
│   └── test_stats.py       # 统计测试文件
├── v2/                     # v2版本文件目录
│   ├── v2.html             # v2主页面
│   ├── v2.main.py          # v2 Python主程序
│   ├── pyscript.json       # v2 PyScript配置
│   ├── test/               # v2测试文件目录
│   └── favicon.ico         # 网站图标
└── assets/                 # 静态资源目录
    ├── css/
    │   ├── input.css       # tailwind输入样式文件
    |   └── output.css      # tailwind输出样式文件
    ├── js/
    │   ├── script.v1.js    # v1 JavaScript
    │   └── script.v2.js    # v2 JavaScript
    ├── images/             # 图片资源
    └── icons/              # 图标资源
```


### 使用到的框架

- [Tailwind v4.1.17](https://tailwindcss.com)
- [Pyscript](https://pyscript.net)
- [SymPy](https://www.sympy.org)


#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


### 版权说明

该项目使用GNU授权许可，详情请参阅 [LICENSE.txt](https://github.com/Developers13/Physics-Experiments-Calculator/blob/main/LICENSE)

### 捐赠
Ethereum:0xE25926d3Df559016eA45552780Eb84c0430cBf97
<br>
<img src='https://github.com/Developers13/Physics-Experiments-Calculator/blob/main/1717301742745.jpg' width=50 height=70>








