# 知識庫操作日誌 (Wiki Operations Log)

本檔案為時間軸單向追加日誌（Append-only）。記錄所有文獻攝取（Ingest）、綜合查詢回填（Query Backfill）與健康檢查（Lint）之歷程。

---

## [2026-11-18] init | 建立心理學論文 LLM Wiki 知識庫規範與骨架
- **操作類型**：系統初始化 (System Init)
- **完成項目**：
  - 建立規範手冊 [[AGENTS.md]]，確立三層架構與 Ingest / Query / Lint 運作流程。
  - 確立採用「由下而上 (Bottom-up)」策略與 APA 7th 證據溯源規範。
  - 建立全域目錄 [[index.md]] 與日誌 [[log.md]]。
  - 建立資料夾結構：`raw/`、`wiki/schools/`、`wiki/theories/`、`wiki/constructs/`、`wiki/paradigms-scales/`、`wiki/controversies/`、`wiki/sources/`。

## [2026-11-18] ingest | Conditioned Emotional Reactions (Watson & Rayner, 1920)
- **操作類型**：論文攝取與網絡編織 (Ingest & Compounding)
- **原始來源**：[[raw/watson-rayner-1920.md]]
- **新建文獻摘要頁**：
  - [[watson-rayner-1920-conditioned-fear]] (N = 1, 7 次 CS-US 配對, 刺激類化至兔/狗/毛皮大衣/面具, 持續 31 天)
- **衍生與更新實體頁面**：
  - 流派頁：[[behaviorism]]（動態建立古典行為主義頁面與 S-R 主張）
  - 理論頁：[[classical-conditioning]]（建立古典制約情緒機制與流程圖）
  - 構念頁：[[fear-conditioning]]（建立恐懼制約定義與吸吮拇指補償反應）
  - 構念頁：[[stimulus-generalization]]（建立刺激類化概念與 Albert 類化梯度圖）
  - 典範頁：[[little-albert-paradigm]]（整理四階段實驗程序與倫理檢討）
  - 爭端頁：[[little-albert-replication-debate]]（記錄 Bregman 1934 複製失敗、Douglas Merritte 腦積水爭端與對抗精神分析之病因論戰）
- **目錄更新**：同步登記於 [[index.md]]

## [2026-11-18] ingest | The Origin and Development of Psychoanalysis (Freud, 1910)
- **操作類型**：論文攝取與網絡編織 (Ingest & Compounding)
- **原始來源**：[[raw/freud-1910.md]]
- **新建文獻摘要頁**：[[freud-1910-psychoanalysis-origin]] (Anna O. 案例, 壓抑, 夢的工作, 幼兒性慾, 移情)
- **衍生實體頁面**：
  - 流派頁：[[psychoanalysis]]（建立精神分析學派與潛意識假設）
  - 理論頁：[[psychoanalytic-theory]]（心智三結構與人格動力模型）
  - 構念頁：[[unconscious]]（潛意識定義）、[[repression]]（壓抑與阻抗機制）、[[transference]]（移情作用）
  - 典範頁：[[talking-cure-catharsis]]（談話療法與情緒宣洩）
  - 爭端頁：[[behaviorism-vs-psychoanalysis]]（行為學派 vs 精神分析在恐懼成因的世紀論戰）

## [2026-11-18] ingest | The Magical Number Seven, Plus or Minus Two (Miller, 1956)
- **操作類型**：論文攝取與網絡編織 (Ingest & Compounding)
- **原始來源**：[[raw/miller-1956.md]]
- **新建文獻摘要頁**：[[miller-1956-magical-number-seven]] (單維通道容量 2.6 bits, 立即記憶廣度 7±2, 重新編碼)
- **衍生實體頁面**：
  - 流派頁：[[cognitive-psychology]]（建立認知心理學派與資訊處理觀）
  - 理論頁：[[information-processing-theory]]（心智通訊與計算流程圖）
  - 構念頁：[[chunking]]（訊息組塊化）、[[channel-capacity]]（單維與多維通道容量）
  - 典範頁：[[immediate-memory-span-task]]（立即記憶廣度作業）
  - 爭端頁：[[chunking-capacity-cowan-debate]]（記憶容量 7±2 vs. Cowan 4±1 爭辯）

## [2026-11-18] ingest | A Theory of Human Motivation (Maslow, 1943)
- **操作類型**：論文攝取與網絡編織 (Ingest & Compounding)
- **原始來源**：[[raw/maslow-1943.md]]
- **新建文獻摘要頁**：[[maslow-1943-human-motivation]] (五大基本需求, 相對優勢性, 階層反轉例外)
- **衍生實體頁面**：
  - 流派頁：[[humanistic-psychology]]（建立人本主義學派「第三勢力」）
  - 理論頁：[[hierarchy-of-needs]]（五層需求階層金字塔與動態特徵）
  - 構念頁：[[self-actualization]]（自我實現構念定義與正向心理學延伸）

## [2026-11-18] ingest | Emotion Circuits in the Brain (LeDoux, 2000)
- **操作類型**：論文攝取與網絡編織 (Ingest & Compounding)
- **原始來源**：[[raw/ledoux-2000.md]]
- **新建文獻摘要頁**：[[ledoux-2000-emotion-circuits]] (側杏仁核感覺介面, 丘腦低路徑/高路徑, LTP 突觸可塑性, 邊緣系統批判)
- **衍生實體頁面**：
  - 流派頁：[[neuroscience]]（建立神經科學與生物心理學派）
  - 理論頁：[[dual-route-emotion-theory]]（情緒雙路徑低路徑/高路徑神經迴路圖）
  - 典範頁：[[auditory-fear-conditioning-paradigm]]（聽覺恐懼制約神經實驗典範）
  - 爭端頁：[[amygdala-storage-vs-modulation]]（杏仁核是直接突觸儲存中樞還是調節器之論戰）
  - 實體多點更新：同步更新 [[fear-conditioning]] 補充細胞與神經迴路層次機制；更新 [[behaviorism]] 增列神經機制還原。

## [2026-11-18] schema | 建立簡報生成 Graph 工作流規範
- **操作類型**：系統規範升級 (Schema Update)
- **更新項目**：
  - 在 [[AGENTS.md]] 正式增訂「第 5 章：簡報生成工作流規範 (Presentation Generation Workflow — Graph Schema)」。
  - 確立 10 節點 Graph 架構（含覆蓋率關卡、忠實度檢查、渲染相容性檢查、大綱階段人工確認與單頁局部退回修復）。
  - 確立簡報目錄架構：`slides/` 與 `slides/drafts/`。
  - 固化春櫻豆沙系日系明朝體、大字級與內聯向量 SVG 圖標設計規範。

## [2026-11-18] presentation | 各流派介紹（五大流派全景解析重點複習講義）
- **操作類型**：Graph 工作流簡報生成 (Presentation Generation)
- **依據大綱**：`slides/drafts/psychology_schools_outline.md`（經使用者人工審查核准）
- **逐頁腳本**：`slides/drafts/psychology_schools_script.md`
- **生成檔案**：`slides/psychology_schools_presentation.html` (9 頁互動簡報)
- **關卡檢驗**：
  - 覆蓋率關卡：Pass（涵蓋 5 篇奠基論文、5 大流派、5 個核心模型、4 項爭端）
  - 忠實度檢查：Pass（數據與 Wiki 實體 100% 吻合，零外推）
  - 渲染相容性：Pass（向量 SVG 圖標、字體放大至 15px+、無文字溢出、全螢幕與鍵盤導航正常）

## [2026-11-18] schema | 固化圖示相容性檢查點與簡報流程定案
- **操作類型**：工作流強化升級 (Workflow Enhancement)
- **完成項目**：
  - 簡報檔案結構定案：最新正式檔存放於 `slides/<主題>_presentation.html`，草稿存於 `slides/drafts/`（不保留多餘歷史備份）。
  - 在 [[AGENTS.md]] 第 5 章增加「圖示完整度專項檢查點」，明訂：零脆弱 Emoji 原則、零外部 CDN 依賴、SVG 格式合法性檢查與安全幾何底座規範。
  - 將實務反思的三大防線（Node 3/4 規格前移、Node 7 數值硬斷言、Node 9 靜態代碼掃描閥門）固化入正式 Graph Schema。

## [2026-11-19] web | 靜態純 HTML 知識庫生成（零前端框架直接部署）
- **操作類型**：Web 發布層架構升級 (Zero-Framework Static Export)
- **完成項目**：
  - 將 31 篇 Markdown 筆記全面預先轉譯為純靜態 HTML 頁面（共 33 篇獨立網頁，無 React/Vue/Node.js 等前端框架依賴）。
  - 所有 `[[雙向鏈接]]` 轉化為原生相對路徑 HTML 超連結，點擊即流暢跳轉，瀏覽器上一頁/下一頁原生支援。
  - 保留春櫻豆沙系日系明朝體、Zen Maru Gothic、Washi 質感與四大高亮引言盒排版。
  - 支援直接部署至 GitHub Pages 即開即看。

## [2026-11-19] fix | 全面修復流程圖語法錯誤與解除 SVG 壓縮（確保高清晰字體）
- **操作類型**：視覺渲染深度修復 (High-DPI Diagram Fix & Anti-Compression)
- **問題根因**：
  1. 部分 Mermaid 流程圖語法存在箭頭標籤格式錯誤（如 `==>|text|` 非標準箭頭語法、未轉義 `<20 ms` 與子圖括號未引號包裹），導致 Mermaid 解析報錯而無法顯示圖形。
  2. 預設 Mermaid 將 SVG 強制壓縮至欄位寬度（`max-width: 100%`），致使寬圖中文字被整體縮放至 7~8px，文字嚴重擁擠擠壓。
  3. 需求階層、五大論文摘要（如 Watson 1920、Freud 1910、Miller 1956）與各學派頁面先前缺少實質向量圖解。
- **修復項目**：
  - 修正所有 Mermaid 圖表之箭頭語法（全面採用標準 `== "text" ==>`）、轉義 `<` 字符並重構 ID 與引號。
  - 於編譯器中追加自動語法正規化濾波器，預防任何非標準箭頭破壞圖形渲染。
  - 在 Mermaid 初始化中配置 `flowchart: { useMaxWidth: false }`，並在 CSS 中宣告 `.mermaid-diagram svg { max-width: none !important; }`，徹底解除向量圖縮放壓縮，保證文字維持 15px+ 原生清晰度，並提供流暢橫向捲軸與提示卡。
  - 為 5 大流派（行為黑盒子、精神分析冰山、認知訊息流、人本動機階層、神經情緒迴路）與 5 篇奠基論文全面補充標準高清晰流程圖解。

## [2026-11-19] layout | 古典制約模型重構為由上往下 1-3 流程並導入 KaTeX 數學排版
- **操作類型**：模型架構垂直重構與數學排版引擎升級 (Model Restructuring & KaTeX Integration)
- **完成項目**：
  - 古典制約理論（`theories/classical-conditioning.md` 及 `sources/watson-rayner-1920-conditioned-fear.md`）核心架構由橫向左右排列全面重構為由上而下（Top-Down, `graph TD`）的階段 1 $\rightarrow$ 階段 2 $\rightarrow$ 階段 3 嚴格循序流程圖，清楚呈現制約前、配對刺激與制約後（含刺激類化）之時序演變。
  - 全站 33 篇靜態 HTML 及簡報頁面全面導入 KaTeX 數學渲染引擎與 Auto-Render 模組，完整呈現 $N = 1$、$7 \pm 2$、$4 \pm 1$、$\mu = 2.6\text{ bits}$、$\sigma = 0.6\text{ bits}$ 等數學與統計符號。

## [2026-11-19] format | 全域統一採用標準 LaTeX 數學與統計語法排版
- **操作類型**：公式與統計量標準化 (Universal LaTeX Math Normalization)
- **完成項目**：
  - 檢索全專案所有 Markdown 實體與互動簡報，將所有樣本數（$N = 1$、$N = 15$）、容量限制常數（$7 \pm 2$、$4 \pm 1$）、資訊理論數值（$\mu = 2.6\text{ bits}$、$\sigma \approx 0.6\text{ bits}$、$2.5\text{ bits}$、$2.3\text{ bits}$、$1.9\text{ bits}$、$3.25\text{ bits}$、$4.6\text{ bits}$、$7.2\text{ bits}$）、指數運算（$2^{2.6} \approx 6.5$）、反應延遲（$< 20\text{ ms}$）、顯著性（$p < .01$）及離散位元單位（$1\text{ bit/item}$、$3.3\text{ bits/item}$、$4.7\text{ bits/item}$、$\approx 10\text{ bits/item}$）全面統一改採標準 LaTeX 數學語法。
  - 在全站與簡報中強化 KaTeX 載入生命週期與多重喚醒機制（`onload`、`DOMContentLoaded`、定時重掃），確保公式 100% 準確轉換為向量級數學排版。

## [2026-11-19] deliver | 心理學五大流派全景解析（各流派介紹圖文簡報）通過 Graph 流程正式交件
- **操作類型**：簡報工作流正式交件 (Presentation Graph Delivery)
- **完成項目**：
  - **節點 5 人工審查確認通過**：使用者審查並正式核准 9 頁簡報大綱（涵蓋 5 大流派、橫評矩陣與歷史論戰）。
  - **節點 6 逐頁稿校準**：嚴格落實防線 1（每張卡片 $\le 3$ 條重點，每條 $\le 25$ 字），留存於 `slides/drafts/psychology_schools_script.md`。
  - **節點 7 忠實度硬斷言檢驗通過**：比對樣本數 $N=1$（Albert B.）、7 次配對、音高 $2.5\text{ bits}$、$7 \pm 2$ 與 $4 \pm 1$ 組塊、LeDoux 低路徑延遲 $< 20\text{ ms}$、Maslow 需求滿足百分比及 Douglas Merritte 早夭病歷，100% 忠實對齊 Wiki 原始文獻。
  - **節點 8 & 9 代碼渲染與靜態掃描通過**：全面移除 Emoji 改採 38 處純向量 SVG 搭配安全底座，字級嚴格保證 $\ge 14\text{px}$，KaTeX 數學公式與按鍵換頁邏輯驗證無誤。
  - **節點 10 正式交付**：交付成品檔 `slides/psychology_schools_presentation.html` 並同步更新首頁入口與遠端儲存庫。

## [2026-11-19] presentation | 五大流派全景解析（11 頁零基礎教學型簡報）
- **操作類型**：教學型 Graph 工作流簡報正式生成 (Pedagogical Presentation Delivery)
- **依據大綱**：`slides/drafts/psychology_schools_outline.md`（經節點 5 人機協同審查核准）
- **逐頁腳本**：`slides/drafts/psychology_schools_script.md`
- **生成檔案**：`slides/psychology_schools_presentation.html` (11 頁零基礎教學互動簡報)
- **關卡檢驗**：
  - **覆蓋率關卡（Node 2）**：Pass（涵蓋 5 篇奠基論文、5 大流派、5 個核心模型、3 大世紀論戰）。
  - **圖示預綁定防線（Node 3）**：Pass（全面預綁定 16 組純向量內聯 SVG 與逐頁映射表，杜絕隨機生成）。
  - **忠實度與易讀性雙重關卡（Node 7）**：Pass（數據比對 100% 吻合；每頁配備日常情境、生活常見誤區破解與名詞降維小辭典，經零背景初學者理解度檢驗無阻礙）。
  - **代碼靜態掃描閥門（Node 9）**：Pass（11 頁完整閉合、44 組向量內聯 SVG 經白名單 100% 比對通過、零 Unicode 豆腐塊 Emoji、字體嚴格 $\ge 14\text{px}$、鍵盤導航與動態進度點無誤）。














