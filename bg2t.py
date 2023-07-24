from PIL import Image
import os
import argparse

def remove_white_bg(img_path, to_path):
    img = Image.open(img_path)
    img = img.convert("RGBA")
    data = img.getdata()

    formatted_data = []
    for item in data:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            formatted_data.append((item[0], item[1], item[2], 0))
        else:
            formatted_data.append(item)

    img.putdata(formatted_data)
    img.save(to_path, format="PNG", quality=95, optimize=True)
    print(f"Modified image saved to {to_path}")

def mass_remove_white_bg(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith((".png")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            remove_white_bg(input_path, output_path)

def main():
    parser = argparse.ArgumentParser(description="Remove white BG in images to make transparent BG")
    parser.add_argument("-i", "--inputDir", help="Input directory holding raw image files to modify", required=True)
    parser.add_argument("-o", "--outputDir", help="Output directory to save modified images", required=True)

    args = vars(parser.parse_args())

    input_dir = args["inputDir"]
    output_dir = args["outputDir"]

    mass_remove_white_bg(input_dir, output_dir)

if __name__ == "__main__":
    main()