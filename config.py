# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24473318"))
API_HASH = getenv("API_HASH", "e7dd0576c5ac0ff8f90971d6bb04c8f5")
BOT_TOKEN = getenv("BOT_TOKEN", "7556497777:AAF4VoCDNvHvQ_DiAfpT9uP703UFzClvcgY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6697397532").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mehuldb:ymLdv8Sf2UW49x2m@withcluster.akoofaz.mongodb.net/")
LOG_GROUP = getenv("LOG_GROUP", "-1002617386015")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002475668850"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
