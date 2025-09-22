# Fresh GitHub Repo with Virtual Environment and Jupyter Kernel

## 1. Create Local Project Folder

``` bash
mkdir my_new_project
cd my_new_project
```

## 2. Set Up Virtual Environment

``` bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# .\venv\Scripts\activate   # Windows PowerShell
```

## 3. Install Required Packages

``` bash
pip install --upgrade pip
pip install ipykernel matplotlib numpy opencv-python
```

## 4. Freeze Dependencies

``` bash
pip freeze > requirements.txt
```

## 5. Create .gitignore

``` bash
# .gitignore
venv/
__pycache__/
*.pyc
*.pyo
.ipynb_checkpoints/
.env
```

## 6. Initialize Git and Commit

``` bash
git init
git add .
git commit -m "Initial commit: venv, requirements, .gitignore"
```

## 7. Create GitHub Repo and Push

1.  Go to [GitHub](https://github.com/new) and create a new repository.
2.  Copy the repo URL.

``` bash
git remote add origin https://github.com/your-username/my_new_project.git
git branch -M main
git push -u origin main
```

## 8. Register venv with Jupyter

``` bash
python -m ipykernel install --user --name=my_new_project --display-name "Python (my_new_project)"
```

## 9. Verify and Use

-   Open Jupyter in VS Code, select **Python (my_new_project)** as
    kernel.
-   Add packages later:

``` bash
pip install somepackage
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add somepackage"
git push
```