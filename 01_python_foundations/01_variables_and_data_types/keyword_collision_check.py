# --- KEYWORD COLLISION ANALYSIS ---

# 1. 'for' fails because it is used to start loops.
# Correction: for -> loop_iterations or forecast_period
forecast_period_months = 12

# 2. 'while' fails because it starts conditional loops.
# Correction: while -> retention_duration or active_cycle
active_cycle_days = 30

# 3. 'return' fails because it is used to send values back from functions.
# Correction: return -> total_returns or investment_return
investment_return_amt = 15000.75

# 4. 'class' fails because it is used to define new object types.
# Correction: class -> product_class or customer_segment
customer_segment = "Premium"

# 5. 'import' fails because it is used to load external libraries.
# Correction: import -> import_tax or imported_volume
imported_volume_units = 500

# --- OUTPUT ---
print("--- Corrected Analytics Variables ---")
print(f"{'Forecast Period':<20}: {forecast_period_months} months")
print(f"{'Active Cycle':20}: {active_cycle_days} days")
print(f"{'Investment Return':<20}: Rs.{investment_return_amt}")
print(f"{'Customer Segment':<20}: {customer_segment}")
print(f"{'Imported Volume':<20}: {imported_volume_units} units")
