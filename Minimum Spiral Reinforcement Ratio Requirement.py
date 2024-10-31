# COMPUTE MINIMUM SPIRAL REINFORCEMENT RATIO AS PER ACI CODE

# COLUMN DIAMETER, inch
col_dia = 20

# CLEAR COVER, inch
cover = 1.5

# MATERIAL STRENGTH, f'c psi, fyt (fy of spiral reinf.) psi
fc = 4000
fyt = 60000

# CALCULATE
Ag = 0.785 * col_dia**2.0

# core dia
core_dia = col_dia - 2 * cover
# core area
Ach = 0.785 * core_dia**2.0

# minimum spiral ratio
rho_sp_min = 0.45 * (Ag/Ach - 1) * (fc/fyt)

# PRINT
print(f"Column gross area = {Ag:0.2f} sq.inch")
print(f"Column core area = {Ach:0.2f} sq.inch")
print()
print(f"Minimum required spiral reinforcement ratio = {rho_sp_min:.6f} ({rho_sp_min*100:0.2f}%)")
print()
