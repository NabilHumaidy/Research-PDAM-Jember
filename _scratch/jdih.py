import re, json, subprocess, time, sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
BASE = "https://jdih.jemberkab.go.id"
CK = r"E:\BCC Manufair Case Research\_scratch\ck3.txt"

def sh(*args):
    return subprocess.run(["curl", *args], capture_output=True, text=True).stdout

def get_page(path):
    for i in range(10):
        sh("-sSL", "-m", "45", "-A", UA, "-c", CK, "-o", r"E:\BCC Manufair Case Research\_scratch\_p.html", BASE + path)
        try:
            s = open(r"E:\BCC Manufair Case Research\_scratch\_p.html", encoding="utf-8", errors="ignore").read()
        except OSError:
            s = ""
        m = re.search(r'name="csrf-token" content="([^"]+)"', s)
        if m and len(s) > 20000:
            return m.group(1)
        time.sleep(3)
    return None

def search(tok, judul, start=0):
    for i in range(10):
        out = sh("-sS", "-m", "45", "-b", CK, "-X", "POST", "-A", UA,
                 "-H", "X-Requested-With: XMLHttpRequest", "-H", f"X-CSRF-TOKEN: {tok}",
                 "-H", "Referer: " + BASE + "/Peraturan",
                 "--data-urlencode", f"start={start}", "--data-urlencode", "limit=100",
                 "--data-urlencode", f"judul={judul}", "--data-urlencode", "nomor=",
                 "--data-urlencode", "tahun=", "--data-urlencode", "jenis=",
                 "--data-urlencode", "status=", BASE + "/Peraturan/postDataPeraturan")
        out = out.strip()
        if out.startswith("[") or out.startswith("{"):
            try:
                return json.loads(out)
            except Exception:
                pass
        time.sleep(3)
    return None

if __name__ == "__main__":
    judul = sys.argv[1]
    tok = get_page("/Peraturan")
    print("token:", bool(tok))
    res = search(tok, judul)
    if res is None:
        print("FAILED")
    else:
        for r in res:
            print("-", r["kode"], "|", r["singkatan"], r["nomor"], "|", r["tgl_penetapan"], "|", r["judul"][:140])
        print("TOTAL", len(res))
