FROM python:3.11-slim
EXPOSE 8080
WORKDIR /app
COPY . /app/
RUN pip install requests streamlit pandas
CMD ["streamlit", "run main.py"]