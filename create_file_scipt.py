import os

# Fill this out
SOURCE = "leet-code"  # Hacker Rank or Leet Code
LINK = r"https://leetcode.com/problems/list-the-products-ordered-in-a-period/"

# Automated file creation...
SQL_FILE_NAME = LINK.split("/")[4]
SQL_TITLE_NAME = SQL_FILE_NAME.replace("-", " ").title()

PATH = f"./{SOURCE}/{SQL_FILE_NAME}.sql"
README_PATH = f"{SOURCE}/README.md"

print("PATH: ", PATH)

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
        readme.write(f"# Problems solved - {SOURCE.replace('-',' ').title()}\n\n")
        readme.write("| Link | Problem Name | My solution |\n")
        readme.write("| --- | --- | --- |\n")

with open(README_PATH, "a") as readme:
    readme.write(
        f"| [Link]({LINK}) | {SQL_TITLE_NAME} | [My solution]({SQL_FILE_NAME}.sql) |\n"
    )
