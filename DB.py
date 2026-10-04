import json
import sqlite3

DB_NAME = "farm.db"


def init_db():
  """データベースとテーブルの準備"""
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()

  c.execute("""
        CREATE TABLE IF NOT EXISTS save_data (
            id INTEGER PRIMARY KEY,
            coin INTEGER,
            tomato_seeds INTEGER,
            strawberry_seeds INTEGER,
            lettuce_seeds INTEGER
        )
    """)

  c.execute("""
        CREATE TABLE IF NOT EXISTS farm_data (
            id INTEGER PRIMARY KEY,
            farms_json TEXT,
            harvested_crops_json TEXT
        )
    """)

  c.execute("SELECT COUNT(*) FROM save_data WHERE id = 1")
  if c.fetchone()[0] == 0:
    c.execute("INSERT INTO save_data VALUES (1, 1000, 0, 0, 0)")

  c.execute("SELECT COUNT(*) FROM farm_data WHERE id = 1")
  if c.fetchone()[0] == 0:
    default_farms = json.dumps([None, None, None])
    c.execute("INSERT INTO farm_data VALUES (1, ?, ?)", (default_farms, "[]"))

  conn.commit()
  conn.close()


def load_data():
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute(
      "SELECT coin, tomato_seeds, strawberry_seeds, lettuce_seeds FROM"
      " save_data WHERE id = 1"
  )
  row = c.fetchone()
  conn.close()
  if row:
    return row[0], row[1], row[2], row[3]
  return 1000, 0, 0, 0


def save_data(coin, tomato_seeds, strawberry_seeds=0, lettuce_seeds=0):
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute(
      """
        UPDATE save_data 
        SET coin = ?, tomato_seeds = ?, strawberry_seeds = ?, lettuce_seeds = ? 
        WHERE id = 1
    """,
      (coin, tomato_seeds, strawberry_seeds, lettuce_seeds),
  )
  conn.commit()
  conn.close()


def load_farm_data():
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()
  c.execute(
      "SELECT farms_json, harvested_crops_json FROM farm_data WHERE id = 1"
  )
  row = c.fetchone()
  conn.close()

  if row and row[0]:
    try:
      farms = json.loads(row[0])
      harvested_crops = json.loads(row[1]) if row[1] else []
      if not isinstance(farms, list):
        farms = [None, None, None]
      return farms, harvested_crops
    except Exception:
      return [None, None, None], []
  return [None, None, None], []


def save_farm_data(farms, harvested_crops):
  conn = sqlite3.connect(DB_NAME)
  c = conn.cursor()

  farms_json = json.dumps(farms)
  harvested_crops_json = json.dumps(harvested_crops)

  c.execute(
      """
        UPDATE farm_data 
        SET farms_json = ?, harvested_crops_json = ? 
        WHERE id = 1
    """,
      (farms_json, harvested_crops_json),
  )
  conn.commit()
  conn.close()
