from datetime import datetime
import re

# Get current day of year
today = datetime.utcnow()
day_of_year = today.timetuple().tm_yday

file_path = "README.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Active Days badge number
updated_content = re.sub(
    r"Active%20Days-\d+/365",
    f"Active%20Days-{day_of_year}/365",
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print(f"Updated Active Days to {day_of_year}/365")
