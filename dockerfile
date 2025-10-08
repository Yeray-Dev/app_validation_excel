FROM python:3.11-slim

WORKDIR /home/student

COPY  . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev\
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    streamlit \
    streamlit-aggrid \
    pandas \
    openpyxl \
    sqlalchemy \
    bcrypt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker run -it --rm -p 8501:8501 -v ${PWD}:/home/student facturas-validator /bin/bash