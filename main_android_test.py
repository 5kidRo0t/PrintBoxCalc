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


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PrintBoxCalc(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.inputs = []
        for label in ["Ancho 1", "Largo 1", "Ancho 2", "Largo 2"]:
            self.add_widget(Label(text=label))
            inp = TextInput(multiline=False, input_filter='float')
            self.inputs.append(inp)
            self.add_widget(inp)

        self.calc_button = Button(text="Calcular Resultados", size_hint=(1, 0.3))
        self.calc_button.bind(on_press=self.calculate)
        self.add_widget(self.calc_button)

        self.result_label = Label(text="", halign="center")
        self.add_widget(self.result_label)

        self.height_button = Button(text="Calcular Altura", size_hint=(1, 0.3))
        self.height_button.bind(on_press=self.calculate_height_popup)
        self.add_widget(self.height_button)

    def calculate(self, instance):
        try:
            n1 = float(self.inputs[0].text)
            n2 = float(self.inputs[1].text)
            n3 = float(self.inputs[2].text)
            n4 = float(self.inputs[3].text)

            res_cliché = [(n1 / 2) + n2, n2 / 2, n3 / 2, (n4 / 2) + n3]
            res_pap = [n1 + n2 - 30, n2 - 30, n3 - 30, n4 + n3 - 30]

            self.result_label.text = (
                f"\n[Cliché] {res_cliché}\n[PAP] {res_pap}"
            )

        except ValueError:
            self.result_label.text = "Introduce todos los valores correctamente."

    def calculate_height_popup(self, instance):
        from kivy.uix.popup import Popup
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        inputs = []
        for label in ["Solapa 1", "Solapa 2", "Solapa 3"]:
            layout.add_widget(Label(text=label))
            inp = TextInput(multiline=False, input_filter='float')
            inputs.append(inp)
            layout.add_widget(inp)

        result = Label(text="")
        layout.add_widget(result)

        def calc(_):
            try:
                a, b, c = float(inputs[0].text), float(inputs[1].text), float(inputs[2].text)
                r = ((a / 2) + (c / 2)) + b
                result.text = f"Altura: {r}"
            except:
                result.text = "Error en los valores."

        btn = Button(text="Calcular")
        btn.bind(on_press=calc)
        layout.add_widget(btn)

        popup = Popup(title="Calcular Altura", content=layout, size_hint=(0.8, 0.8))
        popup.open()


class PrintBoxCalcApp(App):
    def build(self):
        return PrintBoxCalc()

if __name__ == '__main__':
    PrintBoxCalcApp().run()