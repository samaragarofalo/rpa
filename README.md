# RPA
Desafio: Desenvolvimento de um Robô de Automação de Processos (RPA) para extração de dados.

Este repositório contém um projeto de RPA para realizar scraping de jurisprudências no site do Tribunal de Contas do Estado de São Paulo.

Como Funciona?

O projeto utiliza Selenium para automatizar buscas no site e extrair informações relevantes. Os dados coletados são salvos em um banco de dados MongoDB e também exportados para um arquivo JSON.

Fluxo do Projeto

O script principal (main.py) inicia a busca de jurisprudências com palavras-chave definidas.

O SeleniumScraper acessa o site e coleta os dados.

Os resultados são salvos em um arquivo JSON.

Os dados também são armazenados no MongoDB.

Como Rodar o Projeto

1. Clonar o Repositório

git clone https://github.com/samaragarofalo/rpa.git
cd RPA

2. Configurar o Ambiente

Certifique-se de ter o Python 3.13 instalado e crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Instale as dependências:

pip install -r requirements.txt

3. Executar o Projeto

Localmente:

Configure a URI do MongoDB (caso tenha um banco rodando localmente):

export MONGO_URI=mongodb://localhost:27017/

Rode o script principal:

python -m rpa.app.main

Com Docker:

Construa e inicie os containers:

docker-compose up --build

Isso iniciará tanto o scraper quanto o MongoDB.

Testes

Para rodar os testes:

python -m unittest discover -s rpa/tests

Estrutura do Projeto

rpa/
│── app/
│   ├── main.py  # Script principal
│   ├── application/
│   │   ├── scraping_service.py  # Serviço de scraping
│   │   ├── infra/
│   │   │   ├── scraper.py  # Scraper Selenium
│   │   │   ├── db.py  # Interação com MongoDB
│   │   │   ├── file_writer.py  # Exporta dados para JSON
│   │   │   ├── settings.py  # Configuração do MongoDB
│── tests/
│   ├── test_query_results.py  # Testes do banco
│   ├── test_db.py  # Teste de conexão com MongoDB
│── Dockerfile
│── docker-compose.yml
│── requirements.txt

Considerações Finais

Caso tenha problemas ao rodar o projeto, verifique se o MongoDB está ativo e se as dependências estão corretamente instaladas.

Happy coding! 🚀
