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


num1 = float(input("\nIntroduce el ancho 1: "))
num2 = float(input("Introduce el largo 1: "))
num3 = float(input("Introduce el ancho 2: "))
num4 = float(input("Introduce el largo 2: "))

res1 = (num1 / 2) + num2
res2 = num2 / 2
res3 = num3 / 2
res4 = (num4 / 2) + num3

print("\nResultados clichés:\n")
print(f"| {res1} | {res2} | {res3} | {res4} |")

res1 = num1 + num2 - 30
res2 = num2 - 30
res3 = num3 - 30
res4 = num4 + num3 - 30

print("\nResultados pap:\n")
print(f"| {res1} | {res2} | {res3} | {res4} |\n")


sino = input("¿Quieres calcular altura? s/n: ")
if sino.lower() == "s":
    nume1 = float(input("\nIntroduce el primer número: "))
    nume2 = float(input("Introduce el segundo: "))
    nume3 = float(input("Introduce el tercero: "))
    resulaltura = ((nume1 / 2) + (nume3 / 2)) + nume2
    print(f"\nResultado altura: {resulaltura}")
else:
    print("Calculo de altura omitido")
