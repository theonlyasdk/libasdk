#!/usr/bin/env python3
import json

project_file = "projects.json"
data = []

with open(project_file, "r") as file:
    data = json.load(file)
    print(f"Data loaded from {project_file}.")

print(f"Total {len(data)} items.")
print("Listing data...")

for project in data:
	name = project["name"]
	desc = project["description"]
	url = project["url"]
	tags = project["tags"]

	print("-----------------------")
	print(f"Name: {name}")
	print(f"Desc: {desc}")
	print(f"URL: {url}")
	print(f"Tags: {tags}")
	print("-----------------------")

print("\nEnd.")