<<<<<<< HEAD
# 🥊 Fighting for the Grade

📖 Descripción del juego

Fighting for the Gradee(peleando por la nota) es un juego de pelea uno contra uno (1 vs 1) inspirado en *Urban Champion* (Nintendo, 1984), con modificaciones en su mecánica central.

A diferencia del original, esta versión elimina el sistema de empuje y lo reemplaza por un sistema de combate directo basado en **daño y defensa por turnos**. Dos jugadores se enfrentan en combate directo: el objetivo es reducir la vida del oponente a cero antes de ser derrotado, combinando ataques y bloqueos de forma estratégica.

### Mecánica principal

- Dos personajes se enfrentan en un escenario de combate.
- Cada personaje posee una **barra de vida**.
- En cada turno, un jugador puede **atacar** mientras el otro decide si **bloquear** o no.
- El combate termina cuando la vida de uno de los personajes llega a cero.

---

## 👥 Integrantes

| Nombre | Apellido |
|--------|----------|
| Eliana Jaqueline | Salvo Austin |
| Diego Gabriel | Ponce |

---

## 🗂️ Estructura del proyecto

```
fighting-for-the-grade/
├── src/
│   ├── Personaje.py       # Clase base del combatiente
│   ├── Jugador.py         # Clase Jugador (hereda de Personaje)
│   ├── Ulti.py            # Habilidad especial / animación final
│   └── main.py            # Archivo principal

├── tests/
│   ├── test_personaje.py  # Pruebas unitarias de Personaje
│   └── test_jugador.py    # Pruebas unitarias de Jugador

├── venv/                  # Entorno virtual (no se sube al repo)
├── requirements.txt       # Dependencias del proyecto
├── .gitignore
└── README.md
```

---

## 🧱 Entidades principales

### `Personaje` (clase base)
Representa a cualquier combatiente del juego. Concentra la lógica central del combate.

**Responsabilidades:**
- Gestionar la vida del personaje
- Recibir daño (con control de límite inferior en 0)
- Atacar a otros personajes
- Bloquear ataques
- Calcular el daño (`fuerza + ataque`)
- Determinar si el personaje está vivo

### `Jugador` (hereda de `Personaje`)
Representa al combatiente controlado por el usuario. Extiende `Personaje` con información más completa sobre su estado.

**Responsabilidades:**
- Definir características particulares del jugador
- Mostrar el estado completo (vida actual/máxima, fuerza, ataque)

### `Ulti`
Representa la animación final asociada a un personaje. Encapsula el concepto de ataque definitivo que se ejecuta cuando la vida del oponente llega a 0.

**Responsabilidades:**
- Representar la animación final del personaje
- Asociar una animacion especial al momento de la derrota del oponente

---

## 🎨 Decisiones de diseño

**Herencia:** Se optó por una jerarquía `Personaje → Jugador` para evitar duplicación de código. Todos los combatientes comparten comportamientos comunes (atacar, recibir daño, bloquear, morir), que se centralizan en la clase base.

**Separación de atributos de daño:** El daño no es un valor fijo. Se calcula como `fuerza + ataque`, donde `fuerza` es una característica base del personaje y `ataque` representa su capacidad ofensiva en cada acción.

**Estados booleanos:** Se usan `esta_atacando` y `esta_bloqueando` para representar el estado actual del personaje en el turno. Esto permite, por ejemplo, que un bloqueo activo absorba el daño entrante antes de que se reduzca la vida.

**Control de vida:** La vida nunca puede ser negativa. La lógica de reducción está centralizada en `recibir_danio()` como único punto de control.

**Animacion (Ulti):** Se incorporó la clase `Ulti` como un objeto asociado a `Personaje`. Esto permite representar animaciones finales sin sobrecargar la lógica principal del combate

---

## 🧪 Pruebas unitarias

Las pruebas se implementaron con el módulo `unittest` de Python y cubren los comportamientos principales de ambas clases.

| Clase | Pruebas incluidas |
|-------|------------------|
| `Personaje` | Recibir daño normal, daño en exceso, daño exacto a 0, estado vivo, mostrar estado, morir, bloquear, atacar |
| `Jugador` | Recibir daño, estado vivo, mostrar estado completo, morir, bloquear, bloqueo absorbe daño, calcular daño |

Para ejecutar todas las pruebas:

```bash
python -m unittest discover tests/
```

---

## ⚠️ Manejo de excepciones

Las clases validan sus datos tanto en la creación como en las operaciones:

**En el constructor (`__init__`):**
- `TypeError` si `nombre` no es un string
- `TypeError` si `vida_maxima`, `fuerza` o `ataque` no son números
- `ValueError` si `vida_maxima`, `fuerza` o `ataque` son negativos

**En operaciones:**
- `ValueError` en `recibir_danio()` si el daño recibido es ≤ 0

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Git
- Visual Studio Code (recomendado) con la extensión de Python

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/fighting-for-the-grade.git
   cd fighting-for-the-grade
   ```

2. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv

   # En Windows:
   venv\Scripts\activate

   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar el proyecto:
   ```bash
   python src/main.py
   ```

5. Ejecutar las pruebas:
   ```bash
   python -m unittest discover tests/
   ```

---

## 📅 Estado del proyecto
=======
<h1>🥊 Fighting for the Grade</h1>
>>>>>>> ce0028a182b07fb40d410d70b85fef34c08071f4

<h2>📖 Descripción del juego</h2>
<p>
Fighting for the Grade (<i>Peleando por la nota</i>) es un juego de pelea uno contra uno (1 vs 1) inspirado en <i>Urban Champion</i> (Nintendo, 1984), con modificaciones en su mecánica central.
</p>

<p>
A diferencia del original, esta versión elimina el sistema de empuje y lo reemplaza por un sistema de combate directo basado en <b>daño y defensa por turnos</b>. Dos jugadores se enfrentan en combate directo: el objetivo es reducir la vida del oponente a cero antes de ser derrotado.
</p>

<hr>

<h2>⚔️ Mecánica principal</h2>
<ul>
  <li>Dos personajes se enfrentan en un escenario.</li>
  <li>Cada uno posee una <b>barra de vida</b>.</li>
  <li>En cada turno, un jugador ataca y el otro decide si bloquear.</li>
  <li>El combate termina cuando la vida de uno llega a cero.</li>
</ul>

<hr>

<h2>👥 Integrantes</h2>
<table>
<tr><th>Nombre</th><th>Apellido</th></tr>
<tr><td>Eliana Jaqueline</td><td>Salvo Austin</td></tr>
<tr><td>Diego Gabriel</td><td>Ponce</td></tr>
<tr><td>Alan</td><td>Walker</td></tr>
</table>

<hr>

<h2>🗂️ Estructura del proyecto</h2>

<pre>
peleando_por_la_nota/
├── controlador/
│   └── controlador.py        (placeholder sin lógica aún)
├── modelo/
│   ├── Jugador.py
│   ├── Personaje.py
│   └── Util.py
├── recursos/
│   ├── Musica/
│   └── Sonidos/
├── test/
│   ├── __init__.py
│   ├── test_jugador.py
│   └── test_personaje.py
├── vista/
│   └── jugador_grafico.py
├── venv/
├── .gitignore
├── main_principal.py
├── main.py
├── README.md
└── requirements.txt
</pre>

<p><b>Nota:</b> La estructura fue reorganizada para comenzar la migración a arquitectura MVC.</p>

<hr>

<h2>🧱 Entidades principales</h2>

<h3>Personaje</h3>
<ul>
  <li>Gestiona la vida</li>
  <li>Recibe daño (sin valores negativos)</li>
  <li>Ataca y bloquea</li>
  <li>Calcula daño (fuerza + ataque)</li>
  <li>Determina si está vivo</li>
</ul>

<h3>Jugador</h3>
<ul>
  <li>Hereda de Personaje</li>
  <li>Representa al usuario</li>
  <li>Muestra estado completo</li>
</ul>

<h3>Ulti</h3>
<p>
Representa la animación final al morir. No afecta la lógica del combate.
</p>

<hr>

<h2>🎨 Decisiones de diseño</h2>

<ul>
  <li><b>Herencia:</b> reutilización mediante Personaje → Jugador</li>
  <li><b>Daño:</b> calculado como fuerza + ataque</li>
  <li><b>Estados:</b> uso de booleanos para ataque y bloqueo</li>
  <li><b>Control de vida:</b> centralizado en recibir_danio()</li>
  <li><b>Separación MVC:</b> sin print() en el modelo</li>
  <li><b>Ulti:</b> encapsula comportamiento con ejecutar()</li>
</ul>

<p><b>Importante:</b> El controlador actualmente no tiene lógica funcional, es solo preparación para MVC.</p>

<hr>

<h2>🔄 Refactorizaciones</h2>

<table>
<tr><th>Elemento</th><th>Cambio</th></tr>
<tr><td>__init__</td><td>Validaciones con bucle</td></tr>
<tr><td>recibir_danio()</td><td>Sin print, retorna 0 al bloquear</td></tr>
<tr><td>estoy_vivo()</td><td>Solo retorna booleano</td></tr>
<tr><td>morir()</td><td>Ejecuta ulti</td></tr>
<tr><td>atacar()</td><td>Retorna daño real</td></tr>
<tr><td>Ulti</td><td>Agrega ejecutar()</td></tr>
</table>

<hr>

<h2>🖥️ Vista en Pygame</h2>
<ul>
  <li>Rectángulos de colores (rojo y azul)</li>
  <li>Texto con vida</li>
  <li>Fondo negro</li>
  <li>Movimiento, colisiones y acciones básicas</li>
</ul>

<hr>

<h2>🎮 Controles</h2>

<table>
<tr><th>Acción</th><th>Jugador 1</th><th>Jugador 2</th></tr>
<tr><td>Mover</td><td>W A S D</td><td>Flechas</td></tr>
<tr><td>Atacar</td><td>F</td><td>L</td></tr>
<tr><td>Bloquear</td><td>E</td><td>K</td></tr>
</table>

<hr>

<h2>🧪 Pruebas</h2>
<p>Se utilizan pruebas unitarias con unittest para validar el modelo de forma independiente.</p>

<ul>
  <li>Daño normal, exceso y exacto</li>
  <li>Bloqueo</li>
  <li>Ataques</li>
  <li>Muerte</li>
</ul>

<hr>

<h2>⚠️ Excepciones</h2>

<ul>
  <li>TypeError: tipos inválidos</li>
  <li>ValueError: valores negativos</li>
  <li>Validación de daño negativo</li>
  <li>Ulti acepta string u objeto</li>
</ul>

<hr>

<h2>🚀 Ejecución</h2>

<pre>
git clone https://github.com/tu-usuario/fighting-for-the-grade.git
cd fighting-for-the-grade

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main_principal.py
</pre>

<hr>

<h2>🧪 Tests</h2>

<pre>
python -m unittest discover test/
</pre>

<hr>

<h2>📅 Estado</h2>

<table>
<tr><th>Entrega</th><th>Estado</th></tr>
<tr><td>Entrega 1</td><td>Completa</td></tr>
<tr><td>Entrega 2</td><td>Completa</td></tr>
</table>

<hr>

<h2>🚀 Próximamente</h2>
<ul>
  <li>Sprites</li>
  <li>Animaciones</li>
  <li>Sonido</li>
  <li>Controlador completo (MVC)</li>
</ul>
