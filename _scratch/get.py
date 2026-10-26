import re, html, sys, subprocess, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
SCRATCH = r"E:\BCC Manufair Case Research\_scratch"

def fetch(url, out):
    subprocess.run(["curl", "-sSL", "-m", "60", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                   capture_output=True, text=True)
    try:
        s = open(out, encoding='utf-8', errors='ignore').read()
    except OSError:
        return ''
    return s

def article_text(s):
    # Jannah theme: entry content
    m = re.search(r'<div class="entry-content(?:-inner)?[^"]*"[^>]*>(.*?)</div>\s*<!-- .entry-content', s, re.S)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', s, re.S)
    body = m.group(1) if m else s
    body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    body = re.sub(r'<(p|div|br|h[1-6]|li)[^>]*>', '\n', body)
    body = re.sub(r'<[^>]+>', '', body)
    body = html.unescape(body)
    body = re.sub(r'\n\s*\n+', '\n', body)
    return body.strip()

if __name__ == '__main__':
    url = sys.argv[1]
    fn = os.path.join(SCRATCH, 'art_' + re.sub(r'[^A-Za-z0-9]+', '_', url)[:60] + '.html')
    s = fetch(url, fn)
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    print('URL:', url)
    print('TITLE:', html.unescape(t.group(1)).strip() if t else '?')
    print('LEN:', len(s))
    print('----')
    print(article_text(s))
