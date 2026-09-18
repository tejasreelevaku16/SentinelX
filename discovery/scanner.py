import socket

target = input("Enter target IP: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

assets = []

print(f"\nScanning {target}...")
print(f"Checking ports {start_port}-{end_port}\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "unknown"

        asset = {
            "ip": target,
            "port": port,
            "protocol": "TCP",
            "state": "open",
            "service": service
        }

        assets.append(asset)

        print(asset)

    sock.close()

print("\nScan completed.")
print(f"{len(assets)} open port(s) found.")
