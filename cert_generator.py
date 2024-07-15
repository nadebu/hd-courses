from pypdf import PdfReader, PdfWriter
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
import tkinter as tk
from tkinter import filedialog as fd


class CertGenerator:

    def load_file(self):
        # Create a Tkinter root window (it will not be shown)
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Open a file dialog to select the Excel or CSV file
        file_path = fd.askopenfilename(
            title="Select an Excel or CSV file",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")],
        )

        # Check if a file was selected
        if not file_path:
            print("No file selected.")
            return None

        # Determine the file type and read the file into a pandas DataFrame
        if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            df = pd.read_excel(file_path, engine="openpyxl")
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            print("Unsupported file type.")
            return None

        # Check if the DataFrame is loaded and print the first few rows
        if df is not None:
            print("File loaded successfully!")
            return df
        else:
            print("Failed to load the file.")

    def generate_certs(self):
        df_attendees = self.load_file()
        df_attendees = df_attendees[
            df_attendees["role"] != "Organizer"
        ]  # To exclude trainer
        trainee_list = df_attendees["name"].to_list()
        course_date = date.today().strftime("%d %B %Y")

        pos1 = (340, 290)
        pos2 = (360, 173)
        for name in trainee_list:
            packet = io.BytesIO()  # No idea what this code does
            can = canvas.Canvas(packet, pagesize=A4)
            can.setFillColorRGB(
                255, 255, 255
            )  # Sets colour of inserted objects to white

            # Insert name
            text_object1 = can.beginText(pos1[0], pos1[1])
            text_object1.setFont("Times-Roman", 28)
            text_object1.textLine(name)
            can.drawText(text_object1)

            # Insert date
            text_object2 = can.beginText(pos2[0], pos2[1])
            text_object2.setFont("Times-Roman", 22)
            text_object2.textLine(course_date)
            can.drawText(text_object2)

            can.save()
            packet.seek(0)
            new_pdf = PdfReader(packet)

            # The certificates currently highlight the text box. Revisit
            cert_template = "assets\\level_1_templates\\Eleanor.pdf"

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
