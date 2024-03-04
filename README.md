# adventOfCode2023 🎄



[![Python application](https://github.com/monpie3/adventOfCode2023/actions/workflows/python-app.yml/badge.svg)](https://github.com/monpie3/adventOfCode2023/actions/workflows/python-app.yml)  [![codecov](https://codecov.io/gh/monpie3/adventOfCode2023/graph/badge.svg?token=LVTAOWR2L5)](https://codecov.io/gh/monpie3/adventOfCode2023)


You can find the puzzle inputs here: [https://adventofcode.com/2023](https://adventofcode.com/2023)


### Recap of my progress in Advent of Code so far:
* [2020](https://github.com/monpie3/adventOfCode2020): 10 days (19 ⭐)
* 2023: 22 days (36 ⭐)


# What have I learned this year?
----
I really liked summary thread on [Reddit](https://www.reddit.com/r/adventofcode/comments/18qntwl/what_have_you_learned_this_year/), particularly [Leftfish](https://github.com/Leftfish/Advent-of-Code-2023/blob/main/README.md)'s summary, and although mine won't be as detailed, I would still like to share a few words here.
### Geometry Formulas:
- I found out about Shoelace and Pick's formula

* In the shoelace algorithm, we can use either just the polygon edges or all the points that define the shape.
* In the case of going clockwise the result will be negative.
* In Pick's formula the edges themselves are not enough - here the number of points inside the figure and on the edges is important.


---

### Data Structures & Algorithms:

- I became more familiar with deque (list-like container with fast appends and pops) which helps avoiding unnecessary recursion.
- I learned more about tracing the path in BFS and Dijkstra’s Algorithm.

---
### Python Insights:

* **Simpler Debugging With F-Strings**

I did not know that you can just add `=` to the end of an expression,and this will print both the expression and its value.

```
tmp = "Have a good day 😊!"

print(f"tmp = '{tmp}'")
print(f"{tmp = }")
```

Both prints will show the same output.

If interested, you can read more here → [Python documentation](https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging) and [Post on Real Python](https://realpython.com/lessons/simpler-debugging-f-strings/).


* **The `in` operator with a Pandas series will check the index.**

In the task from day 11, when I wanted to filter a DataFrame using list comprehension, I encountered a problem. As it turned out:
```"#" not in data[:][col_ind]```
is not the same as:
```"#" not in list(data[:][col_ind])```


The `in` operator on a `pandas.Series` checks whether something is in the index, just like it works with a `dict`. So, to get the behaviour I wanted, I had to convert `pandas.Series` to a list (as shown in the second example).

Below is a short example illustrating the diffrence.

```
import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

filtred_columns_1 = [col for col in data.columns if 4 not in data[:][col]]
filtred_columns_2 = [col for col in data.columns if 4 not in list(data[:][col])]

print("Result (Expression 1):", filtred_columns_1)  # ['A', 'B', 'C']
print(4 in data[:]['B'])  # False

print("Result (Expression 2):", filtred_columns_2) # ['A', 'C']
print(4 in list(data[:]['B']))  # True

```
So our dataframe looks:
| A  | B  |  C |
| ---| ---| ---|
| 1  | 4  | 7  |
| 2  | 5  | 8  |
| 3  | 6  | 9  |



In first case, we received all columns, despite the fact that in second columns there is 4, because `pandas.Series` looks like this:


|    | B |
|----|---|
| **0** | 4 |
| **1** | 5 |
| **2** | 6 |


Because there is no 4 in the indexes (0,1,2), the expression is evaluated to True.

Of coursem there are more Pandorable approaches, for example:
`data.columns[(data != 4).all()]`

But the way this operated caught me off guard.



Here's a helpful StackOverflow [question](https://stackoverflow.com/questions/51962778/python-in-operator-not-working-as-expected-when-comparing-string-and-strftime-va) regarding this topic.

* **I became more familiar with the Python's standard libraries: itertools  and collections**

I used namedtuples, deque, defaultdict, and Counter from collections, and combinations and pairwise from itertools.

---
### Version Control:
At some point, I realized that I had not taken into account the fact that if I named the folder Day_1, and when I create the Day_10 folder, the latter would be displayed above.

Because of this, I read more about git rebase and, as a result, renamed folders (Day_1 -> Day_01) without changing the dates in the commit.

* To do this, you cannot have any unsaved modification.
You need to stash your changes or create a temporary commit:
`git commit -m "tmp"`

* Then execute the command:
`git rebase --committer-date-is-author-date -i HEAD~1`
Instead of using `HEAD~2`, you can use the notation `HEAD^^`.
It is important to have in range the commit from which you want to start making changes.
`git rebase -i --root` will start an interactive rebase of all commits from the beginning.
To preserve the committer date you need to add the `--committer-date-is-author-date` flag. This flag does not preserve the committer date, but it makes the committer date equal to the author date (which is good enough for me).

* VIM will open. Press `i` to start insert mode. Put `e` before commit you want to make changes to and exit VIM (`escape`, then `:wq`).


* Make changes. If you want to remove file, use the following command:
`git rm --cached folder/file_name.txt`


* When you finish, execute:
`git rebase --continue`

* Then VIM will open, if you don't want to change the commit name, simply press `escape`, and then type `:wq`.


How to continue a Git rebase and skip editing the commit message? [More here](https://til.codeinthehole.com/posts/how-to-continue-a-git-rebase-and-skip-editing-the-commit-message/)

### Other

- I created Reddit acount.
- I learned how to create Sankey diagrams → https://sankeymatic.com/build/
---
