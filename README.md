<h1 align="center">ColourFusion</h1>


## Execution Guide:
1. Run the following command line in the terminal:
   ```

   ```

2. 

## Model Prediction:

Input Image:

![image](https://github.com/user-attachments/assets/4e995c47-7578-42b6-8e15-99101df42558)

Output:

![image](https://github.com/user-attachments/assets/0266ecad-91d6-409d-9586-53937cab4eee)

## Overview:
This project is a tool that analyzes an image to identify the most prominent colors and their closest matching names and hexadecimal codes. The detected color information is saved to a text file in a structured format for further use or reference.

### Features:
- Detects the dominant colors in an image.
- Matches colors to their closest CSS3 color names and hexadecimal codes.
- Outputs the detected color information in a sorted list, ranked by prominence.
- Saves the results to a user-defined text file for easy access.

### How It Works:
1. **Image Processing**:
   - The image is loaded using OpenCV and converted to the RGB color space.
   - The image is optionally resized for faster processing.

2. **Color Detection**:
   - Each pixel's RGB values are compared against a predefined set of CSS3 color names and hexadecimal codes.
   - The Euclidean distance is calculated to determine the closest matching color.

3. **Color Aggregation**: Pixels with the same color name are grouped together and their counts are summed up.

4. **Results Output**: The most frequent colors are ranked and saved to a text file, including their names, hexadecimal codes and occurrences.

### Input and Output:
- **Input**: An image file (e.g., `.jpg`, `.png`) provided via the `image_path` variable.
- **Output**: A text file containing a sorted list of detected colors, including their names and hexadecimal codes.
