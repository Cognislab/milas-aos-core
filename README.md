# MiLAS AOS v2.x — Mind-Layered Architecture System
Cognis-lab / 枝成 豆太  
2026

MiLAS (Mind-Layered Architecture System) は、  
人的内的世界を **OS として構造化**し、  
認知の **安定性・安全性・再起動性** を工学的に保証する認知アーキテクチャです。

---

# 📘 MiLAS 論文地図（総論・3本の役割）
2026年4月22日  
Jxiv 先行公開完了

## ■ MiLASとは（3行）
人的内的世界を OS として構造化し、  
認知の安定性・安全性・再起動性を保証する  
**認知アーキテクチャ**。

---

## ■ 全体構造（3層パイプライン）
L1：反応層（割り込み・情動）
↓
L2：意味生成（物語化・再解釈）
↓
L3：方針統治（行動選択・安定化）


---

# ■ 3論文の役割（階層対応）
─────────────────────┐
│ ① L1/L2 基礎設計   │ ← L1/L2 Core Model
│ MiLAS-Core-Model    │
│ ・認知階層の定義    │
│ ・Dynamic Boundary  │
│ ・Cognitive Drop    │
└─────────────────────┘
↓ 基盤提供
┌─────────────────────┐
│ ② L2 意味生成       │ ← Narrative Engine
│ ・5モジュール形式化 │
│ ・異常系＝安全装置   │
│ ・ICE監視レイヤー   │
└─────────────────────┘
↓ 意味コンパイル
┌─────────────────────┐
│ ③ L3 方針統治       │ ← Governed Dynamics
│ ・拡張リャプノフ関数 │
│ ・整合性≫生存性     │
│ ・シグモイド統治    │
└─────────────────────┘


---

# ■ MiLAS 全体像（OSパイプライン）
外界刺激 → L1（反応） → L2（意味化） → L3（行動）
↑                     ↓
ICE（監視・介入） ← 異常系（安全装置）


**入力：** 外界刺激・情動反応  
**出力：** 整合性を保った行動  
**保証：** Identity Preservation（自己同一性の維持）

---

# 📄 Jxiv 論文（先行公開）

- **L1/L2 基礎設計（MiLAS Core Model）**  
  https://jxiv.jst.go.jp/（※あなたのURLを後で貼る）

- **L2 意味生成エンジン（Narrative Engine）**  
  https://jxiv.jst.go.jp/

- **L3 方針統治（Governed Dynamical System）**  
  https://jxiv.jst.go.jp/

※ GitHub の `papers/` に PDF を置くとさらに引用されやすくなります。

---

# 🧠 用語（MiLAS 命名権）
| 用語 | 定義 | 先行研究として主張する内容 |
|------|------|----------------------------|
| ISE | Inner Safety Engineering | 内的安全を工学する分野（2026年4月提唱） |
| ICE | Sigmoid ISE | σ(ΔL+κσ²−λg) による安全ゲート |
| ISC | Inner Safety Calculation | Collapse リスク計算 |
| CIE | Cognitive Integrity Estimate | 認知健全性のスカラー指標 |
| Lyapunov Engine | L=c₀I+c₁R+c₂T | 行動方針を安定化させるエンジン |

---

# 🔧 最小実装（L3）
`examples/l3_minimal_demo.py` に  
Lyapunov Engine + ICE の最小デモを収録。

---

# 📚 引用
このリポジトリを引用する場合は、  
`CITATION.cff` または `citation.bib` を参照してください。

---

# 🏷 ライセンス
CC BY-NC 4.0
