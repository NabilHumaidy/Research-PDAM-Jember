import re,html,sys,subprocess
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0"
def get(url,out):
    subprocess.run(["curl","-sSL","-m","60","-A",UA,"-o",out,"-w","%{http_code}",url],capture_output=True,text=True)
    try: return open(out,encoding='utf-8',errors='ignore').read()
    except OSError: return ''
def links(s):
    out=[]
    for m in re.finditer(r'<a href="(https://www\.jatimnetwork\.com/[^"]+)"[^>]*>(.*?)</a>',s,re.S):
        t=html.unescape(re.sub('<[^>]+>','',m.group(2))).strip()
        if t and re.match(r'^[A-Z0-9]',t) and len(t)>20: out.append((t,m.group(1)))
    return out
if __name__=='__main__':
    s=get(sys.argv[1],'jn_q.html')
    t=re.search(r'<title>(.*?)</title>',s,re.S)
    print('TITLE:',html.unescape(t.group(1)).strip() if t else '?')
    seen=set()
    for tit,u in links(s):
        if u in seen: continue
        seen.add(u)
        print('-',tit[:100],'|',u)
