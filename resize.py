import os
from PIL import Image

def rename_and_resize_images(directory):
    # Initialize a counter for renaming images
    counter = 100
    
    # Create a folder for the resized images
    resized_dir = os.path.join(directory, "resized")
    if not os.path.exists(resized_dir):
        os.makedirs(resized_dir)
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Full path of the file
        filepath = os.path.join(directory, filename)
        
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                # Open the image
                img = Image.open(filepath)
                
                # Resize the image to 28x28
                img_resized = img.resize((28, 28))
                
                # Create a new file name (e.g., 100.jpg, 101.jpg, etc.)
                new_filename = f"{counter}.jpg"
                new_filepath = os.path.join(resized_dir, new_filename)
                
                # Save the resized image
                img_resized.save(new_filepath, "JPEG")
                
                print(f"Processed {filename} -> {new_filename}")
                
                # Increment the counter
                counter += 1
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Usage example
directory_path = "/path/to/your/images"  # Replace with your directory path
rename_and_resize_images(directory_path)