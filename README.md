# Projeto Athena Bot para Xenites

# Finalidade
- Aprimorar imersão dos xenites na comunidade do Discord

# Rodando o Projeto
- Vale ressaltar que é bom preparar nosso ambiente python para rodar o projeto, para isso, rode o seguinte comando

```
    $ sudo apt install python3-dev python3-pip python3-wheel python3-setuptools
```

- Com esses pacotes instalados, podemos rodar o criador do Python Virtual Environment
```
    $ python3 -m venv .venv
```

- Feito isso, vamos atualizar o pip3 wheel e setuptools
```
    $ source ./.venv/bin/activate # inicializa o virtual environment
    $ pip3 install --upgrade pip wheel setuptools
```

- Vamos então instalar as dependências
```
    $ pip3 install discord
```

# Rodando o projeto
- Com a etapa anterior concluída, basta rodarmos no terminal
- Para iniciar o bot:
```
    $ python3 ./main.py
```
- Para parar o bot
`Ctrl + C`

# Próximos passos:
1. Migrar dados para banco de dados atualizável
2. Containerizar o projeto
3. a definir...