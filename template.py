import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


while True:
    project_name = input("Enter the name of the project: ")
    if project_name != "":
        break


list_of_files =[

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
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory{filedir} for the filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating file name{filename}")

    else:
        logging.info(f"filename already exists")