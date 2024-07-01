From python:3.9-slim
RUN sudo yum install python3-devel mysql-devel pkgconfig
RUN RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]