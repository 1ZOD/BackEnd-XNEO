# BackEnd-XNEO


## 1° Passo

Fora do projeto criar a venv

```sh
python -m venv venv
```

```sh
./venv/Scripts/activate.bat
```

## 2° Passo

```sh
cd BackEnd
```
```sh
pip install -r requirements.txt
```

## 3° Passo

```sh
python main.py
```

## 4° Passo

Voce deve criar um arquivo ✨.env✨ fora do projeto para adicionar as variaveis de ambiente do banco.

Exemplo:

```sh
BD_HOST=localhost
BD_USER=root
BD_PASSWORD=admin
BD_TABLE=Tarefas
```

Mude apenas o necessario como por exemplo "root"


## 5° Passo

Criar o banco

```sh
create database Tarefas
```

```sh
create table tasks(
id_task int not null AUTO_INCREMENT,
task_content varchar(30) not null,
PRIMARY KEY(id_task)
)default charset = utf8
```
