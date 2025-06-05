# Final Project Django - Online Course Platform

Este é um projeto Django para uma plataforma de cursos online, onde usuários podem se matricular em cursos, responder exames com perguntas e escolhas, e visualizar seus resultados.

---

## Funcionalidades

- Cadastro de cursos, perguntas, escolhas e matrículas via Django Admin.
- Página para exibir detalhes do curso com perguntas.
- Formulário para envio das respostas do exame.
- Página de resultado mostrando a pontuação e feedback.
- Controle de autenticação e matrícula de usuários.

---

## Tecnologias

- Python 3.13
- Django 5.2
- SQLite (banco de dados padrão)
- HTML e templates Django (com Bootstrap para estilo)

---

## Como rodar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/final_project_django.git
````

2. Crie e ative o ambiente virtual:

```bash
python -m venv djangoenv
source djangoenv/Scripts/activate  # Windows
source djangoenv/bin/activate      # Linux/Mac
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin:

```bash
python manage.py createsuperuser
```

6. Rode o servidor:

```bash
python manage.py runserver
```

7. Acesse o admin: `http://127.0.0.1:8000/admin/` para cadastrar cursos, perguntas, escolhas e usuários.

8. Acesse o site: `http://127.0.0.1:8000/onlinecourse/1/` para testar o exame.

---

## Estrutura do projeto

* `final_project_django/` - pasta do projeto Django.
* `onlinecourse/` - app principal com modelos, views, urls e templates.
* `db.sqlite3` - banco de dados SQLite.
* `manage.py` - script para comandos Django.

---

## Autor

Rhuan - [GitHub](https://github.com/RhuanLUX)

---

## Licença

Este projeto é open source, fique à vontade para usar e contribuir.
