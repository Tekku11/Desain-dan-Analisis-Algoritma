import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools

#Try all tours(exact TSP)
def exact_TSP(cities):
    "Generate all possible tours of the cities and choose the shortest one."
    return shortest(alltours(cities))

def shortest(tours):
    "Return the tour with the minimum total distance."
    return min(tours, key=total_distance)

#Representing tours
alltours = itertools.permutations #The permutation function is already defined in the itertools module
cities = {1, 2, 3}

print(list(alltours(cities)))

#------------------------------------------------------------------------------------------------------------------------------------

#Representing Cities and Distance
def total_distance(tour):
    "The total distance between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i-1])for i in range (len(tour)))

City = complex #Constructor for new cities, e.g. city(300, 400)

def distance(A, B):
    "The distance between two points."
    return abs(A - B)

A = City(300, 0)
B = City(0, 400)
print("")
print(distance(A, B))

#------------------------------------------------------------------------------------------------------------------------------------
def Cities(n):
    "Make a set of n cities, each with random coordinates."
    return set(City(random.randrange(10, 890), random.randrange(10, 590))for c in range(n))

# Let's make some standard sets of cities of various sizes.
# We'll set the random seed so that these sets are the same every time we run this notebook.
random.seed('seed')
cities8, cities10, cities100, cities1000 = Cities(8), Cities(10), Cities(100), Cities(1000)
cities8

#------------------------------------------------------------------------------------------------------------------------------------
'''
tour = exact_TSP(cities8)
print(tour)
print(total_distance(tour))
'''
#------------------------------------------------------------------------------------------------------------------------------------
#Try all non-redundant tours
def alltours(cities):
    "Return a list of tours, each a permutation of cities, but each one starting with the same city."
    start = first(cities)
    return [[start] + list(tour)
            for tour in itertools.permutations(cities - {start})]

def first(collection):
    "Start iterating over collection, and return the first element."
    for x in collection: return x
print("")
print(alltours({1, 2, 3}))
print(alltours({1, 2, 3, 4}))
#------------------------------------------------------------------------------------------------------------------------------------
tour = exact_TSP(cities8) #check if the process is eight times faster
print(tour)
print(total_distance(tour))
#------------------------------------------------------------------------------------------------------------------------------------

# Slide 37
import time

def plot_tour(algorithm, cities):
    "Apply a TSP algorithm to cities , and plot the resulting tour."
    # Find the solution and time how long it takes
    t0 = time.time()
    tour = algorithm(cities)
    t1 = time.time()
    # Plot the tour as blue lines between blue circles, and the starting city as a red square.
    plotline(list(tour) + [tour[0]])
    plotline([tour[0]], 'rs')
    plt.show()
    print("{} city tour; total distance = {:.3f} secs for {}".format(len(tour), total_distance(tour), t1-t0, algorithm.__name__))

def plotline(points, style='bo-'):
    "Plot a list of points (complex numbers) in the 2-D plane."
    X, Y = XY(points)
    plt.plot(X, Y, style)

def XY(points):
    "Given a list of points, return two lists: X coordinates, and Y coordinates."
    return [p.real for p in points], [p.imag for p in points]
plot_tour(exact_TSP, cities8)
plot_tour(exact_TSP, cities10)
#------------------------------------------------------------------------------------------------------------------------------------
# Greedy Nearest Neighbor (greedy_TSP)

def greedy_TSP(cities):
    "At each step, visit the nearest neighbor that is still unvisited."
    start = first(cities)
    tour = [start]
    unvisited = cities - {start}
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour

def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities, key=lambda x: distance(x, A))
#Print cities
cities = Cities(9)
plot_tour(exact_TSP, cities)
plot_tour(greedy_TSP, cities)
#------------------------------------------------------------------------------------------------------------------------------------
plot_tour(greedy_TSP, cities100)    #Slide 41
plot_tour(greedy_TSP, cities1000)
#------------------------------------------------------------------------------------------------------------------------------------
# Algorithm 3: Greedy Nearest Neighbor from All Starting Points (all_greedy_TSP)
def all_greedy_TSP(cities):
    "Try the greedy algorithm form each of the starting cities; return the shortest tour."
    return shortest(greedy_TSP(cities, start=c)for c in cities)

# We will modify greedy_TSP
def greedy_TSP(cities, start=None):
    "At each step, visit the nearest neighbor that is still unvisited."
    if start is None: start = first(cities)
    tour = [start]
    unvisited = cities - {start}
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour
#Compare greedy_TSP to all_greedy_TSP (Slide 46)
plot_tour(greedy_TSP, cities100)
plot_tour(all_greedy_TSP, cities100)

#------------------------------------------------------------------------------------------------------------------------------------
#Algorithm 4: Greedy Nearest Neighbor with Exact End(greedy_exact_end_TSP)
def greedy_exact_end_TSP(cities, start=None, end_size=8):
    """At each step, visit the nearest neighbor that is still unvisited until there are k_end cities left; then choose best of all possible endings."""
    if start is None: start = first(cities)
    tour = [start]
    unvisited = cities - {start}
    # Use greedy algorithm for all but the last end_size cities
    while len(unvisited) > end_size:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
        # Consider all permutations of possible ends to the tour, and choose the best one.
        # (But to make things faster, omit the middle of the tour.)
    ends = map(list, itertools.permutations(unvisited))
    best = shortest([tour[0], tour[-1]] + end for end in ends)
    return tour + best[2:]

#------------------------------------------------------------------------------------------------------------------------------------
plot_tour(greedy_exact_end_TSP, cities100) # Slide 48
plot_tour(greedy_exact_end_TSP, cities1000)

#Algorithm 5: Greedy Nearest Neighbor with Both Ends Search (greedy_bi_TSP)
def greedy_bi_TSP(cities, start_size=12, end_size=6):
    "At each step, visit the nearest neighbor that is still unvisited."
    starts = random.sample(cities, min(len(cities), start_size))
    return shortest(greedy_exact_end_TSP(cities, start, end_size)
                    for start in starts)
#Slide 50
random.seed('bi')
plot_tour(greedy_bi_TSP, cities100)
plot_tour(greedy_bi_TSP, cities1000)

#Benchmarking Algorithms
def compare_algorithms(algorithms, maps):
    "Apply each algorithm to each map and plot results."
    for algorithm in algorithms:
        t0 = time.time()
        results = [total_distance(algorithm(m)) for m in maps]
        t1 = time.time()
        avg = sum(results) / len(results)
        label = '{:.0f}; {:.1f}s: {}'.format(avg, t1-t0, algorithm.__name__)
        plt.plot(sorted(results), label=label)
    plt.legend(loc=2)
    plt.show()
    print('{} x {}-city maps'.format(len(maps), len(maps[0])))

def Maps(M, N):
    "Return a list of M maps, each consisting of a set of N cities."
    return [Cities(N) for m in range(M)]
#Slide 52
compare_algorithms([greedy_TSP, greedy_exact_end_TSP, all_greedy_TSP], Maps(100, 50))
#------------------------------------------------------------------------------------------------------------------------------------
def bi_10_6(cities): return greedy_bi_TSP(cities, 10, 6)
def bi_20_5(cities): return greedy_bi_TSP(cities, 20, 5)
def bi_40_4(cities): return greedy_bi_TSP(cities, 40, 4)
def bi_80_2(cities): return greedy_bi_TSP(cities, 80, 2)
def bi_160_1(cities): return greedy_bi_TSP(cities, 160, 1)

algorithms = [bi_10_6, bi_20_5, bi_40_4, bi_80_2, bi_160_1]
#Slide 54
compare_algorithms(algorithms, Maps(100, 50))
compare_algorithms(algorithms, Maps(50, 100))
#Slide 55
compare_algorithms(algorithms, Maps(25, 160))




