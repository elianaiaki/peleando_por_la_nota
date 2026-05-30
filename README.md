# Fighting for the Grade

Un juego de pelea 1 vs 1 desarrollado en Python con Pygame, inspirado en Urban Champion (Nintendo, 1984), con mecánicas de combate directo basadas en daño y defensa.

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Mecánica principal](#mecánica-principal)
- [Controles](#controles)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Arquitectura MVC](#arquitectura-mvc)
- [Módulos del sistema](#módulos-del-sistema)
- [Sistema de animaciones](#sistema-de-animaciones)
- [Selección de personajes](#selección-de-personajes)
- [Pruebas](#pruebas)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Estado del proyecto](#estado-del-proyecto)
- [Equipo](#equipo)

---

## Descripción

**Fighting for the Grade** reinterpreta la fórmula original de Urban Champion eliminando el sistema de empuje y reemplazándolo por combate directo. Dos jugadores eligen su personaje, se enfrentan en un escenario con paredes, barras de vida y música dinámica: el objetivo es reducir la vida del oponente a cero antes de ser derrotado.

---

## Mecánica principal

Cada jugador posee una barra de vida. En cada frame, uno puede atacar y el otro decidir si bloquear o recibir el daño. El combate finaliza cuando la vida de un jugador llega a cero, desencadenando una animación de derrota con efecto de fade a negro y zoom.

- Daño calculado como `fuerza + ataque`
- El bloqueo anula completamente el daño recibido en ese turno
- Estados de ataque y bloqueo representados con booleanos
- Control centralizado del daño en `recibir_danio()`
- Colisiones entre jugadores: empuje físico con resolución contra paredes
- Música dinámica sincronizada con el estado del juego (menú, pelea, derrota)

---

## Controles

| Acción   | Jugador 1 | Jugador 2 |
|----------|-----------|-----------|
| Mover    | `A` / `D` | ← / →     |
| Atacar   | `F`       | `L`       |
| Bloquear | `E`       | `K`       |

> Mientras un personaje está atacando, siendo golpeado o muriendo, no puede moverse hasta que la animación correspondiente termine.

---

## Estructura del proyecto

```
peleando_por_la_nota/
├── control/
│   ├── controlador.py          # Lógica de eventos, teclas y colisiones
│   ├── controladorGrafico.py   # Renderizado, barras de vida y animación de muerte
│   └── controladorMusica.py    # Gestión de banda sonora por estado
├── modelo/
│   ├── Personaje.py            # Clase base: vida, daño, ataque, bloqueo
│   ├── Jugador.py              # Hereda de Personaje, representa al usuario
│   └── Ulti.py                 # Habilidad definitiva (a uso futuro)
├── recursos/
│   ├── Musica/                 # Canciones de menú, pelea, victoria y derrota
│   ├── Sonidos/
│   └── <personaje>/            # Sprites por estado para cada luchador
├── test/
│   ├── __init__.py
│   ├── test_jugador.py
│   └── test_personaje.py
├── vista/
│   ├── jugador_grafico.py      # Representación visual y física del jugador
│   ├── sprite_jugador.py       # Motor de animaciones por estados
│   ├── seleccionar_personaje.py# Interfaz de selección de personaje
│   └── ulti_grafico.py         # Representación visual de la Ulti (a uso futuro)
├── main.py
├── main_principal.py
├── requirements.txt
└── README.md
```

---

## Arquitectura MVC

El proyecto sigue el patrón **Modelo–Vista–Controlador**:

| Capa | Responsabilidad |
|---|---|
| **Modelo** (`modelo/`) | Lógica pura del combate: vida, daño, estados. Sin `print()` ni dependencias gráficas. |
| **Vista** (`vista/`) | Renderizado de personajes, animaciones, menú de selección y efectos visuales. |
| **Controlador** (`control/`) | Puente entre modelo y vista: procesa entradas del teclado, detecta colisiones y coordina el dibujado. |

---

## Módulos del sistema

### `Personaje.py` — Clase base

Gestiona toda la lógica fundamental de los combatientes:

- Validación estricta en `__init__`: tipos (`TypeError`) y valores negativos (`ValueError`)
- `recibir_danio(danio)`: retorna 0 si está bloqueando; reduce vida y llama a `morir()` si llega a 0
- `calcular_danio()`: retorna `fuerza + ataque`
- `atacar(enemigo)`: verifica que el atacante esté vivo, aplica el daño y retorna el daño real infligido
- `estoy_vivo()`: retorna booleano
- `morir()`: fija vida en 0 y cambia el estado a `"muerto"`

### `Jugador.py` — Usuario jugable

Hereda de `Personaje` sin redefinir la lógica de combate. Agrega `mostrar_estado()`, que devuelve una cadena formateada con nombre, vida actual/máxima, fuerza y ataque.

### `Controlador.py` — Lógica de entrada

- Procesa teclas presionadas frame a frame (`procesar_teclas`)
- Procesa eventos únicos como ataques (`procesar_eventos`)
- Bloquea el movimiento si el jugador está en estado `"atacar"`, `"golpeado"`, `"muriendo"` o `"muerto"`
- Detecta impacto con hitbox dinámica (`obtener_hitbox_ataque`) antes de aplicar daño
- Coordina la interacción **ataque vs. bloqueo**: si el defensor está en estado `"bloquear"`, el ataque no surte efecto

### `ControladorGrafico.py` — Renderizado

- Dibuja escenario, sprites y barras de vida en cada frame
- Barras de vida: tres capas (borde negro, fondo rojo, barra verde proporcional) con nombre y puntos exactos
- **Animación de muerte**: fade a negro progresivo (`alpha += 3` por frame hasta 255), seguido de la imagen de derrota del perdedor con zoom inicial de `2.0` que se reduce gradualmente hasta `1.0`

### `ControladorMusica.py` — Audio dinámico

Centraliza la reproducción con `pygame.mixer`. Cambia de pista automáticamente según el estado del juego:

| Estado  | Comportamiento |
|---------|---------------|
| `menu`  | Loop infinito  |
| `pelea` | Loop infinito  |
| `victoria` | Una sola vez |
| `derrota`  | Una sola vez |

Evita reinicios innecesarios: si el nuevo estado es igual al actual, no interrumpe la pista. Incluye manejo de errores con `try/except` para que el juego no se cierre por archivos de audio faltantes.

### `JugadorGrafico.py` — Vista física del jugador

- Mantiene dos rectángulos: `rect` (60×60, visual) y `col_rect` (40×60, colisiones entre jugadores)
- `mover()`: guarda posición previa, aplica movimiento, revierte si hay colisión con pared o borde; si empuja al enemigo contra una pared, cancela el movimiento de ambos
- `actualizar_direccion(rival)`: voltea todos los frames de animación con `pygame.transform.flip` si el jugador cambia de orientación
- `obtener_hitbox_ataque()`: genera un `pygame.Rect` de 70×80 px hacia adelante del jugador según su dirección actual

---

## Sistema de animaciones

`SpriteJugador` carga hojas de sprites (512×512 px por frame) y las segmenta con `imagen.subsurface()`. Controla el ritmo con un contador interno (`velocidad_animacion = 8` frames por cuadro).

**Estados de animación disponibles:**

| Estado      | Descripción                            |
|-------------|----------------------------------------|
| `quieto`    | Idle                                   |
| `caminar01` | Caminata hacia adelante                |
| `caminar02` | Caminata hacia atrás                   |
| `atacar`    | Golpe                                  |
| `bloquear00/01/02` | Tres fases del bloqueo          |
| `golpeado`  | Recibir impacto                        |
| `muriendo`  | Animación de derrota                   |
| `muerto`    | Frame final estático                   |

Cuando una animación de acción única (`atacar`, `golpeado`, `muriendo`) termina, `actualizar()` devuelve `True` y el bucle principal en `main.py` retorna el estado del jugador a `"quieto"`.

---

## Selección de personajes

Antes del combate, ambos jugadores eligen su luchador en una pantalla de selección con fondo de menú e imágenes de 150×150 px. La selección se realiza con clic del ratón sobre el retrato.

**Personajes disponibles:**

| Nombre  | Vida | Fuerza | Ataque |
|---------|------|--------|--------|
| Eliana  | 100  | 10     | 5      |
| Alan    | 100  | 8      | 6      |
| Gabriel | 100  | 12     | 4      |
| Gabo    | 100  | 15     | 3      |
| Yiyo    | 100  | 11     | 5      |

---

## Pruebas

Las pruebas unitarias utilizan `unittest` y validan el modelo de forma independiente de la vista y el controlador.

```bash
python -m unittest discover test/
```

**Casos cubiertos:**

- Daño normal, exacto y excedente
- Bloqueo de daño
- Lógica de ataque
- Condición de muerte

**Excepciones contempladas:**

- `TypeError` para tipos inválidos en nombre y estadísticas
- `ValueError` para valores negativos
- Validación de daño negativo en `recibir_danio()`
- `Ulti` acepta string u objeto como parámetro

---

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/fighting-for-the-grade.git
cd fighting-for-the-grade

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el juego
python main_principal.py
```

---

## Estado del proyecto

| Entrega   | Estado      |
|-----------|-------------|
| Entrega 1 | ✅ Completa  |
| Entrega 2 | ✅ Completa  |
| Entrega 3 | ✅ Completa  |
| Entrega 4 | ✅ Completa  |

### Próximamente

- Sprites completos para todos los personajes
- Sistema de Ulti funcional integrado al combate
- Controlador MVC completo
- Efectos de sonido adicionales

---

## Equipo

| Nombre           | Apellido     |
|------------------|--------------|
| Eliana Jaqueline | Salvo Austin |
| Diego Gabriel    | Ponce        |
| Alan             | Walker       |
