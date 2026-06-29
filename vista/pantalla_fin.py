class PantallaFinVista:

    def dibujar(self, pantalla, fuente, fondo, opciones, seleccion, mostrar_opciones):
        negro = (0, 0, 0)
        gris = (150, 150, 150)
        amarillo = (255, 220, 0)

        if fondo:
            pantalla.blit(fondo, (0, 0))
        else:
            pantalla.fill(negro)

        if not mostrar_opciones:
            return

        hint = fuente.render("↑ ↓   ENTER para confirmar", True, gris)
        pantalla.blit(hint, (pantalla.get_width() // 2 - hint.get_width() // 2, 400))

        for i, texto in enumerate(opciones):
            color = amarillo if i == seleccion else gris
            label = f"> {texto} <" if i == seleccion else texto

            surf = fuente.render(label, True, color)

            pantalla.blit(
                surf,
                (pantalla.get_width() // 2 - surf.get_width() // 2, 480 + i * 50)
            )