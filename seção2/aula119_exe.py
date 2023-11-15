# User options: add task, list, undo, redo
# Needed things
import os
import json

# Function to add a task
def add_task(task, given_list=None):
        if given_list == None:
            given_list = main_list
        given_list.append(task)
        return given_list

# Function to read a json file.
def ler(main_list, path_file):
    dados = []
    try:
        with open(path_file, 'r', encoding='utf8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(main_list, path_file)
    return dados

# Function to create a json file and save strings on it.
def salvar(main_list, path_file):
    dados = main_list
    with open(path_file, 'w', encoding='utf8') as file:
            dados = json.dump(main_list, file, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula119.json'
main_list = ler([], CAMINHO_ARQUIVO)
backup_list = []

while True:
  
    user_input = input('Please, add a task or choose an option below. \n List - Undo - Redo : ')

        # List all the tasks.
    if user_input == 'list':
        print('Tasks on the list: ')
        print(*main_list, sep='\n')

        # Undo last input.
    elif user_input == 'undo': 
        backup_list.append(main_list[last_index_main])
        del main_list[last_index_main]

        # Redo last change.
    elif user_input == 'redo':
        main_list.append(backup_list[last_index_backup])
        del backup_list[last_index_backup]
        
    elif user_input == 'clear':
         os.system('cls')

        # Add a task to the list.
    else:
        add_task(user_input, main_list)

    salvar(main_list, CAMINHO_ARQUIVO )
    last_index_main = len(main_list) - 1
    last_index_backup = len(backup_list) - 1



        






















