import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from loadingbar import loadingbar
from title import title

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

BLUE = '34'
GREEN = '32'
RED = '31'

urls = []
urls_with_username = []
road = 0

title()

username = False
while not username:
    username = input('\033[1m\033[97m[*] Enter username: \033[0m').strip()
    if ' ' in username:
        print(colored("[ERROR] Username cannot contain spaces.\n", RED))
        username = False
    elif username == '':
        print(colored("[ERROR] Username cannot be empty.\n", RED))
        username = False

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for info in data.values():
    if 'url' in info:
        urls.append(info['url'])

for url in urls:
    if '{account}' in url:
        urls_with_username.append(url.replace('{account}', username))

total = len(urls_with_username)
loadingbar = loadingbar(total)

print(colored(f"[*] Starting profile checks for user '{username}' on {total} sites...\n", BLUE))

# Function to check one URL
def check_profile(url):
    try:
        response = requests.get(url, timeout=5)  # add timeout to avoid hanging
        if response.status_code == 200:
            return True, url
    except requests.exceptions.RequestException:
        return None, url
    return False, url

# Run checks in parallel
with ThreadPoolExecutor(max_workers=30) as executor:  # try 30 threads
    futures = {executor.submit(check_profile, url): url for url in urls_with_username}
    for idx, future in enumerate(as_completed(futures), 1):
        result, url = future.result()
        if result is True:
            road += 1
            loadingbar.log(colored(f"[+] Profile exists: {url}", GREEN))
        elif result is None:
            loadingbar.log(colored(f"[ERROR] Profile error for {url}", RED))
        loadingbar.update(idx)

loadingbar.finish()

print('\n' + '=' * 30)
print(colored(f"\033[1m[*] Total Profiles exists: {road}/{total}", BLUE))
print(colored(f"\033[1m[*] Total Profiles not exists: {total - road}/{total}", BLUE))
print(colored(f"\033[1m[*] Time taken: {loadingbar.elapsed_time():.2f}s", BLUE))

print(colored("✔ Script finished successfully!", GREEN))
