---
title: "Cognitive Psychology"
aliases: ["認知心理學派", "認知學派", "認知革命"]
tags: ["school", "cognitive-psychology", "cognition"]
representative_figures: ["George A. Miller", "Ulric Neisser", "Donald Broadbent", "Jerome Bruner"]
core_assumptions: [
  "人腦是一個主動接收、編碼、儲存、檢索與處理資訊的複雜計算系統。",
  "外在刺激與最終行為之間存在關鍵的內部心智表徵（Mental Representations）與中介歷程。",
  "心智架構具備嚴格的資訊傳遞通道容量與工作記憶瓶頸。"
]
---

# 認知心理學派 (Cognitive Psychology)

> [!info] 流派概述
> 認知心理學興起於 1950 年代中期，史稱「認知革命（Cognitive Revolution）」。該學派推翻了古典行為主義將心智視為不可測「黑盒子」的教條，借用資訊理論、電腦運算架構與語言學概念，重新將注意力、知覺、記憶、語言與思維等內部心理歷程確立為心理學的核心科學主題。

---

## 1. 核心理論支柱 (Theoretical Pillars)

```mermaid
graph LR
    INPUT["外部輸入 (Input)<br>物理訊號 / 刺激"] --> BUFFER["感官暫存 (Sensory)<br>高容量 / 極短暫"]
    BUFFER --> STM["短期/工作記憶 (STM)<br>容量瓶頸: 7 ± 2 Chunks"]
    STM -->|主動組塊編碼| LTM["長時記憶 (LTM)<br>無限容量語意網絡"]
    LTM -.->|由上而下提取脈絡| STM
```

* **人類訊息處理模型 (Information-Processing Model)**：
   * 將心智類比為計算機硬體與軟體，研究資訊如何由感官輸入、短時暫存、編碼轉化並進入長時記憶。
* **容量限制與瓶頸理論 (Capacity Limitations)**：
   * 人類處理外部世界的資訊通道容量是有限的（如 [[channel-capacity|通道容量]] 與 [[short-term-memory-span|短期記憶廣度]]）。
* **主動重新編碼 (Active Recoding)**：
   * 個體並非被動接受刺激，而是透過組織、概念分類與 [[chunking|訊息組塊]] 主動擴增處理效能。

---

## 2. 實證文獻脈絡 (Empirical Context)

| 年份 | 代表文獻 / 學者 | 核心實證發現 | 影響與地位 |
| :--- | :--- | :--- | :--- |
| **1956** | [[miller-1956-magical-number-seven\|Miller (1956)]] | 確立單維絕對判斷通道容量約 $2.6\text{ bits}$，立即記憶廣度受限於 $7 \pm 2$ 個「組塊（Chunks）」，提出重新編碼理論。 | 認知革命的先鋒號角，正式敲響純行為主義黑盒子範式的喪鐘。 |

---

## 3. 學派衝突與對外延伸

* **認知學派 vs. [[behaviorism|行為學派]]**：
  * 行為主義排斥心智中介變數；認知心理學則以精密的反應時間（RT）與資訊理論數學模型，客觀測量出心智表徵的存在與容量瓶頸。
* **認知學派與 [[neuroscience|神經科學]] 的融合**：
  * 早期認知科學偏好抽象的符號計算模型，一度忽略神經生理機制；後續與神經生物學合流為「認知神經科學（Cognitive Neuroscience）」，如 [[ledoux-2000-emotion-circuits|LeDoux (2000)]] 探討情緒與認知在杏仁核及前額葉的交互整合。
