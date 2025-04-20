# Projeto Full Stack com Front-end em Python e Back-end em Java

## Descrição do Projeto

Este projeto é composto por um **front-end** desenvolvido em Python utilizando o framework **Streamlit** e outras bibliotecas auxiliares, e um **back-end** implementado em Java com **Spring Boot**, utilizando o banco de dados **SQLite** e outras dependências.

### Front-end
- Desenvolvido com **Streamlit**, uma biblioteca Python para criação de interfaces web interativas.
- O front-end é executado na porta **8501**.
- Possui um arquivo `Dockerfile` para facilitar a criação de imagens Docker.

### Back-end
- Construído com **Spring Boot**, um framework Java para desenvolvimento de aplicações web robustas.
- Utiliza **SQLite** como banco de dados para persistência de dados.
- O back-end é executado na porta **8080**.
- Também possui um arquivo `Dockerfile` para a criação de imagens Docker.

## Docker e Docker Compose

O projeto utiliza **Docker Compose** para orquestrar os serviços do front-end e do back-end. O arquivo `docker-compose.yml` define os dois serviços principais:

- **front-end**: Responsável por executar a aplicação Streamlit.
- **back-end**: Responsável por executar a aplicação Spring Boot.

### Estrutura do `docker-compose.yml`

- Cada serviço é baseado em sua respectiva imagem Docker, gerada a partir dos arquivos `Dockerfile`.
- As portas são mapeadas para permitir o acesso externo:
  - Porta **8501** para o front-end.
  - Porta **8080** para o back-end.

### Como Executar o Projeto

1. Certifique-se de ter o **Docker** e o **Docker Compose** instalados.
2. No diretório raiz do projeto, execute o comando:
   ```bash
   docker compose up
3. Acesse os serviços:
- Front-end: http://localhost:8501
- Back-end: http://localhost:8080
# Estrutura do Projeto

    ├── front-end/
    │   ├── Dockerfile
    │   └── main.py
    ├── back-end/
    │   ├── Dockerfile
    │   └── src/
    │       └── main/
    │           └── java/
    │               └── edu/
    │                   └── redesII/
    │                       └── monitoramentotrafego
    │                           └── MonitoramentoTrafegoApplication.java
    └── docker-compose.yml

# Tecnologias Utilizadas
- **Python** com Streamlit (front-end)
- **Java** com Spring Boot (back-end)
- **SQLite** como banco de dados
- **Docker** e **Docker Compose** para containerização