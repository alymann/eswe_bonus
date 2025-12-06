class InMemoryDB:
    def __init__(self):
        self._store = {}
        self._active = False
        self._commits = {}

    def begin_transaction(self):
        if self._active:
            raise Exception("Transaction in progress")
        self._active = True
        self._commits = {}

    def put(self, key: str, value: int):
        if not self._active:
            raise Exception("Transaction not in progress")
        self._commits[key] = value

    def get(self, key: str):
        return self._store.get(key, None)

    def commit(self):
        if not self._active:
            raise Exception("commit() called without an active transaction")
        for key, value in self._commits.items():
            self._store[key] = value
        self._active = False
        self._commits = {}

    def rollback(self):
        if not self._active:
            raise Exception("rollback() called without an active transaction")
        self._active = False
        self._commits = {}

def main():
    inmemoryDB = InMemoryDB()
    print(inmemoryDB.get("A"))
    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print(e)

    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)
    print(inmemoryDB.get("A"))
    inmemoryDB.put("A", 6)
    inmemoryDB.commit()

    print(inmemoryDB.get("A"))
    try:
        inmemoryDB.commit()
    except Exception as e:
        print(e)
    try:
        inmemoryDB.rollback()
    except Exception as e:
        print(e)

    print(inmemoryDB.get("B"))

    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    inmemoryDB.rollback()
    print(inmemoryDB.get("B"))

if __name__ == "__main__":
    main()