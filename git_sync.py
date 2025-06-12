import subprocess

def run_git_command(command):
    """Run a Git command and print the output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def git_sync():
    """Automate Git operations: pull, add, commit, and push."""
    # Pull the latest changes
    print("Pulling latest changes...")
    run_git_command(["git", "pull", "origin", "main"])

    # Add all changes
    print("Adding changes...")
    run_git_command(["git", "add", "."])

    # Commit changes
    commit_message = "Automated commit"
    print(f"Committing changes with message: {commit_message}")
    run_git_command(["git", "commit", "-m", commit_message])

    # Push changes
    print("Pushing changes...")
    try:
        # Try pushing normally
        run_git_command(["git", "push", "origin", "main"])
    except subprocess.CalledProcessError:
        # If upstream is not set, set it and push
        print("Setting upstream branch...")
        run_git_command(["git", "push", "--set-upstream", "origin", "main"])

if __name__ == "__main__":
    git_sync()
