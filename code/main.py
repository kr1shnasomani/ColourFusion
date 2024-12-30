# Import the required libraries
import cv2
import numpy as np
from collections import Counter, defaultdict
from webcolors import CSS3_NAMES_TO_HEX, hex_to_rgb
import matplotlib.pyplot as plt

def get_closest_color_name_and_hex(rgb_tuple):
    min_distance = float('inf')
    closest_color_name = None
    closest_hex_code = None
    for color_name, hex_code in CSS3_NAMES_TO_HEX.items():
        r, g, b = hex_to_rgb(hex_code)
        distance = np.sqrt((r - rgb_tuple[0])**2 + (g - rgb_tuple[1])**2 + (b - rgb_tuple[2])**2)
        if distance < min_distance:
            min_distance = distance
            closest_color_name = color_name
            closest_hex_code = hex_code
    return closest_color_name, closest_hex_code

def detect_colors(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return []

    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize image for faster processing (optional)
    scale_percent = 50  
    width = int(image_rgb.shape[1] * scale_percent / 100)
    height = int(image_rgb.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image_rgb, dim, interpolation=cv2.INTER_AREA)

    # Reshape the image to a 2D array of pixels
    pixels = resized_image.reshape(-1, 3)

    # Count occurrences of each color and group by name/hex
    color_counts = Counter(map(tuple, pixels))
    aggregated_colors = defaultdict(int)

    for rgb_tuple, count in color_counts.items():
        rgb_tuple = tuple(map(int, rgb_tuple)) 
        color_name, hex_code = get_closest_color_name_and_hex(rgb_tuple)
        aggregated_colors[(color_name, hex_code)] += count

    # Sort by the most common colors
    sorted_colors = sorted(aggregated_colors.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors

def save_colors_to_file(colors, output_path):
    with open(output_path, "w") as file:
        for i, ((color_name, hex_code), count) in enumerate(colors):
            file.write(f"{i + 1}. {color_name.capitalize()} ")
            file.write(f"{hex_code.upper()}\n")
    
    print(f"Color information saved to {output_path}")

# Path to the image file and output file
image_path = r"C:\Users\krish\OneDrive\Desktop\image.jpg"
output_path = r"C:\Users\krish\OneDrive\Desktop\detected-colors.txt"

# Detect and save colors to a text file
detected_colors = detect_colors(image_path)
if detected_colors:
    save_colors_to_file(detected_colors, output_path)