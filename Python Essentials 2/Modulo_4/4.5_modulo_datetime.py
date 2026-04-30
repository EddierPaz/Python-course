# ============================================================
# 4.5 El Módulo datetime
# ============================================================
# El modulo datetime maneja fechas, horas y diferencias de tiempo.
# Clases principales: date, time, datetime, timedelta.
# ============================================================

from datetime import date, time, datetime, timedelta

# --- Ejemplo 1: Crear y mostrar fechas ---
print("Ejemplo 1 - Fechas con date:")

hoy = date.today()
print("  Hoy:", hoy)
print("  Año:", hoy.year, "| Mes:", hoy.month, "| Dia:", hoy.day)

nacimiento = date(2000, 6, 15)
print("  Fecha nacimiento:", nacimiento)

dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
print("  Dia de la semana:", dias_semana[nacimiento.weekday()])


# --- Ejemplo 2: Calcular diferencias con timedelta ---
print("\nEjemplo 2 - Diferencias de tiempo (timedelta):")

hoy = date.today()
aniversario = date(hoy.year, 12, 31)
dias_restantes = aniversario - hoy
print("  Dias hasta fin de año:", dias_restantes.days)

hace_30_dias = hoy - timedelta(days=30)
print("  Hace 30 dias:", hace_30_dias)

proxima_semana = hoy + timedelta(weeks=1)
print("  Proxima semana:", proxima_semana)


# --- Ejemplo 3: datetime combina fecha y hora ---
print("\nEjemplo 3 - datetime (fecha + hora):")

ahora = datetime.now()
print("  Ahora:", ahora)
print("  Solo fecha:", ahora.date())
print("  Solo hora:", ahora.time())

reunion = datetime(2025, 3, 15, 10, 30, 0)
print("  Reunion programada:", reunion)
diferencia = reunion - ahora
print("  Dias hasta la reunion:", diferencia.days)


# --- Ejemplo 4: Formatear y parsear fechas ---
# strftime() convierte datetime a cadena con formato personalizado.
# strptime() convierte una cadena a datetime.

print("\nEjemplo 4 - Formatear y parsear fechas:")

ahora = datetime.now()

formatos = [
    ("%d/%m/%Y", "dia/mes/año"),
    ("%Y-%m-%d", "ISO 8601"),
    ("%d de %B de %Y", "formato largo"),
    ("%H:%M:%S", "solo hora"),
    ("%A, %d %B %Y", "dia y fecha completa"),
]

for fmt, desc in formatos:
    print(f"  {desc}: {ahora.strftime(fmt)}")

# Parsear cadena a datetime
texto_fecha = "25/12/2024"
fecha_navidad = datetime.strptime(texto_fecha, "%d/%m/%Y")
print("\n  Navidad parseada:", fecha_navidad.date())
