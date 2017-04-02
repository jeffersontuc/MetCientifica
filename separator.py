# coding: utf-8

import random
import os

def remove(path):
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.", format(path))

def separar_dados():
    file = open("task_events.csv")
    linhas = file.readlines()

    tasks_02 = []
    tasks_1 = []
    tasks_4 = []
    
    #remove("log_result.txt")


    for i in range(1, len(linhas)):
        linha = linhas[i].strip().split(";")
        if float(linha[8]) <= 0.02:
            tasks_02.append(linhas[i].strip())
        elif float(linha[8]) <= 0.1:
            tasks_1.append(linhas[i].strip())
        else:
            tasks_4.append(linhas[i].strip())

    random.shuffle(tasks_02)
    random.shuffle(tasks_1)
    random.shuffle(tasks_4)

    task_02 = ""
    task_1 = ""
    task_4 = ""

    menor = min([len(tasks_02), len(tasks_1), len(tasks_4)])

    for i in range(menor):
        task_02 += tasks_02[i] + "\n"
        task_1 += tasks_1[i] + "\n"
        task_4 += tasks_4[i] + "\n"

    arquivo = open("task_02.csv", 'w')
    arquivo.writelines(task_02.strip())
    arquivo.close()

    arquivo = open("task_01.csv", 'w')
    arquivo.writelines(task_1.strip())
    arquivo.close()

    arquivo = open("task_04.csv", 'w')
    arquivo.writelines(task_4.strip())
    arquivo.close()

separar_dados()