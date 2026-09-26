import subprocess, fitz, os, pathlib
S = os.path.dirname(os.path.abspath(__file__))
OUT = r'C:\Users\sol00\Desktop\artflow\knowledge\희곡_감정_대본_v3.pdf'
subprocess.run([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', '--headless', '--disable-gpu', '--user-data-dir=' + os.path.join(S, 'edgeprof'),
                '--no-pdf-header-footer', '--print-to-pdf=' + OUT,
                pathlib.Path(S, 'v3.html').as_uri()], check=True, capture_output=True)
d = fitz.open(OUT)
print('pages', len(d))
for i in (1, len(d)-1):
    d[i].get_pixmap(dpi=80).save(os.path.join(S, 'r%d.png' % i))
print(d[0].get_fonts())
