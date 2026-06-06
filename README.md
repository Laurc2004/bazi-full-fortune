# 八字全方位算命 Skill

> 八字排盘与全方位命理解读工具集

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-bazi--full--fortune-blue.svg)](https://clawhub.com/skills/bazi-full-fortune)

---

## 中文文档

### 简介

八字全方位算命 Skill 是一个完整的八字命理工作流工具集，基于 [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) 构建，涵盖从排盘到全方位解读的完整链路：

- 排盘层 — CLI 脚本，支持阳历/农历输入，输出完整四柱、十神、神煞、大运、刑冲合会
- 分析层 — 全方位命理解读模板，覆盖家庭、健康、事业、财富、感情、人际、学业、精神八大维度
- 参考层 — 家庭背景命理模式速查清单，用于校准分析准确性
- 反推层 — 从已知八字四柱反查阳历日期

### 安装

方式一：通过 ClawHub 安装（推荐，适用于 Hermes / OpenClaw 用户）

```bash
clawhub install bazi-full-fortune
cd skills/bazi-full-fortune
npm install
```

方式二：通过 Git 克隆

```bash
git clone https://github.com/Laurc2004/bazi-full-fortune.git
cd bazi-full-fortune
npm install
```

### 环境要求

- Node.js ≥ 18（推荐 24，可直接运行 TypeScript）
- 兼容方案：若 Node 版本较低，需额外安装 `tsx`（`npm install -D tsx`）

### 使用示例

阳历排盘：

```bash
node scripts/buildBaziFromSolar.ts "2000-12-22T03:30:00" 0 2
```

参数：时间（ISO 8601，不带时区）、性别（1=男 0=女）、子时配置（1=次日 2=当日）

农历排盘：

```bash
node scripts/buildBaziFromLunar.ts "2000-11-27T03:30:00" 0 2
```

黄历查询：

```bash
node scripts/getChineseCalendar.ts
node scripts/getChineseCalendar.ts 2024-02-10
```

反推扫描（从已知四柱反查阳历）：

```bash
node scripts/scan_year.ts 2000 0 --year-pillar 庚辰 --month-pillar 戊子 --day-pillar 甲寅 --hour-pillar 丙寅 --hour 03:30:00
```

### 核心特性

六亲十神对应规则（男女命不同，搞错则全盘皆错）：

| 六亲 | 男命 | 女命 |
|------|------|------|
| 父亲 | 偏财 | 正财 |
| 母亲 | 正印 | 偏印（枭神） |
| 配偶 | 正财（妻） | 正官（夫） |
| 儿子 | 七杀 | 伤官 |
| 女儿 | 正官 | 食神 |
| 兄弟 | 比肩 | 劫财 |
| 姐妹 | 劫财 | 比肩 |

八大维度分析模板：家庭、健康、外貌身材、事业、财富、感情婚姻、人际关系、学业、精神世界

校准工作流：排盘后先问 5 个关键事实（父母关系、父亲驻地、母亲是否带大、家庭经济来源、自己当前状态），再做完整解读，避免"第一轮分析全错"。

### 推荐 LLM 模型

本项目依赖 LLM 进行命理分析和解读，以下是实测后推荐的模型：

| 模型 | 推荐理由 |
|------|----------|
| Claude Sonnet 4 / Opus 4 | 分析深度最强，逻辑严密，长文输出稳定，对命理术语理解精准 |
| Qwen 3.7 Max | 中文理解力极强，对八字术语和文化背景把握到位，性价比高 |
| MiniMax M3 | 中文输出流畅自然，分析有条理，响应速度快 |
| MiMo v2.5 Pro | 推理能力强，逻辑链条清晰，适合复杂命盘 |

### 项目结构

```
bazi-full-fortune/
├── SKILL.md                        完整命理工作流文档
├── README.md                       本文件
├── package.json
├── LICENSE                         MIT
├── scripts/
│   ├── buildBaziFromSolar.ts       阳历排盘
│   ├── buildBaziFromLunar.ts       农历排盘
│   ├── getChineseCalendar.ts       黄历查询
│   ├── scan_year.ts                反推扫描
│   └── util.ts                     公共工具
└── references/
    └── family-patterns.md          家庭背景命理模式参考
```

### 文档

完整命理工作流文档（含排盘用法、六亲规则、分析模板、常见陷阱）请参阅 [SKILL.md](./SKILL.md)

家庭背景命理模式参考（8 种模式：命理信号 → 现实推断 → 校准问题）请参阅 [references/family-patterns.md](./references/family-patterns.md)

### 依赖

- [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) — 底层排盘引擎
- [tyme4ts](https://github.com/6tail/tyme4ts) — 农历/阳历转换

### 许可证

[MIT](./LICENSE) © 2026

### 致谢

底层算法基于 [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) 和 [tyme4ts](https://github.com/6tail/tyme4ts)，命理分析框架融合了传统子平术与现代校准工作流。

---

## English Documentation

### Introduction

Bazi Full Fortune Telling Skill is a complete Bazi (Four Pillars of Destiny) workflow toolkit, built on [cantian-tymext](https://www.npmjs.com/package/cantian-tymext). It covers the full pipeline from chart generation to comprehensive destiny analysis:

- Charting Layer — CLI scripts supporting solar/lunar calendar input, outputting complete Four Pillars, Ten Gods, Auspicious Stars, Luck Cycles, and Interactions (clashes, combinations, punishments, harms)
- Analysis Layer — Full destiny interpretation template covering 8 dimensions: Family, Health, Appearance, Career, Wealth, Love & Marriage, Social Relations, Education, and Spiritual World
- Reference Layer — Family background pattern lookup table for calibrating analysis accuracy
- Reverse Lookup — Find the solar date matching known Bazi four pillars

### Installation

Option 1: Install via ClawHub (recommended for Hermes / OpenClaw users)

```bash
clawhub install bazi-full-fortune
cd skills/bazi-full-fortune
npm install
```

Option 2: Clone from Git

```bash
git clone https://github.com/Laurc2004/bazi-full-fortune.git
cd bazi-full-fortune
npm install
```

### Prerequisites

- Node.js ≥ 18 (Node 24 recommended for native TypeScript execution)
- Fallback: install `tsx` for older Node versions (`npm install -D tsx`)

### Usage Examples

Solar calendar chart:

```bash
node scripts/buildBaziFromSolar.ts "2000-12-22T03:30:00" 0 2
```

Parameters: datetime (ISO 8601, no timezone), gender (1=male, 0=female), late-zi-hour config (1=next day, 2=same day)

Lunar calendar chart:

```bash
node scripts/buildBaziFromLunar.ts "2000-11-27T03:30:00" 0 2
```

Chinese almanac query:

```bash
node scripts/getChineseCalendar.ts
node scripts/getChineseCalendar.ts 2024-02-10
```

Reverse lookup (find solar date from known four pillars):

```bash
node scripts/scan_year.ts 2000 0 --year-pillar 庚辰 --month-pillar 戊子 --day-pillar 甲寅 --hour-pillar 丙寅 --hour 03:30:00
```

### Key Features

Six Relations & Ten Gods mapping (varies by gender — getting it wrong invalidates the entire analysis):

| Relation | Male | Female |
|----------|------|--------|
| Father | Indirect Wealth | Direct Wealth |
| Mother | Direct Seal | Indirect Seal (Owl) |
| Spouse | Direct Wealth (Wife) | Direct Officer (Husband) |
| Son | Seven Killings | Indirect Officer |
| Daughter | Direct Officer | Eating God |
| Brother | Friend | Rob Wealth |
| Sister | Rob Wealth | Friend |

8-Dimension analysis template: Family, Health, Appearance, Career, Wealth, Love & Marriage, Social Relations, Education, Spiritual World

Calibration workflow: Ask 5 key questions after charting (parents' relationship, father's location, mother's role, family economy, current life stage) before full analysis — avoids the "first-round analysis all wrong, second rewrite" trap.

### Recommended LLMs

This project relies on LLMs for destiny analysis and interpretation. Recommended models after real-world testing:

| Model | Why Recommended |
|-------|----------------|
| Claude Sonnet 4 / Opus 4 | Deepest analysis, rigorous logic, stable long-form output, precise understanding of Bazi terminology |
| Qwen 3.7 Max | Excellent Chinese comprehension, strong grasp of Bazi terms and cultural context, great value |
| MiniMax M3 | Fluent and natural Chinese output, well-structured analysis, fast response |
| MiMo v2.5 Pro | Strong reasoning capability, clear logical chains, ideal for complex charts |

### Project Structure

```
bazi-full-fortune/
├── SKILL.md                        Full workflow documentation
├── README.md                       This file
├── package.json
├── LICENSE                         MIT
├── scripts/
│   ├── buildBaziFromSolar.ts       Solar calendar chart
│   ├── buildBaziFromLunar.ts       Lunar calendar chart
│   ├── getChineseCalendar.ts       Almanac query
│   ├── scan_year.ts                Reverse lookup
│   └── util.ts                     Shared utilities
└── references/
    └── family-patterns.md          Family pattern reference
```

### Documentation

Full workflow documentation (charting usage, six-relations rules, analysis templates, common pitfalls): [SKILL.md](./SKILL.md)

Family background pattern reference (8 patterns: signal → real-world inference → calibration questions): [references/family-patterns.md](./references/family-patterns.md)

### Dependencies

- [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) — Core charting engine
- [tyme4ts](https://github.com/6tail/tyme4ts) — Lunar-Solar conversion

### License

[MIT](./LICENSE) © 2026

### Acknowledgments

Core algorithms powered by [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) and [tyme4ts](https://github.com/6tail/tyme4ts). Analysis framework integrates traditional Ziping method with modern calibration workflow.
