import nicegui
from pathlib import Path, PurePosixPath
import subprocess
import os

mainfile_path = str(PurePosixPath(Path(os.getcwd()))) + "/src/main.py"
nicegui_path = str(PurePosixPath(Path(nicegui.__file__).parent)) 
guidir_path = str(PurePosixPath(Path(os.getcwd()))) + "/src/gui"
aidir_path = str(PurePosixPath(Path(os.getcwd()))) + "/src/ai"

print(nicegui_path)
print(mainfile_path)
print(aidir_path)
print(guidir_path)

cmd = f'python -m  PyInstaller "{mainfile_path}" --name "Capitanul Pitonescu" --noconsole --add-data "{guidir_path}:gui" --add-data "{nicegui_path}:nicegui" --add-data "{aidir_path}:ai"'

subprocess.call(cmd)
