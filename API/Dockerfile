FROM Python:3.12.2
COPY requirement.txt /tmp/requirement.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirement.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]