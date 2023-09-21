#!/bin/sh
#wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="1234" psql -h "$host" -d "postgres" -U "postgres" -c '\q'; do
   >&2 echo "Postgres is unavailable - sleeping"
   sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

