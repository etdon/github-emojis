import requests

emoji_data = requests.get("https://api.github.com/emojis", headers={
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
  }
)

readme_file = open("README.md", "w+")
readme_file.write(emoji_data.text)
readme_file.close()
