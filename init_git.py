"""A file for initializing the repository.

This file should be deleted after initial setup.
"""

import json
import re
import shutil
import subprocess
from pathlib import Path


def _main() -> None:
    # Parse the config.
    outer_dir = Path(".").parent.resolve()
    config_file = outer_dir / "config.json"
    assert config_file.exists(), "Missing config file"
    with open(config_file, "r", encoding="utf-8") as fp:
        config = json.load(fp)

    # Validate the config.
    assert "developer" in config, "Missing developer name in config file"
    developer = config["developer"]
    github_username = config["github-username"]

    # Get the repository name from this directory.
    repo_name = outer_dir.name

    # Delete the existing git files if they are from the starter repo.
    git_repo = outer_dir / ".git"
    if git_repo.exists():
        git_config_file = git_repo / "config"
        with open(git_config_file, "r", encoding="utf-8") as fp:
            git_config_contents = fp.read()
        if "git@github.com:madan96/ros-ws-starter.git" in git_config_contents:
            shutil.rmtree(git_repo)

    # Initialize the repo anew.
    subprocess.run(["git", "init"], check=True, capture_output=True)
    subprocess.run(["git", "checkout", "-b", "main"], check=True, capture_output=True)
    subprocess.run(["git", "add", "."], check=True, capture_output=True)

    # Check if the remote already exists (if this script is being run twice).
    # This can happen if the user makes a mistake in their GitHub username.
    ret = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        check=False,
        capture_output=True,
    )
    # Remote already exists, so set the URL.
    if ret.returncode == 0:
        remote_command = "set-url"
    # Remote doesn't exist, so add the URL.
    else:
        remote_command = "add"
    subprocess.run(
        [
            "git",
            "remote",
            remote_command,
            "origin",
            f"git@github.com:{github_username}/{repo_name}.git",
        ],
        check=True,
        capture_output=True,
    )

    # Report succcess.
    print("Configuration applied successfully.")


if __name__ == "__main__":
    _main()