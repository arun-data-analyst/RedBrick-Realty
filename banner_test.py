# encode_image.py
import base64

with open("arsenal banner.jpg", "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read()).decode()

print(encoded_string[:100])  # Just to verify
with open("bg_base64.txt", "w") as out:
    out.write(encoded_string)
