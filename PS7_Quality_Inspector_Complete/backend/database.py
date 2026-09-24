import sqlite3
from pathlib import Path
DB=Path(__file__).parent/"quality_inspector.db"
def conn():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c
def init_db():
 c=conn();c.execute("""CREATE TABLE IF NOT EXISTS inspections(id INTEGER PRIMARY KEY AUTOINCREMENT,filename TEXT,decision TEXT,confidence REAL,defect_score REAL,threshold REAL,reason TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP)""");c.commit();c.close()
def add(row):
 c=conn();q=c.execute("INSERT INTO inspections(filename,decision,confidence,defect_score,threshold,reason) VALUES(?,?,?,?,?,?)",row);c.commit();i=q.lastrowid;c.close();return i
def all_rows():
 c=conn();r=[dict(x) for x in c.execute("SELECT * FROM inspections ORDER BY id DESC").fetchall()];c.close();return r