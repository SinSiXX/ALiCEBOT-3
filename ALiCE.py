import os
import importlib
import json
import time
import discord
import random
import requests
import threading
import asyncio
from asyncio import coroutines, futures
import insult
import requests.packages.urllib3
import urllib3
import youtube_dl
client = discord.Client()

voice = ''
player = ''
playlist = []

usr = '<email>'
password = '<password>'
owner = 177733171553632257
me = 195350693832294400
bot_banned = 195941375437438976
safe = True
aplay = False

# wtf is with url shortening



@client.event
async def on_message(message):

	global usr
	global password
	global owner
	global me
	global bot_banned
	global safe
	global playlist
	global aplay
	
	global player
	global voice
	pv = message.channel.is_private
	author = message.author

	if pv is False:#defines rolelist
		rolelist = message.server.roles
		memroles = []
	highlight = '<@' + author.id + '>'
	s = message.content.split()
	args = len(s)-1

	############################################################
	# Functions 
	############################################################

	# shortening channel output because fuck me
	def send(string):
		return client.send_message(message.channel, string)

	def dm(string):
		return client.send_message(author, string)


	# should determine the video service from url string
	# then return properly formated video url for youtube-dl
	def v_url(url):
		try:
			if url.find('youtu.be') != -1:
				x = url.split('youtu.be/')
				return 'https://youtube.com/watch?v='+x[1]
			elif url.find('www.youtube.com') != -1 or url.find('youtube.com') != -1:	
				x = url.split('?')
				y = x[1].split('&')
				z = {}
				for i in range(len(y)):
					z[y[i].split('=')[0]] = y[i].split('=')[1]

				return 'https://youtube.com/watch?v='+z['v']
			if	 url.find('youtu.be') != -1:
				x = url.split('youtu.be/')
				return 'https://youtube.com/watch?v='+x[1]
			
			
			#https://soundcloud.com/sweatsonklank/sweatson-klank-empty-your-soul?in=sweatsonklank/sets/upcoming-releases
			
			elif url.find('soundcloud.com') != -1:
				x = url.split('soundcloud.com/')
				y = url[1].split('/')
				if y[1] == 'sets':
					send('Cannot be a playlist!')
				elif y[1].find('?') != -1:
					y[1] = y[i].split('?')[0]
				z = 'https://soundcloud.com/'+y[0]+'/'+y[1]+'/'
				print(z)
				return z
			else:
				send('Bad url! - else')
		except:
			send('Bad url! - exception')

	async def p(url):
		global player
		global voice
		global safe

		if not client.is_voice_connected(author.server):
			# joins voice server
			safe = False
			voice = await client.join_voice_channel(author.voice_channel)
			player = await voice.create_ytdl_player(url)
			player.start()
			time.sleep(5)
			safe = True
		elif player == '' or not player.is_playing():
			# plays video cleanly
			safe = False
			player = await voice.create_ytdl_player(url)
			player.start()
			time.sleep(5)
			safe = True
		else:
			# restarts stream with new link
			safe = False
			player.stop()
			player = await voice.create_ytdl_player(url)
			player.start()
			time.sleep(5)
			safe = True

	async def autoplay():
		global player
		global voice
		global safe
		global playlist
		global aplay

		plrange = len(playlist)
		aplay = True
		while plrange > 0:
			time.sleep(1)
			if aplay == True:
				if not player.is_playing():
					if plrang > 1 and safe == True:
						playlist.pop(0)

						safe = False
						player.stop()
						player = await voice.create_ytdl_player(url)
						player.start()
						time.sleep(5)
						safe = True
					else:
						playlist.pop(0)
		aplay = False

	if pv is False:
		for i in range(len(author.roles)):
			memroles.append(author.roles[i].id)

	#ban check
	if (pv is False) and (str(bot_banned) in memroles) and (s[0][0] == '!'):
		await send(highlight+' '+insult.comeback())
	# output help
	elif s[0] == '!help':
		await client.delete_message(message)
		await send('```'+
			' !c !v creates a text/voice channel\n'+
			' !g !i !w !y, creates a google/wiki/youtube link for topic\n'+
			' Example: !i horse cocks\n\n'+

			' !p <[url]|add [url]|current|list|play|pause|skip|stop|disconnect>\n'+
			' examples: !p url\n'+
			'           !p add url\n'+
			' if having problems, try leaving and joining the voice channel.\n'+
			'```')
	# join invite channel
	elif s[0] == '!j' and args > 0 and (int(author.id) == owner):#join given channel
		if pv is False:await client.delete_message(message)
		await client.accept_invite(s[1])
	# leave message.server
	elif s[0] == '!d' and args == 1 and (int(author.id) == owner):#join given channel
		await client.delete_message(message)
		if s[1] == 'y':
			await client.leave_server(message.server)
	# finish this later
	elif 'a/s/l' in s or 'asl' in s:
		await send(highlight+' '+insult.asl())
	# insult on bot mention
	elif ('<@'+str(me)+'>' in s) and (int(author.id) != me):
		await send(highlight+' '+insult.comeback())
	# !g <string>
	elif s[0] == '!g' and args > 0:
		await client.delete_message(message)
		await send(highlight+' '+'https://www.google.com/?gws_rd=ssl#q='+'+'.join(s[1:]))
	# !i <string>
	elif s[0] == '!i' and args > 0:
		await client.delete_message(message)
		await send(highlight+' '+'https://www.google.com/search?tbm=isch&q='+'+'.join(s[1:]))
	# !y <string>
	elif s[0] == '!y' and args > 0:
		await client.delete_message(message)
		await send(highlight+' '+'https://www.youtube.com/results?search_query='+'+'.join(s[1:]))
	# !w <string>
	# formats search results to properly display information on discord link preview
	elif s[0] == '!w' and args > 0:
		await client.delete_message(message)
		x=['is', 'of', 'a', 'and', 'or']
		for i in range(len(s)):
			if i > 0 and s[i] not in x:
				s[i]=s[i].capitalize()
		for x in s[2:]:
			x=s
		await send(highlight+' '+'https://en.wikipedia.org/wiki/'+'_'.join(s[1:]))

	# create text channel
	elif s[0] == '!c' and pv is False:
		await client.delete_message(message)
		if args > 0:
			await client.create_channel(message.server, s[1] , type=discord.ChannelType.text)
			await client.send_message(message.channel, '#'+s[1]+" created.")
		else:
			await send("Too many arguments! Channels can only be one word.")

	# create voice channel
	elif s[0] == '!v' and pv is False:
		await client.delete_message(message)
		await client.create_channel(message.server, " ".join(s[1:]), type=discord.ChannelType.voice)
		await client.send_message(message.channel, " ".join(s[1:])+' voice channel created.')


	# """
	# This whole secion of code is broke
	# uses the youtube-dl library to play music through discord

	# having trouble handling clean disconnections on new video calls
	# and leaving at the end of videos
	# conveniently, discord.py has half the work done already, but now
	# the trouble lies in handling discord channel actions correctly

	# TODO: seeking,  playlist

	elif s[0] == '!p' and pv is False:
		plrange = len(playlist)

		await client.delete_message(message)
		# should check to see if already in room before running
		# plays the yt video linked in s[1], and if already playing,
		# stops and plays new yt link

		# SHOULDN'T SEGFAULT ANYMORE \O/

		if args == 0:
			await send('Not enough arguments!\n'+
						'!p (stop|pause|play|url|disconnect)')
		elif s[1] == 'stop': 
			if not client.is_voice_connected(author.server):
				# checks if playing
				await send("Not playing!")
			else:
				# Stop
				aplay = False
				player.stop()
				playlist.pop(0)
		elif s[1] == 'pause' or s[1] == 'play':
			if not client.is_voice_connected(author.server):
				# checks if playing
				await send("Not playing!")
			elif player == '' or not player.is_playing():
				# Play
				player.resume()
			else:
				# Pause
				player.pause()
		elif s[1] == 'disconnect':
			if not client.is_voice_connected(author.server):
				await send("Not in a room!")
			else:				
				# Leaves current voice room and cleanly closes player
				await voice.disconnect()
		elif s[1] == 'add' and args >= 2:
			if s[2].find('http://') != -1 or s[2].find('https://') != -1:
				if plrange == 0:
					await send('No playlist active!')
				else:
					playlist.append(v_url(s[2]))
			else:
				await send('Improper syntax!')		
		elif s[1] == 'skip':
			if len(playlist) > 1:
				if safe == False:
					await send("Not yet!")
				else:
					playlist.pop(0)
					await p(playlist[0])
			else:
				await send('Nothing next!')
		elif s[1] == 'list':
			if len(playlist) > 1:
				output = 'Current playing: '+playlist[0]+' , then \n'
				for i in range(plrange):
					if i == 3:break
					if i > 0:
						output = output+str(i+1)+': '+playlist[i]+'\n'
				await dm(output)
		elif s[1] == 'current':
			if plrange == 0:
				await dm('Playlist empty!')
			else:
				await dm('Currently playing: '+playlist[0])					
		elif s[1].find('http://') != -1 or s[1].find('https://') != -1:	
			if safe == True:
				if plrange > 0:
					playlist.pop(0)
					playlist.insert(0, v_url(s[1]))
					await p(playlist[0])
				else:
					playlist.append(v_url(s[1]))
				
					await p(playlist[0])
#				if aplay is False:
#					threading.Tread(autoplay())
			else:
				await send("Not yet!")
		else:
			await send("Improper syntax!")
	# End of god forsaken youtube-dl stuff
	# """	


	# refresh insult dictionary
	elif s[0] == '!l' and pv is False and (int(author.id) == owner):
		await client.delete_message(message)
		importlib.reload(insult)
		print("insult.py reloaded")

	elif s[0] == '!r' and (int(author.id) == owner):
		await client.delete_message(message)
		await send('Bye!')
		client.close()
		time.sleep(5)
		client.run(usr, password)
	elif s[0] == 'Hello!' and (int(author.id) == me):
		await client.delete_message(message)
	else:
		# randomly insult someone
		# moved to else so it runs only on actual text and not on commands
		if (random.randint(1,30) is 1) and (int(author.id) != me):
			print(author.id)
			await send(highlight+' '+insult.comeback())


	# Now for some easter eggs

	# hash-check for nhentai joke
	for i in range(len(s)):
		if pv is True and '#' in s[i][0]:
			await send('https://nhentai.net/search/?q='+s[i][1:])
		elif (pv is False) and ('#' in s[i][0]) and (len(s[i]) > 1) and (s[i] not in message.server.channels):
			await send('https://nhentai.net/search/?q='+s[i][1:])



@client.event
async def on_server_join(server):
	await client.send_message(server.default_channel, "Hello!")
	
@client.event
async def on_ready():
	if client.is_logged_in:
		print('Log in successful.')
	client.join_voice_channel("discordurl")
	ss = client.servers
	for s in ss:
		print(s.default_channel)
		await client.send_message(s.default_channel, "Hello!")
	print('Join channel succesful.')

client.run(usr, password)
client.close()
