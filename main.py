from PIL import Image
# 1. Define the Unicode shaded blocks from darkest to lightest.
# (If your terminal/web background is dark, use this order. Swap it if using a light background)
UNICODE_SHADES = " ░▒▓█"
# gemini says this is good
VERTICAL_CORRECTION = .55

    
def image_to_unicode(image_path,new_width=100): 
    try:
        image = Image.open(image_path)
    except Exception as e: 
        return f"Error processing image: {e}"
    original_height,original_width = image.height,image.width
    aspect_ratio = original_height / original_width
    new_height = int(new_width * (aspect_ratio) * VERTICAL_CORRECTION)
    
    img_resized = image.resize((new_width,new_height))
    grayscale = list(img_resized.convert("L").getdata())
    #converting to the Unicode shades
    unicode_list = []
    for pixel in grayscale: 
        index = pixel // 51
        if index > 4:
            index = 4
        unicode_list.append(UNICODE_SHADES[index])
    
    rows = []
    #convert to string 
    for i in range(0,len(unicode_list),new_width):
        row_s = "".join(unicode_list[i:i + new_width])
        
        rows.append(row_s)
    final_ascii_art = "\n".join(rows)
    return final_ascii_art
    
    
if __name__ == "__main__":
    test_img = "funny.jpg"
    
    result = image_to_unicode(test_img, new_width=150)
    
    print(result)
    