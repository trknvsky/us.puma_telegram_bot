from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")
PG_HOST = env.str("PG_HOST")
