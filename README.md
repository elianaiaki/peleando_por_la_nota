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

---

## 🎨 Decisiones de diseño

**Herencia:** Se optó por una jerarquía `Personaje → Jugador` para evitar duplicación de código. Todos los combatientes comparten comportamientos comunes (atacar, recibir daño, bloquear, morir), que se centralizan en la clase base.

**Separación de atributos de daño:** El daño no es un valor fijo. Se calcula como `fuerza + ataque`, donde `fuerza` es una característica base del personaje y `ataque` representa su capacidad ofensiva en cada acción.

**Estados booleanos:** Se usan `esta_atacando` y `esta_bloqueando` para representar el estado actual del personaje en el turno. Esto permite, por ejemplo, que un bloqueo activo absorba el daño entrante antes de que se reduzca la vida.

**Control de vida:** La vida nunca puede ser negativa. La lógica de reducción está centralizada en `recibir_danio()` como único punto de control.

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

<p>
Esta es la <strong>Entrega 1</strong> del trabajo final. En esta etapa se implementó el modelo base del dominio del juego 
(clases, atributos, métodos, pruebas y excepciones).
</p>

<p>
Aún no se incluye interfaz visual, integración MVC, sprites ni persistencia.
</p>

<p>
Las próximas entregas incorporarán la vista, el controlador y la versión jugable del juego.
</p>

<hr>

<h3>🚀 Adelanto de futura entrega</h3>

<h4>🎮 Sprites</h4>

<div style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">

  <div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/95418139-344f-4f94-9890-2f2b9219ab93" width="150">
    <p><strong>Gabriel</strong></p>
  </div>

  <div style="text-align: center;">
    <img src="https://github.com/user-attachments/assets/22c1450b-a59f-4469-a5c8-a13a12141b08" width="150">
    <p><strong>Eliana</strong></p>
  </div>

</div>

<hr>

<h4>🎵 Música</h4>

<ul>
    <li><a href="https://github.com/user-attachments/files/26414228/Cancion.de.Menu.mp3">🎧 Canción de Menú</a></li>
    <li><a href="https://github.com/user-attachments/files/26414225/Cancion.de.Derrota.mp3">💀 Canción de Derrota</a></li>
    <li><a href="https://github.com/user-attachments/files/26414222/Cancion.de.Victoria.mp3">🏆 Canción de Victoria</a></li>
    <li><a href="https://github.com/user-attachments/files/26414218/Cancion.de.Pelea.mp3">⚔️ Canción de Pelea</a></li>
</ul>

<hr>

<p style="font-style: italic; color: gray;">
💡 Próximamente: interfaz gráfica, animaciones y jugabilidad completa.
</p>

