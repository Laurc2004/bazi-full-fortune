# 八字全方位算命 Skill / Bazi Full Fortune Telling Skill

> 八字排盘与全方位命理解读工具集
> Bazi (Four Pillars) Charting & Full Destiny Analysis Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 项目简介 / Introduction

**八字全方位算命 Skill** 是一个完整的八字命理工作流工具集，基于 [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) 构建。涵盖从排盘到全方位解读的完整链路：

**Bazi Full Fortune Telling Skill** is a complete Bazi (Four Pillars of Destiny) workflow toolkit, built on [cantian-tymext](https://www.npmjs.com/package/cantian-tymext). It covers the full pipeline from chart generation to comprehensive destiny analysis:

- **排盘层 / Charting Layer** — CLI 脚本，支持阳历/农历输入，输出完整四柱、十神、神煞、大运、刑冲合会
- **分析层 / Analysis Layer** — 全方位命理解读模板，覆盖家庭、健康、事业、财富、感情、人际、学业、精神八大维度
- **参考层 / Reference Layer** — 家庭背景命理模式速查清单，用于校准分析准确性
- **反推层 / Reverse Lookup** — 从已知八字四柱反查阳历日期

---

## 🤖 推荐模型 / Recommended LLMs

本项目依赖 LLM 进行命理分析和解读。以下是实测后推荐的模型（按推荐度排序）：

This project relies on LLMs for destiny analysis and interpretation. Below are the recommended models after real-world testing (sorted by recommendation):

| 模型 / Model | 推荐理由 / Why Recommended |
|---|---|
| **Claude Sonnet 4 / Opus 4** | 分析深度最强，逻辑严密，长文输出稳定，对命理术语理解精准。全方位分析首选。 |
| **Qwen 3.7 Max** | 中文理解力极强，对八字术语和文化背景把握到位，性价比高。 |
| **MiniMax M3** | 中文输出流畅自然，分析有条理，响应速度快，适合日常排盘解读。 |
| **MiMo v2.5 Pro** | 推理能力强，逻辑链条清晰，适合需要深度分析的复杂命盘。 |

### 不推荐的场景 / Not Recommended Scenarios

- 小参数量模型（<7B）容易在六亲十神对应规则上出错（男女命搞混）
- 未经微调的通用模型可能套"严父慈母"cliché，缺少校准意识
- 纯英文模型对中文命理术语理解不足

---

## 快速开始 / Quick Start

### 环境要求 / Prerequisites

- Node.js ≥ 18（推荐 24，可直接运行 TypeScript）

### 安装 / Installation

```bash
git clone <repo-url>
cd bazi-full-fortune
npm install
```

### 排盘 / Chart Generation

```bash
# 阳历排盘 / Solar calendar chart
node scripts/buildBaziFromSolar.ts "2000-12-22T03:30:00" 0 2
#                                                时间    性别 子时配置
#                                                time   gender  early-late-zi

# 农历排盘 / Lunar calendar chart
node scripts/buildBaziFromLunar.ts "2000-11-27T03:30:00" 0 2

# 查询今日黄历 / Today's Chinese almanac
node scripts/getChineseCalendar.ts

# 查询指定日期 / Specific date
node scripts/getChineseCalendar.ts 2024-02-10
```

### 参数说明 / Parameters

| 参数 / Param | 说明 / Description | 取值 / Values |
|---|---|---|
| `solarTime` / `lunarTime` | ISO 8601 日期时间（不带时区）/ datetime without timezone | `2000-12-22T03:30:00` |
| `gender` | 性别 / gender | `1`=男 male, `0`=女 female |
| `sect` | 早晚子时配置 / late-zi-hour handling | `1`=次日 next day, `2`=当日 same day |

---

## 反推日期 / Reverse Lookup

从已知八字四柱反查阳历日期 / Find solar date(s) matching known Bazi four pillars:

```bash
# 完整四柱匹配 / Full four-pillar match
node scripts/scan_year.ts 2000 0 \
  --year-pillar 庚辰 \
  --month-pillar 戊子 \
  --day-pillar 甲寅 \
  --hour-pillar 丙寅 \
  --hour 03:30:00

# 部分匹配（仅日柱）/ Partial match (day pillar only)
node scripts/scan_year.ts 2000 0 --day-pillar 甲寅

# 跨年份扫描（每60年重复）/ Cross-year scan (60-year cycle)
for y in 1940 2000; do node scripts/scan_year.ts $y 0 --day-pillar 甲寅; done
```

---

## 项目结构 / Project Structure

```
bazi-full-fortune/
├── SKILL.md                        # 完整命理工作流文档 / Full workflow documentation
├── README.md                       # 本文件 / This file
├── package.json
├── LICENSE                         # MIT
├── scripts/
│   ├── buildBaziFromSolar.ts       # 阳历排盘 / Solar chart
│   ├── buildBaziFromLunar.ts       # 农历排盘 / Lunar chart
│   ├── getChineseCalendar.ts       # 黄历查询 / Almanac query
│   ├── scan_year.ts                # 反推扫描 / Reverse lookup
│   └── util.ts                     # 公共工具 / Shared utilities
└── references/
    └── family-patterns.md          # 家庭背景命理模式 / Family pattern reference
```

---

## 核心特性 / Key Features

### 六亲十神对应 / Six Relations & Ten Gods Mapping

根据命主性别，所有六亲对应的十神不同（搞错则全盘皆错）：
Ten Gods mapping for six relations varies by gender (getting it wrong invalidates the entire analysis):

| 六亲 / Relation | 男命 / Male | 女命 / Female |
|---|---|---|
| 父亲 / Father | 偏财 / Indirect Wealth | 正财 / Direct Wealth |
| 母亲 / Mother | 正印 / Direct Seal | 偏印（枭神）/ Indirect Seal (Owl) |
| 配偶 / Spouse | 正财（妻）/ Direct Wealth (Wife) | 正官（夫）/ Direct Officer (Husband) |
| 儿子 / Son | 七杀 / Seven Killings | 伤官 / Indirect Officer |
| 女儿 / Daughter | 正官 / Direct Officer | 食神 / Eating God |
| 兄弟 / Brother | 比肩 / Friend | 劫财 / Rob Wealth |
| 姐妹 / Sister | 劫财 / Rob Wealth | 比肩 / Friend |

### 八大维度分析模板 / 8-Dimension Analysis Template

1. 👨‍👩‍👧 家庭 / Family
2. 🏥 健康 / Health
3. 👤 外貌身材 / Appearance
4. 💼 事业 / Career
5. 💰 财富 / Wealth
6. 💕 感情婚姻 / Love & Marriage
7. 👥 人际关系 / Social Relations
8. 📚 学业 / Education
9. 🧘 精神世界 / Spiritual World

### 校准工作流 / Calibration Workflow

排盘后先向用户确认 5 个关键事实，再做完整解读（避免"第一轮分析全错、二次重写"）：
Confirm 5 key facts before full analysis (to avoid "first-round analysis all wrong, second rewrite"):

1. 父母是否在一起 / Are parents together?
2. 父亲职业/常驻地 / Father's occupation & location
3. 母亲是否在带 / Is mother the primary caregiver?
4. 家庭经济来源 / Family economic background
5. 自己的学历/工作状态 / Own education & career status

---

## 文档 / Documentation

完整命理工作流文档（含排盘用法、六亲规则、分析模板、常见陷阱）请参阅：

For the full workflow documentation (charting usage, six-relations rules, analysis templates, common pitfalls), see:

📄 [SKILL.md](./SKILL.md)

家庭背景命理模式参考（8 种模式的命理信号 → 现实推断 → 校准问题）：

Family background pattern reference (8 patterns: signal → real-world inference → calibration questions):

📄 [references/family-patterns.md](./references/family-patterns.md)

---

## 依赖 / Dependencies

- [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) — 底层排盘引擎 / Core charting engine
- [tyme4ts](https://github.com/6tail/tyme4ts) — 农历/阳历转换 / Lunar-Solar conversion

---

## 许可证 / License

[MIT](./LICENSE) © 2026

---

## 致谢 / Acknowledgments

- 底层算法基于 [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) 和 [tyme4ts](https://github.com/6tail/tyme4ts)
- Core algorithms powered by [cantian-tymext](https://www.npmjs.com/package/cantian-tymext) and [tyme4ts](https://github.com/6tail/tyme4ts)
- 命理分析框架融合了传统子平术与现代校准工作流
- Analysis framework integrates traditional Ziping method with modern calibration workflow
