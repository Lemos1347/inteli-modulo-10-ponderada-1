# Inteli módulo 10 ponderada 1

Esse repositório contém os códigos desenvolvidos para a atividade ponderada 1 do módulo 10 do Inteli.

> [!NOTE]
> Enunciado da atividade: Construção de uma API síncrona e outra asíncrona para o gerenciamento de `tasks` de maturidade 2, ou seja, capaz de autenticar um usuário, criar, listar, atualizar e deletar `tasks`.

Todos os códigos podem ser encontrados na pasta [src](./src). Dentro dela pode ser encontrado duas pastas: [backend-sync](./src/backend-sync/) e [backend-async](./src/backend-async/), as quais ambas tem o seu próprio `README.md` detalhando a construção da API.

_Obs1.: dentro da pasta [src](./src) há um [docker-compose.yml](./src/docker-compose.yml) que lançará os conteiners necessários para todas as partes (incluindo o banco de dados, o qual as suas tabelas podem ser encontradas em [/database](./src/database/)), o único pré-requisito para rodá-lo é a necessidade de adicionar um arquivo `.env` dentro da pasta `src`. Após isso, basta apenas entrar na pasta `src` e rodar o comando: `docker-compose up --build`. As intruções de cada parte pode ser encontrada na sua respectiva pasta._

_Obs2.: você pode consultar ambos os arquivos de documentação de cada backend caso você não encontre qualquer arquivo que estava procurando (e.g.: openapi.yaml, insomnia.json, etc) -- [arquivo de documentação da API sync](./src/backend-sync/README.md) [arquivo de documentação da API async](./src/backend-async/README.md)_

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

Pronto! Agora você pode acessar os seguintes endpoints:

- [API sync](http://localhost:3000/docs).
- [API async](http://localhost:3001/docs).

## Funcionamento

Você pode encontrar um vídeo demonstrando o funcionamento de cada API em suas respectivas documentações:

- [API sync](./src/backend-sync/README.md).
- [API async](./src/backend-async/README.md).

## Comparação

## Conclusão

Com base na análise realizada sobre o desempenho das APIs síncrona e assíncrona, é possível concluir que cada abordagem possui características distintas que influenciam diretamente a eficiência em diferentes cenários de uso. A API síncrona, operando com uma única thread, mostra-se eficaz para operações isoladas, apresentando um tempo de execução comparável ao da API assíncrona em chamadas individuais. Contudo, seu desempenho é significativamente limitado sob condições de múltiplas solicitações simultâneas, devido à sua incapacidade de processar chamadas concorrentemente.  

Por outro lado, a API assíncrona demonstra uma vantagem notável nesses cenários, graças à sua habilidade de gerenciar chamadas de forma concorrente. Isso não apenas reduz o tempo de espera para o processamento de cada chamada, mas também melhora a eficácia geral do sistema em condições de alta demanda.
