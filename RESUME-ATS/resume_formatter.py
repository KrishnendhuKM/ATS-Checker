# resume_formatter.py

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "ATS-Friendly Resume", ln=True, align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 10, content)
        self.ln(2)

def generate_pdf(name, email, experience, skills):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_section("Name", name)
    pdf.add_section("Email", email)
    pdf.add_section("Experience", experience)
    pdf.add_section("Skills", ", ".join(skills))

    output_path = f"{name.replace(' ', '_')}_ATS_Resume.pdf"
    pdf.output(output_path)

    return output_path
