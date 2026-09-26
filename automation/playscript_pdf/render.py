import re, html
K = r'C:\Users\sol00\Desktop\artflow\knowledge'
src = open(K + r'\희곡_감정_대본_v3.md', encoding='utf-8').read()
paras = [p for p in re.split(r'\n\s*\n', src.strip())]
BS = chr(92)

def inline(t):
    return html.escape(t).replace('\n', '<br>')

out = []
section = None
first_scene = True
for p in paras:
    p = p.strip('\n')
    if p.startswith('# '):
        out.append(f'<h1>{inline(p[2:])}</h1>'); continue
    if p.startswith('— 鑑定'):
        out.append(f'<p class="sub">{inline(p)}</p>'); continue
    if p.startswith('작:'):
        out.append(f'<p class="credit">{inline(p)}</p>'); continue
    if p.startswith('## '):
        h = p[3:]
        if h in ('등장인물', '때와 곳', '무대'):
            section = h
            out.append(f'<h3>{inline(h)}</h3>')
        else:
            section = 'body'
            out.append(f'<h2>{inline(h)}</h2>')
        continue
    if section in ('등장인물', '때와 곳', '무대'):
        m = re.match(r'^(\S[^—\n]*?) — (.*)$', p, re.S)
        if section != '무대' and m and '\n' not in p:
            out.append(f'<p class="cast"><span class="cn">{inline(m.group(1))}</span>{inline(m.group(2))}</p>')
        elif p.startswith('이 작품은'):
            out.append(f'<p class="note">{inline(p)}</p>')
        else:
            out.append(f'<p class="front">{inline(p)}</p>')
        continue
    if p == BS + '*':
        out.append('<p class="brk">*</p>'); continue
    if re.match(r'^— .*끝 —$', p):
        out.append(f'<p class="end">{inline(p)}</p>'); continue
    if '\n**' in p or p.startswith('**'):
        groups=[]
        for ln in p.split('\n'):
            if ln.startswith('**') or not groups: groups.append([ln])
            else: groups[-1].append(ln)
        for g in groups:
            t='\n'.join(g)
            m = re.match(r'^\*\*(.+?)\*\*\s?(.*)$', t, re.S)
            if m:
                out.append(f'<div class="dia"><span class="spk">{inline(m.group(1))}</span><span class="line">{inline(m.group(2))}</span></div>')
            else:
                out.append(f'<p class="sd">{inline(t)}</p>')
        continue
    if p.startswith('('):
        out.append(f'<p class="sd">{inline(p)}</p>'); continue
    out.append(f'<p class="sd cont">{inline(p)}</p>')

body = '\n'.join(out)
assert not [x for x in out if "**" in x or "```" in x]
CSS = """
@page { size: A4; margin: 25mm 22mm 25mm 25mm;
  @bottom-center { content: counter(page); font-family: 'Batang', serif; font-size: 9.5pt; } }
body { font-family: 'Batang', 'Noto Serif KR', serif; font-size: 11pt; line-height: 1.75; color: #111; word-break: keep-all; }
h1 { font-size: 30pt; text-align: center; margin: 70mm 0 4mm; font-weight: bold; letter-spacing: 0.1em; }
.sub { text-align: center; font-size: 13pt; margin: 0 0 30mm; }
.credit { text-align: center; font-size: 11.5pt; margin-bottom: 0; page-break-after: always; }
h3 { font-size: 12.5pt; font-weight: bold; margin: 9mm 0 3mm; }
h3:first-of-type { margin-top: 0; }
.cast { margin: 0 0 1.5mm; padding-left: 8em; text-indent: -8em; }
.cast .cn { display: inline-block; width: 8em; text-indent: 0; font-weight: bold; }
.front { margin: 0 0 2mm; }
.note { margin-top: 12mm; font-size: 9.5pt; color: #444; page-break-after: always; }
h2 { font-size: 15pt; font-weight: bold; text-align: center; margin: 0 0 10mm; page-break-before: always; }
h2:first-of-type { page-break-before: auto; }
.dia { margin: 0 0 3.2mm; padding-left: 4.6em; text-indent: -4.6em; page-break-inside: avoid; }
.spk { display: inline-block; min-width: 4em; margin-right: 0.6em; text-indent: 0; font-weight: bold; }
.sd { margin: 1mm 0 4mm 4.6em; font-size: 10pt; color: #333; page-break-inside: avoid; }
.brk { text-align: center; margin: 5mm 0; }
.end { text-align: center; margin: 12mm 0 0; }
"""
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>감정</title><style>{CSS}</style></head><body>{body}</body></html>'
open(r'C:\Users\sol00\AppData\Local\Temp\claude\c--Users-sol00-Desktop-artflow\8670bc67-b8fd-4a51-b578-d51b6f98fc25\scratchpad\v3.html', 'w', encoding='utf-8').write(doc)
print('html ok')
