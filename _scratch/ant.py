import re, html, sys, subprocess, os, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
SCRATCH = r"E:\BCC Manufair Case Research\_scratch"

def fetch(url, out):
    for attempt in range(6):
        r = subprocess.run(["curl", "-sSL", "-m", "60", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        try:
            sz = os.path.getsize(out)
        except OSError:
            sz = 0
        if code == "200" and sz > 5000:
            break
        subprocess.run(["sleep", "2"], capture_output=True)
    try:
        s = open(out, encoding='utf-8', errors='ignore').read()
    except OSError:
        return ''
    return s

def ant_search(query, pages=2):
    out = []
    for p in range(1, pages + 1):
        q = urllib.parse.quote(query)
        fn = os.path.join(SCRATCH, f"as_{re.sub(r'[^A-Za-z0-9]+','_',query)[:40]}_{p}.html")
        url = f"https://www.antaranews.com/search?q={q}&page={p}"
        s = fetch(url, fn)
        # result items: article links + date + title
        items = re.findall(r'<a[^>]*?href="(https://www\.antaranews\.com/(?:berita|video)/[^"?]+)"[^>]*?(?:title="([^"]*)")?[^>]*>(.*?)</a>', s, re.S)
        seen = set()
        for u, tt, t in items:
            if u in seen or '/search' in u:
                continue
            seen.add(u)
            tx = html.unescape(re.sub('<[^>]+>', '', t)).strip()
            tx = re.sub(r'\s+', ' ', tx)
            if len(tx) <= 15 and tt:
                tx = html.unescape(tt).strip()
            if len(tx) > 15:
                out.append((u, tx))
        # dates
        dates = re.findall(r'<span class="text-[a-z0-9\- ]*date[^"]*"[^>]*>(.*?)</span>', s, re.S)
    return out

def article(url):
    fn = os.path.join(SCRATCH, 'art2_' + re.sub(r'[^A-Za-z0-9]+', '_', url)[:70] + '.html')
    s = fetch(url, fn)
    m = re.search(r'<div class="entry-content[^"]*"[^>]*>(.*?)</div>\s*<!--', s, re.S)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', s, re.S)
    body = m.group(1) if m else s
    body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
    body = re.sub(r'<style.*?</style>', '', body, flags=re.S)
    body = re.sub(r'<(p|div|br|h[1-6]|li|strong|em)[^>]*>', '\n', body)
    body = re.sub(r'<[^>]+>', '', body)
    body = html.unescape(body)
    body = re.sub(r'[ \t]+', ' ', body)
    body = re.sub(r'\n\s*\n+', '\n', body)
    t = re.search(r'<title>(.*?)</title>', s, re.S)
    title = html.unescape(t.group(1)).strip() if t else '?'
    d = re.search(r'(\d{1,2}\s+\w+\s+20\d\d)', body)
    return title, (d.group(1) if d else '?'), body.strip()

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 's':
        for u, t in ant_search(sys.argv[2]):
            print('##', t[:110])
            print('  ', u)
    elif mode == 'a':
        title, date, body = article(sys.argv[2])
        print('TITLE:', title)
        print('DATE:', date)
        print('----')
        print(body[:6000])
