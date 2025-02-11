from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)

@app.route('/')
def main():
    return 'Try: <a href="/generate_image?firstname=Bob&lastname=Smith">/generate_image?firstname=Bob&lastname=Smith</a>'

@app.route('/generate_image', methods=['GET'])
def generate_image():
    first_name = request.args.get('firstname', default='A', type=str).strip()
    last_name = request.args.get('lastname', default='A', type=str).strip()

    if not first_name:
        last_name = "A"  # Default letter if the input is empty
    if not last_name:
        last_name = "A"  # Default letter if the input is empty

    
    letters = first_name[0].upper() +  last_name[0].upper()

    # Create an image with a white background
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)

    # Define the font path
    font_path = os.path.join(os.getcwd(), "fonts", "Kagitingan-Bold.otf")

    # Load a font
    try:
        font = ImageFont.truetype(font_path, 150)  # Reduced size to fit better
    except IOError:
        font = ImageFont.load_default()

    # Get the bounding box of the text
    bbox = draw.textbbox((0, 0), letters, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to center the text
    position = ((200 - text_width) // 2, (200 - text_height) // 2)

    # Draw the text on the image
    draw.text(position, letters, fill="black", font=font)

    # Save the image to a bytes buffer
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    # Return the image as a response
    return send_file(img_byte_array, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
