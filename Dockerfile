#Using python
FROM: python:2.7-slim

# Install requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt
