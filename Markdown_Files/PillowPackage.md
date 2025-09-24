This code uses a **hybrid rendering method** that combines **OpenCV** and **Pillow (PIL)** to display the label `"드론"` (Korean for "drone") on top of detected objects in a video. Here's how it works:

---

## 🧠 Method Used: PIL-Based Text Rendering on OpenCV Frames

### 🔹 Why This Is Necessary
OpenCV’s built-in `cv2.putText()` function only supports **ASCII characters** — it cannot render Korean, Chinese, Arabic, or other non-Latin scripts. To overcome this limitation, the code uses **Pillow (PIL)**, which supports Unicode fonts and full character sets.

---

## 🔧 Step-by-Step Breakdown

### 1. **Load a Korean Font**
```python
font_path = "C:/Windows/Fonts/NanumGothic.ttf"
font_pil = ImageFont.truetype(font_path, 20)
```
This loads the **NanumGothic** font, a Korean TrueType font installed on Windows.

---

### 2. **Convert OpenCV Frame to PIL Image**
```python
frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(frame_pil)
```
OpenCV uses BGR format, while PIL uses RGB. This conversion allows PIL to draw on the frame.

---

### 3. **Draw Korean Text Using PIL**
```python
draw.text((x, y - 25), "드론", font=font_pil, fill=(247, 230, 0))
```
This places the Korean word `"드론"` above the bounding box using the loaded font and a yellow color.

---

### 4. **Convert Back to OpenCV Format**
```python
frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
```
After drawing the text, the frame is converted back to OpenCV format for display.

---

### 5. **Draw Bounding Box Using OpenCV**
```python
cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
```
The bounding box is still drawn using OpenCV, which handles shapes and rectangles well.

---

## ✅ Summary

This code uses **Pillow to render Korean text** and **OpenCV to draw bounding boxes**, combining the strengths of both libraries. This method is widely used when working with non-English labels in computer vision tasks.