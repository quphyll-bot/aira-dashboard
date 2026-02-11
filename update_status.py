#!/usr/bin/env python3
import json, datetime, pathlib

root = pathlib.Path(__file__).resolve().parent
status_path = root / 'data' / 'status.json'

data = json.loads(status_path.read_text('utf-8'))
now = datetime.datetime.now(datetime.timezone.utc).astimezone()
data['updated'] = now.strftime('%Y-%m-%d %H:%M:%S %Z')

status_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
