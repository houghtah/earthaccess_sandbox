## Git push notes

Rubric to push files to my GitHub from a terminal window in a jupyter notebook


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
<br>On branch main
<br>Your branch is up to date with 'origin/main'.
<br>nothing to commit, working tree clean


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ cp ../earthdata_scratch.ipynb ../functions/read_sat_functions.py .


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ ls
<br>earthdata_scratch.ipynb  list_pace_suites.ipynb  README.md  read_sat_functions.py


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
<br>On branch main
<br>Your branch is up to date with 'origin/main'.

Untracked files:
<br>  (use "git add <file>..." to include in what will be committed)
<br>        earthdata_scratch.ipynb
<br>        read_sat_functions.py
<br>nothing added to commit but untracked files present (use "git add" to track)


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git add earthdata_scratch.ipynb read_sat_functions.py 


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git commit -m "adding earthdata_scratch and read_sat_functions.py"
<br>[main 87d7513] adding earthdata_scratch and read_sat_functions.py
<br> 2 files changed, 891 insertions(+)
<br> create mode 100644 earthdata_scratch.ipynb
<br> create mode 100644 read_sat_functions.py


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git push
<br>Enumerating objects: 5, done.
<br>Counting objects: 100% (5/5), done.
<br>Delta compression using up to 4 threads
<br>Compressing objects: 100% (4/4), done.
<br>Writing objects: 100% (4/4), 403.26 KiB | 4.03 MiB/s, done.
<br>Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
<br>To github.com:houghtah/earthaccess_sandbox.git
<br>   86067d5..87d7513  main -> main


(**notebook**) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ git status
<br>On branch main
<br>Your branch is up to date with 'origin/main'.
<br>nothing to commit, working tree clean


(notebook) jovyan@jupyter-houghtah:~/earthaccess_sandbox$ 
