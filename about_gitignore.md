# Why Packages Cause Bloat

When you install packages with pip, they are downloaded and placed in your project's virtual environment folder (venv). These packages are made up of hundreds or thousands of files, many of which are large binaries. If your .gitignore file isn't configured correctly, Git will try to track and commit this entire venv folder.

Git is optimized for small, text-based files like your Python scripts. Trying to push a large, constantly changing binary tree like venv will make your repository massive and your pushes extremely slow.

How to Fix It

You need to tell Git to ignore the virtual environment folder. The standard and professional way to do this is by adding a .gitignore file to the root of your project.

    Create a .gitignore file: In your project's root directory, create a new file named .gitignore.
    Bash

### touch .gitignore

Add venv/ to it: Open the file in a text editor and add the following line:

## venv/

This tells Git to completely ignore the venv directory and all of its contents.

Commit the .gitignore file: Add and commit the .gitignore file to your repository.
Bash

###    git add .gitignore
### git commit -m "Add venv to .gitignore"
###    git push

Once this is done, Git will stop tracking the venv folder, and your pushes will be fast again. When you clone the repository on a new machine, you will simply create a new venv and install the packages from your requirements.txt file, which is a much more efficient workflow.