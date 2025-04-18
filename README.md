# Largest Interior Rectangle Detection with OpenCV

This project captures video from your webcam, detects foreground objects, and computes the **Largest Interior Rectangle (LIR)** within those objects using computer vision techniques. The result is displayed in real-time with bounding boxes and dimension labels.

---

## Features

- Real-time video capture and processing
- Background subtraction using MOG2
- Noise reduction with morphological operations
- Largest Interior Rectangle (LIR) detection
- On-screen display of width and height for the rectangle

---


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Infintesky/03.007-Design-Thnking-and-Innovation.git
   ```

2. **Install dependencies and create virtual environment**
    ```bash
    poetry install
    ```

3. **Activate the virtual environment**
    ```bash
    poetry env activate
    ```

## Usage

```bash
poetry run python3 main.py
```

## Credits
[LIR algorithm](https://gist.github.com/zaniarshokati/ea7db9ba11b8424ad9b5dfe683a865f4)