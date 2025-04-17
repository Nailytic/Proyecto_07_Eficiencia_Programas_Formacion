import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF

# Cargar datos
df = pd.read_csv("data/cohortes_formativas.csv")

# Crear gráfico de retención por programa
plt.figure(figsize=(10, 5))
sns.boxplot(x="Programa", y="Retencion_%", data=df)
plt.title("Tasa de Retención por Programa Formativo")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("images/grafico_retencion.png")
plt.close()

# Generar informe resumen en PDF
resumen = df.groupby("Programa").agg({
    "Retencion_%": "mean",
    "Finalizacion_%": "mean",
    "Satisfaccion": "mean"
}).round(2)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Informe de Eficiencia de Programas Formativos", ln=True, align="C")
pdf.ln(10)

for prog in resumen.index:
    r = resumen.loc[prog]
    pdf.cell(200, 10, f"{prog}: Retención {r['Retencion_%']}%, Finalización {r['Finalizacion_%']}%, Satisfacción {r['Satisfaccion']']}", ln=True)

pdf.output("output/informe_eficiencia.pdf")
print("Análisis finalizado.")
