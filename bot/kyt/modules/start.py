from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:.start|/start)$"))
@bot.on(events.CallbackQuery(data=b'start'))
async def start(event):
	inline = [
[Button.inline("PANEL CREATE ACCOUNT","menu")],
[Button.url("WHATSAP","https://wa.me/6283120684925"),
Button.url("ORDER SCRIPT","https://t.me/Rerechan02")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /root/.city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")

		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
     **⚠️ ADMIN FANEL ⚠️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🟢 **» OS     :** `{namaos.strip().replace('"','')}`
🟢 **» CITY :** `{city.strip()}`
🟢 **» DOMAIN :** `{DOMAIN}`
🟢 **» IP VPS :** `{ipsaya.strip()}`
━━━━━━━━━━━━━━━━━━━━━━━
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)