import socket
import concurrent.futures

COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 
    993, 995, 1723, 3306, 3389, 5900, 8080, 8443, 8888
]

def scan_single_port(ip, port, timeout=1.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except Exception:
        pass
    return None

def run_scanner(ip, ports=None, max_threads=50):
    if ports is None:
        ports = COMMON_PORTS
        
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_single_port, ip, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                open_ports.append(res)
    return sorted(open_ports)
  
