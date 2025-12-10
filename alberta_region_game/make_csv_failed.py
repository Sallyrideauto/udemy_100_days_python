import cv2
import pytesseract
import pandas as pd
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# Configure
IMAGE_PATH = "alberta_map.gif"
CSV_FILE = "alberta_regions_1st.csv"

# Read Image
pil_img = Image.open(IMAGE_PATH).convert("RGB")
width, height = pil_img.size

# Conversion to OpenCV
img = cv2.cvtColor(
    cv2.imread(IMAGE_PATH),
    cv2.COLOR_BGR2RGB
)

# Get Information by Tesseract
data = pytesseract.image_to_data(img, lang="eng", output_type=pytesseract.Output.DATAFRAME)

points = []

for _, row in data.iterrows():
    text = row["text"]
    conf = row["conf"]

    # If string empty or conf is too low, except it
    if isinstance(text, str):
        text = text.strip()
    if not text:
        continue
    if conf < 60:
        continue

    x = row["left"]
    y = row["top"]
    w = row["width"]
    h = row["height"]

    # Box Coordinate
    cx = x + w / 2
    cy = y + h / 2

    # Turtle Coordinate
    tx = cx - width / 2
    ty = height / 2 - cy

    points.append({
        "region": text,
        "x_turtle": round(tx, 2),
        "y_turtle": round(ty, 2),
        "x_pixel": int(cx),
        "y_pixel": int(cy),
        "conf": conf
    })

# Save to CSV
df = pd.DataFrame(points)
df.to_csv(CSV_FILE, index=False)

print(f"Completed {len(points)} regions saved in {CSV_FILE}")