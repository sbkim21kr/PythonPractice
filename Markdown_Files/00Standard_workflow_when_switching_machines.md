### 🔹 Standard workflow when switching machines

1. **Clone (or pull) the repo**

   ```bash
   git clone <repo-url>
   cd PythonPractice
   ```

2. **Create a new virtual environment (fresh, per machine)**

   * Linux/macOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Windows (cmd):

     ```bash
     python -m venv venv
     venv\Scripts\activate.bat
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

### 🔹 Best practice to make it smooth

* Always keep `requirements.txt` (or `pyproject.toml`) up to date:

  ```bash
  pip freeze > requirements.txt
  ```
* Then, no matter which machine you’re on, `pip install -r requirements.txt` gives you the same environment.

---

✅ So yes — every time you move to a new machine, **you must** rebuild `venv` and reinstall packages from `requirements.txt`.
But you don’t need to repeat it every day — only when you **first set up** the repo on that machine, or if dependencies change.

---

Do you want me to also show you a **shortcut script** (like `setup.sh` / `setup.bat`) so you can recreate the venv with one command instead of typing all those steps each time?
