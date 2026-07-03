<!-- HEADER PRINCIPAL -->
<div align="center">

  # 📊 Extracción de Conocimiento de Bases de Datos
  <p align="center">
    <strong>Repositorio Oficial de Prácticas — Asignatura de Análisis de Datos</strong>
    <br />
    <sub>Ingeniería en Desarrollo y Gestión de Software</sub>
  </p>
  <img src="/img/Logo_TI.png" alt="Stack Tecnológico" width="900" />

  <!-- BADGES ESTILIZADOS -->
  <p align="center">
    <img src="https://shields.io" alt="Python" />
    <img src="https://shields.io" alt="Jupyter" />
    <img src="https://shields.io" alt="Git Flow" />
    <img src="https://shields.io" alt="Status" />
  </p>
</div>

---

## 📌 Descripción
Este repositorio contendrá los resultados de las prácticas de la materia para tener una mejor organización y agilizar la revisión de las mismas.

El objetivo principal de este repositorio es almacenar, organizar y documentar el código fuente, los procesos de preprocesamiento de datos y los flujos de trabajo de análisis exploratorio de datos (EDA) realizados a lo largo del periodo académico.

---
## ℹ️ Información del Curso
- **Asignatura:** Extracción de Conocimiento en Bases de Datos
- **Docente:** M.T.I. Marco A. Ramírez Hernández
- **Programa Educativo:** Ingeniería en Desarrollo y Gestión de Software
- **Estudiante:** Uriel Abdallah Medina Torres 
- **Acceso:** Privado (Uso Académico Exclusivo)
---

## ⚙️ Estándares de Arquitectura (Git Flow)

<details>
<summary><b>🛠️ Estrategia de Ramificación (Branching Strategy)</b></summary>
<br />
El desarrollo se realiza de forma aislada e incremental. Queda estrictamente prohibido realizar commits directos sobre <code>main</code> o <code>dev</code>.
<ul>
  <li><strong>Ramas de funcionalidad:</strong> <code>feature/practica-XX</code></li>
  <li><strong>Ramas de corrección:</strong> <code>bugfix/issue-XX</code></li>
</ul>
</details>

<details>
<summary><b>💬 Convención de Commits Semánticos</b></summary>
<br />
Los mensajes de confirmación siguen la estructura predictiva de <i>Conventional Commits</i>:
<ul>
  <li><code>feat(p05):</code> Nueva funcionalidad o archivo base de la práctica.</li>
  <li><code>docs(readme):</code> Actualizaciones en la documentación del repositorio.</li>
  <li><code>chore:</code> Modificaciones secundarias en archivos de configuración (<code>.gitignore</code>).</li>
</ul>
</details>

<details>
<summary><b>🛡️ Gestión de Entornos e Aislamiento</b></summary>
<br />
Los binarios, librerías instaladas por <code>pip</code> y cachés locales del sistema de ejecución (<code>__pycache__/</code>) se omiten del repositorio remoto mediante el archivo <code>.gitignore</code> para mantener un repositorio ligero y limpio.
</details>

---

## 🚀 Despliegue Local Rápido

Para replicar el entorno controlado en tu máquina local, ejecuta secuencialmente en tu terminal:

```bash
# 1. Clonar repositorio y acceder al directorio
git clone https://github.com<user>/<repo>.git
cd ECBD_9B_IDGS_Prectices_230768

# 2. Inicializar y activar entorno virtual controlado, mediante terminal(Windows)
py -3.12 -m venv env
envcripts\activate

# 3. Instalar dependencias e indexar Kernel en Jupyter
pip install -r requirements.txt
py -m ipykernel install --user --name=env --display-name "Python 3.12 (ECBD)"

```

## 📅 Matriz de Control de Entregables

<table width="100%">
  <thead>
    <tr>
      <th width="8%" align="center">ID</th>
      <th width="45%" align="left">Actividad Académica</th>
      <th width="27%" align="center">Core Stack / Potenciador</th>
      <th width="20%" align="center">Estatus Técnico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>01</code></td>
      <td>Práctica 1: <em>Nombre de la actividad</em></td>
      <td align="center"><code>N/A</code></td>
      <td align="center">Completada</td>
    </tr>
  </tbody>
</table>

---
