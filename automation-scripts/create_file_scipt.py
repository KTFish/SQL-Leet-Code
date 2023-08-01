import os

# from git import Repo


def handle_documentation(LINK: str, ID: int, SOURCE: str = "leet-code") -> str:
    """Creates a README file if needed. Add row with a exercise based on the arguments provided.

    Args:
        SOURCE (str): Name of the page from which the exercise was taken (Leet Code, Hacker Rank etc). Defaults to 'leet-code'
        LINK (str): Link to the exercise. For example: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
        ID (int): Problem id.

    Returns: Path to my solution (can be used for commiting it to the repository).
    """
    # Automated file creation...
    SQL_FILE_NAME = LINK.split("/")[4].title()
    SQL_TITLE_NAME = SQL_FILE_NAME.replace("-", " ").title()
    SQL_FILE_NAME = str(ID) + "-" + SQL_FILE_NAME
    PATH = f"./{SOURCE}/{SQL_FILE_NAME}.sql"
    README_PATH = f"{SOURCE}/README.md" if SOURCE != "leet-code" else "README.md"

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
    my_solution_path = "./{SOURCE}/{SQL_FILE_NAME}.sql"
    with open(README_PATH, "a") as readme:
        readme.write(
            f"| {ID} |  {SQL_TITLE_NAME} | [Link]({LINK}) | [My solution]({my_solution_path}) |\n"
        )

    return my_solution_path, SQL_TITLE_NAME


def make_commit(
    sql_file_path: str,
    problem_id: int,
    problem_name: str,
    exercise_source: str = "Leet Code",
    readme_path: str = "README.md",
) -> None:
    """Uses GitPython library in order to automate commiting a SQL solution.

    Args:
        sql_file_path (str): Path to the .sql file with the exercise solution.
        problem_id (int): Id of the problem. Used in commit message.
        problem_name (str): Name of the problem. Used in commit message.
        exercise_source (str): Name of the page from which the exercise was taken (Leet Code, Hacker Rank etc). Defaults to 'Leet Code'
        readme_path (str, optional): Path to readme file. After solving a task there is a need to commit the README file as well because the table is updated. Defaults to 'README.md'.
    """
    # sql_repo = Repo(".")
    # print(sql_repo)


# TODO: Sort markdown table function

# Fill this out
SOURCE = "leet-code"  # Specify the site used (Hacker Rank or Leet Code)
LINK = r"https://leetcode.com/problems/duplicate-emails/"  # Input link to your problem
ID = 182  # ID of the problem (only for leet code problems)

sql_file_path, problem_name = handle_documentation(LINK=LINK, ID=ID, SOURCE=SOURCE)
# sql_file_path, problem_name = 'path', 'problem_name'
# make_commit(sql_file_path=sql_file_path,problem_id=ID, problem_name=problem_name, readme_path='README.md')
