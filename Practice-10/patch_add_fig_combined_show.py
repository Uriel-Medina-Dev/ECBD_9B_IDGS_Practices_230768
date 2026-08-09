import json
from pathlib import Path

path = Path(r'c:\9B_IDGS-ECBD\ECBD_9B_IDGS_Practices_230768\Practice-10\explot.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
updated = False
for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and cell.get('id') == '077ee38b':
        source = cell['source']
        if any('fig_combined.show()' in line for line in source):
            print('Already has fig_combined.show()')
            updated = True
            break
        source.append('fig_combined.show()\n')
        cell['source'] = source
        updated = True
        break
if not updated:
    raise RuntimeError('Cell 077ee38b not found or not updated')
path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('Updated notebook: added fig_combined.show()')
