import re, html, sys, urllib.parse, subprocess, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
SCRATCH = r"E:\BCC Manufair Case Research\_scratch"

def bing(query, count=20):
    q = urllib.parse.quote(query)
    fn = os.path.join(SCRATCH, "q_" + re.sub(r'[^A-Za-z0-9]+', '_', query)[:40] + ".html")
    url = f"https://www.bing.com/search?q={q}&count={count}"
    subprocess.run(["curl", "-sS", "-m", "40", "-A", UA, "-o", fn, "-w", "%{http_code}", url],
                   capture_output=True, text=True)
    try:
        s = open(fn, encoding='utf-8', errors='ignore').read()
    except OSError:
        return []
    out = []
    for b in re.findall(r'<li class="b_algo".*?</li>', s, re.S):
        t = re.search(r'<h2>(.*?)</h2>', b, re.S)
        u = re.search(r'<cite[^>]*>(.*?)</cite>', b, re.S)
        d = re.search(r'<p class="b_lineclamp[^"]*"[^>]*>(.*?)</p>', b, re.S)
        title = html.unescape(re.sub('<[^>]+>', '', t.group(1))).strip() if t else ''
        curl = html.unescape(re.sub('<[^>]+>', '', u.group(1))).strip() if u else ''
        desc = html.unescape(re.sub('<[^>]+>', '', d.group(1))).strip() if d else ''
        # normalize cite breadcrumb to a url
        m = re.search(r'https?://[^\s]+', curl.replace(' › ', '/'))
        link = m.group(0) if m else curl
        if title:
            out.append((title, link, desc))
    return out

if __name__ == '__main__':
    q = sys.argv[1]
    for t, u, d in bing(q):
        print('##', t)
        print('  ', u)
        if d:
            print('   >', d[:300])
