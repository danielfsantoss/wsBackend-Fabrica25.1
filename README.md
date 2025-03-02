# Introdução

API Rest para criar reviews de filmes usando consultas da API OMDb

## Requisitos

### Requisitos Obrigatórios

- Python: 3.13.1

### Requisitos Recomendados

- Docker: 27.3.1
- Docker-compose: 2.32.4

## Instalação

1. Execute:
```shell
git clone https://github.com/danielfsantoss/wsBackend-Fabrica25.1.git
```
2. Em seguida execute:
```shell
docker-compose up --build
```
3. A aplicação estará em execução no endereço: `localhost:8000`

## Rotas

__(Em funcionamento até o momento):__

* POST `/users/user/create-user/`
Cria um usuário usando **nome** e **email**:
```JSON
{
  "username": "usuario",
  "email": "usuario@example.com",
}
```
**OBS:** As demais rotas estarão disponíveis em breve. Infelizmente não tinha experiência com Django e enfrentei muitos problemas em relação à infra kkkkk, de qualquer forma, consegui desenrolar mais coisas, porém poucos minutos após o prazo de entrega. Consulta a branch "fora-do-prazo" para mais detalhes.
