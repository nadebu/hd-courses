FROM python:3

# set the working directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy the scripts to the folder
COPY . /app

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]