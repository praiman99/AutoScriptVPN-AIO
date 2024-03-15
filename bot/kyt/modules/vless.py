from kyt import *

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
	async def create_vless_(event):
    async with bot.conversation(chat) as user:
        await event.respond('**Username:**')
        user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
        user = (await user).raw_text
    async with bot.conversation(chat) as exp:
        await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 1 Day ","1"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(1)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" | addvless-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("vless://(.*)",a)]
			print(x)
			uuid = re.search("vless://(.*?)@",x[0]).group(1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
** 🟢 Vless Account 🟢**
**━━━━━━━━━━━━━━━━━**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» port TLS    :** `443`
**» Port NTLS   :** `80`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `(/multi path)/vlessws `
**» Path Dynamic:** `http://BUG.COM/vlessws `
**━━━━━━━━━━━━━━━━━**
**» Link TLS   : **
`{x[0]}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**━━━━━━━━━━━━━━━━━**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
	async def delete_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | bot-delvless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
	async def vless_(event):
		inline = [
[Button.inline(" CREATE VLESS ","create-vless"),
Button.inline(" DELETE VLESS ","delete-vless")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
    **⚠️ MENU VLESS⚠️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🟢 **» Service:** `VLESS`
🟢 **» Hostname/IP:** `{DOMAIN}`
🟢 **» ISP:** `{z["isp"]}`
🟢 **» Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vless_(event)
	else:
		await event.answer("Access Denied",alert=True)
