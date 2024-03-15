from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu|.gas|.sayang)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" MENU SSH","ssh"),
Button.inline("MENU VMESS","vmess")],
[Button.inline("MENU VLESS","vless"),
Button.inline(" MENU TROJAN","trojan")],
[Button.inline(" ‹ Back Menu › ","start")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /root/.city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")

		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━
**  ADMIN PANEL MENU **
━━━━━━━━━━━━━━━━━━━━━━━
**🚦 OS     :** `{namaos.strip().replace('"','')}`
**🚦 CITY   :** `{city.strip()}`
**🚦 DOMAIN :** `{DOMAIN}`
**🚦 IP VPS :** `{ipsaya.strip()}`
━━━━━━━━━━━━━━━━━━━━━━━
** Bot By @fn_project **
━━━━━━━━━━━━━━━━━━━━━━━
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)


