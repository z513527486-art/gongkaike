# 实施说明：从 JSON 到单文件 HTML

## 1. 所需数据结构

项目中保留 `lesson.json`，其字段建议包含：

```json
{
  "title": "课题名称",
  "subtitle": "副标题",
  "overview": "课程概述",
  "objectives": ["学习目标1", "学习目标2"],
  "scenes": [
    {"title": "场景一", "description": "描述"}
  ],
  "hotspots": [
    {"title": "热点一", "text": "对应文本说明"}
  ],
  "exercises": [
    {"title": "练习一", "prompt": "任务说明"}
  ]
}
```

## 2. 构建流程

- 读取 JSON
- 确认每个模块的文本与目标
- 将页面结构渲染为单文件 HTML
- 将 CSS 与 JS 内嵌在 HTML 中
- 输出 `index.html`

## 3. 方法说明

- 优先使用单文件模式，不依赖外部资源
- CSS 应有公开课的层次感和留白设计
- JS 仅保留必要交互，如切页、弹窗、状态切换等

## 4. 最终要求

交付物需要在浏览器中通过 `file://` 打开，并进行人工验收。
