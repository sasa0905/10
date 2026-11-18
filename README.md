# 心理學論文 LLM Wiki (Psychology Papers Knowledge Base)

本知識庫參考 Andrej Karpathy 的 **LLM Wiki** 理念構建，專門用於消化、整合與累積心理學各大學派與實證研究論文。

---

## 📂 資料夾與檔案架構

* **`AGENTS.md`**：知識庫的規格核心（Schema），規範 Agent 如何提取論文、標註雙向連結與維護檔案。
* **`index.md`**：全域目錄索引，按流派、理論、構念、典範量表、爭端與論文分類。
* **`log.md`**：時間軸日誌，記錄每一次攝取與健檢的操作歷程。
* **`raw/`**：【唯讀真實來源】放置您的原始論文 PDF 檔案。
* **`wiki/`**：【知識庫主體】由 Agent 自動撰寫與交叉引用的 Markdown 頁面。
  * `schools/`：各大心理學流派
  * `theories/`：理論與模型
  * `constructs/`：心理學構念
  * `paradigms-scales/`：實驗任務與量表
  * `controversies/`：學術爭論與重複性檢驗
  * `sources/`：每篇論文的結構化摘要與實證數據

---

## 🚀 如何開始使用？

### 1. 使用 Obsidian 開啟
1. 開啟 **Obsidian** 軟體。
2. 點選「開啟資料夾作為儲存庫 (Open folder as vault)」。
3. 選擇 **`wiki`** 資料夾：`c:\Users\sasa\作業10\wiki`。
4. 在左側欄即可看到最純粹的知識庫結構：各大流派、理論、構念、論文摘要，以及總目錄 `index.md` 與日誌 `log.md`。原始文獻與設定則乾淨地存放在外層。

### 2. 攝取新論文 (Ingest)
1. 將下載好的論文 PDF 放入 `raw/` 資料夾（例如 `raw/watson-rayner-1920.pdf`）。
2. 在對話中向 Agent 說：「**請幫我攝取 raw/watson-rayner-1920.pdf**」。
3. Agent 將全自動完成：
   * 精讀論文並提取實證數據與方法學指標。
   * 建立 `wiki/sources/` 結構化摘要頁。
   * 由下而上建立或更新關聯的流派、理論、構念與爭端頁面。
   * 同步更新 `index.md` 與 `log.md`。
   * 輸出處理報告供您審閱！
