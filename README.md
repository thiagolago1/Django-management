# Django-management

Criado a partir de aprendizados em curso.

Obs: é importante frizar que está em dev e é somente para aprender, muito provavelmente conterá erros (faz parte do percurso)

### Ambiente Virtual

Cria Ambiente virtual
`python3 -m venv env`

Ativa Ambiente virtual
`source env/bin/activate`

### Requirements

Instalação do requirements
`pip install -r requirements.txt`

Aplica as migrações do db
`./manage.py makemigrations`
depois
`./manage.py migrate`

cria um usuário para testar
`./manage.py createsuperuser`

### Servidor
Liga o servidor
`./manage.py runserver` 
