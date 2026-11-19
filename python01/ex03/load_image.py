import cv2

def ft_load(path : str) -> np.ndarray:
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Could not load image: {path}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, c = img.shape
    print(f"The shape of img is : ({h}, {w}, {c})")
    return img
