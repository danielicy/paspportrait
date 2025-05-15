import face_recognition
from rembg import remove
from PIL import Image
import numpy as np
import io




def xprocess(t):     
    with open('C:\\TEMP\\ME.jpg', 'rb') as f:
        input_image = f.read()

    output = remove(input_image)
    with open('C:\\TEMP\\no_bg.png', 'wb') as out:
        out.write(output)


def process(t):
    input_path='C:\\TEMP\\W4.jpeg'
    output_path='C:\\TEMP\\w4_bg.png'
    output_size=(600, 600)
    face_padding=100
    # Step 1: Load and remove background
    with open(input_path, 'rb') as f:
        input_image_bytes = f.read()

    bg_removed_bytes = remove(input_image_bytes)
    bg_removed_image = Image.open(io.BytesIO(bg_removed_bytes)).convert("RGBA")

    # Step 2: Convert to RGB for face_recognition
    rgb_image = bg_removed_image.convert("RGB")
    image_array = np.array(rgb_image)

    # Step 3: Detect face
    face_locations = face_recognition.face_locations(image_array)

    if not face_locations:
        raise Exception("No face detected in the image.")

    # Use the first face found
    top, right, bottom, left = face_locations[0]

    # Add padding and stay within bounds
    top = max(0, top - face_padding)
    bottom = min(image_array.shape[0], bottom + face_padding)
    left = max(0, left - face_padding)
    right = min(image_array.shape[1], right + face_padding)

    # Crop the image
    cropped_image = rgb_image.crop((left, top, right, bottom))

    # Step 4: Resize to passport dimensions
    passport_image = cropped_image.resize(output_size, Image.LANCZOS)

    # Step 5: Save the result
    passport_image.save(output_path)
    print(f"Passport-style photo saved as: {output_path}")

 
