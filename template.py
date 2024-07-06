import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


while True:
    project_name = input("Enter the name of the project: ")
    if project_name != "":
        break


list_of_files =[
".github/workflows/.gitkeep",
f"{project_name}/__init__.py",

f"{project_name}/components/__init__.py",
f"{project_name}/components/data_ingestion.py",
f"{project_name}/components/data_transformation.py",
f"{project_name}/components/model_trainer.py",
f"{project_name}/components/model_monitoring.py",

f"{project_name}/pipelines/__init__.py",
f"{project_name}/pipelines/training_pipeline.py.",
f"{project_name}/pipelines/prediction_pipeline.py",

f"{project_name}/exception.py",
f"{project_name}/logger.py",
f"{project_name}/utils.py",

'main.py',
'app.py',
'DockerFile',
'requirements.txt',
'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)            #backslash(\) is used in Windows, "Path" helps to resolve this conflict
    filedir, filename = os.path.split(filepath)

    #Split the path name into a pair head & tail. exmple-->"{project_name}/logger/__init__.py"  --> tail = {project_name}/logger/ , head = __init__.py
    #below if statement to create folders

    if filedir !="":
        #os.mkdir()  : only creates the last folder in the path. Intermediate folders must already exist.
        #os.makedirs() : To create an entire folder structure(folders & file)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory{filedir} for the filename {filename}")

    #below if statement to create files
    #Unlike open() where you have to close the file with the close() method, the with statement closes the file for you without you telling it to.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:    
            pass
        logging.info(f"Creating file name{filename}")

    else:
        logging.info(f"filename already exists")