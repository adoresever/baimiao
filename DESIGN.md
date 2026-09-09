---
name: "白描 / Baimiao"
description: "把一段中文改出人写的分寸和文采，并呈现为自然、克制、可核对的东方编辑案卷。"
colors:
  rice-paper: "#f4eee2"
  finished-sheet: "#fffaf0"
  ink-navy: "#173549"
  muted-ink: "#5b6a70"
  review-teal: "#28726f"
  edit-vermilion: "#aa4d3f"
  focus-ochre: "#c08b37"
  hairline: "rgba(23, 53, 73, .18)"
  selection-vermilion: "#edd1c6"
  step-gold: "#e7bd72"
  inspector-gold: "#f1c97e"
  lab-paper: "#e7ddcc"
  draft-gray: "#68747a"
typography:
  display:
    fontFamily: '"Noto Serif SC", "Source Han Serif SC", "Songti SC", STSong, serif'
    fontSize: "clamp(64px, 8vw, 112px)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.03em"
  hero-title:
    fontFamily: '"Noto Serif SC", "Source Han Serif SC", "Songti SC", STSong, serif'
    fontSize: "clamp(27px, 3vw, 42px)"
    fontWeight: 800
    lineHeight: 1.42
  headline:
    fontFamily: '"Noto Serif SC", "Source Han Serif SC", "Songti SC", STSong, serif'
    fontSize: "clamp(38px, 5vw, 68px)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  title:
    fontFamily: '"Noto Serif SC", "Source Han Serif SC", "Songti SC", STSong, serif'
    fontSize: "25px"
    fontWeight: 800
  body:
    fontFamily: '"Noto Sans SC", "Source Han Sans SC", "Microsoft YaHei", system-ui, sans-serif'
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: '"Noto Sans SC", "Source Han Sans SC", "Microsoft YaHei", system-ui, sans-serif'
    fontSize: "14px"
    fontWeight: 400
rounded:
  sheet: "14px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "20px"
  xl: "24px"
  2xl: "32px"
  3xl: "48px"
  section: "112px"
components:
  tab-default:
    backgroundColor: "transparent"
    textColor: "{colors.muted-ink}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "42px"
  tab-selected:
    backgroundColor: "{colors.ink-navy}"
    textColor: "{colors.finished-sheet}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "42px"
  method-inspector:
    backgroundColor: "{colors.review-teal}"
    textColor: "{colors.finished-sheet}"
    rounded: "{rounded.sheet}"
    padding: "34px"
  comparison-before:
    backgroundColor: "rgba(255,250,240,.76)"
    textColor: "{colors.draft-gray}"
    rounded: "{rounded.sheet}"
    padding: "clamp(28px, 4vw, 46px)"
  comparison-after:
    backgroundColor: "{colors.finished-sheet}"
    textColor: "{colors.ink-navy}"
    rounded: "{rounded.sheet}"
    padding: "clamp(28px, 4vw, 46px)"
---

# Design System: 白描 / Baimiao

## Overview

**Creative North Star: "东方编辑案卷"**

白描是独立的通用中文改写与文采润色 Skill，清理 AI 痕迹只是其中一种用途。界面像一张正在被红笔处理的中文稿：米纸提供安静底面，墨蓝承载原意与结论，朱砂指出删改和转向，青绿确认通过状态与方法检查。稿纸、删改线、重排纸条和细批注线都对应真实的改写动作，不作为泛复古装饰。

整体自然、克制、具体，既表现取舍、重排、节奏和措辞带来的文采，也保留工具的可核对性。粗宋体建立章节观点，无衬线正文承担长文阅读；大块整版、细线表格与少数纸面容器组织一条长而清楚的叙事。项目所有者指定的招财金牌蓝猫是固定主视觉角色，以红笔编辑稿件；界面拒绝通用软件卡片墙、装饰性玻璃、科技渐变和没有编辑含义的纹理。

**Key Characteristics:**

- 米纸、熟宣、墨蓝、青绿和朱砂构成稳定的编辑色谱。
- 红笔删改、稿纸与重排纸条把改写过程直接可视化。
- 招财金牌蓝猫以红笔编辑稿件，是首屏固定的识别角色。
- 宋体负责判断和落点，无衬线负责解释、数据与操作。
- 前后对照、五步流程、方法检查器和回归条都允许逐项核对。

## Colors

色彩以纸墨中性色为主体，青绿与朱砂严格分工：一个确认和检查，一个删改和转向。

### Primary

- **墨蓝：**正文、强标题、深色流程整版与选中标签的主色，承担稳定、可信的原意。
- **检查青绿：**方法检查器、通过状态和最终回归结果的颜色，表达判断已经过核对。

### Secondary

- **删改朱砂：**用于删除线、流程箭头、方法选中态和收束整版；只在内容发生变化时出现。
- **焦点赭黄：**只用于键盘焦点轮廓，让交互在纸色和深色表面上都明确可见。

### Tertiary

- **步骤金与检查器金：**仅用于深色流程编号和青绿检查器中的方向标记，提升局部扫描性。

### Neutral

- **米纸：**全页环境底色。
- **熟宣：**成稿纸、浅色重点表面和深色区反白文字。
- **淡墨：**说明文字、次要导航和低优先级信息。
- **实验纸：**案例实验区和测试轨道的分层底色。
- **草稿灰：**改写前正文的降级色。
- **墨色细线：**统一边框、表格线与章节分隔。

### Named Rules

**The 红笔有因 Rule.** 朱砂只表示删除、选择或方向改变；普通强调不使用朱砂。

**The 纸墨守恒 Rule.** 新增表面必须来自米纸、熟宣、墨蓝或青绿，不引入冷白、纯黑或霓虹色。

## Typography

**Display Font:** Noto Serif SC（回退至 Source Han Serif SC、Songti SC、STSong 和系统 serif）  
**Body Font:** Noto Sans SC（回退至 Source Han Sans SC、Microsoft YaHei、system-ui 和 sans-serif）

**Character:** 粗重中文宋体像编辑部标题与红笔结论，明确但不夸张；中文无衬线让较长说明、方法信号、数据和控件保持现代且易读。

### Hierarchy

- **Display**（800，`clamp(64px, 8vw, 112px)`，0.94 行高）：仅用于首屏产品名；移动端固定为 84px。
- **Hero Title**（800，`clamp(27px, 3vw, 42px)`，1.42 行高）：用于首屏承诺“把一段中文，改出人写的分寸和文采”；移动端为 28px。
- **Headline**（800，`clamp(38px, 5vw, 68px)`，1.08 行高）：用于章节观点；移动端为 43px。
- **Title**（800，25px）：用于规则块与主要局部标题；流程、检查器等按密度在 20–30px 内变化。
- **Body**（400，16px，1.75 行高）：用于解释与长文；通过容器宽度而非缩字控制行长。
- **Label**（400，14px）：用于导航、标签、数据行与说明元信息，重要状态提升至 800。

### Named Rules

**The 宋体下判断 Rule.** 宋体只用于名称、章节观点、稿件正文和决定性落点；操作与核对信息使用无衬线。

**The 两级强标题 Rule.** 只有首屏与章节标题获得超大字号，模块标题必须明显退后。

## Layout

页面使用最大宽度 1260px 的居中容器，桌面两侧至少留 24px，700px 以下留 16px。首屏采用 0.82 / 1.18 非对称双栏：左侧先给“把一段中文，改出人写的分寸和文采”与微型前后对照，右侧完整展示佩戴招财金牌、手持红笔编辑稿件的蓝猫；980px 以下改为单列并保持文字先于图像。

桌面章节纵向留白为 112px，章节头使用 4 / 6 双栏和 48px 间距。流程与方法在桌面使用五列，980px 以下转为两列，700px 以下转为单列；案例对照、硬门和收束整版在 700px 以下同样堆叠。移动端章节留白缩为 82px，导航只保留最后一个入口，复杂信息通过重排而不是缩小正文解决。

**The 先改稿后解释 Rule.** 所有视口先展示改写承诺与真实前后变化，再进入流程、方法和回归证据。

**The 展开而非挤压 Rule.** 高密度结构在 980px 和 700px 两级断点逐步降列，禁止通过压缩字级保持桌面列数。

## Elevation & Depth

系统默认平面，以底色、细线和整版反差组织层级。显著阴影只给首屏主图，较弱阴影只给改写后稿纸；流程、方法表、测试与硬门保持无阴影，让视觉层级对应“原始材料 → 完成稿”的关系。

### Shadow Vocabulary

- **主图纸面**（`0 22px 54px rgba(68,47,25,.15)`）：只用于首屏招财金牌蓝猫红笔改稿插画。
- **完成稿抬升**（`0 18px 42px rgba(68,47,25,.08)`）：只用于前后对照中的完成稿。

### Named Rules

**The 完成稿才抬升 Rule.** 普通信息保持平面，阴影只帮助主图与完成稿从材料中被辨认出来。

**The 暖纸影 Rule.** 阴影使用低透明暖褐色，禁止冷黑重影、辉光和玻璃模糊卡片。

## Shapes

主图、方法检查器、稿件对照、运行参数与收束整版统一使用 14px 纸面圆角。标签和测试轨道使用 999px 胶囊形。流程、方法表、规则与硬门保持直角，以细线和相邻边界形成案卷结构；朱砂箭头使用三角剪裁表示步骤推进。

**The 纸面与表格 Rule.** 独立纸张可以轻微圆角，连续流程和方法表必须保持直角，不把整页软化成圆角卡片集合。

## Components

### Chips

案例标签是横向可滚动的稿件选择器。

- **Style:** 默认透明、淡墨字和一像素墨线；选中后使用墨蓝底与熟宣字。
- **Shape:** 最小高度 42px，横向内边距 16px，全胶囊圆角。
- **State:** 由 `aria-selected` 驱动，支持方向键、Home 与 End；移动端保持横向滚动。

### Cards / Containers

容器按“材料、检查、完成”区分材质，而不是重复同一种卡片。

- **Comparison Sheets:** 原稿为半透明熟宣与草稿灰，完成稿为不透明熟宣与墨蓝，并获得最低抬升。
- **Method Inspector:** 青绿整版、熟宣文字、双栏前后例子和金色方向标记；700px 以下变单列，方向标记旋转 90 度。
- **Pipeline:** 墨蓝整版中的五个直角步骤，以一像素浅线分隔，朱砂箭头标示推进方向。
- **Run Contract:** 青绿圆角面板，以定义列表对齐模型、样本和运行设置。

### Navigation

导航是 58px 高的粘性米纸页眉，使用 12px 背景模糊与底部墨线。品牌为 18px 粗宋体，链接为 14px 淡墨无衬线；悬停转朱砂。700px 以下隐藏前两个入口，只保留“实测”。

### Method Buttons

方法名称是无底色文字按钮，默认与正文同色；悬停或 `aria-pressed="true"` 时转朱砂并出现同色下划线。它们只更新下方方法检查器的信号、前后例子和撤销条件。

### Verification Rows

每项保真检查是一条三列数据行：检查项、胶囊轨道、当前状态。青绿表示当前样本已经通过；条形以 850ms 强减速曲线生长。减少动态偏好下将动画压缩至 0.01ms、单次执行。

## Do's and Don'ts

### Do:

- **Do** 让红笔、删除线、重排纸条和方向箭头对应具体改写动作。
- **Do** 用墨蓝保留原意，用朱砂标记删改，用青绿确认检查与通过。
- **Do** 同时呈现原稿、完成稿、使用方法和撤销条件，让结果可核对。
- **Do** 在桌面与移动端完整保留招财金牌蓝猫主图、金牌和红笔改稿动作。
- **Do** 保留清晰键盘焦点，并尊重减少动态偏好。

### Don't:

- **Don't** 把白描缩窄为清理 AI 痕迹、特定媒介或单一文体的工具。
- **Don't** 为了“更像人写”而添加原文没有的事实、动作、场景、引语或情绪。
- **Don't** 使用卡片墙、图标墙、装饰性玻璃、科技渐变或无编辑含义的复古纹理。
- **Don't** 让朱砂成为常规装饰色，或把青绿用于未经核对的状态。
- **Don't** 用缩小正文替代 980px 与 700px 断点上的结构重排。
