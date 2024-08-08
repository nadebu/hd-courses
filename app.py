from datetime import date
import pandas as pd
import streamlit as st

from event_manager import EventManager
from cert_generator import CertGenerator
from trainer_manager import TrainerManager

# event_manager = EventManager()
# print(event_manager.get_org_events())



# trainer_manager = TrainerManager()
# print(trainer_manager.get_trainers())


today = date.today()

st.title("Certicate Generator")
st.subheader(
    "This resource will generate certificates for the Norfolk MECC Level 1 and 2 training"
)

# Currently asking the input to add the level and trainer manually,
# but later iterations will tap into the various data sources to have this autopopulated
# the use will then be asked to confirm

# Add level of training
level_option = st.radio(
    "What level of training is this for?",
    ("Level 1", "Level 2"),
)

trainer_option = st.radio(
    "Who was the lead trainer for the course?",
    ("Ashlee", "Eleanor", "Helen", "Phil", "Rebecca"),
)

course_date = st.date_input(
    "Select the date for the training", today, format="DD/MM/YYYY"
)

uploaded_file = st.file_uploader("Now upload a file of attendees - Usually a MS Teams list of attendees", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Determine the file type and read accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('xlsx'):
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    # Display the contents of the file
    st.write("Here are the contents of the uploaded file. Note that when the certificates are generated, no certificate will be produced for anyone with the role of `organiser`:")
    st.dataframe(df)
else:
    st.write("Please upload either a csv or Excel file")

st.divider()

st.write(
    f"We will proceed to create {level_option} certificates, with {trainer_option} as the trainer for the date of {course_date.strftime("%d %B %Y")}"
)

st.divider()

if st.button("Press to generate certicates"):
    st.write("Certificates are being generated")

    cert_generator = CertGenerator(level=level_option, trainer=trainer_option, crs_date=course_date, attendee_df=df)
    cert_generator.remove_organiser()
    cert_generator.generate_certs()

