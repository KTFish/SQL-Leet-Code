import os

# Fill this out
SOURCE = "leet-code"  # Specify the site used (Hacker Rank or Leet Code)
LINK = r"https://leetcode.com/problems/list-the-products-ordered-in-a-period/"  # Input link to your problem
ID = None  # ID of the problem (only for leet code problems)

# Automated file creation...
SQL_FILE_NAME = LINK.split("/")[4]
SQL_TITLE_NAME = SQL_FILE_NAME.replace("-", " ").title()

PATH = f"./{SOURCE}/{SQL_FILE_NAME}.sql"
README_PATH = f"{SOURCE}/README.md"

# Create folder if it dosen't exists
if not os.path.exists(SOURCE):
    os.mkdir(SOURCE)

# Create SQL file
if not os.path.exists(PATH):
    with open(PATH, "w") as file:
        # Add a title row
        file.write(f"-- {SQL_FILE_NAME}\n")
        file.write(f"-- Exercise from: {LINK}\n")

# Write information about the problem to a .md file
if not os.path.exists(README_PATH):
    with open(README_PATH, "w") as readme:
        readme.write(f"# Solved Problems - {SOURCE.replace('-',' ').title()}\n\n")
        readme.write("| Problem ID | Problem Name | Link | My solution |\n")
        readme.write("| --- | --- | --- | --- |\n")

# Add new row with the exercise details
# Link - link to the webpage wit the exercise
# Problem Name - Name of exercise
# My solution - link to .sql file containing the solution
with open(README_PATH, "a") as readme:
    readme.write(
        f"| {ID} | [Link]({LINK}) | {SQL_TITLE_NAME} | [My solution]({SQL_FILE_NAME}.sql) |\n"
    )

# TODO: Sort markdown table function
