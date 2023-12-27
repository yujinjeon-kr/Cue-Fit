from rembg import remove
import os

def remove_background(input_image_path, output_image_path):
    # 입력 이미지 파일을 읽습니다.
    with open(input_image_path, 'rb') as file:
        input_data = file.read()

    # rembg를 사용하여 배경을 제거합니다.
    output_data = remove(input_data)

    # 결과 이미지를 파일로 저장합니다.
    with open(output_image_path, 'wb') as file:
        file.write(output_data)

    return output_image_path




import cv2
import numpy as np

def blend_images(foreground_path, background_path, output_path):
    # Read the images
    foreground = cv2.imread(foreground_path, cv2.IMREAD_UNCHANGED)
    background = cv2.imread(background_path)

    # Resize foreground image to match background dimensions
    h, w = background.shape[:2]
    foreground = cv2.resize(foreground, (w, h), interpolation=cv2.INTER_AREA)

    # Extract alpha channel and create a mask
    alpha_channel = foreground[:, :, 3]
    rgb_channels = foreground[:, :, :3]

    # Calculate alpha factor
    alpha_factor = alpha_channel[..., np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor, alpha_factor, alpha_factor), axis=2)

    # Blend images
    foreground_part = alpha_factor * rgb_channels
    background_part = (1 - alpha_factor) * background
    combined_image = foreground_part + background_part

    # Save and return the combined image
    cv2.imwrite(output_path, combined_image.astype(np.uint8))
    
    return combined_image
