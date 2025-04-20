FROM python:3.11-slim
EXPOSE 8501
WORKDIR /app
COPY . /app/
RUN pip install requests streamlit pandas matplotlib
CMD ["streamlit", "run", "/app/main.py"]