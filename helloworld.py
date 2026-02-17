from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def create_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # --- Header ---
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1 * inch, height - 0.5 * inch, "Project Report")
    c.line(1 * inch, height - 0.6 * inch, width - 1 * inch, height - 0.6 * inch)

    # --- Footer ---
    c.setFont("Helvetica", 10)
    c.drawString(1 * inch, 0.5 * inch, "Generated in GitHub Codespaces")
    c.drawRightString(width - 1 * inch, 0.5 * inch, "Page 1")

    # --- Content: Text ---
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1 * inch, "Hello World! This PDF was generated in a Codespace.")

    # --- Content: Image ---
    # Make sure to upload 'logo.png' to your workspace first
    try:
        c.drawImage("logo.png", 1 * inch, height - 3 * inch, width=2*inch, preserveAspectRatio=True)
    except:
        c.drawString(1 * inch, height - 2 * inch, "[Image 'logo.png' not found]")

    c.showPage()
    c.save()
    print(f"PDF generated: {file_path}")

if __name__ == "__main__":
    create_pdf("output.pdf")