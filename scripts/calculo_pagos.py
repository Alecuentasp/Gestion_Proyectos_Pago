# Datos de ejemplo
valor_facturado = 10000
impuesto = 0.11
ganancia = 0.30
gastos_indirectos = 0.15
participacion = {"Juan": 0.4, "Maria": 0.6}

# Paso 1: deducciones
neto = valor_facturado * (1 - impuesto - ganancia - gastos_indirectos)

# Paso 2: fondo salarial
fondo_salarial = neto
salario_bruto_total = fondo_salarial * 0.77

# Paso 3: distribución
for trabajador, porcentaje in participacion.items():
    pago = salario_bruto_total * porcentaje
    print(trabajador, pago)
