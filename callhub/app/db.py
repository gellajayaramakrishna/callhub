import mysql.connector

LOCAL_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password_here",
    "database": "CallHub",
}

SHARD_HOST = "your_shard_host"
SHARD_USER = "your_shard_user"
SHARD_PASSWORD = "your_password_here"
SHARD_DB = "your_shard_db"
NUM_SHARDS = 3