# MiLAS AOS Core  
MiLAS 多層認知アーキテクチャ体系（コア定義）

このリポジトリは、MiLAS を中核とする  
「内的状態を記述し・動かし・実装し・運用する」  
多層認知アーキテクチャ体系のコア構造をまとめたものです。

本体系は、次の 4 層で構成されます。

1. 記述言語層：MiLAS（Mind-Layer Architecture System）  
2. 抽象OS層：MiLAS-OS（抽象的認知オペレーティングシステム）  
3. 実装層：Agent Architecture  
4. 運用層：User Protocol  

---

## 1. 記述言語層：MiLAS（Mind-Layer Architecture System）

**定義**  
内的状態およびその変化を、  
階層構造（L1 / L2 / L3）と閉ループダイナミクスとして記述する形式言語。

- モデルではない  
- 実装でもない  
- **「書く」ための枠組み**

**MiLAS が扱うもの**

- 内部状態 \( z(t) \) の定義  
- 層構造（L1 / L2 / L3）の表現  
- 状態遷移の統一記述  

**一言で言うと**

👉 MiLAS = 書く（記述言語）

---

## 2. 抽象OS層：MiLAS-OS

**定義**  
MiLAS 記述に基づき、内部状態の更新・制御・安定化を行う  
抽象的認知オペレーティングシステム。

**構成**

- Core（構造・不変条件）  
- Dynamics（状態遷移）  
- Extensions（拡張機構）

### 2.1 Core（構造・不変条件）

- **z(t)**：内部状態ベクトル  
- **L1（Reactive Layer）**：入力・身体状態を即時反映する変換  
- **L2（Narrative Layer）**：意味付与・物語化を行う変換  
- **L3（Boundary Layer）**：許容範囲・制約・自他境界を設定する変換  
- **Policy**：状態 \( z(t) \) から行動 \( a(t) \) を生成する関数  
- **Stability（ICS）**：内部状態の有界性を維持する横断制御機構  
- **Collapse**：負荷が処理能力を超え、通常更新が維持できない状態  
- **Recovery**：Collapse 後に状態を安定領域へ戻す制御過程  
- **Kernel Stable State**：有界かつ再帰的に安定する基底状態  

### 2.2 Dynamics（状態遷移）

- **状態遷移**：  
  

\[
  z(t+1) = z(t) + \Delta(t)
  \]


- **Δ(t)**：  
  - Δ_input（入力）  
  - Δ_pred（予測誤差）  
  - Δ_control（制御）  
  - ノイズ  

- **Prediction**：次状態の推定  
- **Error**：予測と観測の差分  
- **Load**：入力および内部誤差による負荷量  
- **Capacity**：状態更新を維持可能な処理能力  
- **Energy**：行動・更新を可能にする余力  
- **Mode**：Reactive / Predictive / Safe などの動作様式  

- **AOS（Adaptive Operation System）**：  
  入力・予測・誤差・更新・行動から構成される状態遷移ループ  
  （レイヤーではなくダイナミクスそのもの）

### 2.3 Extensions（拡張機構）

- **Defixation**：L2 における固定化を緩める調整機構  
- **Compassion Interface**：他者状態を安全に行動方針へ変換する機構  
- **Staged Protocol**：負荷・安定性に応じて更新を段階制御する機構  
- **Guidance Filter**：不適切な状態遷移を事前に抑制するフィルタ  
- **Activation Condition**：特定条件下で状態・方針を大域的に再構成するトリガー  

---

## 3. 実装層：Agent Architecture

- **State S(t)**：実装上の状態表現（例：S(t) = [X, M, C]）  
- **Memory**：Episodic / Semantic / Working  
- **Narrative**：状態履歴から構成される自己モデル  
- **Goal**：状態に基づき生成される行動指向  
- **Policy（実装）**：Goal と State から行動を生成する関数  
- **Social Layer**：他者状態を扱う拡張層  
- **LLM Interface**：言語と状態を相互変換する機構  

👉 Agent = 実装

---

## 4. 運用層：User Protocol

- **「今どこ？」（State Classification）**：内部状態を離散的に分類する観測インターフェース  
- **A状態**：安定状態（通常更新可能）  
- **B状態**：中間状態（観察・軽調整）  
- **C状態**：高負荷状態（更新制限・回復優先）  

**操作原則**

- A：放置  
- B：ゆるめる  
- C：何もしない  

👉 User = 使う

---

## 最終定義

MiLAS とは、  
**内的状態を統一的に記述し、その変化・制御・安定化を扱うための  
多層認知アーキテクチャ体系** である。

👉 MiLAS = 書く  
👉 OS = 動く  
👉 Agent = 実装  
👉 User = 使う

# 📚 引用
このリポジトリを引用する場合は、  
`CITATION.cff` または `citation.bib` を参照してください。

---

# 🏷 ライセンス
CC BY-NC 4.0
