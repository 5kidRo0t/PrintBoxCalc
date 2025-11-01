# PrintBoxCalc
# Copyright (c) 2025 5kidRo0t
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class PrintBoxCalc(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Entradas principales
        self.num1 = toga.TextInput(placeholder='Ancho 1', style=Pack(padding=5))
        self.num2 = toga.TextInput(placeholder='Largo 1', style=Pack(padding=5))
        self.num3 = toga.TextInput(placeholder='Ancho 2', style=Pack(padding=5))
        self.num4 = toga.TextInput(placeholder='Largo 2', style=Pack(padding=5))

        # Botón principal
        calc_button = toga.Button(
            'Calcular',
            on_press=self.calcular,
            style=Pack(padding=10)
        )

        # Etiqueta de resultados
        self.result_label = toga.Label(
            'Resultados:',
            style=Pack(padding=10, font_size=15, font_weight='bold', color='black')
        )

        # Añadir widgets al layout principal
        for widget in [
            self.num1, self.num2, self.num3, self.num4,
            calc_button, self.result_label
        ]:
            main_box.add(widget)

        # Ventana principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calcular(self, widget):
        """Calcula los resultados de clichés y los muestra en pantalla."""
        try:
            num1 = float(self.num1.value)
            num2 = float(self.num2.value)
            num3 = float(self.num3.value)
            num4 = float(self.num4.value)

            # Cálculos de clichés
            res1 = (num1 / 2) + num2
            res2 = num2 / 2
            res3 = num3 / 2
            res4 = (num4 / 2) + num3

            resultados = f"Clichés:\n| {res1:.2f} | {res2:.2f} | {res3:.2f} | {res4:.2f} |"
            self.result_label.text = resultados

        except ValueError:
            self.result_label.text = "⚠️ Introduce solo números válidos."


def main():
    return PrintBoxCalc("PrintBoxCalc", "com.example.printboxcalc")


if __name__ == "__main__":
    main().main_loop()
