# Fábrica de Software 2 - GRUPO 3 - Backend
Repositório do Back-End do projeto de avaliação da Fábrica de Software 2 - GRUPO 3

## Executando o projeto:
O projeto foi desenvolvido utilizando **Flask** e o **RRIA** para controle e comunicação com o robô. Para isso, precisa de algumas configurações específicas para garantir a execução correta e estável.
Para isso, foi incluído um arquivo yaml em `dependencies/environment.yaml` que contém as configurações necessárias para criação de um ambiente virtual **conda** com as dependências necessárias para execução do projeto. Para isso, basta executar o comando:

```powershell
conda env create -f dependencies/environment.yaml
```

Em seguida, ative o ambiente virtual com o comando:

```powershell
conda activate kortex
```

### Atualizando o ambiente
Caso seja necessário atualizar o ambiente, basta executar o comando:

```powershell
conda env update -f dependencies/environment.yaml --prune
```

### Conectando com o Kinova

Para conexão via cabo Ethernet com o Kinova, é necessário configurar o IP do computador para a faixa de IP do robô. Para isso, basta seguir os passos abaixo:
1. Painel de Controle
2. Central de Rede e Compartilhamento
3. Alterar as configurações do adaptador
4. Ethernet Status
5. Ethernet Properties
6. Internet Protocol Version 4 (TCP/IPv4) Properties
7. Usar o seguinte endereço IP:
    - Endereço IP: `192.168.2.11`
    - Máscara de sub-rede: `255.255.255.0`
8. Acesse o front-end via IP `192.168.2.10`.

## Banco de Movimentos:
O banco de movimentos é composto por um arquivo `positions_kinova.json` (com as informações de posições cartesianas e angulares do robô em cada etapa intermediária do movimemento) e um módulo `MoveBank` responsável por traduzir o arquivo json para os tipos de pose e juntas conhecido pelo robô.

### Estrutura do Arquivo `positions_kinova.json`
```json
{
    "nome_posicao": {
        "cartesian": "[x, y, z, roll, pitch, yaw]",
        "joints": "[j1, j2, j3, j4, j5, j6]"
    }
}
```
### Posições Mapeadas:
Foram mapeadas posições de movimentação geral do robô, bem como a posição do **drop** e cada casa jogável do tabuleiro.

| Nome da Posição | Descrição |
| :--- | :--- |
| `capture_height` | Posição de Altura pré-captura das peças. Valores de _x_ e _y_ devem ser obtidos à partir da posição alvo. |
| `home` | Posição inicial do robô antes da operação de jogo. |
| `middle_move_height` | Posição de Altura utilizada entre a movimentação de peças. Valores de _x_ e _y_ devem ser obtidos à partir da posição alvo. |
| `upper_drop_height` | Posição de drop pós captura de peça. |
| `upper_movement_height` | Posição intermediária de Altura utilizada antes de movimentação para drop. |
| `upper_view` | Posição **iddle** utilizada para visualizar o tabuleiro. |
| `safe_shutdown` | Posição pré-desligamento do robô. |
| `pregrip_height` | Posição de movimentação em tabuleiro. Valores de _x_ e _y_ devem ser obtidos à partir da posição alvo. |
| `n0` | Posição no formato `LetraNumero` representando cada casa jogável no tabuleiro. Os valores de _z_ são quase rentes ao tabuleiro, e devem ser combinados com os valores de `capture_height` e `pregrip_height` para movimentações. |
| `dama0c` | Valores de posição das damas no formato `damaNC` onde `N = Numero` e `C = cor`. Valores de _z_ são referentes à posição rente ao tabuleiro. |
| `dama0c_pregrip` | Valores de posição das damas no formato `damaNC_pregrip` onde `N = Numero` e `C = cor`. Valores de _z_ são referentes à altura antes da captura da peça. |

## Entregável Semana 1 - Scripts de Movimentação do Robô
Para executar o projeto, basta executar o arquivo `main.py` com o comando:

```powershell
python .\src\main.py
```

Com isso um menu de escolha do robô será exibido, possibilitando a execução do projeto com o robô de Testes ou o robô Kinova. Basta digitar o número correspondente à escolha e pressionar `Enter`. Em seguida, o menu de escolha da mesa do robô será exibida, possibilitando selecionar entre o Kinova (Mesa da Direita) ou o "KAnova" (Mesa da Esquerda). Basta digitar o número correspondente à escolha e pressionar `Enter`.

O programa fará a instância dos robôs, banco de movimentos e controlador do robô e permitirá a execução das tarefas de:
- Movimentar Peças
- Remover Peças
- Colocar uma Dama no Tabuleiro

> Na versão atual, o controlador do robô executará a conexão e se desconectará em cada uma das opções do menu. Em versões futuras, a conexão será mantida durante a execução do programa.

![Menu de Escolha do Robô](docs/images/robot_menu.png)

### Movimentar Peças [Opção 3]
Para movimentar peças, basta selecionar a opção `3` no menu de escolha de tarefas. Em seguida, o menu de escolha de movimentação será exibido, possibilitando a escolha entre movimentação de peças de um ponto de origem, para 1 ou mais pontos de destino.
A escrita dos pontos de origem e destino devem seguir o padrão `LetraNumero` (ex: `A1`, `B2`, `C3`, etc), separados por ponto e vírgula (`;`).

O robô irá capturar a peça no primeiro ponto informado, e passar pelas posições intermediárias saltando entre os espaços, até o ponto de destino, onde a peça será solta.

![Menu de Escolha de Movimentação](docs/images/capture_pieces.png)

### Remover Peças [Opção 4]
Para remover uma peça do tabuleiro, basta selcionar a opção `4` no menu de escolha de tarefas. Em seguida, o menu de escolha de remoção será exibido, esperando a informação da coordenada `LetraNumero` (ex: `A1`, `B2`, `C3`, etc) da peça a ser removida.

![Menu de Escolha de Remoção](docs/images/remove_pieces.png)

### Colocar uma Dama no Tabuleiro [Opção 5]
Para colocar uma dama no tabuleiro, basta selecionar a opção `5` no menu de escolha de tarefas. Em seguida, o menu de escolha de movimentação será exibido, esperando a informação da coordenada `LetraNumero` (ex: `A1`, `B2`, `C3`, etc) da casa onde a dama será colocada. Em seguida, o programa solicitará a informação de qual dama deve ser colocada. A movimentação do robô espera que as damas sejam colocadas nas posições paralelas às casas pretas no lado direito (da visão do robô), sendo numeradas de 1 a 4, onde 1 é a dama mais próxima ao robô, e 4 a mais distante.

![Menu de Escolha de Colocação de Dama](docs/images/place_queen.png)
