"""Module to quickly access common commands used during development."""

import os

option = input(
    "What do you want to do? "
    + "Run flake8 (1), run formatting (2), or run a local server (3)? "
)
option = int(option)
if option == 1:
    os.system("python -m flake8 .")
elif option == 2:
    os.system(
        r"python -m black . && npx prettier **\*.css --write && npx prettier **\*.js --write"
    )
elif option == 3:
    os.system("python -m flask run")
