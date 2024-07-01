#!/usr/bin/env python3
import json

project_file = "projects.json"
data = []

with open(project_file, "r") as file:
    data = json.load(file)
    print(f"Data loaded from {project_file}.")
    print(f"Total {len(data)} items in list (before adding).")

name = input("Project name: ")
desc = input("Project description: ")
url = input("Project URL: ")
tags = input("Tags: ")

data.append({
    "name": name,
    "description": desc,
    "url": url,
    "tags": tags,
})

with open(project_file, "w") as file:
    json.dump(data, file, indent=2)
    print(f"Data written to {project_file}.")
    print(f"Total {len(data)} items in list (after adding).")
