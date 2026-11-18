import os
import re
import html

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

# Canonical paper shortcuts
paper_shortcuts = {
    "watson-rayner-1920": "sources/watson-rayner-1920-conditioned-fear.html",
    "watson-rayner-1920-conditioned-fear": "sources/watson-rayner-1920-conditioned-fear.html",
    "freud-1910": "sources/freud-1910-psychoanalysis-origin.html",
    "freud-1910-psychoanalysis-origin": "sources/freud-1910-psychoanalysis-origin.html",
    "maslow-1943": "sources/maslow-1943-human-motivation.html",
    "maslow-1943-human-motivation": "sources/maslow-1943-human-motivation.html",
    "miller-1956": "sources/miller-1956-magical-number-seven.html",
    "miller-1956-magical-number-seven": "sources/miller-1956-magical-number-seven.html",
    "ledoux-2000": "sources/ledoux-2000-emotion-circuits.html",
    "ledoux-2000-emotion-circuits": "sources/ledoux-2000-emotion-circuits.html",
}

for k, v in paper_shortcuts.items():
    slug_to_rel_html[k] = v
    slug_to_rel_html[k.lower()] = v

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
            slug_to_rel_html[title] = html_rel_path
            slug_to_rel_html[title.lower()] = html_rel_path
            if aliases:
                for a in aliases.split(","):
                    a_clean = a.strip()
                    if a_clean:
                        slug_to_rel_html[a_clean] = html_rel_path
                        slug_to_rel_html[a_clean.lower()] = html_rel_path

# Relative path calculator
def get_relative_link(from_path, to_path):
    if to_path.startswith("http://") or to_path.startswith("https://"):
        return to_path
    from_dir = os.path.dirname(from_path)
    rel = os.path.relpath(to_path, from_dir if from_dir else ".").replace("\\", "/")
    return rel

# Universal Link Resolver
def resolve_target(target):
    target_clean = target.strip()
    
    # Check if pointing to raw file
    if target_clean.startswith("raw/") or "/raw/" in target_clean:
        filename = target_clean.split("/")[-1].replace(".md", "").replace(".pdf", "")
        for k, v in paper_shortcuts.items():
            if filename in k or k in filename:
                return v
        return f"../raw/{target_clean.split('/')[-1]}"
    
    # Check AGENTS.md
    if "AGENTS" in target_clean.upper():
        return "https://github.com/sasa0905/10/blob/main/AGENTS.md"

    # Remove .md if present
    target_slug = target_clean.split("/")[-1].replace(".md", "").strip()
    
    # Direct match
    if target_slug in slug_to_rel_html:
        return slug_to_rel_html[target_slug]
    if target_slug.lower() in slug_to_rel_html:
        return slug_to_rel_html[target_slug.lower()]
    
    # Paper shortcuts match
    for k, v in paper_shortcuts.items():
        if target_slug.startswith(k) or k.startswith(target_slug):
            return v
            
    # Substring in parenthesis, e.g. "行為學派 (Behaviorism)" -> check "行為學派" and "Behaviorism"
    sub_name = re.sub(r'\(.*?\)', '', target_slug).strip()
    if sub_name and sub_name in slug_to_rel_html:
        return slug_to_rel_html[sub_name]
    if sub_name and sub_name.lower() in slug_to_rel_html:
        return slug_to_rel_html[sub_name.lower()]
        
    m = re.search(r'\((.*?)\)', target_slug)
    if m:
        inside = m.group(1).strip()
        if inside in slug_to_rel_html:
            return slug_to_rel_html[inside]
        if inside.lower() in slug_to_rel_html:
            return slug_to_rel_html[inside.lower()]
            
    # Check if target is an author citation like "Watson & Rayner (1920)" or "Freud (1910)"
    if "Watson" in target_clean or "Albert" in target_clean:
        return paper_shortcuts["watson-rayner-1920"]
    if "Freud" in target_clean or "Anna O" in target_clean:
        return paper_shortcuts["freud-1910"]
    if "Maslow" in target_clean or "需求階層" in target_clean:
        return paper_shortcuts["maslow-1943"]
    if "Miller" in target_clean or "7±2" in target_clean:
        return paper_shortcuts["miller-1956"]
    if "LeDoux" in target_clean or "杏仁核" in target_clean:
        return paper_shortcuts["ledoux-2000"]

    return None

# Simple yet complete Markdown to HTML converter with code & diagram support
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
        
        target_html = resolve_target(target)
        if target_html:
            rel_url = get_relative_link(current_html_path, target_html)
            return f'<a href="{rel_url}" class="wiki-link" title="{label}">{label}</a>'
        else:
            # Elegant unresolved badge WITHOUT strikethrough!
            return f'<span class="wiki-link-unresolved" title="參照項目">{label}</span>'

    text = re.sub(r'\[\[(.*?)\]\]', replace_wikilink, text)

    # Pre-process standard markdown links [label](path.md)
    def replace_md_link(match):
        label = match.group(1)
        url = match.group(2)
        if url.endswith(".md") or url.endswith(".pdf"):
            target_html = resolve_target(url)
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
    in_code_block = False
    code_lang = ""
    code_lines = []

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

        # Handle Code Fences (```mermaid, ```text, ```)
        if stripped.startswith("```"):
            if in_code_block:
                # End of code block
                in_code_block = False
                code_content = "\n".join(code_lines)
                if code_lang == "mermaid":
                    clean_code = code_content.strip()
                    # Automatically fix invalid thick arrow syntax ==>|text| into == "text" ==>
                    clean_code = re.sub(r'==>\|"?(.*?)"?\|', r'== "\1" ==>', clean_code)
                    out.append(f'<div class="mermaid-diagram"><div class="mermaid-caption"><span>📊</span> 核心機制圖解（完整向量呈現 • 高清晰字體 • 可左右滑動查看全貌）</div><pre class="mermaid">\n{clean_code}\n</pre></div>')
                else:
                    escaped_code = html.escape(code_content)
                    out.append(f'<div class="code-container"><pre class="code-block"><code>{escaped_code}</code></pre></div>')
                code_lines = []
                code_lang = ""
                continue
            else:
                # Start of code block
                flush_callout()
                if in_list:
                    out.append("</ul>")
                    in_list = False
                if in_table:
                    out.append("</tbody></table></div>")
                    in_table = False
                in_code_block = True
                code_lang = stripped[3:].strip().lower()
                code_lines = []
                continue

        if in_code_block:
            code_lines.append(line)
            continue

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

    if in_code_block:
        code_content = "\n".join(code_lines)
        if code_lang == "mermaid":
            out.append(f'<div class="mermaid-diagram"><pre class="mermaid">\n{code_content}\n</pre></div>')
        else:
            escaped_code = html.escape(code_content)
            out.append(f'<div class="code-container"><pre class="code-block"><code>{escaped_code}</code></pre></div>')

    flush_callout()
    if in_list:
        out.append("</ul>")
    if in_table:
        out.append("</tbody></table></div>")

    return "\n".join(out)

# HTML Generator
def build_html_page(note, current_html_path):
    rel_root = get_relative_link(current_html_path, "index.html")
    rel_log = get_relative_link(current_html_path, "log.html")
    rel_slides = get_relative_link(current_html_path, "../slides/psychology_schools_presentation.html")
    rel_portal = get_relative_link(current_html_path, "../index.html")

    # Render Left Navigation Tree
    sidebar_sections = []
    
    grouped = {}
    for cat_key in cat_info.keys():
        grouped[cat_key] = []
    for p, n in all_notes.items():
        if n["category"] in grouped:
            grouped[n["category"]].append(n)

    for cat_key, items in grouped.items():
        cat = cat_info[cat_key]
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
    apa_card = ""
    if fm:
        badges = []
        if fm.get("aliases"):
            badges.append(f'<span class="badge badge-rose font-bold">{fm["aliases"]}</span>')
        
        # Clean Authors Display
        if fm.get("authors"):
            raw_authors = fm["authors"].replace("[", "").replace("]", "").replace('"', '').replace("'", "")
            authors_list = [a.strip() for a in raw_authors.split(",") if a.strip()]
            authors_str = ", ".join(authors_list)
            badges.append(f'<span class="badge badge-warm font-bold">✍️ 作者：{authors_str}</span>')

        if fm.get("year"):
            badges.append(f'<span class="badge badge-gray">📅 年份：{fm["year"]}</span>')
        if fm.get("journal"):
            badges.append(f'<span class="badge badge-gray">📰 期刊：{fm["journal"]}</span>')
        if fm.get("sample_size"):
            badges.append(f'<span class="badge badge-warm">🔬 樣本：{fm["sample_size"]}</span>')
        if fm.get("effect_size"):
            badges.append(f'<span class="badge badge-gray">📊 效應值：{fm["effect_size"]}</span>')
        if fm.get("replication_status"):
            rep_status = fm["replication_status"]
            if rep_status == "supported":
                badges.append('<span class="badge badge-green font-bold">✓ 複製支持 (supported)</span>')
            elif rep_status == "failed":
                badges.append('<span class="badge badge-rose font-bold">✖ 複製爭議/失敗 (failed)</span>')
            else:
                badges.append(f'<span class="badge badge-warm">⚠️ 狀態：{rep_status}</span>')
        if fm.get("doi"):
            badges.append(f'<a href="https://doi.org/{fm["doi"]}" target="_blank" class="badge badge-rose">🔗 DOI: {fm["doi"]} ↗</a>')

        if badges:
            meta_card = f'<div class="meta-card">{"".join(badges)}</div>'

        # Prominent APA Citation Card
        if fm.get("apa_citation"):
            apa_card = f'''
            <div class="apa-card">
              <div class="apa-header">
                <span class="apa-badge">APA 7th 官方文獻出處</span>
                <span class="apa-tip">奠基論文完整引用字串</span>
              </div>
              <div class="apa-text">{fm["apa_citation"]}</div>
            </div>
            '''

    # Render Body HTML
    body_html = convert_markdown_to_html(note["raw_text"], current_html_path)

    # Category display name
    cat_name = cat_info.get(note["category"], {}).get("title", note["category"])
    
    html_doc = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{note["title"]} — 心理學 LLM Wiki</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Shippori+Mincho:wght@500;700;800&family=Zen+Maru+Gothic:wght@400;500;700&display=swap" rel="stylesheet">
  <!-- Mermaid.js for beautiful interactive diagram rendering -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      if (window.mermaid) {{
        mermaid.initialize({{
          startOnLoad: true,
          theme: 'neutral',
          securityLevel: 'loose',
          flowchart: {{
            useMaxWidth: false,
            htmlLabels: true,
            curve: 'basis',
            padding: 16
          }},
          themeVariables: {{
            primaryColor: '#faf2f4',
            primaryBorderColor: '#c27685',
            primaryTextColor: '#2e292d',
            lineColor: '#8c4b57',
            secondaryColor: '#f7ebeb',
            tertiaryColor: '#ffffff',
            fontFamily: "'Zen Maru Gothic', 'Noto Serif TC', sans-serif",
            fontSize: '15px'
          }}
        }});
      }}
    }});
  </script>
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
      background-color: var(--rose-deep);
      color: #ffffff;
      border-color: var(--rose-deep);
    }}
    .btn-rose:hover {{
      background-color: var(--rose-accent);
    }}
    .btn-white {{
      background-color: #ffffff;
      color: var(--text-main);
    }}
    .btn-white:hover {{
      background-color: #faf5f2;
      border-color: var(--rose-accent);
    }}

    /* Layout Dual Column */
    .wiki-container {{
      display: flex;
      flex: 1;
      max-width: 1440px;
      width: 100%;
      margin: 0 auto;
    }}

    /* Left Sidebar */
    .wiki-sidebar {{
      width: 290px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-warm);
      padding: 18px 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      height: calc(100vh - 61px);
      position: sticky;
      top: 61px;
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
      font-size: 13px;
      text-decoration: none;
      color: var(--text-main);
      display: block;
      transition: all 0.15s ease;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-family: 'Zen Maru Gothic', sans-serif;
    }}
    .nav-item:hover {{
      background-color: #ede2dd;
      color: var(--rose-deep);
    }}
    .nav-item-active {{
      background-color: #ffffff !important;
      color: var(--rose-deep) !important;
      font-weight: 700;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      border-left: 3px solid var(--rose-accent);
    }}

    /* Main Content Area */
    .wiki-main {{
      flex: 1;
      padding: 36px 48px;
      max-width: 1060px;
      background-color: var(--bg-cream);
    }}
    .breadcrumb {{
      font-size: 12px;
      font-family: 'Zen Maru Gothic', sans-serif;
      color: var(--text-sub);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .breadcrumb a {{
      color: var(--text-sub);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--rose-accent);
    }}
    
    /* Meta Card */
    .meta-card {{
      background-color: #faf5f2;
      border: 1px solid var(--border-warm);
      border-radius: 12px;
      padding: 10px 14px;
      margin-bottom: 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 12px;
    }}
    .badge {{
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 12px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .badge-rose {{
      background-color: var(--rose-light);
      color: var(--rose-deep);
      border: 1px solid #ebd4d8;
    }}
    .badge-gray {{
      background-color: #ffffff;
      color: var(--text-sub);
      border: 1px solid var(--border-warm);
    }}
    .badge-warm {{
      background-color: #f7edea;
      color: #634335;
      border: 1px solid #ecd5cd;
    }}
    .badge-green {{
      background-color: #eaf4ed;
      color: #275632;
      border: 1px solid #c7e2ce;
    }}

    /* APA Citation Card */
    .apa-card {{
      background-color: #ffffff;
      border: 1px solid #ecd5cd;
      border-left: 4px solid var(--rose-accent);
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 24px;
      box-shadow: 0 1px 4px rgba(140, 75, 87, 0.04);
    }}
    .apa-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}
    .apa-badge {{
      font-size: 11px;
      font-weight: 700;
      color: var(--rose-deep);
      background-color: var(--rose-light);
      padding: 2px 8px;
      border-radius: 4px;
      font-family: 'Zen Maru Gothic', sans-serif;
    }}
    .apa-tip {{
      font-size: 11px;
      color: #a89fa4;
      font-family: 'Zen Maru Gothic', sans-serif;
    }}
    .apa-text {{
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 13.5px;
      color: #382e32;
      line-height: 1.6;
    }}

    /* Typography in Articles */
    .content h1 {{
      font-size: 28px;
      font-weight: 800;
      color: #262123;
      margin-bottom: 18px;
      letter-spacing: 0.03em;
    }}
    .content h2 {{
      font-size: 20px;
      font-weight: 700;
      color: #2e292d;
      margin-top: 30px;
      margin-bottom: 12px;
      border-bottom: 1px solid var(--border-warm);
      padding-bottom: 6px;
    }}
    .content h3 {{
      font-size: 16px;
      font-weight: 700;
      color: #423b3f;
      margin-top: 20px;
      margin-bottom: 8px;
    }}
    .content p {{
      margin-bottom: 14px;
      font-size: 15px;
      color: #383134;
      line-height: 1.8;
    }}
    .content ul {{
      margin-bottom: 16px;
      padding-left: 20px;
    }}
    .content li {{
      margin-bottom: 6px;
      font-size: 14.5px;
      color: #383134;
      line-height: 1.7;
    }}
    .content hr {{
      border: none;
      border-top: 1px dashed var(--border-warm);
      margin: 28px 0;
    }}
    .content code {{
      font-family: ui-monospace, Consolas, monospace;
      background-color: #f2e9e6;
      color: var(--rose-deep);
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 13px;
    }}

    /* Diagrams & Code Blocks */
    .mermaid-diagram {{
      background: #ffffff;
      border: 1px solid var(--border-warm);
      border-radius: 14px;
      padding: 22px 20px 20px 20px;
      margin: 26px 0;
      overflow-x: auto;
      overflow-y: hidden;
      text-align: center;
      box-shadow: 0 2px 10px rgba(140, 75, 87, 0.04);
      -webkit-overflow-scrolling: touch;
    }}
    .mermaid-caption {{
      font-size: 12.5px;
      color: var(--rose-deep);
      font-weight: 700;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      font-family: 'Zen Maru Gothic', sans-serif;
      letter-spacing: 0.04em;
    }}
    .mermaid-diagram svg {{
      max-width: none !important;
      width: auto !important;
      height: auto;
      display: inline-block;
      margin: 0 auto;
    }}
    .mermaid-diagram pre.mermaid {{
      background: transparent;
      border: none;
      margin: 0;
      padding: 0;
      font-family: 'Zen Maru Gothic', 'Noto Serif TC', sans-serif;
      font-size: 15px;
      line-height: 1.6;
      display: inline-block;
      text-align: left;
    }}
    .mermaid-diagram::-webkit-scrollbar {{
      height: 8px;
    }}
    .mermaid-diagram::-webkit-scrollbar-thumb {{
      background-color: #edd5da;
      border-radius: 4px;
    }}
    .mermaid-diagram::-webkit-scrollbar-track {{
      background-color: #faf7f5;
    }}
    .code-container {{
      margin: 20px 0;
    }}
    .code-block {{
      background-color: #f7f1ee;
      color: #382e32;
      border: 1px solid var(--border-warm);
      border-radius: 10px;
      padding: 14px 18px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      line-height: 1.6;
      overflow-x: auto;
      white-space: pre;
    }}
    .code-block code {{
      background: transparent;
      color: inherit;
      padding: 0;
      font-family: inherit;
    }}

    /* Wikilinks */
    a.wiki-link {{
      color: var(--rose-deep);
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
    /* UNRESOLVED ITEMS: Clean, soft tag with NO line-through or dead gray! */
    .wiki-link-unresolved {{
      color: #5d5357;
      background-color: #f6efec;
      border: 1px solid #ebdcd5;
      border-radius: 5px;
      padding: 1px 7px;
      font-size: 13px;
      font-family: 'Zen Maru Gothic', sans-serif;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      text-decoration: none;
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
      border-radius: 10px;
      border: 1px solid var(--border-warm);
      background-color: #ffffff;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-size: 13.5px;
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
      .wiki-sidebar {{ width: 100%; max-height: none; position: static; height: auto; }}
      .wiki-main {{ padding: 24px 20px; }}
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header class="top-header">
    <a href="{rel_portal}" class="header-logo" title="回總傳送門">
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

      {apa_card}

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
    return html_doc

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

print(f"Successfully generated {count} static zero-framework HTML pages with Mermaid diagrams & fixed citations!")
