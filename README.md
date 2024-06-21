# GitHub Repository Scraper and Cloner

This script scrapes all repository links from a specified GitHub user's profile and clones them into a local directory.

## Prerequisites

- Python 3.x
- Git
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

## Installation

1. **Install Git**:
    - On Ubuntu/Debian:
      ```sh
      sudo apt update
      sudo apt install git
      ```
    - On macOS:
      ```sh
      brew install git
      ```
    - On Windows:
      Download and install Git from [git-scm.com](https://git-scm.com/).

2. **Install Python packages**:
    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

1. Save the script as `clone_repos.py`.
2. Run the script:
    ```sh
    python clone_repos.py
    ```

The script will create a directory named after the GitHub user and clone all their repositories into this directory.



## Troubleshooting

- Ensure Git is installed and accessible from your PATH.
- Verify the GitHub username and the URL format.
- Handle potential rate limits imposed by GitHub.
