from rembg import remove

input_path = "top_secret_img.jpg"
output_path = "../secret_notes_ex/top_secret_img_o.jpg"

with open(input_path,'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)