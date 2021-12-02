# API de Validação de email com Flask

API que faz a validação se um email é valido ou não e ainda utiliza uma blacklist de palavras inapropriadas.

Docker (https://www.docker.com/)

### Utilização

Realizar a chamada passando os seguintes dados:

```
curl -XPOST '127.0.0.1:5000/api/v1/' -H 'Content-Type: application/json' -d '{"emailAddress":"teste@gmail.com","clientId":"MEUID","tokenId":"1234567890"}'
```

Retorno de Sucesso:

{
  "emailAddress": "teste@gmail.com",
  "status": 1
}

```
curl -XPOST '127.0.0.1:5000/api/v1/' -H 'Content-Type: application/json' -d '{"emailAddress":"sexo@gmail.com","clientId":"MEUID","tokenId":"1234567890"}'
```
Retorno de Falha com palavra inapropriada:

{
  "bounce": {
    "code": 511,
    "detail": "Bad destination mailbox address",
    "type": 1
  },
  "emailAddress": "sexo@gmail.com",
  "status": 2
}

```
curl -XPOST '127.0.0.1:5000/api/v1/' -H 'Content-Type: application/json' -d '{"emailAddress":"testegmail.com","clientId":"MEUID","tokenId":"1234567890"}'
```

Retorno de falha para email inválido:

{
  "bounce": {
    "code": 990,
    "detail": "Invalid mail format",
    "type": 1
  },
  "emailAddress": "testegmail.com",
  "status": 2
}

