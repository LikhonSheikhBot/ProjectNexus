import os
from KazukoBot.events import register
from KazukoBot import telethn as tbot
from PIL import Image, ImageDraw, ImageFont


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if not quew:
        await event.reply("Provide Some Text To Draw!")
        return 
 try:
    memek = await event.reply('Creating your logo...wait!')
    text = event.pattern_match.group(1)
    img = Image.open('./KazukoBot/resources/1621467863b9e4cd03603.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./KazukoBot/resources/Chopsic.otf", 55)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=4, stroke_fill="yellow")
    fname2 = "Kazuko.png"
    img.save(fname2, "png")
    await memek.edit("`Uploading`")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @KazukoRobot")
    if os.path.exists(fname2):
            os.remove(fname2)
            await memek.delete()
 except Exception as e:
   await event.reply(f'Error Report @CFC_BOT_support, {e}')


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name
 """
__mod_name__ = "Logo"
