import pulp

# Instantiate our problem class (Slide 13)
model = pulp.LpProblem("ProfitMaximizingProblem", pulp.LpMaximize)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')

# Objective function (Slide 14)
model += 4200 * A + 2800 * B, "Profit"
#Constraints
model += 3 * A + 2 * B <= 20
model += 4 * A + 3 * B <= 30
model += 4 * A + 3 * B <= 44
# Solve our problem
model.solve()
pulp.LpStatus[model.status]

# Print our decision (Slide 15)
print(A.varValue)
print(B.varValue)
# Print our objective function value
print(pulp.value(model.objective))