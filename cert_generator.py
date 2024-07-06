from pypdf import PdfReader, PdfWriter
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# from reportlab.pdfbase import pdfmetrics


# Find list of attendees
df_attendees = pd.read_csv(
    "assets\\teams_attendance\\attendance_report_2024_06_19-24.csv", encoding="utf-8"
)

# Change logic so that trainers are excluded
name_list = df_attendees["name"].to_list()

# Look at this again to confirm that they are most useful co-ordinates
horz = 350
vert = 290
for name in name_list:
    packet = io.BytesIO()  # No idea what this code does
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFillColorRGB(255, 255, 255)  # Sets colour of inserted objects to white

    # Use text object instead
    text_object = can.beginText(horz, vert)
    text_object.setFont("Times-Roman", 28)
    text_object.textLine(name)
    can.drawText(text_object)

    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # The certificates currently highlight the text box. Revisit
    cert_template = "assets\level_1_templates\Eleanor.pdf"

    template_pdf = PdfReader(open(cert_template, "rb"))

    output = PdfWriter()
    page = template_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    destination = "certificates" + os.sep + name + ".pdf"
    outputStream = open(destination, "wb")
    output.write(outputStream)
    outputStream.close()
    print("Created " + name + ".pdf")
