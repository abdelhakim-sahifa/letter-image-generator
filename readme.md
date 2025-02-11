# [Letter Image Generator](https://letter-image-generator.vercel.app)

This Flask application generates an image featuring the initials of a given first name and last name. The initials are centered within a square image, and the font is customizable. You can specify the names via URL parameters, and the app will respond with an image containing the initials.

## Features

- Generates an image with the initials of a given first name and last name.
- Customizable font (default font is used if a custom font is not available).
- Returns the image in PNG format.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdelhakim-sahifa/letter-image-generator.git
   cd letter-image-generator
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Ensure you have the necessary font file (`Kagitingan-Bold.otf`) in the `fonts` directory. If the font file is not available, the application will fall back to the default font.

## Usage

Run the Flask application:

```bash
python app.py
```

The app will run locally, and you can access the endpoint:

```
http://127.0.0.1:5000/generate_image?firstname=John&lastname=Doe
```

Replace `John` and `Doe` with any first name and last name, and the app will return an image with the initials of those names.

### Example

- Request:
  ```
  http://127.0.0.1:5000/generate_image?firstname=John&lastname=Doe
  ```
- Response: An image with the initials 'JD' centered on a white background.

## Contributing

Feel free to open issues or pull requests for improvements. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---

### Key Updates:

1. **Clarified Functionality**: The application now generates initials for both first name and last name, so the description has been updated to reflect this.
2. **Updated Usage Instructions**: The example URL now includes both `firstname` and `lastname` parameters.
3. **Improved Readability**: Simplified and reorganized sections for better clarity.
4. **Font Handling Note**: Added a note about the fallback to the default font if the custom font is not available.
