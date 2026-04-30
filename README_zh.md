# Claude Code Skills

[English README](README.md)

Claude Code 专用技能集合，提升 AI 在特定任务中的表现。

## 概述

这些 skills 为 Claude Code 提供了特定领域的专业指导，确保输出符合预期的格式、风格和质量要求。

## 可用 Skills

### latex-textbook-writer

**用途**：编写专业数学教材（XeLaTeX）

**特点**：
- 定义/定理盒子样式
- 正确的配色方案（定义绿色、定理橙色、例子蓝色）
- 学术性叙述风格（解释优先于定义）
- 中英文模板支持

**适用场景**：数学教材章节、LaTeX 论文格式、学术文档

**调用方式**：`/latex-textbook-writer`

---

### md-report-writer

**用途**：编写专业 Markdown 报告

**特点**：
- 叙述流畅性（解释优先于技术内容）
- 连贯的解释（非步骤式列表）
- 直接专业语气（无对话填充）
- 粗体强调（不用斜体）
- 嵌入代码片段和引用文献
- 简单代码注释变量，复杂代码详细解释逻辑

**适用场景**：技术报告、进度报告、项目文档、会议记录

**调用方式**：`/md-report-writer`

---

### latex-compile

**用途**：LaTeX 编译助手（XeLaTeX）

**特点**：
- VSCode LaTeX Workshop 标准编译命令
- 常见编译错误诊断
- 快速诊断命令
- 编译工作流指导

**适用场景**：LaTeX 项目编译、错误诊断、交叉引用问题

**调用方式**：`/latex-compile`

---

### update-skill

**用途**：根据对话反馈更新现有 skills

**工作流程**：
1. 用某个 skill 生成输出
2. 通过对话调整直到满意
3. 调用 `/update-skill <skill-name>` 更新该 skill
4. 下次调用时直接应用改进

**适用场景**：任何需要迭代改进 skill 输出的情况

**调用方式**：`/update-skill <skill-name>`

---

### syncthing-cleanup

**用途**：清理 Syncthing 同步文件夹中的意外项目

**特点**：
- 自动识别并清理冲突文件（`.sync-conflict-*`）
- 删除加密文件夹中的空目录
- 清理临时文件（`*.swp`, `*~`, `.DS_Store`, `Thumbs.db`, `*.tmp`）
- 删除损坏的符号链接
- 集成 Syncthing REST API，清理后自动触发重新扫描
- 包含可执行的 Python 清理脚本
- 支持 dry-run 模式预览删除内容
- 跨平台支持（Linux、macOS、Windows WSL）

**适用场景**：Syncthing 显示意外项目、同步冲突、定期清理同步文件夹

**调用方式**：`/syncthing-cleanup`

**脚本使用**：
```bash
# 交互模式
python3 scripts/cleanup_syncthing.py

# 预览模式
python3 scripts/cleanup_syncthing.py --dry-run

# 自动清理
python3 scripts/cleanup_syncthing.py --yes

# 清理特定文件夹
python3 scripts/cleanup_syncthing.py --folders ~/Develop ~/Codes
```

---

## 仓库结构

```
skills/
├── latex-textbook-writer/    # LaTeX 教材编写
│   └── SKILL.md
├── md-report-writer/         # Markdown 报告编写
│   └── SKILL.md
├── latex-compile/            # LaTeX 编译助手
│   └── SKILL.md
├── update-skill/             # Skill 更新工具
│   └── SKILL.md
├── syncthing-cleanup/        # Syncthing 清理工具
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── cleanup_syncthing.py
│   │   └── test_skill.py
│   ├── references/
│   │   └── implementation_details.md
│   └── evals/
│       └── evals.json
└── README.md                 # 本文件
```

## 使用方式

### 调用 Skill

在 Claude Code 中直接使用命令：

```
/skill-name
```

例如：
```
/latex-textbook-writer
/md-report-writer
```

### 更新 Skill

当某个 skill 的输出需要调整时：

1. 在对话中指出需要改进的地方
2. 待输出满意后，调用：
   ```
   /update-skill skill-name
   ```
3. AI 会分析对话并更新 skill 文件
4. 更新会自动提交到 git

## 开发

### 添加新 Skill

1. 在 `skills/` 目录下创建新文件夹
2. 创建 `SKILL.md` 文件，包含：
   - frontmatter（name, description）
   - 详细的使用指南
   - 示例和最佳实践
3. 提交到 git

### Skill 文件格式

```markdown
---
name: skill-name
description: 简短描述
---

# Skill 标题

详细的 skill 说明...

## 何时使用
...

## 核心原则
...

## 示例
...
```

## 贡献

这些 skills 是根据个人使用需求定制的。如需修改：
1. 直接编辑对应 `SKILL.md` 文件
2. 提交到 git
3. 或使用 `/update-skill` 在对话中迭代改进

## 许可

MIT License

---

**作者**：xjsongphy
**仓库**：[github.com:xjsongphy/skills.git](https://github.com/xjsongphy/skills)
