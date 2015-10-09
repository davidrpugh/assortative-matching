#!/bin/sh

# create the database...
sqlite3 qwi.sqlite ".read create_qwi.sql"

# ...then import the data files (this could take 12-15 hours to complete!)...
for filename in ./data/*.gz
do
    echo "Started importing $filename..."
        gzcat -d $filename |                                        # decompress the .gz file
        tail -n +2 |                                                # skip the headers
        sqlite3 -separator ',' qwi.sqlite ".import /dev/stdin qwi"  # import from stdin
    echo "...finished importing $filename!"    
done
