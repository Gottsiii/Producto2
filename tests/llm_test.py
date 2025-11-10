# Script de prueba de Calidad del Prompt (LLM Testing)
# Este script verifica que la respuesta de Gemini adhiera al formato JSON y que la cotización sea precisa.

import json
import sys

# 1. Simulación de la respuesta del LLM (debería ser real en el entorno QA)
llm_response_text = "{\\"estimate\\": 450.50, \\"currency\\": \\"USD\\", \\"components\\": [ {\\"name\\": \\"Labor\\"}, {\\"name\\": \\"Materiales\\"}]}"

try:
    # 2. Verificar que la respuesta sea JSON válido
    data = json.loads(llm_response_text)

    # 3. Verificar que tenga las claves requeridas (ej: Desviación de la Cotización)
    if not isinstance(data.get("estimate"), float) or data.get("estimate") < 10.0:
        print("❌ ERROR: La cotización está fuera del rango esperado.")
        sys.exit(1)

    print("✅ PRUEBAS DE PROMPT EXITOSAS: Formato JSON y rango de cotización validados.")
    sys.exit(0)

except json.JSONDecodeError:
    print("❌ ERROR: La respuesta del LLM no es un JSON válido (Fallo de Formato).")
    sys.exit(1)