## Git push notes

Rubric to push files to my GitHub from a terminal window in a jupyter notebook


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ cp ../earthdata_scratch.ipynb ../functions/read_sat_functions.py .


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ ls
earthdata_scratch.ipynb  list_pace_suites.ipynb  README.md  read_sat_functions.py


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        earthdata_scratch.ipynb
        read_sat_functions.py

nothing added to commit but untracked files present (use "git add" to track)


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git add earthdata_scratch.ipynb read_sat_functions.py 


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git commit -m "adding earthdata_scratch and read_sat_functions.py"
[main 87d7513] adding earthdata_scratch and read_sat_functions.py
 2 files changed, 891 insertions(+)
 create mode 100644 earthdata_scratch.ipynb
 create mode 100644 read_sat_functions.py


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 403.26 KiB | 4.03 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:houghtah/earthaccess_sandbox.git
   86067d5..87d7513  main -> main


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
(notebook) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ 
