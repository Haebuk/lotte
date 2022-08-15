import urllib

import pandas as pd
import sqlalchemy

from src import constants, secrets


def _create_engine():
    cfg = secrets.Secrets(constants.VAULT_URL.DB_CONFIG).get_secret_name_value_dict()
    quoted = urllib.parse.quote_plus(
        f"""DRIVER={cfg["driver"]};SERVER={cfg['server']};DATABASE={cfg['database']};uid={cfg['user']};pwd={cfg['password']}"""
    )
    engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect={}".format(quoted))
    return engine


def insert_csv_to_db():

    df = pd.read_csv("./data/힐미1102동 임대인 전처리.csv")

    df.to_sql(
        name="lessor",
        con=_create_engine(),
        index=False,
        if_exists="append",
    )

    print(f"{len(df)} are written.")
    return True


if __name__ == "__main__":
    insert_csv_to_db()
