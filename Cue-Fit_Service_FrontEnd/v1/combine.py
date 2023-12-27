import cv2
from matplotlib import pyplot as plt

def blend_images_with_transparency_bottom_aligned(foreground, background, scale=0.8):

    # Resize the foreground to match the scaled size
    foreground = cv2.resize(foreground, (int(background.shape[1] * scale), int(background.shape[0] * scale)))

    # Calculate the position to place the foreground on the background
    start_x = (background.shape[1] - foreground.shape[1]) // 2
    start_y = background.shape[0] - foreground.shape[0]

    # Split the alpha channel from the foreground
    b, g, r, alpha = cv2.split(foreground)
    alpha = cv2.merge([alpha, alpha, alpha])
    
    # Convert uint8 to float
    foreground = cv2.merge([b, g, r]).astype(float)
    alpha = alpha.astype(float)/255

    # Create a region of interest in the background
    roi = background[start_y:start_y+foreground.shape[0], start_x:start_x+foreground.shape[1]]

    # Perform alpha blending
    foreground = cv2.multiply(alpha, foreground)
    roi = cv2.multiply(1.0 - alpha, roi.astype(float))
    roi = cv2.add(foreground, roi)

    # Insert ROI back into the background image
    result = background.copy()
    result[start_y:start_y+foreground.shape[0], start_x:start_x+foreground.shape[1]] = roi

    return result.astype('uint8')

def load_and_blend_images(foreground_path, background_path, scale=0.8):
 
    foreground = cv2.imread(foreground_path, cv2.IMREAD_UNCHANGED)
    background = cv2.imread(background_path)

    if foreground.shape[2] != 4:
        raise ValueError("Foreground image does not have an alpha channel")

    result_image = blend_images_with_transparency_bottom_aligned(foreground, background, scale)
    return result_image

def save_combined_image(image, output_path):

    cv2.imwrite(output_path, image)
