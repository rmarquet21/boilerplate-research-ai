import os
import csv

from sqlalchemy import create_engine, Table, MetaData
from tqdm import tqdm

from alembic.config import Config
from alembic import command

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "../data")

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=False)
connection = engine.connect()
metadata = MetaData()

if __name__ == '__main__':
    def lintValue(s):
        if s == '':
            return None
        elif s == '1':
            return 1
        elif s == '0':
            return 0
        else:
            return s


    alembic_cfg = Config(os.path.join(ROOT_DIR, "../alembic.ini"))
    command.upgrade(alembic_cfg, "head")

    for file in os.listdir(DATA_DIR):
        print(file[:-4])
        table = Table(file[:-4], metadata, autoload=True, autoload_with=engine)
        num_lines = sum(1 for line in open(os.path.join(DATA_DIR, file), "r"))
        header = ''
        with open(os.path.join(DATA_DIR, file), "r") as f:
            lines = csv.reader(f, delimiter=",", quotechar='"')
            for idx, line in tqdm(enumerate(lines), total=num_lines):
                if idx == 0:
                    header = line
                if idx != 0:
                    connection.execute(table.insert(), {header[i]: lintValue(line[i]) for i in range(len(header))})
