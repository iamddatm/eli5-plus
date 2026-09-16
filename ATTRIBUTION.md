# 来源归属(Attribution)

本仓库内容以原创为主;唯一例外是下表中记录的上游 `eli5` skill 收录副本。

## 来源列表

| 目录 | 上游 | 许可证 | 备注 |
|---|---|---|---|
| `skills/eli5/` | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community/tree/main/eli5) | ✅ MIT | 许可证以插件自身 [`.claude-plugin/plugin.json`](./skills/eli5/.claude-plugin/plugin.json) 中的声明为准(作者 Thariq Shihipar);上游仓库根目录 LICENSE 为 Apache-2.0,插件目录内未附独立 LICENSE 文件 |

其余内容(含 [`skills/eli5-plus/`](./skills/eli5-plus))均为本仓库原创,以 [MIT](./LICENSE) 授权。

## 逐文件映射

### skills/eli5/(MIT — anthropics/claude-plugins-community)

| 本地路径 | 上游路径 |
|---|---|
| `skills/eli5/SKILL.md`                    | `eli5/skills/eli5/SKILL.md` |
| `skills/eli5/README.md`                   | `eli5/README.md` |
| `skills/eli5/.claude-plugin/plugin.json`  | `eli5/.claude-plugin/plugin.json` |

文件内容与上游逐字节一致,仅将上游插件的目录层级展平(`eli5/skills/eli5/` → `skills/eli5/`)。

抓取于 2026-09-16,对应上游 commit `a727be1c7bd6064419b6f60d71993a19198adc17`。
