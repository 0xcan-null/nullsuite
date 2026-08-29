import socket
import concurrent.futures

COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk",
    "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test",
    "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn",
    "ns3", "mail2", "new", "mysql", "old", "lists", "support", "mobile", "mx",
    "static", "docs", "beta", "shop", "sql", "secure", "demo", "cp", "calendar",
    "wiki", "web", "media", "email", "images", "img", "download", "server", "apps"
]

def check_subdomain(subdomain, domain):
    target = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        return {"subdomain": target, "ip": ip}
    except socket.gaierror:
        return None

def run_recon(domain, max_threads=20):
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(check_subdomain, sub, domain) for sub in COMMON_SUBDOMAINS]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                found.append(res)
    return found
  
