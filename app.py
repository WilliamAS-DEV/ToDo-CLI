# 1. Importar as bibliotecas necessarias
import json
import argparse
import os

# 2. Abrir o arquivo de tarefas; Se não existe, crie ele
if not os.path.exists('./src/'):
    os.makedirs('./src/')
    with open('./src/tasks.json', 'w') as f:
        json.dump([], f, indent=4)
elif not os.path.exists("./src/tasks.json"):
    with open('./src/tasks.json', 'w') as f:
        json.dump([], f, indent=4)
else:
    pass

with open('./src/tasks.json', 'r') as f:
    tasks = json.load(f)
    
# 3. Classes e Funções
class ToDo:
    def list():
        print("ID     Name     Date")
        for i in tasks["tasks"]:
            print(f"{i}    {i['name']}    {i['dh']}")
# 4. Configurar o argparse

print(tasks)