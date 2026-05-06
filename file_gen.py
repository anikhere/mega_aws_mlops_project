from pathlib import Path
project_dir = 'MLOPS'
project = Path(project_dir)
folders = [
    project / 'components',
    project / 'config',
    project / 'constants',
    project / 'yaml_folder'
]
component_files = [
    "data_ingestion.py",
    "data_validation.py",
    "data_transformation.py",
    "model_trainer.py",
    "model_evaluation.py"
]

for folder in folders:
    folder.mkdir(parents= True,exist_ok=True)
    print(f'created the {folder}')

for file in component_files:
    file_path = project / 'components' / file
    file_path.touch(exist_ok=True)
    print(f'created the {file} at the path {file_path}')


