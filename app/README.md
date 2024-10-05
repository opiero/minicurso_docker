# Instruções

## Construção de imagem
Para contruir esta imagem, rode:
```bash
[sudo] docker build --tag very-simple-server .
```
Conforme o texto entre conchetes acima, talvez seja necessário adicionar um `sudo` antes para rodar como super usuário
### Explicação dos componentes:

- **`sudo`**: Executa o comando com privilégios de superusuário. É necessário quando o usuário não tem permissões suficientes para executar comandos do Docker.

- **`docker build`**: Comando que constrói uma imagem Docker a partir de um `Dockerfile`.

- **`--tag very-simple-server`**: O parâmetro `--tag` (ou `-t` de forma abreviada) permite nomear e etiquetar a imagem que será construída. Nesse caso, a imagem será chamada de `very-simple-server`.

- **`.`**: Este ponto representa o diretório atual onde está localizado o `Dockerfile`. O Docker irá procurar pelo `Dockerfile` neste diretório para construir a imagem.

### Exemplo de fluxo:
1. O Docker busca o `Dockerfile` no diretório atual (`.`).
2. A imagem é construída usando as instruções do `Dockerfile`.
3. A imagem gerada é nomeada como `very-simple-server`.

## Criação e execução do container
Para criar e executar o container, rode:
```bash
docker run -d -p 5000:5000 --name very-simple-server-container very-simple-server
```
### Explicação dos componentes:

- **`docker run`**: Comando para rodar um contêiner baseado em uma imagem Docker.

- **`-d`**: A flag `-d` (modo detached) faz com que o contêiner seja executado em segundo plano, permitindo que o terminal fique disponível para outros comandos.

- **`-p 5000:5000`**: Mapeia uma porta do contêiner para uma porta no host. Neste caso:
  - A primeira `5000` é a porta do host (máquina local).
  - A segunda `5000` é a porta exposta no contêiner.
  Esse mapeamento permite acessar o serviço que está rodando no contêiner (na porta `5000`) através da porta `5000` do host.

- **`--name very-simple-server-container`**: A flag `--name` especifica um nome para o contêiner. Neste caso, o contêiner será chamado de `very-simple-server-container`. Isso facilita a identificação do contêiner em operações subsequentes.

- **`very-simple-server`**: Este é o nome da imagem Docker que será usada para criar o contêiner. No caso, a imagem foi previamente construída com o nome `very-simple-server` no comando `docker build`.

### Exemplo de fluxo:
1. O Docker procura pela imagem `very-simple-server` localmente.
2. Se a imagem existir, um contêiner será criado e iniciado com base nessa imagem.
3. O contêiner será executado em segundo plano (`-d`) e a porta `5000` do contêiner será mapeada para a porta `5000` do host (`-p 5000:5000`).
4. O contêiner será nomeado como `very-simple-server-container`.
