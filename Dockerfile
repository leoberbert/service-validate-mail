FROM cgr.dev/chainguard/wolfi-base as builder

RUN apk add python3~3.11 py3.11-pip
RUN adduser -D -u 65332 leoberbert
USER leoberbert
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --user

FROM cgr.dev/chainguard/wolfi-base

RUN apk add python3~3.11
RUN adduser -D -u 65332 leoberbert
WORKDIR /app

COPY --from=builder /home/leoberbert/.local/lib/python3.11/site-packages /home/leoberbert/.local/lib/python3.11/site-packages

USER leoberbert
COPY service-validate-mail.py blacklist.conf .

WORKDIR /app

ENTRYPOINT [ "python", "/app/service-validate-mail.py" ]
