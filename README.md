Deploy

Objetivo - Como realizar o Run Server em sua Maquina Local e deixar o programa pronto para o desenvolvimento.
Roteiro para rodar o Programa em Maquina Local usando Ubuntu.

Este programa devera obrigatoriamente usar:
-> python3.8 com todas as libs de desenvolvimento pre instaladas.
-> sqlite3( ou reconfigurar para um db que preferir)
-> docker(>=5) e docker-compose(>=1.25)


Primeiro Passo - O Repositorio

PS1: Considerar utilizando direitamente via git, pois caso utilize via docker, haverá mudanças nos comandos, 
consulte os comandas para a sua OS, no geral costumam ser acrecidos de docker-compose

Clonar o repositorio:
1-git clone https://github.com/victorbrittoferreira/DRF_API_test

Proximo Passo - venv
Paralelo ao diretorio clonado, cria um ambiente virtual Python3.8 via terminal:
1-Python3.8.10 -m venv env
Ative o respectivo ambiente via terminal:
2-source env/bin/activate
Instale as dependencias contidas no arquivo requirements.txt no ambiente virtual criado via terminal:
3-pip3.8 install -r /requirements.txt

Proximo Passo - Criando Super Usuario e entrando na Tela de Administração do Django e DRF.
1- Digite na CLI: python manage.py createsuperuser.
2 - Preencha todos os campos solicitados.

Proximo Passo - realizando as migrações na Banco de Dados.
1-Dentro da pasta "./igs_api/" digite no terminal: python manage.py makemigrations
2- Depois ....: python manage.py migrate.

Proximo Passo - rodando o app no servidor local.
1-Dentro da pasta "./igs_api/" digite no terminal: python manage.py runserver

Proximo Passo - abrindo a tela de administração do Django.
1- Login como super usuario no seguinte endereço:  "/admin/".


PS2: Todos os links da APIs, exceto a função que lista os empregados, demandam de colocar o id do funcionário no final da url:
EG: localhost:8000/api/delete-employee/4     <<<indicar

