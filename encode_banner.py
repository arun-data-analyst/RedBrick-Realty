import base64

with open("AB3.png", "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read()).decode()

with open("bg_base64.txt", "w") as out_file:
    out_file.write(encoded_string)

print("✅ Banner encoded and written to bg_base64.txt")
