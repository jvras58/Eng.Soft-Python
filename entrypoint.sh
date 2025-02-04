#!/bin/bash
set -e

if [ -f "/app/.venv/bin/activate" ]; then
    echo "Ativando ambiente virtual..."
    source /app/.venv/bin/activate
else
    echo "Ambiente virtual não encontrado!"
    exit 1
fi

if [ "$ENVIRONMENT" = "homolog" ]; then
    echo "Iniciando em ambiente HOMOLOG (com reload)"
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
else
    echo "Iniciando em ambiente PROD"
    uvicorn src.main:app --host 0.0.0.0 --port 8000
fi
