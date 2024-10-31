# COMPUTE NOMINAL LOAD CAPACITY OF SHORT COLUMN WITHOUT ANY ECCENTRICITY
# CODE LIMITATIONS NOT INCORPORATED

# COLUMN SIZE, inch
width = 12
depth = 12

# REINFORCEMENT, number of bars and area in sq.inch
n = 12
Ab = 0.44

# MATERIAL STRENGTH, f'c psi, fy psi
fc = 3000
fy = 60000

# CALCULATE
Ast = n * Ab
Ag = width * depth
An = Ag - Ast

P = 0.85*fc*An + Ast*fy

# PRINT
print(f"Total area of steel = {Ast:0.2f} sq.inch")
print(f"Column gross area = {Ag:0.2f} sq.inch")
print(f"Column net area = {An:0.2f} sq.inch")
print()
print(f"Nominal Load capacity of the section = {P:.2f} lb.")
print()
