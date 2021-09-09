""" upload , rename and convert telegram files """

# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os
import io
import re
import time
from datetime import datetime
from pathlib import Path

import stagger
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram.errors.exceptions import FloodWait

from userge import userge, Config, Message
from userge.utils import sort_file_name_key, progress, take_screen_shot, humanbytes
from userge.utils.exceptions import ProcessCanceled
from userge.plugins.misc.download import tg_download, url_download

LOGGER = userge.getLogger(__name__)
CHANNEL = userge.getCLogger(__name__)

LOGO_PATH = 'resources/userge.png'

async def audio_upload(message: Message, path, del_path: bool = False,
						extra: str = '', with_thumb: bool = True):
	title = None
	artist = None
	thumb = None
	duration = 0
	str_path = str(path)
	file_size = humanbytes(os.stat(str_path).st_size)
	if with_thumb:
		try:
			album_art = stagger.read_tag(str_path)
			if album_art.picture and not os.path.lexists(Config.THUMB_PATH):
				bytes_pic_data = album_art[stagger.id3.APIC][0].data
				bytes_io = io.BytesIO(bytes_pic_data)
				image_file = Image.open(bytes_io)
				image_file.save("album_cover.jpg", "JPEG")
				thumb = "album_cover.jpg"
		except stagger.errors.NoTagError:
			pass
	if not thumb:
		thumb = await get_thumb(str_path)
	metadata = extractMetadata(createParser(str_path))
	if metadata and metadata.has("title"):
		title = metadata.get("title")
	if metadata and metadata.has("artist"):
		artist = metadata.get("artist")
	if metadata and metadata.has("duration"):
		duration = metadata.get("duration").seconds 
	sent: Message = await message.client.send_message(
	message.chat.id, f"`Uploading {str_path} as audio ... {extra}`")
	start_t = datetime.now()
	await message.client.send_chat_action(message.chat.id, "upload_audio")
	
	try:
		if "FLAC" in path.name:
			quax = "FLAC"
		if "320" in path.name:
			quax = "320 kbps"
		if "256" in path.name:
			quax = "256 kbps"
		if "120" in path.name:
			quax = "120 kbps"
		msg = await message.client.send_audio(
			chat_id=message.chat.id,
			audio=str_path,
			thumb=thumb,
			caption=f"🎧 {duration} | **{quax}** | **{file_size}**",
			title=title,
			performer=artist,
			duration=duration,
			parse_mode="html",
			disable_notification=True,
			progress=progress,
			progress_args=(message, f"uploading {extra}", str_path)
		)
	except ValueError as e_e:
		await sent.edit(f"Skipping `{str_path}` due to {e_e}")
	except Exception as u_e:
		await sent.edit(str(u_e))
		raise u_e
	else:
		await sent.delete()
		await finalize(message, msg, start_t)
		if os.path.exists(str_path) and del_path:
			os.remove(str_path)
	finally:
		if os.path.lexists("album_cover.jpg"):
			os.remove("album_cover.jpg")
