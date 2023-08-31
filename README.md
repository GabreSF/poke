# Poke - PokeAPI

O projeto Poke é um sistema onde é feito para puxar dados de uma API (https://pokeapi.co)

## Instalação

1. Clone este repositório: `git clone https://github.com/GabreSF/poke.git`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` ou `venv\Scripts\activate` no Windows
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o banco de dados: `python manage.py migrate`

## Uso

1. Execute o servidor de desenvolvimento: `python manage.py runserver`
2. Acesse o aplicativo em: `http://127.0.0.1:8000`

## Funcionalidades

- Visualizar os 150 pokemons
- visualizar nome e tipo do pokemon
- selecionar os pokemons pelos seus tipos (Fogo, água, gelo e etc)

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adiciona nova feature'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
