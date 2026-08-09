import json
from pathlib import Path

path = Path(r'c:\9B_IDGS-ECBD\ECBD_9B_IDGS_Practices_230768\Practice-10\explot.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))

code_updated = False
layout_updated = False

for cell in nb['cells']:
    if cell.get('cell_type') == 'code' and cell.get('id') == '9a6bc4ce':
        cell['source'] = [
            "type_order = sorted(unique_types)\n",
            "type_coords = {t: i for i, t in enumerate(type_order)}\n",
            "df_sprites['type_coord'] = df_sprites['type1'].map(type_coords)\n",
            "\n",
            "hover_texts = []\n",
            "for _, row in df_sprites.iterrows():\n",
            "    hover_text = (\n",
            "        f\"<b>{row['name']}</b><br>\"\n",
            "        f\"Tipo: {row['type1']} / {row['type2']}<br>\"\n",
            "        f\"Generación: {row['generation_label']}<br>\"\n",
            "        f\"HP: {row['hp']}<br>\"\n",
            "        f\"Ataque: {row['attack']}<br>\"\n",
            "        f\"Defensa: {row['defense']}<br>\"\n",
            "        f\"Sp. Atk: {row['sp_attack']}<br>\"\n",
            "        f\"Sp. Def: {row['sp_defense']}<br>\"\n",
            "        f\"Velocidad: {row['speed']}<br>\"\n",
            "        f\"<b>Promedio: {row['promedio_estadisticas']}</b><extra></extra>\"\n",
            "    )\n",
            "    hover_texts.append(hover_text)\n",
            "\n",
            "fig_sprites.add_trace(go.Scatter(\n",
            "    x=df_sprites['generation'],\n",
            "    y=df_sprites['type_coord'],\n",
            "    mode='markers',\n",
            "    marker=dict(size=1, opacity=0),\n",
            "    text=hover_texts,\n",
            "    hoverinfo='text',\n",
            "    hovertemplate='%{text}<extra></extra>',\n",
            "    showlegend=False\n",
            "))\n",
            "\n",
            "sprite_size = 0.6\n",
            "for _, row in df_sprites.iterrows():\n",
            "    fig_sprites.add_layout_image(dict(\n",
            "        source=row['sprite_url'],\n",
            "        xref='x',\n",
            "        yref='y',\n",
            "        x=row['generation'],\n",
            "        y=row['type_coord'],\n",
            "        xanchor='center',\n",
            "        yanchor='middle',\n",
            "        sizex=sprite_size,\n",
            "        sizey=sprite_size,\n",
            "        sizing='contain',\n",
            "        opacity=1,\n",
            "        layer='above',\n",
            "    ))\n"
        ]
        code_updated = True

    if cell.get('cell_type') == 'code' and any('fig_sprites.update_layout(' in line for line in cell.get('source', [])):
        cell['source'] = [
            "fig_sprites.update_layout(\n",
            "    title=dict(\n",
            "        text=\"<b>Pokémon Destacados por Tipo y su Promedio de Estadísticas</b><br>\" +\n",
            "             \"<sup>Visualización con Sprites de Pokémon</sup>\",\n",
            "        font=dict(size=20, color='#2E4053')\n",
            "    ),\n",
            "    xaxis=dict(\n",
            "        title=\"<b>Generación</b>\",\n",
            "        tickvals=[1, 2, 3, 4, 5, 6],\n",
            "        ticktext=['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6'],\n",
            "        tickangle=45,\n",
            "        gridcolor='lightgray',\n",
            "        showgrid=True\n",
            "    ),\n",
            "    yaxis=dict(\n",
            "        title=\"<b>Tipo Principal</b>\",\n",
            "        tickvals=list(type_coords.values()),\n",
            "        ticktext=list(type_order),\n",
            "        gridcolor='lightgray',\n",
            "        showgrid=True,\n",
            "        range=[-1, len(type_order)],\n",
            "    ),\n",
            "    width=1400,\n",
            "    height=900,\n",
            "    margin=dict(l=50, r=50, t=100, b=150),\n",
            "    paper_bgcolor='rgba(245, 245, 245, 0.95)',\n",
            "    plot_bgcolor='rgba(245, 245, 245, 0.95)',\n",
            "    showlegend=False,\n",
            "    hovermode='closest'\n",
            ")\n"
        ]
        layout_updated = True

if not code_updated:
    raise RuntimeError('fig_sprites code cell not found')
if not layout_updated:
    raise RuntimeError('fig_sprites layout cell not found')

path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('Updated notebook with fig_sprites changes.')
