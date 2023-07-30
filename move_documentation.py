# List of exercises ---> Nice markdown table

import os

with open("leet-code\README.md", "a") as readme:
    with open("temp.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line[2:]
            problem_id, name_and_link = line.split(". ")
            problem_id = problem_id[1:]
            name_and_link = "[" + name_and_link
            link = name_and_link[name_and_link.find("(") + 1 : name_and_link.find(")")]
            name = name_and_link[name_and_link.find("[") + 1 : name_and_link.find("]")]
            print(problem_id)
            my_solution_link = f"./leet-code/{problem_id}.{name.replace(' ', '-')}.sql"
            print(my_solution_link)
            readme.write(
                f"| {problem_id} | {name} | [Link]({link}) |  [My solution]({my_solution_link}) |\n"
            )
