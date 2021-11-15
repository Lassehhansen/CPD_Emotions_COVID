import ujson as json
import pandas as pd

records = map(json.loads, open('/path/to/records.ndjson'))
df = pd.DataFrame.from_records(records)