import json
import os

notebook_path = r'c:\Users\User\Downloads\Mundial ia\multiagente_rag_mundiales.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

md_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Consultas Rápidas al Sistema (Q&A)\n",
        "Utiliza esta celda para hacerle preguntas directas a la base de datos sobre la historia de los mundiales. Esta celda buscará la respuesta y te la mostrará directamente sin generar el reporte completo."
    ]
}

code_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Escribe tu pregunta aquí:\n",
        "pregunta = \"¿Quién jugó la final del mundial 2010?\"\n",
        "\n",
        "print(f\"\\n🔍 Buscando información para: '{pregunta}'...\\n\")\n",
        "\n",
        "# 1. Buscamos en la base de datos vectorial\n",
        "resultados = vector_db.search(pregunta, k=5)\n",
        "\n",
        "if not resultados:\n",
        "    print(\"No se encontró información relevante.\")\n",
        "else:\n",
        "    print(\"⚽ Resultados Históricos Encontrados:\\n\")\n",
        "    for i, res in enumerate(resultados):\n",
        "        # El 'document' es el texto descriptivo del partido\n",
        "        print(f\"{i+1}. {res['document']}\")\n"
    ]
}

nb['cells'].extend([md_cell, code_cell])

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
    
print('Successfully added the Q&A section.')
