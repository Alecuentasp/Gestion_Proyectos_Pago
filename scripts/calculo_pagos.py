import os
import pandas as pd

def calcular_pagos(input_csv, output_excel):
    # Crear carpeta de salida si no existe
    os.makedirs(os.path.dirname(output_excel), exist_ok=True)

    # Leer datos de facturación
    df = pd.read_csv(input_csv)

    resultados = []

    for _, fila in df.iterrows():
        valor = fila['Valor_Facturado']
        impuesto = fila['Impuesto(%)'] / 100
        ganancia = fila['Ganancia(%)'] / 100
        gastos = fila['Gastos_Indirectos(%)'] / 100
        participacion = fila['Participacion(%)'] / 100

        # Fondo salarial
        fondo = valor * (1 - impuesto - ganancia - gastos)

        # Salario bruto total (77%)
        salario_bruto_total = fondo * 0.77

        # Pago por trabajador
        pago = salario_bruto_total * participacion

        resultados.append({
            "Proyecto": fila['Proyecto'],
            "Etapa": fila['Etapa'],
            "Trabajador": fila['Trabajador'],
            "Valor Facturado": valor,
            "Fondo Salarial": round(fondo, 2),
            "Salario Bruto Total": round(salario_bruto_total, 2),
            "Pago Asignado": round(pago, 2)
        })

    # Convertir a DataFrame y exportar
    reporte = pd.DataFrame(resultados)
    reporte.to_excel(output_excel, index=False)

if __name__ == "__main__":
    calcular_pagos("data/ejemplo_facturacion.csv", "reports/reporte_mensual.xlsx")
