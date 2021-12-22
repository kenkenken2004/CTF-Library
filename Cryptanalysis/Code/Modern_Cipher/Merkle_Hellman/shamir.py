import pulp
from .basic import *


def solve(b: []):
    length = len(b)
    epsilon = 0
    l = 0
    k = 0
    delta = 0
    problem = pulp.LpProblem("Finder", pulp.LpMinimize)
    x = [pulp.LpVariable('x_{}'.format(i), cat=pulp.LpInteger, lowBound=1, upBound=b[i] - 1) for i in range(l)]
    problem += pulp.lpSum(x[0] * b[i] - x[i] * b[0] for i in range(1, l))
    for _ in range(1, l):
        problem += abs(x[0] * b[_] - x[_] * b[0]) <= delta
    result = problem.solve()
    print(problem)


w, q, r, b = key_gen()
solve(b)
