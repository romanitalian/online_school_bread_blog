import requests

url = 'https://speed.hetzner.de/10GB.bin'

# response = requests.get(url)
# with open('./10GB.bin', 'wb') as file:
#     file.write(response.content)

with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open("./10GB.bin", 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
