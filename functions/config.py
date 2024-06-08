#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2024 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default=29922662, cast=int)
    API_HASH = config("API_HASH", default="fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = config("BOT_TOKEN", "6672385958:AAESlGvQv7szlROFnXyT0zigg0pwZXE5jCE")
    FORCESUB_CHANNEL = int("-1002160935563")
    FORCESUB_CHANNEL_2 = int("-1002180087052")
    FORCESUB_CHANNEL_LINK = "https://t.me/pirate_flicks"
    FORCESUB_CHANNEL_LINK_2 = "https://t.me/cv_official_channel"
    # Database Credentials

    REDIS_URI = config("REDIS_URI", default="redis-10802.c330.asia-south1-1.gce.redns.redis-cloud.com:10802") 
    REDIS_PASS = config("REDIS_PASSWORD", default="rOvg9VosqTpuE2bcX7sPVDAvuERbezEV")

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1002198961306, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default="-1002160695715", cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1001836315219", cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default="-1002238472168", cast=int)
    OWNER = config("OWNER", default="6047510747", cast=int)
    BUTTON_UPLOAD = True 
    # Other Configs 

    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/f2ed939fa595810b6c08a.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=False, cast=bool)
