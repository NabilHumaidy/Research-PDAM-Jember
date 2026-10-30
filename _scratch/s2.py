import re, html, sys, subprocess, os, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
SCRATCH = r"E:\BCC Manufair Case Research\_scratch"

def fetch(url, out):
    subprocess.run(["curl", "-sSL", "-m", "45", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                   capture_output=True, text=True)
    try:
        s = open(out, encoding='utf-8', errors='ignore').read()
    except OSError:
        return ''
    return s

def bing(query, count=25):
    q = urllib.parse.quote(query)
    fn = os.path.join(SCRATCH, "b_" + re.sub(r'[^A-Za-z0-9]+', '_', query)[:50] + ".html")
    url = f"https://www.bing.com/search?q={q}&count={count}&setlang=id&cc=ID"
    s = fetch(url, fn)
    out = []
    for b in re.findall(r'<li class="b_algo".*?</li>', s, re.S):
        t = re.search(r'<h2>(.*?)</h2>', b, re.S)
        u = re.search(r'<cite[^>]*>(.*?)</cite>', b, re.S)
        d = re.search(r'<p class="b_lineclamp[^"]*"[^>]*>(.*?)</p>', b, re.S)
        title = html.unescape(re.sub('<[^>]+>', '', t.group(1))).strip() if t else ''
        curl = html.unescape(re.sub('<[^>]+>', '', u.group(1))).strip() if u else ''
        desc = html.unescape(re.sub('<[^>]+>', '', d.group(1))).strip() if d else ''
        m = re.search(r'https?://[^\s]+', curl.replace(' › ', '/'))
        link = m.group(0) if m else curl
        if title:
            out.append((title, link, desc))
    return out, len(s)

def yahoo(query):
    q = urllib.parse.quote(query)
    fn = os.path.join(SCRATCH, "y_" + re.sub(r'[^A-Za-z0-9]+', '_', query)[:50] + ".html")
    url = f"https://search.yahoo.com/search?p={q}&n=20"
    s = fetch(url, fn)
    out = []
    for b in re.findall(r'<div class="algo-slice".*?(?=<div class="algo-slice"|</ol>)', s, re.S):
        t = re.search(r'<h3[^>]*>(.*?)</h3>', b, re.S)
        u = re.search(r'<a[^>]*href="([^"]+)"', b, re.S)
        d = re.search(r'<p class="lh-16[^"]*"[^>]*>(.*?)</p>', b, re.S) or re.search(r'<span class="lemma[^"]*"[^>]*>(.*?)</span>', b, re.S)
        title = html.unescape(re.sub('<[^>]+>', '', t.group(1))).strip() if t else ''
        link = u.group(1) if u else ''
        desc = html.unescape(re.sub('<[^>]+>', '', d.group(1))).strip() if d else ''
        if title:
            out.append((title, link, desc))
    if not out:
        for b in re.findall(r'<li>(.*?)</li>', s, re.S):
            t = re.search(r'<a[^>]*>(.*?)</a>', b, re.S)
            u = re.search(r'<a[^>]*href="([^"]+)"', b, re.S)
            if t and u and 'yahoo.com' not in u.group(1):
                out.append((html.unescape(re.sub('<[^>]+>', '', t.group(1))).strip(), u.group(1), ''))
    return out, len(s)

def mojeek(query):
    q = urllib.parse.quote(query)
    fn = os.path.join(SCRATCH, "m_" + re.sub(r'[^A-Za-z0-9]+', '_', query)[:50] + ".html")
    url = f"https://www.mojeek.com/search?q={q}"
    s = fetch(url, fn)
    out = []
    for b in re.findall(r'<li class="result-item">(.*?)</li>', s, re.S):
        t = re.search(r'<a class="ob"[^>]*>(.*?)</a>', b, re.S)
        u = re.search(r'<a class="ob"[^>]*href="([^"]+)"', b, re.S)
        d = re.search(r'<p class="s">(.*?)</p>', b, re.S)
        title = html.unescape(re.sub('<[^>]+>', '', t.group(1))).strip() if t else ''
        link = u.group(1) if u else ''
        desc = html.unescape(re.sub('<[^>]+>', '', d.group(1))).strip() if d else ''
        if title:
            out.append((title, link, desc))
    return out, len(s)

def ecosia(query):
    q = urllib.parse.quote(query)
    fn = os.path.join(SCRATCH, "e_" + re.sub(r'[^A-Za-z0-9]+', '_', query)[:50] + ".html")
    url = f"https://www.ecosia.org/search?q={q}"
    s = fetch(url, fn)
    out = []
    for b in re.findall(r'<div class="result"[^>]*>(.*?)(?=<div class="result"|</main>)', s, re.S):
        t = re.search(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
        d = re.search(r'<span class="snippet"[^>]*>(.*?)</span>', b, re.S)
        if t:
            link = t.group(1)
            title = html.unescape(re.sub('<[^>]+>', '', t.group(2))).strip()
            desc = html.unescape(re.sub('<[^>]+>', '', d.group(1))).strip() if d else ''
            out.append((title, link, desc))
    return out, len(s)

if __name__ == '__main__':
    eng = sys.argv[1]
    q = sys.argv[2]
    res, ln = {'bing': bing, 'yahoo': yahoo, 'mojeek': mojeek, 'ecosia': ecosia}[eng](q)
    print(f"[{eng}] len={ln} n={len(res)}")
    for t, u, d in res:
        print('##', t)
        print('  ', u)
        if d:
            print('   >', d[:280])
