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

curl -X POST http://localhost:3000/usuario/postusuario \
    -H "Content-Type: application/json" \
    -d '{
    "id": 16,
    "nome": "Andrea Braga Melo",
    "matricula": "322256987",
    "email": "alice@pgmail.mail.com"
}'; echo
echo \\

curl -X POST http://localhost:3000/usuario/postusuario \
    -H "Content-Type: application/json" \
    -d '{
    "id": 17,
    "nome": "Vini Malvadeza",
    "matricula": "171691572",
    "email": "soccermaster@outlook.com"
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



