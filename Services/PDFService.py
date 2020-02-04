from fpdf import FPDF

headers=["nazwa", "wynik pacjenta", "minimalny zakres","maksymalny zakres","jednostka"]
 
def add_title(title: str, pdf: FPDF):
    pdf.set_font("calibri", style="B", size=16)
    pdf.cell(pdf.w, pdf.font_size, txt=title, align="C")
    pdf.ln(3*pdf.font_size)

def add_headers(headers: list, pdf: FPDF):
    pdf.set_font("calibri", style="B", size=10)
    pdf.cell(pdf.w*0.18*0.05, pdf.font_size, txt="")
    for header in headers:
        pdf.cell(pdf.w*0.18, txt=header, align="C")
    pdf.ln(1.5*pdf.font_size)

def add_data(elements: list, pdf: FPDF):
    pdf.set_font("calibri", style="", size=10)
    for element in elements:
        pdf.cell(pdf.w*0.18*0.05, pdf.font_size, txt="")
        for cell in element:
            pdf.cell(pdf.w*0.18, pdf.font_size, txt=cell, align="C")
        pdf.ln(1.25*pdf.font_size)


def generate_pdf(elements: list): 
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('calibri', '', './calibri.ttf', uni=True)
    pdf.add_font('calibri', 'B', './calibrib.ttf', uni=True)
    add_title("Klasyfikacja", pdf)
    add_headers(headers, pdf)
    add_data(my_list,pdf)
    pdf.output("test.pdf")

my_list=[["panda", "8", "8", "8", "miś"], ["kot","8", "8", "8","głupi", "zesraniec"], ["pająk", "8", "8", "8","straszny", "stwór"]]
  
generate_pdf(my_list)
    