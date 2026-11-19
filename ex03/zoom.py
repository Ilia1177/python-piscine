from load_image import ft_load
import cv2

def main():
    img = ft_load("../animal.jpeg")
    print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    end = min(400, h, w)                                     
    new_img = gray[0:end, 0:end]
    h, w = new_img.shape
    print(f"New shape of img is : ({h}, {w})")
    print(new_img)

if __name__ == "__main__":
    main()
