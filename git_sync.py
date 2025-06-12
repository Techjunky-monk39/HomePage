import subprocess

def run_git_command(command):
    """Run a Git command and print the output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def git_sync():
    """Automate Git operations: add, commit, and force push."""
    # Add all changes
    print("Adding changes...")
    run_git_command(["git", "add", "."])

    # Commit changes
    commit_message = "Automated commit"
    print(f"Committing changes with message: {commit_message}")
    run_git_command(["git", "commit", "-m", commit_message])

    # Force push changes
    print("Force pushing changes...")
    run_git_command(["git", "push", "origin", "main", "--force"])

if __name__ == "__main__":
    git_sync()
