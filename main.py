import os
import subprocess
import requests
from bs4 import BeautifulSoup

github_user = 'Mustkeem324'
url = f'https://github.com/{github_user}?tab=repositories'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    repos = soup.find_all('a', itemprop='name codeRepository')
    repo_links = [f"https://github.com{repo.get('href')}.git" for repo in repos]
    if not os.path.exists(github_user):
      os.makedirs(github_user)
    # Clone each repository
    for link in repo_links:
        subprocess.run(['git', 'clone', link], cwd=github_user)
        print(f"Cloned {link}")
else:
    print("Failed to retrieve repositories.")
