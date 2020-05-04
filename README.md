# auto_chooser

## Introdução

O objetivo inicial desse projeto é facilitar a vida de muitos cientistas de dados no tratamento de bases com formatos "padrões" ou comuns, por exemplo, um cientista de dados que recebe recorrentemente uma base com CPFs e telefones de clientes cadastrados, mas tem o trabalho manual de verificar quais os tipos das colunas e corrigir a base toda vez.

Pensando de uma forma mais genérica esse problema pode ser replicado aos mais diversos padrões que não somente CPFs e telefones, mas em dados como:
* Endereços;
* E-mails;
* Datas;
* Itens;
* Preços

Assim o Sonho Grande desse projeto seria uma plataforma que conseguisse importar qualquer base, trata-lá com um mínimo de erros e realizar o upload dessa base para uma estrutura de dados genérica.

## Existem plataformas/programas/gambiarras que fazer isso atualmente?

Sim, mas a maioria é paga ou demanda de muita interação do usuário, sendo que muitas delas não tem uma adaptação para os cenários brasileiros. Entre elas cabe destacar:
* Data Cleaner (http://datacleaner.org/)
* Talend Open Studio (https://www.talend.com/products/talend-open-studio/)

## Como o programa ~~deveria~~ funcionar atualmente?

É possível separar o processo todo em 2 partes, uma em que o usuário atua e outra em que o Python trabalha:

![image](https://raw.githubusercontent.com/vbiral/auto_chooser/master/images/Python.png)

Outra em que o usuário trabalha:

![image](https://raw.githubusercontent.com/vbiral/auto_chooser/master/images/Usu%C3%A1rio.png)

As partes em vermelho indicam funções que respectivamente não tem uma versão inicial desenvolvida. Não gostariamos que existisse.

PS: Para facilitar a vida eu deixei um .cmd para a criação do enviroment conda que estou utilizando no projeto.
