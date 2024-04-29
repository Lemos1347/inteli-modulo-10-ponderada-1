# Inteli módulo 10 ponderada 1

Esse repositório contém os códigos desenvolvidos para a atividade ponderada 1 do módulo 10 do Inteli.

> [!NOTE]
> Enunciado da atividade: Construção de uma API síncrona para o gerenciamento de `tasks` de maturidade 2, ou seja, capaz de autenticar um usuário, criar, listar, atualizar e deletar `tasks`.

Todos os códigos podem ser encontrados na pasta [src](./src). A pasta do [backend](./src/backend-sync/) tem o seu próprio `README.md` detalhando a construção da API.

_Obs1.: dentro da pasta [src](./src) há um [docker-compose.yml](./src/docker-compose.yml) que lançará os conteiners necessários para todas as partes, o único pré-requisito para rodá-lo é a necessidade de adicionar um arquivo `.env` dentro da pasta `src`. Após isso, basta apenas entrar na pasta `src` e rodar o comando: `docker-compose up --build`. As intruções de cada parte pode ser encontrada na sua respectiva pasta._

_Obs2.: consulte o [arquivo de documentação da API](./src/backend-sync/README.md) caso você não encontre qualquer arquivo que estava procurando (e.g.: openapi.yaml, insomnia.json, etc)._

## Como rodar

> [!IMPORTANT]
> Para rodar o projeto é necessário ter o `git`, `docker` e o `docker-compose` instalados na máquina.

Primeiro você deve clonar o repositório:

```bash
git clone https://github.com/Lemos1347/inteli-modulo-10-ponderada-1.git
```

Depois, entre na pasta `src` do projeto:

```bash
cd inteli-modulo-10-ponderada-1/src
```

Crie um arquivo `.env` com as seguintes variáveis:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:3002/Ponderada1M10
```

Por fim, rode o comando:

```bash
docker-compose up --build
```

Pronto! Agora você pode acessar o projeto em [http://localhost:3001/docs](http://localhost:3001/docs).

## Funcionamento

https://github.com/Lemos1347/inteli-modulo-10-ponderada-1/assets/99190347/62431ae8-0c89-49b6-a99c-fa269ef0844e

## Conclusão

Em resumo, as chamadas exibidas no vídeo destacam a rapidez de execução, uma vez que cada operação foi realizada individualmente. Se houvesse múltiplas chamadas ocorrendo ao mesmo tempo, a duração poderia dobrar para a segunda chamada, devido à falta de recursos assíncronos na API.
