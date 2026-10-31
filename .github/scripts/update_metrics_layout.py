from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = '''.metric-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px}\n.metric{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.17);border-radius:14px;padding:16px}\n.metric strong{font-size:1.55rem;display:block}\n.metric span{font-size:.82rem;opacity:.86}'''
new = '''.metric-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-top:28px}\n.metric{background:linear-gradient(180deg,rgba(255,255,255,.12),rgba(255,255,255,.08));border:1px solid rgba(255,255,255,.20);border-radius:15px;padding:18px 16px;min-height:132px;display:flex;flex-direction:column;justify-content:flex-start;box-shadow:0 8px 22px rgba(0,0,0,.08)}\n.metric strong{font-size:1.6rem;line-height:1.05;display:block;margin-bottom:10px;letter-spacing:-.02em}\n.metric span{font-size:.80rem;line-height:1.45;opacity:.90}'''
if old not in s:
    raise SystemExit('metric CSS block not found')
s = s.replace(old, new, 1)

old_media = '''@media(max-width:850px){\n  .hero{grid-template-columns:1fr;text-align:center} .photo{margin:auto}\n  .actions{justify-content:center} .metric-grid{grid-template-columns:repeat(2,1fr)}\n  .span-4,.span-6{grid-column:span 12}.academic-links{grid-template-columns:1fr}\n}\n@media(max-width:520px){.metric-grid{grid-template-columns:1fr}}'''
new_media = '''@media(max-width:1100px){.metric-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}\n@media(max-width:850px){\n  .hero{grid-template-columns:1fr;text-align:center} .photo{margin:auto}\n  .actions{justify-content:center} .metric-grid{grid-template-columns:repeat(2,minmax(0,1fr))}\n  .span-4,.span-6{grid-column:span 12}.academic-links{grid-template-columns:1fr}\n}\n@media(max-width:520px){.metric-grid{grid-template-columns:1fr}.metric{min-height:auto}}'''
if old_media not in s:
    raise SystemExit('metric media block not found')
s = s.replace(old_media, new_media, 1)

p.write_text(s, encoding='utf-8')
