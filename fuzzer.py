import urllib.request
import urllib.error
import concurrent.futures

COMMON_PATHS = [
    "admin", "login", "dashboard", "api", "v1", "v2", "swagger", "docs",
    "robots.txt", "sitemap.xml", ".env", ".git", "backup", "config",
    "uploads", "test", "dev", "server-status", "phpmyadmin", "app"
]

def check_path(base_url, path, timeout=2.0):
    url = f"{base_url.rstrip('/')}/{path}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'nullsuite-recon-framework/1.0'}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return {"path": f"/{path}", "status": response.status}
    except urllib.error.HTTPError as e:
        if e.code in [401, 403]:  # Yetki gerektiren ilginç yerler
            return {"path": f"/{path}", "status": e.code}
    except Exception:
        pass
    return None

def run_fuzzer(target_url, max_threads=15):
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url
        
    found_paths = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(check_path, target_url, path) for path in COMMON_PATHS]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                found_paths.append(res)
    return found_paths
  
