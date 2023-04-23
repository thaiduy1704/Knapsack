import time

from ortools.algorithms import pywrapknapsack_solver
from data import readData


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    solver.set_time_limit(180)
    # values = [
    #     360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    #     78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    #     87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    #     312
    # ]
    # weights = [[
    #     7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    #     42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    #     3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    # ]]
    # capacities = [850]

    str_n = ['00050', '00100', '00200', '00500', '01000', '02000', '05000']
    problem_types = [
        '00Uncorrelated',
        '01WeaklyCorrelated',
        '02StronglyCorrelated',
        '03InverseStronglyCorrelated',
        '04AlmostStronglyCorrelated',
        '05SubsetSum',
        '06UncorrelatedWithSimilarWeights',
        '07SpannerUncorrelated',
        '08SpannerWeaklyCorrelated',
        '09SpannerStronglyCorrelated',
        '10MultipleStronglyCorrelated',
        '11ProfitCeiling',
        '12Circle'

    ]

    problems = []
    for t in problem_types:
        tmp = []
        for k in str_n:
            tmp.append(f"kplib/{t}/n{k}/R01000/s060.kp")
        problems.append(tmp)

    for problem in problems:
        for file in problem:
            values, weights, capacities = readData(file)
            t1 = time.time()
            solver.Init(values, weights, capacities)
            computed_value = solver.Solve()
            t2 = time.time()
            print(t2 - t1)

            packed_items = []
            packed_weights = []
            total_weight = 0

            with open('final_result.txt', 'a') as writer:
                writer.write(f'Solution for {file}\n')
                writer.write(f'Total value = {computed_value}\n')
                for i in range(len(values)):
                    if solver.BestSolutionContains(i):
                        packed_items.append(i)
                        packed_weights.append(weights[0][i])
                        total_weight += weights[0][i]

                writer.write(f'Total weight: {total_weight}\n')
                writer.write(f'Packed items: {packed_items}\n')
                writer.write(f'Packed_weights: {packed_weights}\n')
                writer.write(f'Run time: {t2-t1}\n')
                writer.write(f'--------------------------------------\n')


if __name__ == '__main__':
    main()