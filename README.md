# [GoogleCodeJam 2015](https://codingcompetitions.withgoogle.com/codejam/archive/2015) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Progress](https://img.shields.io/badge/progress-28%20%2F%2028-ff69b4.svg)

Python solutions of Google Code Jam 2015. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A `4-minute` timer is set for the small dataset and a `8-minute` timer is set for the large dataset this year.

* [Code Jam 2014](https://github.com/kamyu104/GoogleCodeJam-2014)
* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2015#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2015#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2015#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2015#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2015#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2015#round-3)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2015#world-finals)
* [Code Jam 2016](https://github.com/kamyu104/GoogleCodeJam-2016)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Standing Ovation](https://code.google.com/codejam/contest/6224486/dashboard#s=p0)| [Python](./Qualification%20Round/standing-ovation.py)| _O(S)_ | _O(1)_ | Easy | | |
|B| [Infinite House of Pancakes](https://code.google.com/codejam/contest/6224486/dashboard#s=p1)| [Python](./Qualification%20Round/infinite-house-of-pancakes.py)| _O(max(P) * D)_ | _O(1)_ | Easy | | |
|C| [Dijkstra](https://code.google.com/codejam/contest/6224486/dashboard#s=p2)| [Python](./Qualification%20Round/dijkstra.py)| _O(L)_ | _O(L)_ | Medium | | |
|D| [Ominous Omino](https://code.google.com/codejam/contest/6224486/dashboard#s=p3)| [Python](./Qualification%20Round/ominous-omino.py)| _O(1)_ | _O(1)_ | Hard | | |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Mushroom Monster](https://code.google.com/codejam/contest/4224486/dashboard#s=p0)| [Python](./Round%201A/mushroom-monster.py)| _O(S)_ | _O(1)_ | Easy | | |
|B| [Haircut](https://code.google.com/codejam/contest/4224486/dashboard#s=p1)| [Python](./Round%201A/haircut.py)| _O(log(N * max(M)) + BlogB)_ | _O(B)_ | Medium | | Binary Search |
|C| [Logging](https://code.google.com/codejam/contest/4224486/dashboard#s=p2)| [C++](./Round%201A/logging.cpp) [Python](./Round%201A/logging.py)| _O(N^2)_ | _O(N)_ | Hard | | |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Counter Culture](https://code.google.com/codejam/contest/8224486/dashboard#s=p0)| [Python](./Round%201B/counter-culture.py)| _O(logN)_ | _O(logN)_ | Easy | | |
|B| [Noisy Neighbors](https://code.google.com/codejam/contest/8224486/dashboard#s=p1)| [C++](./Round%201B/noisy-neighbors.cpp) [Python](././Round%201B/noisy-neighbors.py)| _O(R * C)_ | _O(1)_ | Medium | | |
|C| [Hiking Deer](https://code.google.com/codejam/contest/8224486/dashboard#s=p2)| [C++](./Round%201B/hiking-deer.cpp) [Python](./Round%201B/hiking-deer.py)| _O(HlogH)_ | _O(H)_ | Hard | | Heap |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Brattleship](https://code.google.com/codejam/contest/4244486/dashboard#s=p0)| [Python](./Round%201C/brattleship.py)| _O(1)_ | _O(1)_ | Easy | | |
|B| [Typewriter Monkey](https://code.google.com/codejam/contest/4244486/dashboard#s=p1)|[Python](./Round%201C/typewriter-monkey.py)| _O(K + L * S)_ | _O(K + L)_ | Medium | | DP |
|C| [Less Money, More Problems](https://code.google.com/codejam/contest/4244486/dashboard#s=p2)| [Python](./Round%201C/less-money-more-problems.py)| _O(V / ((C + D) * D))_ | _O(1)_ | Easy | | |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Pegman](https://code.google.com/codejam/contest/8234486/dashboard#s=p0)| [Python](./Round%202/pegman.py)| _O(R * C)_ | _O(R + C)_ | Easy | | |
|B| [Kiddie Pool](https://code.google.com/codejam/contest/8234486/dashboard#s=p1)| [Python](./Round%202/kiddie-pool.py)| _O(NlogN)_ | _O(1)_ | Medium | | Optimization |
|C| [Bilingual](https://code.google.com/codejam/contest/8234486/dashboard#s=p2)| [C++](./Round%202/bilingual.cpp) [Python](./Round%202/bilingual.py)| _O((N * L)^2)_ | _O(N * L)_ | Hard | | Max Flow |
|D| [Drum Decorator](https://code.google.com/codejam/contest/8234486/dashboard#s=p3)| [Python](./Round%202/drum-decorator.py)| _O(R^2)_ | _O(1)_ | Hard | | DP |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Fairland](https://code.google.com/codejam/contest/4254486/dashboard#s=p0)| [Python](./Round%203/fairland.py)| _O(NlogN)_ | _O(N)_ | Easy | | |
|B| [Smoothing Window](https://code.google.com/codejam/contest/4254486/dashboard#s=p1)| [Python](./Round%203/smoothing-window.py)| _O(N)_ | _O(N)_ | Medium | | |
|C| [Runaway Quail](https://code.google.com/codejam/contest/4254486/dashboard#s=p2)| [C++](./Round%203/runaway-quail.cpp) [Python](./Round%203/runaway-quail.py)| _O(N^3)_ | _O(N^2)_ | Medium | | DP |
|D| [Log Set](https://code.google.com/codejam/contest/4254486/dashboard#s=p3)| [Python](./Round%203/log-set.py)| _O(N * (logN)^2)_ | _O(logN)_ | Hard | | Hash |
|E| [River Flow](https://code.google.com/codejam/contest/4254486/dashboard#s=p4)| [Python](./Round%203/river-flow.py)| _O(DlogD)_ | _O(D)_ | Medium |

## World Finals
You can relive the magic of the 2015 Code Jam World Finals by watching the [Live Stream Recording](https://www.youtube.com/watch?v=rh_EYIu7Ztc) of the competition, problem explanations, interviews with Google and Code Jam engineers, and announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Costly Binary Search](https://code.google.com/codejam/contest/5224486/dashboard#s=p0)| [C++](./World%20Finals/costly-binary-search.cpp) [PyPy](./World%20Finals/costly-binary-search.py) | _O(NlogN)_ | _O(N)_ | Medium | | DP |
|B| [Campinatorics](https://code.google.com/codejam/contest/5224486/dashboard#s=p1)| [Python](./World%20Finals/campinatorics.py) | _O(N)_ | _O(N)_ | Medium | | DP, Euler's Theorem |
|C| [Pretty Good Proportion](https://code.google.com/codejam/contest/5224486/dashboard#s=p2)| [C++](./World%20Finals/pretty-good-proportion.cpp) [Python](./World%20Finals/pretty-good-proportion.py) | _O(NlogN)_ | _O(N)_ | Easy | |Sort|
|D| [Taking Over The World](https://code.google.com/codejam/contest/5224486/dashboard#s=p3)| [C++](./World%20Finals/taking-over-the-world.cpp) [Python](./World%20Finals/taking-over-the-world.py) | _O(K * N * M^2)_ |  _O(N^2)_ | Hard | | Max Flow |
|E| [Merlin QA](https://code.google.com/codejam/contest/5224486/dashboard#s=p4)| [Python](./World%20Finals/merlin-qa.py) | _O(M! * (N * M))_ | _O(N * M)_ | Medium | | |
|F| [Crane Truck](https://code.google.com/codejam/contest/5224486/dashboard#s=p5)| [C++](./World%20Finals/crane-truck.cpp) [PyPy](./World%20Finals/crane-truck.py) | _O(N^2)_ | _O(N^2)_ | Very Hard | ❤️ | Simulation |
