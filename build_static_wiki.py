import os
import re

wiki_dir = r"c:\Users\sasa\作業10\wiki"

cat_info = {
    "schools": {"title": "各大心理學流派", "icon": "📚"},
    "theories": {"title": "理論與心理模型", "icon": "🏛️"},
    "constructs": {"title": "核心心理學構念", "icon": "💡"},
    "paradigms-scales": {"title": "實驗典範與量表", "icon": "🔬"},
    "controversies": {"title": "學術爭端與檢驗", "icon": "⚖️"},
    "sources": {"title": "奠基論文文獻庫", "icon": "📄"},
}

all_notes = {}
slug_to_rel_html = {}

# 1. Discover all files
for root, dirs, files in os.walk(wiki_dir):
    if ".obsidian" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, wiki_dir).replace("\\", "/")
            slug = f.replace(".md", "")
            
            with open(full_path, "r", encoding="utf-8") as file:
                raw_text = file.read()
            
            html_rel_path = rel_path.replace(".md", ".html")
            
            title = slug
            aliases = ""
            yaml_meta = {}
            if raw_text.startswith("---"):
                end_fm = raw_text.find("---", 3)
                if end_fm != -1:
                    fm_text = raw_text[3:end_fm].strip()
                    for line in fm_text.split("\n"):
                        if ":" in line:
                            k, v = line.split(":", 1)
                            k = k.strip()
                            v = v.strip().strip('"').strip("'")
                            yaml_meta[k] = v
                            if k == "title":
                                title = v
                            elif k == "aliases":
                                aliases = v.replace("[", "").replace("]", "").replace('"', '').replace("'", "")
            
            if not title or title == slug:
                for line in raw_text.split("\n"):
                    if line.startswith("# "):
                        title = line.replace("# ", "").strip()
                        break

            category = rel_path.split("/")[0] if "/" in rel_path else "root"
            display_name = aliases.split(",")[0].strip() if aliases else title

            all_notes[rel_path] = {
                "full_path": full_path,
                "rel_path": rel_path,
                "html_rel_path": html_rel_path,
                "slug": slug,
                "title": title,
                "aliases": aliases,
                "display_name": display_name,
                "yaml_meta": yaml_meta,
                "raw_text": raw_text,
                "category": category
            }
            slug_to_rel_html[slug] = html_rel_path
            slug_to_rel_html[slug.lower()] = html_rel_path

# Relative path calculator
def get_relative_link(from_html, to_html):
    from_dir = os.path.dirname(from_html)
    return os.path.relpath(to_html, from_dir).replace("\\", "/")

# Simple yet complete Markdown to HTML converter
def convert_markdown_to_html(md_text, current_html_path):
    # Remove YAML frontmatter if present
    text = md_text
    if text.startswith("---"):
        end_fm = text.find("---", 3)
        if end_fm != -1:
            text = text[end_fm + 3:].strip()

    # Pre-process [[wikilinks]]
    def replace_wikilink(match):
        inner = match.group(1).strip()
        if "|" in inner:
            target, label = inner.split("|", 1)
            target = target.strip()
            label = label.strip()
        else:
            target = inner
            label = inner
        
        target_slug = target.split("/").pop().replace(".md", "").strip()
        target_html = slug_to_rel_html.get(target_slug) or slug_to_rel_html.get(target_slug.lower())
        
        if target_html:
            rel_url = get_relative_link(current_html_path, target_html)
            return f'<a href="{rel_url}" class="wiki-link" title="{label}">{label}</a>'
        else:
            return f'<span class="wiki-link-unresolved" title="未建立頁面">{label}</span>'

    text = re.sub(r'\[\[(.*?)\]\]', replace_wikilink, text)

    # Pre-process standard markdown links [label](path.md)
    def replace_md_link(match):
        label = match.group(1)
        url = match.group(2)
        if url.endswith(".md"):
            # Resolve to .html
            target_slug = url.split("/").pop().replace(".md", "")
            target_html = slug_to_rel_html.get(target_slug)
            if target_html:
                rel_url = get_relative_link(current_html_path, target_html)
                return f'<a href="{rel_url}" class="wiki-link">{label}</a>'
        return f'<a href="{url}">{label}</a>'

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_md_link, text)

    lines = text.split("\n")
    out = []
    in_list = False
    in_callout = False
    callout_type = ""
    callout_lines = []
    in_table = False
    table_header = True

    def flush_callout():
        nonlocal in_callout, callout_type, callout_lines
        if in_callout:
            c_body = "\n".join(callout_lines)
            c_html = convert_markdown_to_html(c_body, current_html_path)
            
            callout_titles = {
                "abstract": ("📋 核心發現與摘要", "callout-abstract"),
                "info": ("💡 理論與構念精準定義", "callout-info"),
                "warning": ("⚠️ 方法學評價與研究限制", "callout-warning"),
                "important": ("⚖️ 核心學術爭端與理論衝突", "callout-important"),
            }
            c_title, c_class = callout_titles.get(callout_type.lower(), ("📌 說明", "callout-info"))
            out.append(f'<div class="callout {c_class}"><div class="callout-title">{c_title}</div><div class="callout-body">{c_html}</div></div>')
            in_callout = False
            callout_type = ""
            callout_lines = []

    for line in lines:
        stripped = line.strip()

        # Check callouts > [!type]
        callout_match = re.match(r'^>\s*\[!([a-zA-Z]+)\]\s*(.*)$', stripped)
        if callout_match:
            flush_callout()
            if in_list:
                out.append("</ul>")
                in_list = False
            in_callout = True
            callout_type = callout_match.group(1)
            first_line = callout_match.group(2).strip()
            if first_line:
                callout_lines.append(first_line)
            continue
        
        if in_callout:
            if stripped.startswith(">"):
                callout_lines.append(stripped[1:].strip())
                continue
            else:
                flush_callout()

        # Lists
        if stripped.startswith("* ") or stripped.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            item_text = stripped[2:].strip()
            # inline formatting
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
            item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
            out.append(f"<li>{item_text}</li>")
            continue
        else:
            if in_list:
                out.append("</ul>")
                in_list = False

        # Table row
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                out.append('<div class="table-container"><table>')
                in_table = True
                table_header = True
            
            cells = [c.strip() for c in stripped[1:-1].split("|")]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                table_header = False
                continue

            tag = "th" if table_header else "td"
            cell_htmls = []
            for c in cells:
                c = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                c = re.sub(r'`(.*?)`', r'<code>\1</code>', c)
                cell_htmls.append(f"<{tag}>{c}</{tag}>")
            
            row_html = "".join(cell_htmls)
            if table_header:
                out.append(f"<thead><tr>{row_html}</tr></thead><tbody>")
            else:
                out.append(f"<tr>{row_html}</tr>")
            continue
        else:
            if in_table:
                out.append("</tbody></table></div>")
                in_table = False

        # Headings
        if stripped.startswith("# "):
            out.append(f"<h1>{stripped[2:].strip()}</h1>")
            continue
        elif stripped.startswith("## "):
            out.append(f"<h2>{stripped[3:].strip()}</h2>")
            continue
        elif stripped.startswith("### "):
            out.append(f"<h3>{stripped[4:].strip()}</h3>")
            continue
        elif stripped.startswith("#### "):
            out.append(f"<h4>{stripped[5:].strip()}</h4>")
            continue

        # Horizontal Rule
        if stripped in ["---", "***", "___"]:
            out.append("<hr>")
            continue

        # Empty line
        if not stripped:
            continue

        # Normal paragraph
        p_text = stripped
        p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_text)
        p_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_text)
        p_text = re.sub(r'`(.*?)`', r'<code>\1</code>', p_text)
        out.append(f"<p>{p_text}</p>")

    flush_callout()
    if in_list:
        out.append("</ul>")
    if in_table:
        out.append("</tbody></table></div>")

    return "\n".join(out)

# Shared Pure CSS Template (No Framework, Zero External Dependencies)
def build_html_page(note, current_html_path):
    # Calculate navigation paths
    rel_root = get_relative_link(current_html_path, "index.html")
    rel_log = get_relative_link(current_html_path, "log.html")
    
    # Path to slides
    # if in schools/ -> ../../slides/...
    # if in root -> ../slides/...
    is_root = "/" not in note["rel_path"]
    rel_slides = "../slides/psychology_schools_presentation.html" if is_root else "../../slides/psychology_schools_presentation.html"
    rel_home = "../index.html" if is_root else "../../index.html"

    # Build sidebar HTML
    sidebar_sections = []
    for cat_key, cat in cat_info.items():
        items = [n for n in all_notes.values() if n["category"] == cat_key]
        items.sort(key=lambda x: x["slug"])
        if not items:
            continue
        
        items_html = []
        for it in items:
            target_url = get_relative_link(current_html_path, it["html_rel_path"])
            is_active = (it["rel_path"] == note["rel_path"])
            active_class = " nav-item-active" if is_active else ""
            label = it["aliases"].split(",")[0].strip() if it["aliases"] else it["title"]
            items_html.append(f'<a href="{target_url}" class="nav-item{active_class}" title="{it["title"]}">{label}</a>')
        
        sec_html = f'''
        <div class="nav-section">
          <div class="nav-section-title">
            <span>{cat["icon"]} {cat["title"]}</span>
            <span class="nav-section-count">{len(items)}</span>
          </div>
          <div class="nav-section-items">
            {"".join(items_html)}
          </div>
        </div>
        '''
        sidebar_sections.append(sec_html)

    # Render Frontmatter Metadata Card
    fm = note["yaml_meta"]
    meta_card = ""
    if fm and (fm.get("aliases") or fm.get("year") or fm.get("authors") or fm.get("sample_size")):
        badges = []
        if fm.get("aliases"):
            badges.append(f'<span class="badge badge-rose font-bold">{fm["aliases"]}</span>')
        if fm.get("year"):
            badges.append(f'<span class="badge badge-gray">年份：{fm["year"]}</span>')
        if fm.get("authors"):
            badges.append(f'<span class="badge badge-gray">作者：{fm["authors"]}</span>')
        if fm.get("sample_size"):
            badges.append(f'<span class="badge badge-warm">樣本量：{fm["sample_size"]}</span>')
        if fm.get("effect_size"):
            badges.append(f'<span class="badge badge-gray">效應值：{fm["effect_size"]}</span>')
        if fm.get("replication_status"):
            badges.append(f'<span class="badge badge-gray">複製狀態：{fm["replication_status"]}</span>')

        meta_card = f'<div class="meta-card">{"".join(badges)}</div>'

    # Render Body HTML
    body_html = convert_markdown_to_html(note["raw_text"], current_html_path)

    # Category display name
    cat_name = cat_info.get(note["category"], {}).get("title", note["category"])
    
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{note["title"]} — 心理學 LLM Wiki</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Shippori+Mincho:wght@500;700;800&family=Zen+Maru+Gothic:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    /* Pure Vanilla CSS - Zero Framework Dependencies */
    :root {{
      --bg-cream: #faf7f5;
      --bg-sidebar: #f5eeea;
      --card-white: #ffffff;
      --border-warm: #ebdcd5;
      --border-rose: #edd5da;
      --text-main: #332d30;
      --text-sub: #786f73;
      --rose-deep: #8c4b57;
      --rose-accent: #c27685;
      --rose-light: #f7ebeb;
      --green-soft: #597864;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Shippori Mincho', 'Noto Serif TC', serif;
      background-color: var(--bg-cream);
      color: var(--text-main);
      line-height: 1.7;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }}
    /* Top Header */
    .top-header {{
      background-color: rgba(250, 247, 245, 0.95);
      border-bottom: 1px solid var(--border-warm);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(8px);
    }}
    .header-logo {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}
    .logo-badge {{
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: linear-gradient(135deg, #e8c7cd, #f7ebeb);
      border: 1px solid #e5b9c1;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--rose-deep);
      font-weight: bold;
      font-size: 15px;
    }}
    .logo-text h1 {{
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.05em;
    }}
    .logo-text span {{
      font-size: 11px;
      color: var(--text-sub);
      font-family: 'Zen Maru Gothic', sans-serif;
      display: block;
      margin-top: -2px;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn {{
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 12px;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      border: 1px solid var(--border-warm);
    }}
    .btn-rose {{
      background-color: var(--rose-light);
      color: var(--rose-deep);
    }}
    .btn-rose:hover {{
      background-color: #f0dde0;
    }}
    .btn-white {{
      background-color: #ffffff;
      color: #554a4f;
    }}
    .btn-white:hover {{
      background-color: #f7f2ef;
    }}

    /* Main Dual Layout */
    .wiki-container {{
      max-width: 1360px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex: 1;
    }}
    /* Sidebar */
    .wiki-sidebar {{
      width: 290px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-warm);
      padding: 18px 14px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-height: calc(100vh - 59px);
      position: sticky;
      top: 59px;
      overflow-y: auto;
    }}
    .nav-search {{
      width: 100%;
      padding: 7px 12px;
      border-radius: 10px;
      border: 1px solid var(--border-warm);
      background-color: #ffffff;
      font-size: 12px;
      font-family: 'Zen Maru Gothic', sans-serif;
      outline: none;
    }}
    .nav-search:focus {{
      border-color: var(--rose-accent);
    }}
    .nav-section {{
      margin-bottom: 6px;
    }}
    .nav-section-title {{
      font-size: 11px;
      font-weight: 700;
      color: var(--text-sub);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'Zen Maru Gothic', sans-serif;
    }}
    .nav-section-count {{
      font-size: 10px;
      color: #a89fa4;
    }}
    .nav-section-items {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      padding-left: 6px;
      margin-top: 2px;
    }}
    .nav-item {{
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-family: 'Zen Maru Gothic', sans-serif;
      color: #52474c;
      text-decoration: none;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      transition: all 0.15s ease;
    }}
    .nav-item:hover {{
      background-color: #ede2dd;
      color: var(--rose-deep);
    }}
    .nav-item-active {{
      background-color: var(--card-white);
      color: var(--rose-deep);
      font-weight: 700;
      box-shadow: 0 1px 4px rgba(140, 75, 87, 0.08);
      border-left: 3px solid var(--rose-accent);
    }}

    /* Main Reading Content */
    .wiki-main {{
      flex: 1;
      background-color: var(--card-white);
      padding: 36px 48px;
      max-width: 960px;
      min-width: 0;
    }}
    .breadcrumb {{
      font-size: 12px;
      color: var(--text-sub);
      font-family: 'Zen Maru Gothic', sans-serif;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .breadcrumb a {{
      color: inherit;
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--rose-accent);
    }}
    .meta-card {{
      background-color: #faf5f2;
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 10px 14px;
      margin-bottom: 24px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 12px;
    }}
    .badge {{
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
    }}
    .badge-rose {{ background: #ffffff; border: 1px solid var(--border-rose); color: var(--rose-deep); }}
    .badge-gray {{ background: #eee7e4; color: #5a5055; }}
    .badge-warm {{ background: #fcefe8; color: #a05a30; border: 1px solid #ebd4c6; }}

    /* Markdown Styling */
    .content h1 {{
      font-size: 28px;
      font-weight: 800;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border-warm);
      padding-bottom: 10px;
      color: #2e292d;
    }}
    .content h2 {{
      font-size: 20px;
      font-weight: 700;
      margin-top: 28px;
      margin-bottom: 12px;
      color: #40363a;
    }}
    .content h3 {{
      font-size: 16px;
      font-weight: 700;
      margin-top: 20px;
      margin-bottom: 8px;
      color: #55484d;
    }}
    .content p {{
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 15px;
      line-height: 1.85;
      margin-bottom: 14px;
      color: #40383b;
    }}
    .content ul {{
      padding-left: 24px;
      margin-bottom: 16px;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 14px;
      line-height: 1.8;
      color: #483f43;
    }}
    .content li {{
      margin-bottom: 6px;
    }}
    .content hr {{
      border: 0;
      border-top: 1px dashed var(--border-warm);
      margin: 28px 0;
    }}
    .content code {{
      font-family: ui-monospace, Consolas, monospace;
      background-color: #f2e9e6;
      color: var(--rose-deep);
      padding: 2px 6px;
      border-radius: 5px;
      font-size: 13px;
    }}

    /* Clickable Wiki Links */
    a.wiki-link {{
      color: var(--rose-accent);
      font-weight: 600;
      text-decoration: none;
      border-bottom: 1px dashed var(--rose-accent);
      padding-bottom: 1px;
      transition: all 0.15s ease;
    }}
    a.wiki-link:hover {{
      color: var(--rose-deep);
      background-color: var(--rose-light);
      border-bottom-style: solid;
      border-radius: 4px;
      padding: 2px 4px;
    }}
    .wiki-link-unresolved {{
      color: #a89fa4;
      text-decoration: line-through;
    }}

    /* Callout Boxes */
    .callout {{
      border-radius: 12px;
      padding: 14px 18px;
      margin: 20px 0;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 14px;
      line-height: 1.75;
    }}
    .callout-abstract {{ background-color: #fdf5f6; border-left: 4px solid var(--rose-accent); color: #423237; }}
    .callout-info {{ background-color: #f3f8f5; border-left: 4px solid var(--green-soft); color: #2e3d33; }}
    .callout-warning {{ background-color: #faf5f0; border-left: 4px solid #b56b3e; color: #473325; }}
    .callout-important {{ background-color: #fbf0f2; border-left: 4px solid #8c4b57; color: #47262d; }}
    .callout-title {{
      font-weight: 700;
      margin-bottom: 6px;
      font-size: 14px;
    }}

    /* Tables */
    .table-container {{
      overflow-x: auto;
      margin: 20px 0;
      border: 1px solid var(--border-warm);
      border-radius: 12px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 13px;
      text-align: left;
    }}
    th {{
      background-color: var(--rose-light);
      color: var(--rose-deep);
      padding: 10px 14px;
      font-weight: 700;
      border-bottom: 1px solid var(--border-warm);
    }}
    td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-warm);
      color: #483f43;
    }}
    tr:last-child td {{
      border-bottom: none;
    }}
    tr:hover td {{
      background-color: #faf5f2;
    }}

    @media (max-width: 860px) {{
      .wiki-container {{ flex-direction: column; }}
      .wiki-sidebar {{ width: 100%; max-height: none; position: static; }}
      .wiki-main {{ padding: 24px 20px; }}
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <a href="{rel_home}" class="header-logo" title="回總傳送門">
      <div class="logo-badge">栞</div>
      <div class="logo-text">
        <h1>心理學論文 LLM Wiki</h1>
        <span>純靜態直接部署 • 零框架</span>
      </div>
    </a>
    <div class="header-actions">
      <a href="{rel_slides}" class="btn btn-rose"><span>📊</span> 簡報播放</a>
      <a href="{rel_root}" class="btn btn-white"><span>📑</span> 總索引</a>
      <a href="{rel_log}" class="btn btn-white"><span>📜</span> 日誌</a>
    </div>
  </header>

  <!-- Dual Layout Container -->
  <div class="wiki-container">

    <!-- Left Sidebar -->
    <aside class="wiki-sidebar">
      <input type="text" id="navSearch" class="nav-search" placeholder="搜尋構念、流派..." oninput="filterNav(this.value)">
      <div id="navGroupList">
        {"".join(sidebar_sections)}
      </div>
    </aside>

    <!-- Main Article -->
    <main class="wiki-main">
      <div class="breadcrumb">
        <a href="{rel_root}">Wiki</a> <span>/</span>
        <span>{cat_name}</span> <span>/</span>
        <span style="color: var(--rose-deep); font-weight: 700;">{note["display_name"]}</span>
      </div>

      {meta_card}

      <article class="content">
        {body_html}
      </article>
    </main>

  </div>

  <script>
    // Lightweight vanilla JS search filter (no framework)
    function filterNav(q) {{
      q = q.toLowerCase().trim();
      const items = document.querySelectorAll('.nav-item');
      items.forEach(el => {{
        const text = el.textContent.toLowerCase();
        el.style.display = (!q || text.includes(q)) ? 'block' : 'none';
      }});
    }}
  </script>
</body>
</html>
"""
    return html

# 2. Build all 33 static HTML files
count = 0
for rel_path, note in all_notes.items():
    html_rel = note["html_rel_path"]
    target_file = os.path.join(wiki_dir, html_rel)
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    
    html_content = build_html_page(note, html_rel)
    with open(target_file, "w", encoding="utf-8") as out_f:
        out_f.write(html_content)
    count += 1

print(f"Successfully generated {count} static zero-framework HTML pages!")
