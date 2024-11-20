echo \"GET ALL Test:\"; echo

curl -X GET http://localhost:3000/professores; echo
echo \\

echo \"GET UNIQUE Test:\"; echo

curl -X GET http://localhost:3000/professor/10; echo
echo \\

echo \"DELETE Test:\"; echo

curl -X DELETE http://localhost:3000/delete/16; echo
echo \\

echo \"POST Test:\"; echo

curl -X POST http://localhost:3000/professor/postProfessor \
    -H "Content-Type: application/json" \
    -d '{
    "id": 16,
    "nome": "Andrea Braga Melo",
    "matricula": "322256987",
    "email": "alice@pgmail.mail.com"
}'; echo
echo \\

curl -X POST http://localhost:3000/professor/postProfessor \
    -H "Content-Type: application/json" \
    -d '{
    "id": 17,
    "nome": "Vini Malvadeza",
    "matricula": "171691572",
    "email": "soccermaster@outlook.com"
}'; echo
echo \\

echo \"PUT Test:\"; echo

curl -X PUT http://localhost:3000/professor/update/16 \
    -H "Content-Type: application/json" \
    -d '{
    "nome": "Andrea Braga Melo",
    "matricula": "322256999",
    "email": "alice@gmailcom"
}'; echo
echo \\



