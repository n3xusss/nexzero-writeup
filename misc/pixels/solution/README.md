# Pixels

**Difficulty:** Easy
**Category:** Misc
**Author:** M3551
**Description:** Exo01: What is steganography??


## Solution

Given a png file: 
![challenge](pixels.png)

As we look at the image, we see lots of colored pixels. If we check the colors closely, we notice something interesting: each pixel has the same amount of red, green, and blue (RGB). So, we can iterate over each pixel and take one of those colors, and it will represent hidden text encoded as ASCII characters.

Here is a python script doing so:

```python 
from PIL import Image

def image_to_string(input_image_path):
    image = Image.open(input_image_path)
    image_width = image.width
    output_string = ""

    # Iterate over each pixel in the image and retrieve the ASCII value
    for x in range(image_width):
        # Get the color of the pixel at (x, 0)
        pixel_color = image.getpixel((x, 0))  
        # Assuming R, G, and B values are the same
        ascii_value = pixel_color[0]  
        # Convert ASCII value to character and append to output string
        output_string += chr(ascii_value)  

    return output_string

input_image_path = "pixels.png"
retrieved_text = image_to_string(input_image_path)
print(retrieved_text)
```

## Output

Steganography is the art and science of concealing secret information within non-secret data, such as images, audio files, or text, in a way that does not arouse suspicion. Dating back to ancient times, steganography has been employed by various civilizations for covert communication, including the use of invisible ink or hidden messages within wax tablets. One of the earliest documented instances of steganography is the 'Histories' of Herodotus, where a message was tattooed onto a messenger's shaved head, hidden by allowing his hair to regrow before sending him on his way. Throughout history, steganography has evolved nexus{st3g4n0gr4ph1c_1m4g3_cr4ft} alongside advancements in technology, with modern techniques involving digital media and sophisticated algorithms to embed secret information within seemingly innocuous files, making detection challenging without prior knowledge of the method used. Today, steganography plays a crucial role in cybersecurity, espionage, and digital forensics, where it is both a tool for covert communication and a method of protecting sensitive data.
                   
## Flag

`nexus{st3g4n0gr4ph1c_1m4g3_cr4ft}`