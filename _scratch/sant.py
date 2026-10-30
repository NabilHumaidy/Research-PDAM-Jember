import re, html, sys, subprocess, os, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
SCRATCH = r"E:\BCC Manufair Case Research\_scratch"

def fetch(url, out):
    for attempt in range(8):
        r = subprocess.run(["curl", "-sSL", "-m", "60", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        try:
            sz = os.path.getsize(out)
        except OSError:
            sz = 0
        if code == "200" and sz > 5000:
            break
        subprocess.run(["sleep", "3"], capture_output=True)
    try:
        return open(out, encoding='utf-8', errors='ignore').read()
    except OSError:
        return ''

PAT = r'<h2 class="h5"><a[^>]*?href="(https://www\.antaranews\.com/(?:berita|video)/[^"?]+)"[^>]*>(.*?)</a></h2>'
PAT_T = r'<a[^>]*?href="(https://www\.antaranews\.com/(?:berita|video)/[^"?]+)"[^>]*?title="([^"]+)"[^>]*>'
PAT_D = r'<span class="text-dark text-capitalize">([^<]+)</span>'

def search(query, pages=3):
    q = urllib.parse.quote(query)
    out = []
    for p in range(1, pages + 1):
        fn = os.path.join(SCRATCH, f"as_{re.sub(r'[^A-Za-z0-9]+','_',query)[:40]}_{p}.html")
        url = f"https://www.antaranews.com/search?q={q}&page={p}"
        s = fetch(url, fn)
        if 'Kami memiliki' in s:
            m = re.search(r'Kami memiliki (\d+) berita', s)
            print(f"--- page {p}: total {m.group(1) if m else '?'}", file=sys.stderr)
        dates = re.findall(PAT_D, s)
        items = [(u, t) for u, t in re.findall(PAT_T, s, re.S)]
        if not items:
            items = [(u, re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', t)).strip())
                     for u, t in re.findall(PAT, s, re.S)]
        seen = {x[0] for x in out}
        k = 0
        for u, tx in items:
            if u in seen:
                continue
            seen.add(u)
            d = dates[k].strip() if k < len(dates) else ''
            k += 1
            if len(tx) > 10:
                out.append((u, re.sub(r'\s+', ' ', html.unescape(tx)).strip(), d))
    return out


def article(url):
    fn = os.path.join(SCRATCH, 'artx_' + re.sub(r'[^A-Za-z0-9]+', '_', url)[:80] + '.html')
    s = fetch(url, fn)
    m = re.search(r'<div class="wrap__article-detail-content post-content">(.*?)</div>\s*<!--', s, re.S)
    if not m:
        m = re.search(r'<div class="wrap__article-detail-content post-content">(.*?)</div>', s, re.S)
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
    if len(sys.argv) > 2 and sys.argv[1] == 'a':
        title, date, body = article(sys.argv[2])
        print('TITLE:', title)
        print('DATE:', date)
        print('----')
        print(body[:7000])
    else:
        for u, t, d in search(sys.argv[1]):
            print('##', f'[{d}]' if d else '', t[:120])
            print('  ', u)
