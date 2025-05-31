import requests
import re
import matplotlib.pyplot as plt
from matplotlib import rcParams
from collections import defaultdict
import os

rcParams['font.family'] = 'Hiragino Sans'

# 環境変数からGitHub情報を取得
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")

HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

def get_issues():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=all&per_page=100"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_comments(issue_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def extract_hours_from_comment(comment):
    # 例: "作業時間: 2.5h" の形式から時間を抽出
    match = re.search(r'作業時間[:：]?\s*([\d.]+)h', comment)
    if match:
        return float(match.group(1))
    return None

def collect_work_logs():
    #work_logs = defaultdict(float)
    work_logs = defaultdict(lambda: defaultdict(float))
    issues = get_issues()
    for issue in issues:
        number = issue["number"]
        milestone = issue.get("milestone")
        milestone_name = milestone["title"] if milestone else "(None)"
        print(f"Issue #{number}: {issue['title']}")
        comments = get_comments(number)
        for comment in comments:
            print(f"  Comment: {comment['body']}")
            text = comment["body"]
            date = comment["created_at"][:10]  # YYYY-MM-DD
            hours = extract_hours_from_comment(text)
            if hours:
                work_logs[date][milestone_name] += hours
    return work_logs

def plot_work_logs(work_logs):
    if not work_logs:
        print("No work logs found.")
        return

    dates = sorted(work_logs.keys())
    milestones = sorted(set(m for d in logs.values() for m in d.keys()))
    hours = [work_logs[d] for d in dates]

    data = {m: [logs[d].get(m, 0) for d in dates] for m in milestones}

    # プロット
    plt.figure(figsize=(12,6))
    bottom = [0]*len(dates)
    for m in milestones:
        plt.bar(dates, data[m], bottom=bottom, label=m)
        bottom = [sum(x) for x in zip(bottom, data[m])]

    plt.title("WorkTime (PerMilestone)")
    plt.ylabel("worktime (h)")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig("progress_milestone.png")
    print("progress_milestone.png saved.")

if __name__ == "__main__":
    logs = collect_work_logs()
    plot_work_logs(logs)

