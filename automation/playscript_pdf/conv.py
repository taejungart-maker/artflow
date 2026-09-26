import re, sys
SRC = r'C:\Users\sol00\Desktop\artflow\knowledge\희곡_감정_대본_합본_v2.md'
DST = r'C:\Users\sol00\Desktop\artflow\knowledge\희곡_감정_대본_v3.md'
L = open(SRC, encoding='utf-8').read().split('\n')

FRONT = """# 《감정》

— 鑑定, 혹은 感情

작: 태정 · 공동 집필: artflow (AI)

## 등장인물

서인화 — 60대 여성. 화가. 달과 새를 그린다.

윤소해 — 20~30대 여성. 현재의 학예사.

그림 속 여인 — 〈푸른 여인〉 속 존재.

한백규 — 60대 남성. 화랑 '백규당' 주인. 인화의 40년 지기.

정도윤 — 40~50대 남성. 국립근대미술관 학예실장. 인화의 오랜 숭배자.

최무영 — 30~40대 남성. 무명화가·위조범.

배우는 다섯 명이다. 윤소해와 그림 속 여인은 한 배우가 맡는다. 직원·기자·목소리들은 배우들이 겸한다. 단, 6장에서는 최무영 역 배우가 무대 위에 있으므로 기자는 문 밖 소리로만 들린다.

## 때와 곳

때 — 1991년 봄~여름. 그리고 2021년.

곳 — 서울. 성북동 화실과 마당 · 국립근대미술관. 그리고 2021년, 미술관 수장고.

## 무대

텅 빈 무대에 크고 작은 빈 액자들이 떠 있듯 걸려 있다.
이 극에서 그림은 단 한 점도 보이지 않는다. 모든 그림은 빈 액자이며,
그림은 오직 배우의 말과 관객의 상상 속에서만 존재한다.

이 작품은 실제 사건들에서 영감을 받은 허구이며, 등장하는 인물과 단체는 모두 창작된 것입니다.
"""

# body starts at prologue heading
start = next(i for i, l in enumerate(L) if l.startswith('## 프롤로그'))
body = L[start:]
out = []
inb = False
cur = []
END_RE = re.compile(r'^\**— .*끝 —\**$')

def emit_block(lines):
    # strip leading/trailing blanks
    while lines and not lines[0].strip(): lines.pop(0)
    while lines and not lines[-1].strip(): lines.pop()
    tail = None
    if lines and END_RE.match(lines[-1].strip()):
        tail = lines.pop().strip()
        while lines and not lines[-1].strip(): lines.pop()
    t = '\n'.join(lines)
    res = []
    if t.strip():
        if t.startswith('(') and t.endswith(')'):
            paras = [t]
        else:
            paras = []
            for p in re.split(r'\n\s*\n', t):
                p = p.strip('\n')
                paras.append('(' + p + ')')
        res = paras
    for p in res:
        out.append('')
        out.append(p)
        out.append('')
    if tail:
        out.append('')
        out.append(tail.strip('*'))
        out.append('')

def nb(i,d):
    j=i+d
    while 0<=j<len(body) and not body[j].strip(): j+=d
    return body[j].strip() if 0<=j<len(body) else ''
for idx,l in enumerate(body):
    if l.startswith('```'):
        if inb:
            emit_block(cur); cur = []
        inb = not inb
        continue
    if inb:
        cur.append(l); continue
    s = l.strip()
    if s == '---':
        n,p=nb(idx,1),nb(idx,-1)
        if not inb and n!='---' and p!='---' and not n.startswith('## ') and not n.startswith('*— 《') and not END_RE.match(p):
            out.append(''); out.append('\*'); out.append('')
        else:
            out.append('')
        continue
    if s.startswith('*— 《감정》 공연 대본 합본'):
        continue  # internal version tag
    if END_RE.match(s):
        out.append(s.strip('*')); continue
    out.append(l)

# in-scene single '---' separators: mark them. Detect: v2 '---' single (not paired) inside a scene
# Re-run simple approach: replace single '---' with '＊' marker
res = []
body_txt = '\n'.join(body)
# find single separators positions in original body
text = '\n'.join(out)
text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
open(DST, 'w', encoding='utf-8').write(FRONT + '\n' + text)
print('ok')
