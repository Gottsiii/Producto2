# Script para la Generación del Entorno (Simulación)
echo "Instalando dependencias de Python..."
pip install -r requirements.txt

echo "Configurando variables de entorno (simulación de inyección segura)..."
# En la vida real, $GEMINI_API_KEY se inyecta desde GitHub Secrets
export GEMINI_API_KEY=dummy_key

