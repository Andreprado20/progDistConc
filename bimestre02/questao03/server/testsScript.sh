#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:5000/api"

# Test usuario CRUD
echo "Testing Usuario CRUD..."
USER_ID=$(curl -s -X POST "$BASE_URL/usuarios" -H "Content-Type: application/json" -d '{"nome": "Test User", "login": "testuser", "senha": "12345"}' | jq -r '.id')
echo "Created Usuario with ID: $USER_ID"

curl -X GET "$BASE_URL/usuarios"
curl -X PUT "$BASE_URL/usuarios/$USER_ID" -H "Content-Type: application/json" -d '{"nome": "Updated Test User", "login": "updateduser", "senha": "54321"}'
curl -X GET "$BASE_URL/usuarios/$USER_ID"
curl -X DELETE "$BASE_URL/usuarios/$USER_ID"
echo "Deleted Usuario with ID: $USER_ID"

# Test carteira CRUD
echo "Testing Carteira CRUD..."
CARTEIRA_ID=$(curl -s -X POST "$BASE_URL/carteiras" -H "Content-Type: application/json" -d '{"nome": "Test Carteira", "id_usuario": 1}' | jq -r '.id')
echo "Created Carteira with ID: $CARTEIRA_ID"

curl -X GET "$BASE_URL/carteiras"
curl -X PUT "$BASE_URL/carteiras/$CARTEIRA_ID" -H "Content-Type: application/json" -d '{"nome": "Updated Test Carteira", "id_usuario": 1}'
curl -X GET "$BASE_URL/carteiras/$CARTEIRA_ID"
curl -X DELETE "$BASE_URL/carteiras/$CARTEIRA_ID"
echo "Deleted Carteira with ID: $CARTEIRA_ID"

# Test criptoativo CRUD
echo "Testing Criptoativo CRUD..."
CRIPTO_ID=$(curl -s -X POST "$BASE_URL/criptoativos" -H "Content-Type: application/json" -d '{"nome": "Test Criptoativo", "codigo": "TST", "preco": 1234.5678}' | jq -r '.id')
echo "Created Criptoativo with ID: $CRIPTO_ID"

curl -X GET "$BASE_URL/criptoativos"
curl -X PUT "$BASE_URL/criptoativos/$CRIPTO_ID" -H "Content-Type: application/json" -d '{"nome": "Updated Criptoativo", "codigo": "TSTUPD", "preco": 9876.5432}'
curl -X GET "$BASE_URL/criptoativos/$CRIPTO_ID"
curl -X DELETE "$BASE_URL/criptoativos/$CRIPTO_ID"
echo "Deleted Criptoativo with ID: $CRIPTO_ID"

# Test carteira_cripto GET only
echo "Testing Carteira_Cripto GET..."
curl -X GET "$BASE_URL/carteira_cripto"

# Test transacao CRUD
echo "Testing Transacao CRUD..."
TRANSACAO_ID=$(curl -s -X POST "$BASE_URL/transacoes" -H "Content-Type: application/json" -d '{"id_carteira_origem": 1, "id_carteira_destino": 2, "id_criptoativo": 1, "quantidade": 0.1, "tipo": "transferencia"}' | jq -r '.id')
echo "Created Transacao with ID: $TRANSACAO_ID"

curl -X GET "$BASE_URL/transacoes"
curl -X PUT "$BASE_URL/transacoes/$TRANSACAO_ID" -H "Content-Type: application/json" -d '{"id_carteira_origem": 1, "id_carteira_destino": 2, "id_criptoativo": 1, "quantidade": 0.5, "tipo": "transferencia"}'
curl -X GET "$BASE_URL/transacoes/$TRANSACAO_ID"
curl -X DELETE "$BASE_URL/transacoes/$TRANSACAO_ID"
echo "Deleted Transacao with ID: $TRANSACAO_ID"

echo "All tests completed successfully."
