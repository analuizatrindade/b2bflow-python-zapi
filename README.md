
# Desafio b2bflow

Este projeto foi desenvolvido em Python com o objetivo de buscar contatos armazenados no Supabase e enviar mensagens personalizadas pelo WhatsApp utilizando a Z-API.

## Estrutura da tabela

Foi utilizada uma tabela chamada `contatos` no Supabase, contendo os seguintes campos:

- `nome`
- `telefone`

## Variáveis de ambiente

Crie um arquivo `.env` com as seguintes informações:

```env
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_chave

ZAPI_INSTANCE_ID=sua_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

## Instalação

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Como executar

Para iniciar o programa, execute:

```bash
python main.py
```

## Funcionamento

O sistema consulta os contatos cadastrados no Supabase e envia a mensagem:

```
Olá, <nome_contato> tudo bem com você?
```

para até 3 números diferentes, substituindo `<nome_contato>` pelo nome armazenado no banco de dados.

## Tecnologias utilizadas

- Python
- Supabase
- Z-API
