from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

links = {
    '23811': 'https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&c=CNEG_PT_094_0748_23811',
    '23814': 'https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&c=CNEG_PT_084_0683_23814',
    '23815': 'https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&c=CNEG_PT_090_0727_23815',
    '23816': 'https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&c=CNEG_PT_092_0738_23816',
    '23817': 'https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&c=CNEG_PT_090_0725_23817',
}

for article_id, url in links.items():
    marker = f'Article {article_id} • ISSN 1984-9354 • '
    pos = s.find(marker)
    if pos < 0:
        raise SystemExit(f'Article marker not found: {article_id}')
    a_start = s.find('<a href="', pos)
    a_end = s.find('</a>', a_start) + 4
    if a_start < 0 or a_end < 4:
        raise SystemExit(f'Link not found for article: {article_id}')
    escaped = url.replace('&', '&amp;')
    new = f'<a href="{escaped}" target="_blank" rel="noopener">Individual proceedings record</a>'
    s = s[:a_start] + new + s[a_end:]

# Selected Research card for article 23815.
old = '<a href="https://nuieventos.com.br/cneg/anais/" target="_blank" rel="noopener">Official proceedings →</a>'
new = '<a href="https://nuieventos.com.br/cneg/anais/artigo.php?e=CNEG2026&amp;c=CNEG_PT_090_0727_23815" target="_blank" rel="noopener">Individual proceedings record →</a>'
if old in s:
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
