# Script de Despliegue (Simulación)
echo "Desplegando la nueva version del Prompt y el Backend al Servidor de Produccion..."
# Comando que activa la ultima version aprobada del Prompt Template
./deploy-service.sh --version $PROMPT_VERSION --env prod

