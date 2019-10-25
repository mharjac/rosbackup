FROM python:3.8-slim
WORKDIR /tmp
COPY . ./rosbackup/
RUN pip3 install ./rosbackup && rm -rf /tmp/rosbackup
WORKDIR /backup
CMD ["rosbackup"]


