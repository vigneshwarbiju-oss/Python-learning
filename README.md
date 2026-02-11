# Python Learning

This repository contains small Python practice files and exercises from the local `Python learning` folder.

How to push this folder to GitHub

Option A — create the repo on GitHub web then push locally:

1. On GitHub, create a new repository under your account `vigneshwarbiju-oss` named `Python-learning` (or any name you prefer).
2. Run the following commands in the `Python learning` folder (PowerShell or Git Bash):

```powershell
cd "c:\Users\BIJU\Documents\Git practice\Python learning"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/vigneshwarbiju-oss/Python-learning.git
git push -u origin main
```

Option B — use GitHub CLI (if `gh` is installed and authenticated):

```bash
cd "c:\Users\BIJU\Documents\Git practice\Python learning"
gh repo create vigneshwarbiju-oss/Python-learning --public --source=. --remote=origin --push
```

Notes:
- Replace `Python-learning` with your preferred repository name.
- If you already have a local Git repo, skip `git init` and adjust commands accordingly.
