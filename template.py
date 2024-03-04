from pathlib import Path
import logging
import os

project_name = 'TEXT_SUMMARIZATION_NLP'

logging.basicConfig(level=logging.INFO,  format='%(asctime)s - %(message)s')
# Set up project directory

file_names = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params/param.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in file_names:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Make directories {filedir} successfully.")
    
    if  not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("")
            logging.info(f"Create empty file {filename}.")
    else:
        logging.info(f"File {filename} already exists.")
        