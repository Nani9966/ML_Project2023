import os
                        
              

from pathlib import Path
import logging  
                                                        
 

while True:
    project_name = input("Enter you project name")
    if project_name !='':
        break

logging .basicConfig(  
    level=logging.INFO,
    format ="[%(asctime)s: %(levelname)s ] %(message)s"

)
list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
                                           
    f"{project_name}/utils/__init__.py",
    f"{project_name}/artifact/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
                       
    "setup.py",
    "main.py",
    "requirements.txt",
    "README.md"
 

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating new directory at :{filedir} for file : {filename} ")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w")as f:
            pass
            logging.info(f"creating new file at :{filename} for path : {filepath} ")

    else:
        logging.info(f"file is already present at : {filepath}")