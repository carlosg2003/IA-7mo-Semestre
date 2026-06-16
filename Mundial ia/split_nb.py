import json
import os
import re

notebook_path = r'c:\Users\User\Downloads\Mundial ia\multiagente_rag_mundiales.ipynb'
if not os.path.exists(notebook_path):
    print('Notebook not found')
    exit(1)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

modified = False
new_cells = []

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code' and any('TrainerAgent()' in line for line in cell.get('source', [])):
        source_lines = cell['source']
        
        split_index = -1
        for i, line in enumerate(source_lines):
            if 'communicator = CommunicatorAgent(vector_db)' in line:
                split_index = i
                break
                
        if split_index != -1:
            part1 = source_lines[:split_index]
            
            # Unindent part2
            part2 = []
            for line in source_lines[split_index:]:
                if line.startswith('    '):
                    part2.append(line[4:])
                else:
                    part2.append(line)
            
            # Replace query in part2
            for i, line in enumerate(part2):
                if 'query=' in line:
                    part2[i] = re.sub(r'query=.*', 'query=\"Quien jugo la final del mundial 2010?\"\\n', line)
            
            cell['source'] = part1
            new_cells.append(cell)
            
            md_cell = {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Paso 5.1: Realizar Preguntas al Bot\n",
                    "Ejecuta solo esta celda para hacer nuevas preguntas sin reentrenar los modelos. Puedes cambiar el texto del `query`."
                ]
            }
            new_cells.append(md_cell)
            
            new_code_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": part2
            }
            new_cells.append(new_code_cell)
            modified = True
            continue
            
    new_cells.append(cell)

if modified:
    nb['cells'] = new_cells
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    print('Successfully split the cell.')
else:
    print('Cell to split not found.')
