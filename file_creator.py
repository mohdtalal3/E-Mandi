import os

# Define the directory structure
directories = [
    "project_folder",
    "project_folder/pages",
]

# Define the files to be created within the directories
files = {
    "project_folder/main.py": "",
    "project_folder/auth.py": "",
    "project_folder/database.py": "",
    "project_folder/pages/login.py": "",
    "project_folder/pages/signup.py": "",
    "project_folder/pages/dashboard.py": "",
    "project_folder/styles.py": "",
}

# Create directories if they don't exist
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create files with empty content
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)

print("Directory structure and files created successfully.")
