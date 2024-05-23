import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# Replace 'YOUR_GITHUB_ACCESS_TOKEN' with your actual GitHub access token
headers = {
    'Authorization': 'your token',
    'Accept': 'application/vnd.github.v3+json'
}

def fetch_github_data(max_pages=10):
    all_repo_data = []
    for page in range(1, max_pages + 1):
        url = f'https://api.github.com/search/repositories?q=stars:>10000&sort=stars&order=desc&page={page}&per_page=100'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            break
        data = response.json()
        for item in data['items']:
            created_at = datetime.datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            age_years = round((datetime.datetime.now() - created_at).days/365,2)
            license_info = item.get('license', {})
            if license_info is None:
                license_name = 'No License'
            else:
                license_name = license_info.get('name', 'No License')
            all_repo_data.append({
                'name': item['name'],
                'stars': item['stargazers_count'],
                'language': item['language'],
                'owner': item['owner']['login'],
                'url': item['html_url'],
                'created_at': item['created_at'],
                'age_years': age_years,
                'license': license_name


            })
    return all_repo_data


# Fetch the data
repo_data = fetch_github_data(max_pages=50)  # Adjust max_pages as needed

# Convert to DataFrame
df = pd.DataFrame(repo_data)
print(df.head())

# Save to CSV for later use
df.to_csv('github_repos.csv', index=False)