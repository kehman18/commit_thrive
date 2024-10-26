import os
import git
import datetime
from git import Repo

# Corrected path to your local Git repository folder (not the Python file)
repo_path = r'C:/Users/Owner/Desktop/commit_thrive'
repo = Repo(repo_path)

# Check if the repository is valid
if repo.bare:
    print("The repository is bare. Please check the repo path.")
    exit(1)

# Create a commit with a specific message and backdate it
def create_backdated_commit(message, date):
    # Change the date format
    date_str = date.strftime("%Y-%m-%dT%H-%M-%S")
    dummy_file_path = os.path.join(repo_path, "dummy.txt")
    
    # Modify the dummy file by appending or overwriting content
    with open(dummy_file_path, "a") as file:
        file.write(f"Commit at {date_str}\n")
    
    # Stage and commit
    repo.index.add([os.path.relpath(dummy_file_path, repo_path)])
    commit_command = f'git commit --date="{date_str}" -m "{message}"'
    os.system(f'cd {repo_path} && {commit_command}')


# Function to create multiple backdated commits
def create_multiple_commits(num_commits):
    today = datetime.datetime.now()
    for i in range(num_commits):
        days_ago = i % 365
        commit_date = today - datetime.timedelta(days=days_ago)
        create_backdated_commit(f"Backdated commit {i + 1}", commit_date)

# Number of backdated commits you want to create
num_commits = 10  # Set to a lower number for testing

# Create the commits
create_multiple_commits(num_commits)

print(f"{num_commits} backdated commits have been created.")
