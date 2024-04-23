# Inteli módulo 10 ponderada 1

_Instruções_

```
Pessoal nossa atividade ponderada vai ser desenvolvida em diversas frentes e por partes. A primeira parte vai ser a construção da API. Existe aqui um único pré-requisito, ela precisa ser SINCRONA!!!. Mais sobre esse ponto no nosso próximo encontro.

O que vocês devem entregar, em um repositório do Github (até as 23h59 de hoje, dia 21/04/2024 - pessoal nesse ponto eu não vou ser flexível na entrega, pois o objetivo é que vocês consigam desenvolver em sala e entrega extendida é só para contemplar quem não conseguiu terminar em sala):

Collections do Insomnia para testar a API
YAML do OpenAPI (Swagger) para documentar a API
Código fonte da API
Instruções para executar a API
Obrigatóriamente ela deve ser uma API de grau de maturidade 2, ou seja, ela deve ser capaz de fazer a autenticação do usuário e permitir que ele crie, leia, atualize e delete tarefas. Você podem utilizar o código fornecido como base.

```

## API de Gerenciamento de Tarefas

Esta é uma API Flask desenvolvida para gerenciar tarefas com autenticação de usuários e controle de uma to-do list.

> [!IMPORTANT]
> A to-do list está sendo administrada em memória! Ou seja, ao reiniciar a aplicação, todos os dados serão perdidos.

## Instalação

> [!NOTE]
> Antes de iniciar, você precisará ter o Python, Git, Docker e docker-compose instalado em sua máquina.

Primeiro, clone este repositório e entre na pasta do projeto:

```bash
git clone https://github.com/Lemos1347/inteli-modulo-10-ponderada-1.git ; cd inteli-modulo-10-ponderada-1/src/backend-sync
```

Para rodar esta aplicação, você precisa instalar as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

É necessário também rodar um banco de dados postgresql. Para isso, você pode navegar até a pasta [build](./build) e rodar o seguinte comando:

```bash
docker-compose up --build
```

E por fim, crie um arquivo `.env` na root da pasta [src/backend-sync](.) com as seguintes variáveis de ambiente (você pode encontrar um exemplo em [.env.template](./src/backend-sync/.env.template)):

```env
DATABASE_URL={your_database_url}
```

## Executando a API

Para iniciar a API, rode o seguinte comando na root desse repositório:

```bash
python main.py
```

Agora você pode acessar a API em [http://localhost:3001](http://localhost:3001).

## Documentação da API

Após iniciar a API, você pode acessar a documentação da API via Swagger UI pelo seguinte URL: [http://localhost:3001/docs](http://localhost:3001/docs).

Acesse este link para interagir com a API através da interface Swagger, onde você pode testar os endpoints diretamente.

Você pode encontrar a documentação da API em OpenAPI (Swagger) no arquivo [swagger.yaml](./static/swagger.yml).

Caso você prefira, você pode importar o arquivo [Insomnia_collection.json](./static/Insomnia_collection.json) no Insomnia para testar a API.

## Endpoints

> [!NOTE]
> Caso você tenha rodado o docker-compose, já existe um usário cadastrado no banco de dados com o id: 03fd5486-2030-47cf-bf14-0e569d64fad9c com o role de 'admin'

A API consiste nos seguintes endpoints:

- `POST /create_user`: Cria um novo usuário (acesso restrito a administradores).
- `POST /create_task`: Permite a um usuário autenticado criar uma nova tarefa.
- `GET /tasks`: Retorna todas as tarefas do usuário autenticado.
- `PUT /update_task`: Atualiza o status de uma tarefa específica.
- `DELETE /delete_task`: Remove uma tarefa específica.

Cada endpoint requer que o usuário esteja autenticado e passe o seu id no header 'Authorization'. Alguns endpoints exigem que o usuário seja um administrador (nesse caso, apenas `/create_user`).