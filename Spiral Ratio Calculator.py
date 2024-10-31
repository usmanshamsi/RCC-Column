# inputs

col_dia = 20 # inch
clear_cover = 1.5 #inch
spiral_bar_dia = 3/8 #inch
spiral_bar_area = 0.11 # sq.inch
spiral_spacing = 2

# core dia
core_dia = col_dia - 2 * clear_cover

# spiral ratio
rho_sp = 4 * spiral_bar_area * (core_dia - spiral_bar_dia) / ((core_dia ** 2.0) * spiral_spacing)

# PRINT
print(f"Column core diameter = {core_dia:0.2f} sq.inch")
print()
print(f"Spiral reinforcement ratio = {rho_sp:.6f} ({rho_sp*100:0.2f}%)")
print()
