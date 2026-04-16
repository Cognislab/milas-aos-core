# MiLAS / CIE / ISC Core Architecture  
初版公開（2026-04-16）

このリポジトリは、内的世界の構造化と安全性のための  
3層アーキテクチャ（MiLAS / CIE / ISC）の初版公開です。

---

## ■ 3層構造（MiLAS → CIE → ISC）

MiLAS（地図）  
　└── CIE（内的安全工学・設計思想）  
　　　　└── ISC（内的安全計算・実行アルゴリズム）

---

## ■ 各層の概要

### ● MiLAS（Mind Layer Architecture System）
内的世界を「状態・遷移・層構造」として整理するための地図。

### ● CIE（Cognitive Inner-safety Engineering）
内的世界の安全性を設計するための工学的アプローチ。  
安全条件・負荷分散・遷移安定性などの設計規範（Design Doctrine）を扱う。

### ● ISC（Inner Safety Calculation）
CIE の設計思想を実際に“回す”ための計算層。  
安全条件の充足度、遷移安定性、負荷バランスなどを計算する。

---

## ■ 含まれるもの

- **docs/MiLAS_v2x_初版_2026-04-16.pdf**  
　MiLAS / CIE / ISC の初版ドキュメント（PDF）

- **isc/calc.py**  
　ISC（内的安全計算）の簡易実装例

---

## ■ License
MIT License  
（理論部分は著作権により保護されます）

---

# English Summary

## MiLAS / CIE / ISC — Core Architecture  
Initial public release (2026-04-16)

This repository contains the first public release of the  
three-layer architecture for internal world modeling and safety:

- **MiLAS** — structural map of the inner world  
- **CIE** — cognitive inner-safety engineering  
- **ISC** — executable inner-safety calculation

Included files:  
- PDF documentation (initial edition)  
- Simple ISC implementation (calc.py)

Licensed under MIT (theoretical content protected by copyright).
