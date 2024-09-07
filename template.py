import os
from pathlib import Path
import logging
from typing import List

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s:')

project_name = 'cnn-classifier'

list_of_files = [

"github/workflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/configuration.py",
"config/config.yaml",
"dvc.yaml",
"params.yaml",
"requirements.txt",
"setup.py",
"research/trails.ipynb"

]


for file in list_of_files:
    file_path = Path(file)
    filedir,filename=os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("creating directory:{filedir} for the file:{filename}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'creating empty file :{file_path}')
            
    else:
        logging.info(f'file already exists:{file_path}')



