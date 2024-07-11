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