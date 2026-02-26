FROM --platform=linux/amd64 python:3.11-slim


WORKDIR /app

RUN pip install pipenv

# copy dependency file dulu
COPY Pipfile Pipfile.lock ./
#  kalau pakai -- system nanti pas running tidak perlu pakai pipenv
# RUN pipenv install --system --deploy
RUN pipenv install --deploy

# copy source code
COPY . .

# expose port
EXPOSE 5000

# start server dengan gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]