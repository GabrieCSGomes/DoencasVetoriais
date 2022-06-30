# DoencasVetoriais
Projeto referente a disciplina Laboratório de Engenharia de Sofware, do curso de Sistemas de Informação da Universidade Federal do Pará (2022.2)

### Introdução
Sistema para cadastro de visitas de agentes de saúde a domicílio, sobretudo nas verificações de doencas vetoriais.

### Instruções de execução
Para executar o código localmente, é necessário:
- (Opcional) Criar e ativar um ambiente virtual python
    > `python -m venv .venv`
- Instalar as dependências contidas em 'requirements.txt'
    > `pip install -r requirements.txt`
- Executar o código
    > `python manage.py runserver`

### Ferramentas Utilizadas [^used]
```
python          == 3.10.4
django          == 3.1.14
gunicorn        == 19.9.0
whitenoise      == 5.1.0
heroku          == 7.60.2
environs        == 8.0.0
psycopg2        == 2.8.5 
```

<sub>Feito por: Equipe 3[^equipe]</sub>

[^equipe]: Squad 3: Elane Garcia, Gabriel Gomes, Manoel Neto
[^used]: [Django Docs](https://docs.djangoproject.com/en/3.1/), [Django for Beginners - William S. Vicent](https://djangoforbeginners.com/), etc.