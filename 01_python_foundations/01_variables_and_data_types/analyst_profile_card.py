# 1. Defining the Profile Data
full_name = "Parth Parikh"
role = "Data Analyst"
city = "Ahmedabad"
skills_count = 5
top_skill = "Python"
years_experience = 2.5
is_available_for_work = True

# 2. Status Label (Convert Boolean to a human-readable string)
# If is_available_for_work is True, show "Open to Work", else "Busy"
status = "Open to Work" if is_available_for_work else "Currently Employed"

# 3. Printing the Profile Card
print("=" * 30)
print("   DATA ANALYST PROFILE   ")
print("=" * 30)
print(f"Name       : {full_name}")
print(f"Role       : {role}")
print(f"Location   : {city}")
print(f"Experience : {years_experience} Years")
print(f"Top Skill  : {top_skill}")
print(f"Skills     : {skills_count} Tools Mastered")
print(f"Status     : {status}")
print("=" * 30)
