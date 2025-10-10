```markdown
# 🧪 Git Merge Strategies: Imagine This Git History

This guide walks through three essential Git merge strategies — Fast-Forward, 3-Way Merge, and Squash Merge — using a realistic example.

---

## 📦 Setup: Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature-branch

# Add a new function
echo "def multiply(a, b): return a * b" >> utils.py
git add utils.py
git commit -m "Add multiply function"
```

Now you have:
- `main`: no changes
- `feature-branch`: one new commit

---

## 1️⃣ Fast-Forward Merge

```bash
git checkout main
git merge feature-branch
```

- Used when `main` has no new commits.
- Git simply moves the pointer forward.
- No merge commit is created.
- Clean, linear history.

---

## 2️⃣ 3-Way Merge

```bash
# Make a change on main
git checkout main
echo "# Simple Calculator Project" >> README.md
git add README.md
git commit -m "Update README title"

# Merge feature branch
git merge feature-branch
```

- Used when both branches have new commits.
- Git compares the latest commits and their common ancestor.
- A merge commit is created to combine changes.

---

## 3️⃣ Squash Merge

```bash
# Add multiple commits to feature branch
git checkout -b feature-branch
echo "def divide(a, b): return a / b" >> utils.py
git add utils.py
git commit -m "Add divide function"

echo "# Division feature added" >> README.md
git add README.md
git commit -m "Update README for division"

# Squash merge into main
git checkout main
git merge --squash feature-branch
git commit -m "Add division feature (squashed)"
```

- Combines all commits from `feature-branch` into one.
- Keeps history clean and focused.
- Great for tidying up before merging.

---

## 🧠 Summary

| Strategy         | When to Use                          | Result                        |
|------------------|--------------------------------------|-------------------------------|
| Fast-Forward     | `main` has no new commits            | Pointer moves forward, no merge commit |
| 3-Way Merge      | Both branches have new commits       | Creates a merge commit        |
| Squash Merge     | Want to compress history             | One new commit, no full history |

---

Save this file as `merge-strategies.md` and keep it in your Git learning folder — it’s a great reference for real-world workflows!

```

---

Let me know if you want this turned into a GitHub README or expanded with diagrams and visuals — I can help you build a full tutorial page!


✅ Here's How It Works:

    One GitHub repository can hold many branches.

    You only need to create the repo once (e.g., simple-calculator).

    After that, you can push as many branches as you want into it:
    bash

git push -u origin feature-login
git push -u origin bugfix-typo
git push -u origin experimental-ui


    Each branch will appear in the same GitHub repo, and you can:

    Switch between them on GitHub

    Open pull requests to merge them into main

    Collaborate with others on specific features