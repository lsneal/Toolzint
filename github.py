import requests
from bs4 import BeautifulSoup

def get_repos(user):
    
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    repos = response.json()

    repos_name = []

    for repo in repos:
        repos_name.append(repo['name']) # add all repo name

    return repos_name

def get_commits(user, repo):
    
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    sha_commit = []

    for commit in commits:
            sha_commit.append(commit['sha'])

    return sha_commit

def get_patch_lines(user, repo, commit_sha):
    
    url = f"https://github.com/{user}/{repo}/commit/{commit_sha}.patch" # .patch
    response = requests.get(url)
    
    if response.status_code == 200:
        lines = response.text.split('\n')[:5] # 5 first lines (format json)
        return lines

    return 

def github_search():
    user = input("Enter the GitHub username: ")
    
    repos = get_repos(user)
    for repo in repos:
        commits = get_commits(user, repo)
        for commit_sha in commits:
            
            lines = get_patch_lines(user, repo, commit_sha)
            print(f"Repo: {repo}, Commit: {commit_sha}")
            
            for line in lines:
                print(line)
            print("\n" + "================================" + "\n")
