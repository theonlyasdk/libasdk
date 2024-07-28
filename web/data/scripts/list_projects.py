#!/usr/bin/env python3
import json, sys

project_file = sys.argv[1]
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
	demo_url = "None"
	
	if "demo_url" in project:
		demo_url = project["demo_url"]

	print("-----------------------")
	print(f"Name: {name}")
	print(f"Desc: {desc}")
	print(f"URL: {url}")
	print(f"Demo URL: {demo_url}")
	print(f"Tags: {tags}")
	print("-----------------------")

print("\nEnd.")
