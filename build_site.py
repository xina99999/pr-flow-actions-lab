"""A minimal lab application to deploy via GitHub Pages, not the Streamlit server."""
import html
import json
import os
from pathlib import Path

revision = os.environ.get('GITHUB_SHA', 'local-demo')
target = Path('site')
target.mkdir(exist_ok=True)
(target / 'version.json').write_text(json.dumps({'commit_sha': revision, 'environment': 'github-pages', 'status': 'ok'}))
(target / 'index.html').write_text('''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ứng dụng mẫu PR Flow</title>
<style>body{background:#f5f7fc;color:#183050;font:18px system-ui;margin:10vh auto;max-width:760px;padding:30px}main{background:white;border:1px solid #dfe6f2;border-radius:18px;padding:40px}code{overflow-wrap:anywhere;color:#4059d7}a{color:#4059d7}</style>
<main><p>PR FLOW / LAB DEPLOYMENT</p><h1>Thay đổi đã được phát hành</h1><p>Phiên bản thực nghiệm: ghi nhận hành trình từ Pull Request đến triển khai.</p><p>Đây là ứng dụng thử nghiệm để tạo bằng chứng deployment cho đề tài. Môi trường này không đại diện cho production của doanh nghiệp.</p><p>Commit: <code>'''+html.escape(revision)+'''</code></p><a href="version.json">Xem phiên bản triển khai</a></main></html>''', encoding='utf-8')
print('Built lab site with commit', revision)
