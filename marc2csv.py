# Simple marc2csv script.

import csv
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

from pymarc import MARCReader

filepath = 'data.mrc'
if len(sys.argv) > 1:
    filepath = sys.argv[1]

try:
    reader = MARCReader(open(filepath, 'rb'), to_unicode=True)
except IOError:
    print('cannot open "%s"' % filepath, file=sys.stderr)
    sys.exit(1)

csv_records = []
marc_tags = []

for marc_record in reader:
    csv_record = {}
    for marc_field in marc_record.fields:
        if marc_record is None:
            print(
                "Current chunk: ",
                reader.current_chunk,
                " was ignored because the following exception raised: ",
                reader.current_exception
            )
        else:
            if marc_field.tag not in marc_tags:
                marc_tags.append(marc_field.tag)
            csv_record[marc_field.tag] = marc_field.value()
        csv_records.append(csv_record)

marc_tags.sort()

print(','.join(['"%s"' % tag for tag in marc_tags]))
writer = csv.DictWriter(sys.stdout, marc_tags)
writer.writerows(csv_records)

