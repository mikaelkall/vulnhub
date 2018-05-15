#!/bin/bash

SCRIPT_DIR=$(dirname $0)
cd ${SCRIPT_DIR}

# Give couchdb time to boot
until curl -Lks -o /dev/null "http://localhost:5984"
do
    sleep 5
    echo "Waiting..."
done

# Create database
curl -X PUT http://127.0.0.1:5984/simpsons
curl -X PUT -d '{"character":"Homer","quote":"Doh!"}' http://127.0.0.1:5984/simpsons/1
curl -X PUT -d '{"character":"Marge","quote":"I don’t want to alarm anybody, but I think there’s a little al-key-hol in this punch."}' http://127.0.0.1:5984/simpsons/2
curl -X PUT -d '{"character":"Bart","quote":"Eat My Shorts!"}' http://127.0.0.1:5984/simpsons/3
curl -X PUT -d '{"character":"Maggie","quote":"Good night"}' http://127.0.0.1:5984/simpsons/4
curl -X PUT -d '{"character":"Lisa","quote":"Prayer. The last refuge of a scoundrel."}' http://127.0.0.1:5984/simpsons/5
curl -X PUT -d '{"character":"Apu","quote":"Please, could you just take the children home? The porno magazine buyers are too embarrassed to make their move. Look."}' http://127.0.0.1:5984/simpsons/6
curl -X PUT -d '{"character":"Moe","quote":"Oh, business is slow. People today are healthier and drinking less. You know, if it wasnt for the junior high school next door, no one would even use the cigarette machine."}' http://127.0.0.1:5984/simpsons/7
