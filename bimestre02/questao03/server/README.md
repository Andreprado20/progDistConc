# dbTestsWithNestJS

<p align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="200" alt="Nest Logo" /></a>
</p>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

  
  <!--[![Backers on Open Collective](https://opencollective.com/nest/backers/badge.svg)](https://opencollective.com/nest#backer)
  [![Sponsors on Open Collective](https://opencollective.com/nest/sponsors/badge.svg)](https://opencollective.com/nest#sponsor)-->

## Getting Started

Este repositório contém um projeto que é uma versão em NestJS do projeto contido no repositório [dbTests](https://github.com/Andreprado20/dbTests). Você pode saber mais sobre o NestJS através deste [link](https://github.com/nestjs/nest) que contém o repositório oficial do framework, ou neste [link](https://nestjs.com/) com o site oficial da ferramenta e com acesso à [documentação oficial do Framework](https://docs.nestjs.com/). O projeto dbTests é uma remodelagem e reconstrução do projeto prático do Primeiro Bimestre da matéria Programação Avançada para Web com o CRUD funcionando totalmente. 

O banco usado é um PostgreSQL em localhost (em breve lançaremos aqui e no repositório dbTests uma versão nova contendo [Docker](https://www.docker.com/)).

Neste repositório, as pessoas com acesso à modificação também podem criar outras branches para irem colocando novas features na aplicação.

## Como configurar seu terminal para interagir com o GitHub??

Você pode fazer isso através de uma autenticação com uma chave SSH

- [ ] Consulte [este link](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) para ver sobre a criação de sua chave SSH.


- [ ] Consulte [este link](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) para adicionar sua chave pública criada no passo anterior à sua conta do GitHub.

## Alguns comandos úteis:

- [ ] Depois de configurar o passo anterior, clone seu repositório com o comando:
``` 
git clone git@github.com:<nome do usuário>/<nome do repositório>.git
```


- [ ] Para verificar em qual branch você está, rode:
``` 
git branch
``` 
A Branch que aparecer de verde será a sua branch atual


- [ ] Caso você queira criar uma nova branch, rode:
``` 
git branch <nome da sua nova branch>
```


- [ ] Caso queira mudar a sua branch, rode:
``` 
git checkout <nome da branch para onde você quer mudar>
```


- [ ] Uma vez que você tem certeza de que está na branch desejada, rode:
``` 
git commit -m "<Sua Mensagem de Commit aqui>"
```


- [ ] Caso você receba a mensagem "Changes not staged for commit:[...] no changes added to commit (use "git add" and/or "git commit -a")" tente rodar ```git add .``` e depois repita o passo anterior


- [ ] Depois de dar o commit, você deverá subir seus commits para o GitHub através de um push, para isso rode:
``` 
git push -u origin <nome da branch para onde você quer dar o push>
```


- [ ] Caso você tenha alterações feitas remotamente no repositório que você gostaria de adicionar no seu repositório local, rode:
``` 
git pull origin <nome da branch de onde você quer pegar as alterações>
```
- [ ] Qualquer dúvida com os comandos git, basta consultar a [documentação do GitHub](https://docs.github.com/pt)

##

- [ ] Caso você tenha problemas de permissão com o arquivo "tsc" ou com a pasta "node_modules", tente alguma dessas opções:
``` 
chmod +rwx node_modules/.bin/tsc
chmod a+x node_modules/.bin/tsc
chmod -R a+x node_modules
chmod -R a+x node_modules/.bin/tsc
```
- [ ] Caso nenhuma delas funcione, tente apagar a pasta node_modules e depois reinstalar através do comando:
``` 
rm -rf ./node_modules; npm i 
```
e depois tente rodar o comando "npm run dev" novamente

## Automatizando os testes de CRUD

- [ ] Para testar o funcionamento correto do funcionamento do CRUD (Create, Read, Update, Delete) da sua aplicação, você deve testar se os métodos HTTP equivalentes ao CRUD estão funcionando corretamente na sua aplicação. Segue abaixo a relação de HTTP Methods para o CRUD:

    | HTTP Method |  CRUD  |
    |-------------|--------|
    |     GET     |  Read  |
    |     POST    | Create |
    |     PUT     | Update |
    |    DELETE   | Delete |

- [ ] Para isso, você pode usar programas como por exemplo o [Insomnia](https://insomnia.rest/) ou então uma extensão no Visual Studio Code, como por exemplo o [ThunderClient](https://www.thunderclient.com/)

- [ ] Outra opção, quando se está no Linux, é usar o comando ```curl```. Aqui neste repositório, ao acessar a branch wslVersion, você vai encontrar um arquivo bash (.sh) chamado ```testsScript.sh```, contendo o seguinte código:

``` 
echo \"GET ALL Test:\"; echo

curl -X GET http://localhost:3000/usuarioes; echo
echo \\

echo \"GET UNIQUE Test:\"; echo

curl -X GET http://localhost:3000/usuario/10; echo
echo \\

echo \"DELETE Test:\"; echo

curl -X DELETE http://localhost:3000/delete/16; echo
echo \\

echo \"POST Test:\"; echo

curl -X POST http://localhost:3000/usuario/post \
    -H "Content-Type: application/json" \
    -d '{
    "id": 16,
    "nome": "Andrea Braga Melo",
    "matricula": "322256987",
    "email": "alice@pgmail.mail.com"
}'; echo
echo \\

echo \"PUT Test:\"; echo

curl -X PUT http://localhost:3000/usuario/update/16 \
    -H "Content-Type: application/json" \
    -d '{
    "nome": "Andrea Braga Melo",
    "matricula": "322256999",
    "email": "alice@gmailcom"
}'; echo
echo \\
```

- [ ] Ele vai rodar uma série de comandos 'echo' para imprimir no terminal uma mensagem especificando qual é o teste que está sendo feito em uma determinada linha e logo abaixo vem os comandos ```curl``` para testar as requisições HTTP via terminal. Acesse este [link](https://www.hostinger.com.br/tutoriais/comando-curl-linux) para ler mais sobre o comando ```curl``` no Linux.

- [ ] Para usar este script para testar automaticamente o seu CRUD, certifique-se de que este arquivo possui as permissões para ser rodado no seu Linux ou WSL através do seguinte comando:
``` 
chmod +rwx testsScript.sh
```
Depois de rodar este comando, rode: 
```
ls -l testsScript.sh
```
Este comando irá listar as permissões do arquivo com o script. Se o output deste último comando for ```-rwxr-xr-x 1 <usuário> <usuário> 785 <mês> <dia> <hora> testsScript.sh``` é sinal de que ele está com as permissões necessárias para ser rodado.

- [ ] Depois disso, abra duas janelas do terminal de comando dentro da pasta do projeto. Em uma delas, rode o comando ```npm run start:dev``` para rodar o seu servidor e fazer a aplicação funcionar. Depois, na outra janela que não está rodando o comando ```npm run start:dev```, rode o seguinte comando:
```
./testsScript.sh
```
Este comando irá rodar o script criado para testes.

- [ ] Se o seu output for igual o abaixo, é sinal de que a aplicação está com o seu CRUD funcionando corretamente:

```
"GET ALL Test:"

{"lista":[{"id":10,"nome":"Alice Braga Melo","matricula":"321456987","email":"alice@prisma.mail.com"},{"id":15,"nome":"Ana Braga Melo","matricula":"322999987","email":"ana@gmail.com"}]}
\
"GET UNIQUE Test:"

{"usuario":{"id":10,"nome":"Alice Braga Melo","matricula":"321456987","email":"alice@prisma.mail.com"}}
\
"POST Test:"

{"status":"ok","criaProf":{"id":16,"nome":"Andrea Braga Melo","matricula":"322256987","email":"alice@pgmail.mail.com"}}
\
"PUT Test:"

{"updateProf":{"id":16,"nome":"Andrea Braga Melo","matricula":"322256999","email":"alice@gmailcom"}}
\
"DELETE Test:"

{"apagausuario":{"id":16,"nome":"Andrea Braga Melo","matricula":"322256999","email":"alice@gmailcom"}}
\
```

Depois é só comparar o output e os métodos de acordo com sua aplicação pra ver se o retorno vai ser igual ou não o que estava aqui já previamente.
