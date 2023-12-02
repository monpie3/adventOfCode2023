import os

DAY_NUM = 3

# path for the directory
path = f"./Day_{DAY_NUM}"

# create new single directory
os.makedirs(path, exist_ok=False)

filenames = [
    f"{path}/example_{DAY_NUM}a.txt",
    f"{path}/example_{DAY_NUM}b.txt",
    f"{path}/task_{DAY_NUM}a.py",
    f"{path}/task_{DAY_NUM}b.py",
    f"{path}/test_task_{DAY_NUM}a.py",
    f"{path}/test_task_{DAY_NUM}b.py",
    f"{path}/puzzle_input.txt",
    f"{path}/README.md",
]
for filename in filenames:
    open(filename, "w")
