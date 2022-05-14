FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY = 'jf38fu3gu0thjr493tjgkbkgrt67'
ENV DB_NAME=meteo
ENV DB_USER=postgres
ENV DB_SECRET=Akiq8exp
ENV DB_HOST=postgres
RUN apt-get update && apt-get install -y \
  && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt
COPY /projectX/projectXback/ .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
