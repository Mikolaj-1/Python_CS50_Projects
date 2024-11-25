from fpdf import FPDF,Align
import sys

def main():
    try:
        name=str(input("Name: "))
    except ValueError:
        sys.exit(1)
    pdf = FPDF(orientation="portrait",format=(210,297))
    pdf.add_page( format="A4")
    pdf.set_font('helvetica',"B", 32)
    pdf.cell(0,10, align="C", text="CS50 Shirtificate")
    pdf.image("shirtificate.png",Align.C,52)
    pdf.set_text_color(255,255,255)
    pdf.set_font('helvetica', "B",26)
    pdf.cell(-190,240, align="C",text=name+" took CS50")
    pdf.output("shirtificate.pdf")


main()