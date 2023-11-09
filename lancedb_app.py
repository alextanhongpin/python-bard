import json
import lancedb
from lancedb.pydantic import Vector, LanceModel
from datetime import datetime

# import pyarrow as pa

TABLE_NAME = "documents"

uri = "data/sample-lancedb"
db = lancedb.connect(uri)


# vector: list of vectors
# file_name: name of file
# file_path: path of file
# id
# updated_at
# created_at
class Document(LanceModel):
    id: str
    file_name: str
    file_path: str
    created_at: datetime
    updated_at: datetime
    vector: Vector(768)  # Palm Embeddings size


try:
    table = db.create_table(TABLE_NAME, schema=Document)
except OSError:
    print("table exists")
    table = db.open_table(TABLE_NAME)
except Exception as inst:
    # Print out the type of exceptions.
    print(type(inst))
    print(inst.args)
    print(inst)

if True:
    now = datetime.now()
    # Idempotent upsert. Alternatively we can delete first, then insert.
    table.add(
        [
            Document(
                id="1",
                file_name="test_name",
                file_path="test_path",
                created_at=now,
                updated_at=now,
                vector=[i for i in range(768)],
            )
        ]
    )
    table.delete(f'id="1" AND created_at != timestamp "{now}"')


if False:
    table.update(
        where='id="1"',
        values=Document(
            id="1",
            file_name="test_name",
            file_path="test_path",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            vector=[i for i in range(768)],
        ),
    )

vector = [i for i in range(768)]
result = table.search(vector).limit(2).to_list()
for item in result:
    print(item)
    # print(json.dumps(item, indent=2))


print(db[TABLE_NAME].head())
