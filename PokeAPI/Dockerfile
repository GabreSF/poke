# Use a imagem base do Python
FROM python:3.11

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Exponha a porta em que o servidor do Django estará executando
EXPOSE 8000

# Comando para iniciar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
