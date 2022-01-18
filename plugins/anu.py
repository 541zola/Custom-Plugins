"Nganu"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#ch
@userge.on_cmd("ch", about={
	'header': "Stripe $1",
	'usage': "{tr}ch [Enter bin]\n"})
	
async def gen(message: Message):
	"""Stripe Auth $1"""
	replied = message.input_str
	chat = "@binwatcher_bot"
	await message.edit("```Tunggu mas ```")
	msgs = []
	ERROR_MSG = "Unblok bot @binwatcher_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/ch {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)


#bin
@userge.on_cmd("bin", about={
	'header': "BIN",
	'usage': "{tr}bin [Enter bin]\n"})
	
async def bin(message: Message):
	"""BIN Ingfo"""
	replied = message.input_str
	chat = "@binwatcher_bot"
	await message.edit("```Tunggu mas```")
	msgs = []
	ERROR_MSG = "Unblok bot @binwatcher_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/bin {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)


#auth
@userge.on_cmd("auth", about={
	'header': "Cek Auth",
	'usage': "{tr}auth [Input CC]\n"})
	
async def key(message: Message):
	"""Auth $0"""
	replied = message.input_str
	chat = "@binwatcher_bot"
	await message.edit("```Jangan Percaya Hasil Auth```")
	msgs = []
	ERROR_MSG = "Unblok bot @binwatcher_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/auth {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)
