# ============================================================
# 4.6 El Módulo calendar
# ============================================================
# El modulo calendar permite generar calendarios, verificar
# años bisiestos y obtener informacion sobre dias y semanas.
# ============================================================

import calendar

# --- Ejemplo 1: Mostrar calendarios de texto ---
print("Ejemplo 1 - Calendarios de texto:")

# Calendario de un mes especifico
print(calendar.month(2025, 1))

# Cabecera de la semana
print("Cabecera (2 chars):", calendar.weekheader(2))
print("Cabecera (3 chars):", calendar.weekheader(3))


# --- Ejemplo 2: Años bisiestos ---
print("Ejemplo 2 - Anos bisiestos:")

anos = [2020, 2021, 2022, 2024, 2100, 2000]
for ano in anos:
    es_bisiesto = calendar.isleap(ano)
    simbolo = "SI" if es_bisiesto else "NO"
    print(f"  {ano}: {simbolo} es bisiesto")

print("  Bisiestos entre 2000 y 2030:", calendar.leapdays(2000, 2031))


# --- Ejemplo 3: Dia de la semana y primer dia del mes ---
print("\nEjemplo 3 - Dia de la semana:")

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

fechas = [(2025, 1, 1), (2025, 7, 4), (2024, 12, 25)]
for ano, mes, dia in fechas:
    num_dia = calendar.weekday(ano, mes, dia)
    print(f"  {dia:02d}/{mes:02d}/{ano} es: {dias[num_dia]}")

# monthrange devuelve (primer_dia_semana, total_dias)
primer_dia, total_dias = calendar.monthrange(2025, 2)
print(f"\n  Febrero 2025:")
print(f"    Empieza en: {dias[primer_dia]}")
print(f"    Total dias: {total_dias}")


# --- Ejemplo 4: Clase Calendar para iteracion ---
print("\nEjemplo 4 - Clase Calendar:")

c = calendar.Calendar(firstweekday=0)  # 0 = Lunes

# Dias de la semana como numeros
print("  Dias semana (0=Lun):", list(c.iterweekdays()))

# Semanas del mes de enero 2025
print("  Semanas de enero 2025 (dia, dia_semana):")
for semana in c.monthdays2calendar(2025, 1):
    dias_semana_str = []
    for dia, num_dia in semana:
        if dia != 0:
            dias_semana_str.append(f"{dia:2d}({dias[num_dia][:3]})")
    if dias_semana_str:
        print("   ", " | ".join(dias_semana_str))
