from kyt import *

@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
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
		time.sleep(0)
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
		cmd = f'printf "%s\n" "{user}" "{exp}" | addws-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
 **🟢 VMESS ACCOUNT 🟢**
**━━━━━━━━━━━━━━━━━**
**» Username     :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» port TLS     :** `443`
**» Port NTLS    :** `80`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path         :** `/vmessws`
**» Path Dynamic :** `https://bug.com/vmessws`
**» ServiceName  :** `vmess-grpc`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**» Expired On:** `{later}`
**━━━━━━━━━━━━━━━━━**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
	async def delete_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | bot-delws'
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
		await delete_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" CREATE VMESS ","create-vmess"),
Button.inline(" DELETE VMESS ","delete-vmess")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
   **⚠️ MENU VMESS ⚠️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🟢 **» Service:** `VMESS`
🟢 **» Hostname/IP:** `{DOMAIN}`
🟢 **» ISP:** `{z["isp"]}`
🟢 **» Country:** `{z["country"]}`
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)