# 1. Importar as bibliotecas necessarias
import json
import argparse
import os
import datetime as dt

# 2. Abrir o arquivo de tarefas; Se não existe, crie ele
if not os.path.exists('./src/'):
    os.makedirs('./src/')
elif not os.path.exists("./src/tasks.json"):
    with open('./src/tasks.json', 'w') as f:
        json.dump({"tasks":{}}, f, indent=4)
else:
    with open('./src/tasks.json', 'r') as f:
        tasks = json.load(f)

# 3. Classes e Funções
class ToDo:
    @staticmethod
    def list():
        print("ID     Name     Date")
        for i in tasks["tasks"]:
            print(f"{i}    {i['name']}    {i['dh']}")
    
    @staticmethod
    def add(name):
        ids = len(tasks["tasks"])
        if ids < 10:
            id = f"0{ids+1}"
        else:
            id = ids+1
        dh = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
        tasks[id] = {
            "name": name,
            "datetime": dh,
        }
# 4. Configurar o argparse

ToDo.add(name="Buy a Gift")
ToDo.list()