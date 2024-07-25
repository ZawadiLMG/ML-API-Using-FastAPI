FROM Python:3.12.2
COPY requirement.txt /tmp/requirement.txt
RUN python -m pip install -r /tmp/requirement.txt
COPY . /app
WORKDIR /app
EXPOSE 8501
CMD ["streamlit","run","main.py","--server.port=8501"]