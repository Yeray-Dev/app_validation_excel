FROM python:3.11

WORKDIR /home/student

COPY . .

RUN apt-get update && apt-get install -y \
    python3-dev \
    libffi-dev \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    streamlit==1.50.0 \
    streamlit-aggrid==0.3.4.post3 \
    pandas==2.3.3 \
    openpyxl==3.1.5 \
    sqlalchemy==2.0.43 \
    bcrypt==4.2.0

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker run -it --rm -p 8501:8501 -v ${PWD}:/home/student facturas-validator /bin/bash