# Setup Posgres Database

## Pull the latest postgres image

```bash
podman pull docker.io/library/postgres:latest
```

## Create a volume for the database

```bash
podman volume create postgres-data
```

## Run the postgres container

```bash
podman run -p 5432:5432 \
    --name postgres-test \
    -e POSTGRES_PASSWORD=password \
    -v postgres-data:/var/lib/postgresql/data \
    -d \
    postgres
```

## Connect to the postgres container

```bash
# install psql client
# on linux
sudo apt-get install postgresql-client

# on macOS
brew install libpq
echo 'export PATH="/opt/homebrew/opt/libpq/bin:$PATH"' >> ~/.zshrc
```

```bash
# connect via ssh tunnel if from remote host, map port 5432 to localhost:5555
ssh -L {local_port}:localhost:5432 user@remote_host -fN

psql -h localhost -p 5432 -U postgres -d postgres
# or
psql postgresql://postgres:password@localhost:5432/postgres
```

## Create a database and user

```sql
CREATE DATABASE mydb;
CREATE USER myuser WITH PASSWORD 'mypass';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
-- grant all privileges in the schema public to myuser
-- this is needed after postgres 15, otherwise you will get
-- ERROR: permission denied for schema public
\c mydb postgres
GRANT ALL ON SCHEMA public TO myuser;
```

## Create a test table

```sql
CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);
```
