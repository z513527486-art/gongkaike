#!/usr/bin/env python3
"""Build a single-file HTML lesson artifact from a JSON lesson descriptor.

This is a lightweight reference implementation for the interactive lesson skill.
It supports the essential fields needed by public-class lesson generation:
- title
- subtitle
- objectives
- overview
- scenes
- hotspots
- exercises
"""

import json
import os
import re
from html import escape
from pathlib import Path


def read_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_html(data: dict) -> str:
    title = escape(str(data.get('title', '公开课课件')))
    subtitle = escape(str(data.get('subtitle', '')))
    overview = escape(str(data.get('overview', '')))
    objectives = data.get('objectives', [])
    scenes = data.get('scenes', [])
    hotspots = data.get('hotspots', [])
    exercises = data.get('exercises', [])

    objective_html = ''.join(
        f'<li>{escape(str(item))}</li>' for item in objectives
    )

    scene_html = ''.join(
        f'''
        <div class="scene-card">
          <h3>{escape(str(item.get("title", "场景")))}</h3>
          <p>{escape(str(item.get("description", "")))}</p>
        </div>
        ''' for item in scenes
    )

    hotspot_html = ''.join(
        f'''
        <div class="hotspot-card">
          <h3>{escape(str(item.get("title", "热点")))}</h3>
          <p>{escape(str(item.get("text", "")))}</p>
        </div>
        ''' for item in hotspots
    )

    exercise_html = ''.join(
        f'''
        <div class="exercise-card">
          <h3>{escape(str(item.get("title", "练习")))}</h3>
          <p>{escape(str(item.get("prompt", "")))}</p>
        </div>
        ''' for item in exercises
    )

    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #f5efe6;
      --paper: #fffaf3;
      --ink: #1f2430;
      --muted: #5b6475;
      --accent: #b86b38;
      --accent2: #d5b98b;
      --line: #e6d7ba;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
      background: linear-gradient(180deg, #f7f1e9 0%, #fffaf3 100%);
      color: var(--ink);
    }}
    .page {{
      max-width: 1200px; margin: 0 auto; padding: 40px 24px 80px;
    }}
    .hero {{
      background: linear-gradient(135deg, #f0dfc9, #fffaf3);
      border: 1px solid var(--line);
      border-radius: 20px; padding: 40px 36px; box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    }}
    h1 {{ font-size: clamp(2rem, 4vw, 4rem); margin: 0 0 16px; }}
    h2 {{ margin-top: 36px; font-size: 2rem; }}
    .subtitle {{ color: var(--muted); font-size: 1.15rem; margin-bottom: 14px; }}
    .overview {{ line-height: 1.9; font-size: 1.05rem; }
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 18px; margin-top: 24px; }}
    .scene-card, .hotspot-card, .exercise-card {{
      background: var(--paper); border: 1px solid var(--line); border-radius: 16px; padding: 18px 20px;
      box-shadow: 0 8px 18px rgba(0,0,0,0.03);
    }}
    ul {{ padding-left: 20px; line-height: 2; }}
    .tag {{
      display: inline-block; background: rgba(184, 107, 56, 0.08);
      color: var(--accent); border: 1px solid rgba(184,107,56,0.2);
      border-radius: 999px; padding: 6px 12px; font-size: 0.85rem; margin-bottom: 16px;
    }}
  </style>
</head>
<body>
  <div class="page">
    <section class="hero">
      <div class="tag">语文公开课 · 沉浸式课件</div>
      <h1>{title}</h1>
      <div class="subtitle">{subtitle}</div>
      <div class="overview">{overview}</div>
    </section>

    <section>
      <h2>学习目标</h2>
      <ul>{objective_html}</ul>
    </section>

    <section>
      <h2>场景总览</h2>
      <div class="grid">{scene_html}</div>
    </section>

    <section>
      <h2>重点热点</h2>
      <div class="grid">{hotspot_html}</div>
    </section>

    <section>
      <h2>课题练习</h2>
      <div class="grid">{exercise_html}</div>
    </section>
  </div>
</body>
</html>
'''


def main():
    if len(os.sys.argv) < 3:
        print('Usage: build.py <input_json> --out <output_html>')
        raise SystemExit(1)

    input_path = os.sys.argv[1]
    output_path = None

    if '--out' in os.sys.argv:
        idx = os.sys.argv.index('--out')
        if idx + 1 < len(os.sys.argv):
            output_path = os.sys.argv[idx + 1]

    if output_path is None:
        print('Missing output path.')
        raise SystemExit(1)

    data = read_json(input_path)
    html = render_html(data)

    out_dir = Path(output_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Generated: {output_path}')


if __name__ == '__main__':
    main()
