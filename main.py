import requests
import json
import os

proxies = []
page = 1
max_pages = 50

while len(proxies) < 1000 and page <= max_pages:
    url = f"https://www.proxyscan.io/api/proxy?limit=100&page={page}"
    response = requests.get(url)
    proxy_data = json.loads(response.content)

    for proxy in proxy_data:
        ip = proxy["Ip"]
        port = proxy["Port"]
        proxies.append(f"{ip}:{port}")

    page += 1

# Masaüstüne kaydetmek için dosya yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "proxy_list.txt")

with open(output_file, "w") as file:
    for proxy in proxies:
        file.write(f"{proxy}\n")

print(f"{len(proxies)} proxy {output_file} dosyasına kaydedildi.")
