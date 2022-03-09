FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir psycopg2-binary --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

COPY . .

CMD python main.py
