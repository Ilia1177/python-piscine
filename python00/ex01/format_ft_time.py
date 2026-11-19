import time

current_time = time.time()
standard_notation = f"{current_time:,.4f}"
scientific_notation = f"{current_time:.2e}"
current_date = time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: "
      f"{standard_notation} or {scientific_notation} "
      f"in scientific notation")
print(current_date)
