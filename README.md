# Largest Interior Rectangle Detection with OpenCV

## About

This Largest Interior Rectangle Detection is designed to determine if used materials in makerspaces are still reusable based on the largest interior rectangular area left on the material. It is developed for SUTD - DTI 03.007.

This code leverages image segmentation techniques from computer vision and result is displayed in real-time with bounding boxes and reusability labels.

https://github.com/user-attachments/assets/aa6e1058-bd67-4b06-a3e6-ba7eb7eae827

https://github.com/user-attachments/assets/8fcde1dd-e40f-4d4d-92d1-138e5d04a25c

---

## Features

- Real-time video capture and processing
- Background subtraction using MOG2
- Noise reduction with morphological operations
- Largest Interior Rectangle (LIR) detection
- On-screen display for reusability of material

---
## Get Started
### Prerequisites

Make sure you have the following installed on your system:

- Python 3.13 or later 
- `Poetry` for dependency management (install using `pipx install poetry`)


### Installation Steps

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

4. **Run**
    ```bash
    poetry run python3 src/main.py
    ```

## References
[Largest Interior algorithm](https://gist.github.com/zaniarshokati/ea7db9ba11b8424ad9b5dfe683a865f4)

[Computing the largest orthogonal rectangle in a convex polygon](https://cgm.cs.mcgill.ca/%7Eathens/cs507/Projects/2003/DanielSud/)

[The Polygon Containment Problem](https://www.cs.princeton.edu/%7Echazelle/pubs/PolygContainmentProb.pdf)

[Finding the Axis Aligned Largest Interior Rectangle in a simple polygon](https://www.evryway.com/largest-interior/)

[Algorithm for finding the largest inscribed rectangle in polygon](https://journals.ut.ac.ir/article_71280_2a21de484e568a9e396458a5930ca06a.pdf)
