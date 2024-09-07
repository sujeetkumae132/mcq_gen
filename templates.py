import os
from pathlib import Path

project_name="genai_implementation"

file_list=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/common.py",
    "experiments/mcq.ipynb",
    "setup.py",
    
]

for path_name in file_list:
    path=Path(path_name)
    filedir,filename=os.path.split(path)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        
    if not os.path.exists(path_name):
        with open(filename,'w') as b:
            pass