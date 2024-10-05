# Explicação do Código Docker e Redis

Este documento explica detalhadamente cada linha do código fornecido, que utiliza Docker para gerenciar instâncias do Redis e realiza operações básicas com o cliente `redis-cli`.

```bash
docker pull redis
```
- **docker pull redis**: Este comando baixa a imagem mais recente do Redis do [Docker Hub](https://hub.docker.com/_/redis). É necessário fazer o pull da imagem antes de criar contêineres a partir dela.

```bash
docker create --name redis-instance-1 -p 6380:6379 redis
```
- **docker create**: Cria um novo contêiner a partir de uma imagem, mas não inicia o contêiner imediatamente.
- **--name redis-instance-1**: Nomeia o contêiner como `redis-instance-1` para facilitar a referência futura.
- **-p 6380:6379**: Mapeia a porta 6379 do contêiner (porta padrão do Redis) para a porta 6380 na máquina host. Isso permite acessar o Redis na porta 6380 do host.
- **redis**: Especifica a imagem do Docker a ser usada para criar o contêiner, neste caso, a imagem do Redis baixada anteriormente.

```bash
docker start redis-instance-1
```
- **docker start redis-instance-1**: Inicia o contêiner chamado `redis-instance-1` que foi criado anteriormente. Após este comando, o Redis estará rodando e acessível na porta 6380 do host.

```bash
redis-cli -p 6380 set foo "bar"
```
- **redis-cli**: Ferramenta de linha de comando para interagir com o servidor Redis.
- **-p 6380**: Especifica que o comando deve ser enviado para a porta 6380, onde a instância `redis-instance-1` está escutando.
- **set foo "bar"**: Comando Redis para definir a chave `foo` com o valor `"bar"`. Este comando armazena o par chave-valor no banco de dados Redis.

```bash
redis-cli -p 6380 get foo
```
- **redis-cli -p 6380**: Invoca o cliente Redis para se conectar à instância na porta 6380.
- **get foo**: Recupera o valor associado à chave `foo`. Espera-se que retorne `"bar"` se o comando anterior foi bem-sucedido.

```bash
docker run --name redis-instance-2 -p 6379:6379 -d redis
```
- **docker run**: Cria e inicia imediatamente um novo contêiner a partir da imagem especificada.
- **--name redis-instance-2**: Nomeia o contêiner como `redis-instance-2`.
- **-p 6379:6379**: Mapeia a porta 6379 do contêiner para a porta 6379 do host. Esta é a porta padrão do Redis.
- **-d**: Executa o contêiner em modo "detached", ou seja, em segundo plano.
- **redis**: Especifica a imagem do Docker a ser usada para criar o contêiner.

```bash
redis-cli -p 6379 get "foo"
```
- **redis-cli -p 6379**: Conecta-se ao Redis na porta 6379, onde a instância `redis-instance-2` está rodando.
- **get "foo"**: Tenta recuperar o valor da chave `foo` na segunda instância do Redis. Como esta é uma nova instância sem dados compartilhados, retornará `(nil)` ou uma resposta indicando que a chave não existe.

## Resumo das Operações

1. **Baixar a imagem do Redis**: Garante que a imagem necessária esteja disponível localmente.
2. **Criar e iniciar `redis-instance-1`**: Configura uma instância do Redis mapeada para a porta 6380 do host.
3. **Definir e obter uma chave na `redis-instance-1`**: Realiza operações básicas de armazenamento e recuperação de dados.
4. **Executar `redis-instance-2`**: Inicia uma segunda instância do Redis na porta padrão 6379.
5. **Tentar obter uma chave na `redis-instance-2`**: Demonstra que as instâncias são independentes, já que a chave definida na primeira não está presente na segunda.

Este conjunto de comandos é útil para testar múltiplas instâncias do Redis em uma única máquina host, bem como para entender como as portas são mapeadas e como os dados são isolados entre diferentes contêineres.
