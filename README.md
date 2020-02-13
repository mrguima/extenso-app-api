# API para escrever números por extenso
Ferramenta que retorna um JSON para cada requisição GET cuja chave 'extenso' é a versão por extenso do número inteiro enviado no caminho (exemplo localhost:5000/10). Os números podem estar no intervalo [-99999, 99999]. Servidor web em Python utlizando Flask. 


# Rodando o servidor com Docker

Para subir o servidor utilizando Docker, primeiro clone ou faça download da aplicação, extraia para o caminho desejado, em seguida abra um terminal no caminho da pasta escolhida e crie a imagem a partir do Dockerfile com o comando no terminal:

``` docker build -t nome_da_imagem . ```

Escolha um nome para a imagem em  **nome_da_imagem**. O ponto indica o caminho atual (pasta da aplicação) para localização do Dockerfile.
Aguarde a criação da imagem finalizar e crie um container a partir dela. Para isto, utilize o comando:

``` docker run --name nome_do_container -d -p 5000:5000 nome_da_imagem ```

Escolha um nome para o container em  **nome_do_container**  e em  **nome_da_imagem**  utilize o nome escolhido para a imagem criada a partir do Dockerfile. Utilizamos o **-d** para rodar o servidor em segundo plano.

Pronto! O servidor deve estar rodando em **localhost:5000**. Faça as requisições a partir da rota localhost:5000/*num* sendo *num* um valor entre -99999 e 99999.

# Rodando o servidor sem Docker
Primeiro certifique-se que você possui [Python 3](https://www.python.org/) instalado e então clone ou faça download da aplicação, extraia para o caminho desejado, em seguida abra um terminal no caminho da pasta escolhida. Crie um ambiente para rodar a aplicação:
``` python3 -m venv venv ```
No Windows:
``` py -3 -m venv venv ```

É necessário ativar o ambiente antes de começarmos, para isso execute:
``` $ . venv/bin/activate ```
No Windows:
``` venv\Scripts\activate ```

Agora com o ambiente ativado, instale o Flask utilizando o seguinte comando: ``` pip install Flask ```

Com o Flask instalado, rode o servidor com o comando: ``` python server.py``` e pronto! O servidor deve estar rodando em **localhost:5000**. Faça as requisições a partir da rota localhost:5000/*num* sendo *num* um valor entre -99999 e 99999.