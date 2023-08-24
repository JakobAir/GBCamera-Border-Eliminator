from PIL import Image
import os

def crop_and_save_image(input_path, output_path):
    try:
        # Open the image
        image = Image.open(input_path)
        
        # Define the crop box
        width, height = image.size
        left = (width - 386) // 2
        top = (height - 338) // 2
        right = left + 386
        bottom = top + 338
        
        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))
        
        # Add prefix to the filename
        filename = os.path.basename(input_path)
        new_filename = f"GBCam_{filename}"
        
        # Save the cropped image
        cropped_image.save(os.path.join(output_path, new_filename))
        
        print(f"Processed {filename} and saved as {new_filename}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main(input_folder, output_folder):
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each PNG file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            crop_and_save_image(input_path, output_folder)

if __name__ == "__main__":
    input_folder = "C:\GBCam"  # Input folder path
    output_folder = "C:\GBCam"  # Output folder path
    main(input_folder, output_folder)
