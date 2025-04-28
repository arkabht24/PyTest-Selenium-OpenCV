import cv2
import numpy as np

class Screenshot_comparison:
    def compare_images_with_contours(self, image_path1, image_path2, output_path):
   
        img1 = cv2.imread(image_path1)
        img2 = cv2.imread(image_path2)

    
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    
        diff = cv2.absdiff(gray1, gray2)

    
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    
        kernel = np.ones((5,5), np.uint8)
        dilated = cv2.dilate(thresh, kernel, iterations=2)

    
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
        for contour in contours:
            if cv2.contourArea(contour) > 200:  
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

   
        cv2.imwrite(output_path, img2)
        print(f"Differences highlighted and saved to: {output_path}")


