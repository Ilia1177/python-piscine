import time

# Get current time in seconds since epoch
current_time = time.time()

# Format the time in standard notation with 4 decimal places
standard_notation = f"{current_time:,.4f}"

# Format the time in scientific notation
scientific_notation = f"{current_time:.2e}"

# Get current date in the required format
current_date = time.strftime("%b %d %Y")

# Print the output
print(f"Seconds since January 1, 1970: {standard_notation} or {scientific_notation} in scientific notation")
print(current_date)