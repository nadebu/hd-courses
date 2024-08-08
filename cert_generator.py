from pypdf import PdfReader, PdfWriter
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import streamlit as st


class CertGenerator:

    def __init__(self, level, trainer, crs_date, attendee_df) -> None:
        self.level = level
        self.trainer = trainer
        self.crs_date = crs_date
        self.attendee_df = attendee_df

    def remove_organiser(self):
        """
        Takes in the attendee dataframe and remove any attendee listed as an organizer
        """
        self.attendee_df = self.attendee_df[self.attendee_df["role"] != "Organizer"]

    def generate_certs(self):
        trainee_list = self.attendee_df["name"].to_list()
        course_date = self.crs_date.strftime("%d %B %Y")

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

            template_paths = {
                (
                    "Level 1",
                    "Ashlee",
                ): "templates\\level_1_templates\\Ashlee_Level_1.pdf",
                (
                    "Level 1",
                    "Eleanor",
                ): "templates\\level_1_templates\\Eleanor_Level_1.pdf",
                ("Level 1", "Helen"): "templates\\level_1_templates\\Helen_Level_1.pdf",
                ("Level 1", "Phil"): "templates\\level_1_templates\\Phil_Level_1.pdf",
                (
                    "Level 1",
                    "Rebecca",
                ): "templates\\level_1_templates\\Rebecca_Level_1.pdf",
                (
                    "Level 2",
                    "Ashlee",
                ): "templates\\level_2_templates\\Ashlee_Level_2.pdf",
                (
                    "Level 2",
                    "Eleanor",
                ): "templates\\level_2_templates\\Eleanor_Level_2.pdf",
                ("Level 2", "Helen"): "templates\\level_2_templates\\Helen_Level_2.pdf",
                ("Level 2", "Phil"): "templates\\level_2_templates\\Phil_Level_2.pdf",
                (
                    "Level 2",
                    "Rebecca",
                ): "templates\\level_2_templates\\Rebecca_Level_2.pdf",
            }

            cert_template = template_paths.get((self.level, self.trainer))

            template_pdf = PdfReader(open(cert_template, "rb"))

            output = PdfWriter()
            page = template_pdf.pages[0]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)
            destination = "certificates" + os.sep + name + ".pdf"
            outputStream = open(destination, "wb")
            output.write(outputStream)
            outputStream.close()
            st.write("Created " + name + ".pdf")
