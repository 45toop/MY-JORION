import sqlite3
import json
from datetime import datetime
import os

class ProvenanceStore:
    def __init__(self, db_path=None):
        self.db_path = db_path or os.path.join(os.getcwd(), 'cce_provenance.sqlite')
        self._ensure()

    def _ensure(self):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cur = self.conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS provenance (
            id TEXT PRIMARY KEY,
            created_at TEXT,
            kind TEXT,
            payload TEXT
        )
        ''')
        self.conn.commit()

    def record(self, kind, payload):
        pid = json.dumps(payload, sort_keys=True)[:64]  # not ideal, but unique-ish for small use
        rec = (str(json.dumps({'id': payload.get('id', pid)})), datetime.utcnow().isoformat(), kind, json.dumps(payload))
        cur = self.conn.cursor()
        cur.execute('INSERT OR REPLACE INTO provenance (id, created_at, kind, payload) VALUES (?,?,?,?)', rec)
        self.conn.commit()
        return rec[0]

    def list(self, limit=100):
        cur = self.conn.cursor()
        cur.execute('SELECT id, created_at, kind, payload FROM provenance ORDER BY created_at DESC LIMIT ?', (limit,))
        rows = cur.fetchall()
        return [{'id': r[0], 'created_at': r[1], 'kind': r[2], 'payload': json.loads(r[3])} for r in rows]
