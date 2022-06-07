FROM  python:3.8.3-alpine

RUN pip3 install --upgrade pip

# Set to a non-root built-in user `fhir`
RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY --chown=myuser:myuser . .

ENV PATH="/home/myuser/.local/bin:${PATH}"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000