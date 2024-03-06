from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mn", format="A4")

data = pd.read_csv("resource/topics.csv")

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Time", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)


pdf.output("output.pdf")