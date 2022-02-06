"KFC Terus Terang Terang Terus"
import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#chk
@userge.on_cmd("chk", about={
	'header': "Auth Only",
	'usage': "{tr}chk [Input CC]\n"})
	
async def gen(message: Message):
	"""Cek Auth"""
	replied = message.input_str
	chat = "@AKUDANEMPATORANGTOLOL_BOT"
	await message.edit("```Disuruh nunggu sama ayang ```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/chk {}".format(replied))
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
	chat = "@AKUDANEMPATORANGTOLOL_BOT"
	await message.edit("```Disuruh nunggu sama ayang```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
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


#fake
@userge.on_cmd("fake", about={
	'header': "Generate Fake Address",
	'usage': "{tr}bin [Input Country Code]\n"})
	
async def key(message: Message):
	"""Generate Fake Address"""
	replied = message.input_str
	chat = "@AKUDANEMPATORANGTOLOL_BOT"
	await message.edit("```Disuruh nunggu sama ayang```")
	msgs = []
	ERROR_MSG = "Ijin dulu sama @Dappzx"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/fake {}".format(replied))
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
		

#ch
@userge.on_cmd("ch", about={
	'header': "Chase Paymentech $1 Charge",
	'usage': "{tr}ch [Input Country Code]\n"})
	
async def key(message: Message):
	"""Chase Paymentech $1 Charge"""
	replied = message.input_str
	chat = "@SDBB_Bot"
	await message.edit("```Disuruh nunggu sama ayang```")
	msgs = []
	ERROR_MSG = "Ga dibales sama ayang"
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
		
		
#Spotify
@userge.on_cmd("spo", about={
	'header': "Auto Create Spotify Account",
	'usage': "{tr}spo [nama ayang]\n"})
	
async def key(message: Message):
	"""Auto Create Spotify Account"""
	replied = message.input_str
	chat = "@Hcsacc_bot"
	await message.edit("```Wait for result...```")
	msgs = []
	ERROR_MSG = "Error"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/spo {}".format(replied))
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
