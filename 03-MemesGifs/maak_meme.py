from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("policeman.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

#De afbeelding is 872 pixels breed en 492 pixels hoog

lettertype = ImageFont.truetype("impact.ttf", 40)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

tekst = "error on line 28"
tekst2 = "me rushing to line 28 to fix it"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

#tekstbreedte=460, tekst_hoogte=70

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = 0
tekst_x2 = 218
tekst_y2 = 450

tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((tekst_x2, tekst_y2), tekst2, font=lettertype, fill=(0,0,0))
# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")
