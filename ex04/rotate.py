from load_image import ft_load
import cv2

def main():
    try:
        img = ft_load("../animal.jpeg")
    except * as e:
        print({e})
        return;
    print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    end = min(400, h, w)
    gray = gray[0:end, 0:end]
    rotated = gray.transpose()[::-1]
    h, w = rotated.shape
    print(f"The shape of img is : ({h}, {w}, 1)")
    print(rotated)

if __name__ == "__main__":
    main()
