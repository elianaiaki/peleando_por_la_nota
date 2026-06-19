# =====================================================================
# config.py — Constantes y configuración global del juego
# =====================================================================
 
# -----------------------------
# PANTALLA
# -----------------------------
ANCHO = 800
ALTO = 600
 
# -----------------------------
# COLORES
# -----------------------------
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
 
# -----------------------------
# SPRITES — configuración por personaje
# Formato de cada animación: (ruta, ancho_frame, alto_frame, columnas, escala)
# -----------------------------
SPRITES_CONFIG = {

    "alan": {
        "quieto":     ("recursos/alan/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/alan/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/alan/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/alan/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/alan/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/alan/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/alan/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/alan/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/alan/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/alan/golpeado.png",   512, 512,  3, 1.0),
        "festejo01":  ("recursos/alan/festejo01.png",  512, 512, 14, 1.0)
    },

    "eliana": {
        "quieto":     ("recursos/eliana/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/eliana/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/eliana/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/eliana/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/eliana/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/eliana/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/eliana/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/eliana/muriendo.png",   512, 512,  7, 1.0),
        "muerto":     ("recursos/eliana/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/eliana/golpeado.png",   512, 512,  3, 1.0),
        "festejo01":  ("recursos/eliana/festejo01.png",  512, 512, 12, 1.0)
    },

    "gabriel": {
        "quieto":     ("recursos/gabriel/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/gabriel/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/gabriel/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/gabriel/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/gabriel/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/gabriel/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/gabriel/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/gabriel/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/gabriel/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/gabriel/golpeado.png",   512, 512,  3, 1.0),
        "festejo01":  ("recursos/gabriel/festejo01.png",  512, 512, 15, 1.0)
    },

    "gabo": {
        "quieto":     ("recursos/gabo/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/gabo/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/gabo/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/gabo/atacar.png",     512, 512,  8, 1.0),
        "bloquear00": ("recursos/gabo/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/gabo/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/gabo/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/gabo/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/gabo/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/gabo/golpeado.png",   512, 512,  3, 1.0),
        "festejo01":  ("recursos/gabo/festejo01.png",  512, 512, 12, 1.0)
    },

    "yiyo": {
        "quieto":     ("recursos/yiyo/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/yiyo/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/yiyo/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/yiyo/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/yiyo/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/yiyo/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/yiyo/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/yiyo/muriendo.png",   512, 512,  7, 1.0),
        "muerto":     ("recursos/yiyo/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/yiyo/golpeado.png",   512, 512,  3, 1.0),
        # -remplazar cuando este el de yiyo----------------------------
        "festejo01":  ("recursos/alan/festejo01.png",  512, 512, 14, 1.0)
    },

    "cliver": {
        "quieto":     ("recursos/cliver/quieto.png",     512, 512, 12, 1.0),
        "caminar01":  ("recursos/cliver/caminar01.png",  512, 512,  8, 1.0),
        "caminar02":  ("recursos/cliver/caminar02.png",  512, 512,  8, 1.0),
        "atacar":     ("recursos/cliver/atacar.png",     512, 512,  7, 1.0),
        "bloquear00": ("recursos/cliver/bloquear00.png", 512, 512,  1, 1.0),
        "bloquear01": ("recursos/cliver/bloquear01.png", 512, 512,  8, 1.0),
        "bloquear02": ("recursos/cliver/bloquear02.png", 512, 512,  8, 1.0),
        "muriendo":   ("recursos/cliver/muriendo.png",   512, 512,  6, 1.0),
        "muerto":     ("recursos/cliver/muerto.png",     512, 512,  1, 1.0),
        "golpeado":   ("recursos/cliver/golpeado.png",   512, 512,  3, 1.0),
        # -remplazar cuando este el de yiyo----------------------------
        "festejo01":  ("recursos/alan/festejo01.png",  512, 512, 14, 1.0)
    },






    "profe": {
        "quieto":     ("recursos/profe/quieto.png",     512, 512, 12, 1.2),
        "caminar01":  ("recursos/profe/caminar01.png",  512, 512,  8, 1.2),
        "caminar02":  ("recursos/profe/caminar02.png",  512, 512,  8, 1.2),
        "atacar":     ("recursos/profe/atacar.png",     512, 512,  7, 1.2),
        "bloquear00": ("recursos/profe/bloquear00.png", 512, 512,  1, 1.2),
        "bloquear01": ("recursos/profe/bloquear01.png", 512, 512,  8, 1.2),
        "bloquear02": ("recursos/profe/bloquear02.png", 512, 512,  8, 1.2),
        "muriendo":   ("recursos/profe/muriendo.png",   512, 512,  6, 1.2),
        "muerto":     ("recursos/profe/muerto.png",     512, 512,  1, 1.2),
        "golpeado":   ("recursos/profe/golpeado.png",   512, 512,  3, 1.2),
        # -----------------------------
        "festejo01":  ("recursos/alan/festejo01.png",  512, 512, 14, 1.0)
    }
}