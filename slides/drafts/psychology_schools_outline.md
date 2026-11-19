# 簡報結構大綱：心理學五大流派全景解析（零基礎教學型 HTML 簡報）

* **主題識別碼**：`psychology_schools`
* **目標成品檔**：`slides/psychology_schools_presentation.html`
* **主旨定位**：零基礎友好教學型 HTML 簡報（核心目標：讓完全沒有心理學背景的初學者僅透過簡報就能透徹理解觀念，文字充實展開）
* **預計篇幅**：11 頁（每個流派獨立 1 頁充分展開，搭配生活案例、五維度總表、學術論戰、新手思維自測與結語）
* **教學三部曲核心進程**：日常生活經驗開場 $\rightarrow$ 理論白話機制解釋 $\rightarrow$ 經典實驗故事與圖解
* **新手專屬必備模組**：每頁必備「生活常見誤區破解」＋「名詞降維對照小辭典」
* **視覺風格**：春櫻豆沙系（奶油米白底 `#faf7f5`、純白卡片、深玫瑰重點色 `#8c4b57`、櫻粉標籤 `#f7ebeb`、深炭豆沙文字 `#332d30`）、日系明朝體搭配圓體標籤、全篇使用內聯向量 SVG 圖標、大字級（$\ge 14\text{px}$）與層次卡片排版。

---

## 【節點 3 規格前移】：完整向量 SVG 圖示庫預綁定清單 (Icon Shift-Left Registry)

為徹底杜絕渲染階段隨機生成或引發圖示遺失、Unicode 豆腐塊破圖，在 **Node 3 階段全面鎖定 16 組純向量內聯 SVG** 與安全幾何底座（`w-6 h-6 rounded-md bg-[#fbf0f2] border border-[#f5dade] inline-flex items-center justify-center text-[#8c4b57]`）：

### 1. 全域語法與標準 SVG 代碼庫

| 代碼識別碼 | 圖示名稱 | 用途與語義 | 標準內聯 SVG 代碼 (viewBox="0 0 24 24") |
| :--- | :--- | :--- | :--- |
| `icon-sakura` | 櫻花徽章 | 封面與總結標籤 | `<svg class="w-4 h-4 text-[#8c4b57] inline-block mr-1 align-text-bottom" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a4 4 0 0 1 4 4c0 2-2 3-4 5-2-2-4-3-4-5a4 4 0 0 1 4-4z"/><path d="M22 12a4 4 0 0 1-4 4c-2 0-3-2-5-4 2-2 3-4 5-4a4 4 0 0 1 4 4z"/><path d="M12 22a4 4 0 0 1-4-4c0-2 2-3 4-5 2 2 4 3 4 5a4 4 0 0 1-4 4z"/><path d="M2 12a4 4 0 0 1 4-4c2 0 3 2 5 4-2 2-3 4-5 4a4 4 0 0 1-4-4z"/></svg>` |
| `icon-coffee` | 咖啡杯 | 日常生活情境開場 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>` |
| `icon-bulb` | 燈泡 | 理論白話機制核心 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/></svg>` |
| `icon-flask` | 燒瓶試管 | 經典實驗故事與數據 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 2v7.31L4.5 19.5A2 2 0 0 0 6.23 22h11.54a2 2 0 0 0 1.73-2.5L14 9.31V2"/><line x1="8" y1="2" x2="16" y2="2"/><line x1="8" y1="14" x2="16" y2="14"/></svg>` |
| `icon-shield-alert` | 盾牌驚嘆號 | 生活常見誤區破解 | `<svg class="w-4 h-4 text-[#c27685]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>` |
| `icon-book-open` | 翻開書本 | 名詞降維對照小辭典 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>` |
| `icon-box` | 黑盒子 | 行為學派 S-R 刺激反應 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>` |
| `icon-mountain` | 冰山 | 精神分析意識與潛意識 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m8 3 4 8 5-5 5 15H2L8 3z"/><path d="M4.14 15h15.72"/></svg>` |
| `icon-triangle` | 金字塔 | 人本主義需求階層 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 22 22"/><line x1="7" y1="12" x2="17" y2="12"/><line x1="4.5" y1="17" x2="19.5" y2="17"/></svg>` |
| `icon-cpu` | 晶片硬體 | 認知心理學訊息處理通道 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>` |
| `icon-zap` | 閃電直覺 | 神經認知低路徑快速警報 | `<svg class="w-4 h-4 text-[#c27685]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>` |
| `icon-brain` | 大腦皮質 | 神經認知高路徑理性分析 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a5 5 0 0 0-5 5v1a5 5 0 0 0-3 4.5A4.5 4.5 0 0 0 8 17h1a3 3 0 0 0 6 0h1a4.5 4.5 0 0 0 4-4.5A5 5 0 0 0 17 8V7a5 5 0 0 0-5-5z"/><line x1="12" y1="2" x2="12" y2="17"/></svg>` |
| `icon-compass` | 指南針 | 探索地圖與階梯導航 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>` |
| `icon-table` | 表格方陣 | 五維度跨流派對照總表 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="12" y1="3" x2="12" y2="21"/></svg>` |
| `icon-scale` | 司法天平 | 學術世紀三大論戰裁決 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>` |
| `icon-check-circle` | 勾選圓圈 | 新手思維自測對對碰 | `<svg class="w-4 h-4 text-[#8c4b57]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>` |

---

### 2. 逐頁圖示綁定映射表（嚴格禁止臨時抽換）

| 頁次 | 頁面名稱 | 封面/標題徽章 | 開場情境圖示 | 理論機制圖示 | 實驗/模型圖示 | 誤區破解圖示 | 降維辭典圖示 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P1** | 封面與五大流派全景 | `icon-sakura` | — | `icon-compass` | `icon-box`, `icon-mountain`, `icon-triangle`, `icon-cpu`, `icon-zap` | — | — |
| **P2** | 百年心靈探索階梯 | `icon-sakura` | `icon-compass` | `icon-bulb` | `icon-table` | — | — |
| **P3** | 古典行為主義 | `icon-box` | `icon-coffee` | `icon-bulb` | `icon-flask` | `icon-shield-alert` | `icon-book-open` |
| **P4** | 精神分析學派 | `icon-mountain` | `icon-coffee` | `icon-bulb` | `icon-flask` | `icon-shield-alert` | `icon-book-open` |
| **P5** | 人本主義心理學 | `icon-triangle` | `icon-coffee` | `icon-bulb` | `icon-flask` | `icon-shield-alert` | `icon-book-open` |
| **P6** | 認知心理學派 | `icon-cpu` | `icon-coffee` | `icon-bulb` | `icon-flask` | `icon-shield-alert` | `icon-book-open` |
| **P7** | 神經認知心理學 | `icon-zap` | `icon-coffee` | `icon-brain` | `icon-flask` | `icon-shield-alert` | `icon-book-open` |
| **P8** | 五大流派跨維度對照總表 | `icon-table` | — | `icon-bulb` | `icon-table` | — | — |
| **P9** | 三大世紀論戰白話裁決 | `icon-scale` | — | `icon-bulb` | `icon-scale` | — | — |
| **P10** | 新手思維自測對對碰 | `icon-check-circle` | `icon-coffee` | `icon-bulb` | `icon-check-circle` | — | — |
| **P11** | 結語與學習導航 | `icon-sakura` | — | `icon-compass` | `icon-book-open` | — | — |

---

## 頁面結構規劃（共 11 頁詳細內容）

### 第 1 頁：封面與五大學派時空全景 (Cover & Overview)
* **主標題**：現代心理學 <span class="text-[#c27685]">五大流派全景解析</span>
* **標籤**：`icon-sakura` 零基礎直觀教學 • 從日常現象到科學實證
* **核心意象**：心理學不是「讀心術」，而是理解人類行為與心靈運作的嚴謹科學。五大學派以不同視角解開人類心靈之謎。
* **五大門派時空卡片**（綁定專屬 SVG）：
  1. 行為學派 (1913, `icon-box`)：環境如何塑造我們的行為？
  2. 精神分析 (1910, `icon-mountain`)：被遺忘的童年如何暗中操控我們？
  3. 人本主義 (1943, `icon-triangle`)：人到底為了什麼而活？
  4. 認知心理 (1956, `icon-cpu`)：我們的大腦如何處理資訊與記憶？
  5. 神經認知 (2000, `icon-zap`)：腦中神經迴路如何產生喜怒哀樂？

---

### 第 2 頁：導論 • 心理學百年探索地圖 (The Scaffolding Map)
* **主標題**：從「看不見的心」到「看得見的大腦」
* **情境引言**：人類探索心靈的三大里程碑——從只看外在行為、到探勘深層潛意識、再到以現代科技看清大腦神經元。
* **循序漸進階梯**：
  * 階梯一（行為學派）：只研究「看得見、摸得著」的行為反應。
  * 階梯二（精神分析與人本）：探討看不見的深層慾望、主觀意義與生命價值。
  * 階梯三（認知與神經）：將大腦打開，看清記憶晶片如何儲存、神經迴路如何點亮。

---

### 第 3 頁：古典行為主義 • 「刺激與反應黑盒子」 (Behaviorism)
* **核心比喻**：**「黑盒子」與「條件反射」** (`icon-box`)
* **日常生活經驗** (`icon-coffee`)：為什麼每次一聽到牙醫診所刺耳的鑽牙聲，或是鬧鐘獨有的鈴聲，哪怕事情還沒發生，手心就開始冒汗、心跳加速？
* **理論白話機制** (`icon-bulb`)：人類就像一個輸入與輸出的黑盒子。我們不需要猜測內部在想什麼，只要給予特定環境刺激（S），就能預測並訓練出相對應的行為反應（R）。
* **經典實證故事** (`icon-flask`)：Watson & Rayner (1920) 小阿爾伯特實驗（Little Albert, $N=1$）。11 個月大的嬰兒原本喜愛白鼠，在白鼠與鐵鎚敲擊巨響（US）配對 7 次後，看見白鼠即產生強烈恐懼（CR）。
* **新手教學模組**：
  * **【生活常見誤區破解】** (`icon-shield-alert`)：誤以為制約就是「懲罰」？錯！制約是神經系統學會「這兩件事有連結」，就像鈴聲連結食物、白鼠連結巨響，是環境學習而非打罵。
  * **【名詞降維小辭典】** (`icon-book-open`)：「**刺激類化**」＝俗話說的「一朝被蛇咬，十年怕草繩」（小阿爾伯特後來連白兔、狗、甚至聖誕老人白鬍子都害怕）。

---

### 第 4 頁：精神分析學派 • 「意識冰山」與潛意識深海 (Psychoanalysis)
* **核心比喻**：**「漂浮的冰山」** (`icon-mountain`)
* **日常生活經驗** (`icon-coffee`)：你有沒有過這種經驗：在重要場合突然「口誤說溜嘴」、明明想減肥卻忍不住狂吃、或是遇到壓力時做出莫名幼稚的舉動？
* **理論白話機制** (`icon-bulb`)：人類能自覺的意識（Ego 自我）只是露出海面的 10% 冰山角；海平面下藏著 90% 巨大的「潛意識深海」，儲存著童年被壓抑的渴望、創傷與本能慾望（Id 本我）。
* **經典實證故事** (`icon-flask`)：Freud (1910) 奠基個案「安娜·O」（Anna O.）的臨床研究。透過「談話療法」（Talking Cure），在自由聯想與催眠中將被壓抑的情感重新語言化並宣洩，身體的痙攣與失語症狀隨之消退。
* **新手教學模組**：
  * **【生活常見誤區破解】** (`icon-shield-alert`)：誤以為潛意識是算命或神秘玄學？錯！現代認知科學已證實，大腦超過 90% 的運算都是在意識底層自動化進行的（自動導航）。
  * **【名詞降維小辭典】** (`icon-book-open`)：「**心理防衛機制（壓抑）**」＝大腦為了保護自己不崩潰，把太過痛苦的記憶「塞進地下室鎖起來」。

---

### 第 5 頁：人本主義心理學 • 人性尊嚴與「需求金字塔」 (Humanistic Psychology)
* **核心比喻**：**「向陽生長的花草種子」** (`icon-triangle`)
* **日常生活經驗** (`icon-coffee`)：為什麼人在吃飽穿暖、生活無虞之後，非但不會徹底滿足，反而會開始感到空虛？為什麼我們會渴望被朋友肯定、渴望追求藝術、甚至渴望找到「人生的意義」？
* **理論白話機制** (`icon-bulb`)：人不是被動被環境訓練的動物（反駁行為派），也不是被童年創傷支配的傀儡（反駁精神分析）。人天生俱備追求成長的內在驅力，需求是有層次向上發展的。
* **經典實證架構** (`icon-flask`)：Maslow (1943) 需求階層金字塔。底層匱乏需求（生理、安全）獲得穩定支持後，高階心理成長需求（愛與歸屬、自尊、自我實現）自然浮現。
* **新手教學模組**：
  * **【生活常見誤區破解】** (`icon-shield-alert`)：誤以為必須等到「億萬富翁、徹底安全」才能追求理想？錯！馬斯洛強調需求滿足是「相對動態」的，只要底層大致溫飽，高階渴望就會萌發。
  * **【名詞降維小辭典】** (`icon-book-open`)：「**自我實現**」＝「成為你本來就能成為的最好模樣」（發揮所有天賦潛能）。

---

### 第 6 頁：認知心理學派 • 人腦如「電腦晶片」的訊息流 (Cognitive Psychology)
* **核心比喻**：**「電腦硬體與作業系統」** (`icon-cpu`)
* **日常生活經驗** (`icon-coffee`)：為什麼別人隨口念一串 10 碼電話號碼，你幾秒後就忘得一乾二淨？但如果把電話分成 `0912-345-678` 三段，你就瞬間記住了？
* **理論白話機制** (`icon-bulb`)：認知學派打碎了行為派的黑盒子，主張人腦就像一台精密的電腦：接收外界輸入（Input）$\rightarrow$ 透過快取暫存（短期工作記憶）$\rightarrow$ 壓縮編碼儲存至硬碟（長時記憶）。
* **經典實證數據** (`icon-flask`)：Miller (1956)《神奇數字 $7 \pm 2$》。人類單次絕對判斷通道容量極限約為 2.6 位元（約 7 個項目）。但只要運用「組塊化」（Chunking）打包資訊，記憶效能就能倍增。
* **新手教學模組**：
  * **【生活常見誤區破解】** (`icon-shield-alert`)：誤以為記憶力差是智商問題？錯！所有人類的工作記憶「快取記憶體」天生都很小，差別只在於高手懂得如何把瑣碎資訊「打包成大包裹」。
  * **【名詞降維小辭典】** (`icon-book-open`)：「**組塊化（Chunking）**」＝把散落一地的散件，裝進標有分類標籤的箱子（打包壓縮）。

---

### 第 7 頁：神經認知學派 • 恐懼的「直覺快通道 vs 皮質慢分析」 (Neuroscience)
* **核心比喻**：**「緊急火警警報器與大腦偵探」** (`icon-zap`, `icon-brain`)
* **日常生活經驗** (`icon-coffee`)：在黃昏的山路上散步，腳邊突然竄過一條長條黑影，你還沒看清楚是蛇還是枯枝，身體就已經嚇得原地彈起、心臟狂跳！等過了一秒定睛一看，才發現只是截水管？
* **理論白話機制** (`icon-brain`)：大腦處理恐懼具備「雙路徑（Dual-Route）」：
  1. **低路徑（極速粗糙）**：眼睛 $\rightarrow$ 視丘 $\rightarrow$ 杏仁核（$<20\text{ ms}$）。不求看清楚，先逃命再說！
  2. **高路徑（精準理性）**：視丘 $\rightarrow$ 大腦皮質 $\rightarrow$ 杏仁核（數百毫秒）。皮質負責仔細分析「到底危不危險」，若安全則下令杏仁核解除警報。
* **經典實證成果** (`icon-flask`)：LeDoux (2000) 恐懼神經迴路實證。證實側杏仁核（LA）為恐懼記憶的突觸可塑性（LTP）物理儲存中樞。
* **新手教學模組**：
  * **【生活常見誤區破解】** (`icon-shield-alert`)：誤以為恐懼膽小是一種缺點？錯！低路徑神經迴路是數百萬年演化留給我們的「保命神器」，寧可誤報一百次，也不能漏報一次被老虎咬死。
  * **【名詞降維小辭典】** (`icon-book-open`)：「**杏仁核（Amygdala）**」＝大腦內部的煙霧偵測與警報主機。

---

### 第 8 頁：總複習一覽 • 五大流派跨維度對照總表 (Comparison Matrix)
* **主標題**：五大流派全景對照：一表看透人類心靈
* **標題徽章**：`icon-table`
* **維度對照橫跨 5 欄**：
  | 流派名稱 | 核心生活比喻 | 人性本質觀 | 核心關注焦點 | 日常生活生活應用 |
  | :--- | :--- | :--- | :--- | :--- |
  | **行為主義** | 輸入輸出的黑盒子 | 白紙一張（環境決定） | 外顯可觀察行為與制約學習 | 習慣養成、戒癮與畏懼症暴露療法 |
  | **精神分析** | 海平面下的巨大冰山 | 衝突與壓抑（早期決定） | 潛意識慾望、童年創傷與防衛 | 深度心理諮商、夢的解析、情緒洞察 |
  | **人本主義** | 向陽生長的花草種子 | 自主良善（追求實現） | 主觀體驗、尊嚴與成長潛能 | 自我探索、正向教養、職場動機賦能 |
  | **認知心理** | 電腦硬體與訊息晶片 | 資訊處理器（主動架構） | 注意力、記憶編碼與思維邏輯 | 學習策略、記憶法、認知行為治療(CBT) |
  | **神經認知** | 電路網絡與警報開關 | 生物演化機具（神經迴路） | 大腦分區、突觸可塑性、神經傳導 | 精神醫學、抗憂鬱藥物、腦機介面 |

---

### 第 9 頁：思維深化 • 三大經典世紀論戰 (Academic Controversies)
* **主標題**：大師們在吵什麼？三大歷史世紀論戰白話裁決
* **標題徽章**：`icon-scale`
* **三大並列論戰卡片**：
  1. **恐懼症到底因何而來？**（病因之爭）
     * 精神分析：恐懼是內心被壓抑的童年性創傷投射（不處理根源會產生症狀置換）。
     * 行為學派：恐懼純粹是環境配對出來的條件反射！
     * $\rightarrow$ **現代裁決**：行為暴露療法徹底治癒恐懼，反駁了症狀置換；神經科學證實恐懼是古老的防禦迴路。
  2. **大腦短期記憶到底能裝幾件事？**（容量之爭）
     * Miller (1956)：神奇數字 $7 \pm 2$。
     * Cowan (2001)：不對！7 個是因為你心裡偷偷在默背，純粹的注意力焦點只有 $4 \pm 1$ 個！
     * $\rightarrow$ **現代裁決**：日常有策略輔助時約為 7，純核心無意識複誦容量確實只有 4。
  3. **恐懼記憶到底是存在杏仁核、還是大腦皮質？**（儲存之爭）
     * LeDoux：杏仁核是直接的突觸記憶庫（突觸長出新受體）。
     * McGaugh：杏仁核只是「調味劑」，真正儲存在皮質。
     * $\rightarrow$ **現代裁決**：杏仁核兼具直接記憶物理儲存與向外調節記憶強度的雙重角色。

---

### 第 10 頁：新手思維自測 • 日常情境對對碰 (Interactive Scenarios)
* **主標題**：自我檢驗：你能用心理學視角看懂生活嗎？
* **標題徽章**：`icon-check-circle`
* **四個生活常見情境問答**：
  1. **情境 A**：「看到前任留下來的玩偶，突然心痛難受」 $\rightarrow$ 行為派制約反射（玩偶＝中性刺激，爭吵分手＝痛苦體驗）。
  2. **情境 B**：「明知道明天要大考，今天晚上卻瘋狂打掃房間」 $\rightarrow$ 精神分析防衛機制（拖延與逃避焦慮的潛意識妥協）。
  3. **情境 C**：「背單字時，把前綴 `un-` 和根詞組合起來背」 $\rightarrow$ 認知心理學組塊化（Chunking 克服通道容量）。
  4. **情境 D**：「突然有車闖紅燈，腳比大腦先踩下煞車」 $\rightarrow$ 神經認知低路徑杏仁核反射（$<20\text{ ms}$ 保命直覺）。

---

### 第 11 頁：結語與學習導航 • 走入心理學的智慧殿堂 (Conclusion & Navigation)
* **主標題**：五大學派全景巡禮完畢
* **標籤**：`icon-sakura` 探索人性的五具望遠鏡
* **溫柔總結**：心理學的五大流派並非互斥的敵人，而是觀察人類靈魂的五具望遠鏡。當我們把五個視角拼在一起，才能看見人類完整而豐富的立體全貌。
* **導引連結**：
  * 點擊跳轉：[線上 Wiki 知識庫總首頁 (`wiki/index.html`)](../../wiki/index.html)
  * 點擊跳轉：[專案總入口 (`index.html`)](../../index.html)
  * 點擊跳轉：[五大流派實證文獻專區 (`wiki/schools/`)](../../wiki/schools/behaviorism.html)
