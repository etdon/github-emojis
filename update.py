import requests

emoji_data = requests.get("https://api.github.com/emojis", headers={
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
  }
)

formatted_data = [ "||||", "|---|---|---|" ]
line_components = []
for key, value in emoji_data.json().items():
    line_components.append(f":{key}: `{key}`|")
    if (len(line_components) == 3):
        formatted_data.append(f"|{''.join(line_components)}")
        line_components.clear()
if (len(line_components) > 0):
    for i in range(3 - len(line_components)):
        line_components.append("|")
    formatted_data.append(f"|{''.join(line_components)}")
    line_components.clear()

readme_file = open("README.md", "w+")
readme_file.write('\n'.join(formatted_data))
readme_file.close()
