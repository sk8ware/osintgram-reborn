#!/bin/bash

echo "🛠️  Inicializando entorno virtual de Osintgram-Reborn..."

# 1. Verificamos si ya existe el venv
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Entorno virtual creado."
fi

# 2. Activamos el entorno virtual
source venv/bin/activate

# 3. Instalamos las dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Ejecutamos la herramienta
python3 main.py

