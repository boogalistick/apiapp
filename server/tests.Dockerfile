FROM python:3.7.4

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org

COPY . .

CMD pytest -q
