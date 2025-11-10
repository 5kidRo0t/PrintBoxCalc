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
from toga.style.pack import COLUMN, ROW


class PrintBoxCalc(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        label_style = Pack(
            width=100,
            padding_right=10,
            font_size=14,
            font_weight='bold',
            color='#333333'
        )

        fila1 = toga.Box(style=Pack(direction=ROW, padding=5))
        fila1.add(toga.Label('Ancho 1:', style=label_style))
        self.num1 = toga.NumberInput(style=Pack(flex=1))
        fila1.add(self.num1)

        fila2 = toga.Box(style=Pack(direction=ROW, padding=5))
        fila2.add(toga.Label('Largo 1:', style=label_style))
        self.num2 = toga.NumberInput(style=Pack(flex=1))
        fila2.add(self.num2)

        fila3 = toga.Box(style=Pack(direction=ROW, padding=5))
        fila3.add(toga.Label('Ancho 2:', style=label_style))
        self.num3 = toga.NumberInput(style=Pack(flex=1))
        fila3.add(self.num3)

        fila4 = toga.Box(style=Pack(direction=ROW, padding=5))
        fila4.add(toga.Label('Largo 2:', style=label_style))
        self.num4 = toga.NumberInput(style=Pack(flex=1))
        fila4.add(self.num4)

        calc_button = toga.Button(
            'Calcular',
            on_press=self.calcular,
            style=Pack(padding=10, background_color="#dcdcdc")
        )

        self.result_label = toga.Label(
            'Resultados:',
            style=Pack(padding=10, font_size=15, font_weight='bold', color='black')
        )

        reset_button = toga.Button(
            'Restablecer',
            on_press=self.resetear,
            style=Pack(padding=10, background_color="#ffcccc")
        )

        for fila in [fila1, fila2, fila3, fila4, calc_button, self.result_label, reset_button]:
            main_box.add(fila)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calcular(self, widget):
        try:
            num1 = float(self.num1.value)
            num2 = float(self.num2.value)
            num3 = float(self.num3.value)
            num4 = float(self.num4.value)

            res1 = (num1 / 2) + num2
            res2 = num2 / 2
            res3 = num3 / 2
            res4 = (num4 / 2) + num3

            papizq1 = (num1 - 35) + num2
            papizq2 = num2 - 35
            papizq3 = 35
            papizq4 = num3 + 35

            papder1 = num2 + 35
            papder2 = 35
            papder3 = num3 - 35
            papder4 = (num4 - 35) + num3

            resultados = (
                f"Clichés:\n<| {res1:.2f} | {res2:.2f} | {res3:.2f} | {res4:.2f} |\n\n"
                f"PAP a la izquierda:\n<| {papizq1:.2f} | {papizq2:.2f} | {papizq3:.2f} | {papizq4:.2f} |\n\n"
                f"PAP a la derecha:\n<| {papder1:.2f} | {papder2:.2f} | {papder3:.2f} | {papder4:.2f} |\n\n"
                f"Asas:\n | {res4:.2f} | {res3:.2f} | {res2:.2f} | {res1:.2f} |>\n"
            )
            self.result_label.text = resultados

        except (ValueError, TypeError):
            self.result_label.text = "⚠️ Introduce solo números válidos."

    def resetear(self, widget):
        """Restaura los campos y el resultado sin cerrar la app."""
        try:
            self.num1.value = ""
            self.num2.value = ""
            self.num3.value = ""
            self.num4.value = ""
            self.result_label.text = "Resultados:"
        except Exception as e:
            print("Error al restablecer:", e)


def main():
    return PrintBoxCalc("PrintBoxCalc", "com.example.printboxcalc")


if __name__ == "__main__":
    main().main_loop()