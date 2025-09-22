# Python Virtual Environment + Git Workflow Cheat Sheet

## 1. Create & Activate Virtual Environments

* **Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

* **Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

* **Windows (cmd.exe):**

```cmd
venv\Scripts\activate.bat
```

> Avoids PowerShell execution policy issues.

---

## 2. Common PowerShell Issue

* If activation fails with execution policy error:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

* Optional permanent fix for your user:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 3. Using requirements.txt

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Update after adding packages:

```bash
pip freeze > requirements.txt
```

---

## 4. Git & .gitignore

* Create `.gitignore` in project root with:

```
venv/
__pycache__/
*.py[cod]
.DS_Store
Thumbs.db
.vscode/
.idea/
```

* Commit once and push:

```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

## 5. Switching Between Machines

* On new machine:

```bash
git pull
```

* Recreate venv locally (see step 1).
* Activate venv and install dependencies:

```bash
pip install -r requirements.txt
```

---

## 6. Extra Tips

* Use branches for experiments:

```bash
git checkout -b feature-name
```

* Quickly clean & rebuild venv:

```bash
rm -rf venv && python -m venv venv
```

* In VS Code: `Ctrl+Shift+P → Python: Select Interpreter → choose local venv`
