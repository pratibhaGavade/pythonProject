from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def create_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # --- Header ---
 # 1. Logo at top left
    try:
        # Increased 1.0 to 1.3 to move the image lower
        c.drawImage("logo.png", 0.5 * inch, height - 1.3 * inch, width=1.5*inch, preserveAspectRatio=True)
    except:
        c.drawString(0.5 * inch, height - 0.5 * inch, "[Image 'logo.png' not found]")
    # 2. Title next to logo
    c.setFont("Helvetica-Bold", 16)
    # Moved text to the right to be beside the logo
    # c.drawString(2.0 * inch, height - 0.6 * inch, "Project Report")                

    # 3. Line below header
    c.line(0.5 * inch, height - 1.1 * inch, width - 0.5 * inch, height - 1.1 * inch)

    # --- Footer ---
    c.setFont("Helvetica", 8)
    c.drawString(0.5 * inch, 0.5 * inch, "SonarQube Static Analysis Report - Confidential")
    c.drawRightString(width - 0.5 * inch, 0.5 * inch, "Page 1")
    # Optional line above footer
    c.line(0.5 * inch, 0.7 * inch, width - 0.5 * inch, 0.7 * inch)

    # --- Content ---
    c.setFont("Helvetica", 12)
    c.drawString(0.5 * inch, height - 1.5 * inch, "SonarQube results will be populated here.")

  
    c.showPage()
    c.save()
    print(f"PDF generated: {file_path}")

if __name__ == "__main__":
    create_pdf("sonar_report.pdf")