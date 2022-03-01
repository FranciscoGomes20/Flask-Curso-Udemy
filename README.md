# Flask-Curso-Udemy
 Desenvolvimento WEB com Python e Flask - Curso realizado na plataforma udemy.

## Pré-Requisitos

Deve possuir o Python na versão 3.9 instalado na máquina (preferencialmente a versão 3.9.8)

## Instalação

Inicie um ambiente virtual

```python
python -m venv venv
```

Após isso, acesse a pasta do ambiente pelo terminal e ative o arquivo "activate.bat"

```bash
venv\Scripts\activate
```

## Instalando dependências do projeto

Use o gerenciador de pacotes do python para baixar as as bibliotecas necessárias do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Criando o repositório de migração

Então, vamos criar o repositório de migração para o sistema executando o comando abaixo.

```bash
python run.py db init
```

## A primeira migração do banco de dados

Com esse comando o flask gera essas migrações automáticamente.

```bash
python run.py db migrate
```

## Upgrade no Banco de Dados

Para aplicar as alterações ao banco de dados, execute o comando abaixo.

```bash
python run.py db upgrade
```

## Inicialização do servidor

Execute o comando abaixo para iniciar o servidor.

```bash
python run.py runserver
```
