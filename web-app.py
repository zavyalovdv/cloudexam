#!/usr/bin/python3

from flask import Flask, request
import tomllib
import psycopg2
import time
import math

app = Flask(__name__)

with open('config.toml', 'rb') as f:
  data = tomllib.load(f)

def _check_postgres():
  try:
    conn = psycopg2.connect(f"dbname={data['DBNAME']} user={data['DBUSER']} host={data['DBHOST']} password={data['DBPASSWORD']} connect_timeout=1")
    conn.close()
    return True
  except:
    return False

@app.route('/')
def hello():
  return 'hello world'

@app.route('/status')
def status():
  return 'app is ok' if _check_postgres() else 'fail connect to database'

if __name__ == '__main__':
  app.run(host=data['HOST'])

                       

