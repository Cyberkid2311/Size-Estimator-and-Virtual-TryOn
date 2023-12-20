# Size Estimator and Virtual Try-On Solution

## Overview

In the dynamic world of e-commerce, particularly in the fashion sector, the persisting challenge of returns and dissatisfied customers due to sizing issues demands a revolutionary solution. This project presents an innovative Size Estimator and Virtual Try-On system. Leveraging cutting-edge AI and ML techniques, the aim is to empower shoppers to make informed decisions about fit and style effortlessly.

## Size Estimator

### Process Flow

1. **User Input**: The user provides height and a photo.
2. **OpenPose Integration**: The photo is processed using OpenPose to identify key body points.
3. **Contour Analysis**: A contour-based model in OpenCV extracts the contours of the person's actual flesh, providing precise measurements.
4. **Pixel to Centimeter Conversion**: The obtained pixel measurements are converted into centimeters.
5. **Extreme Points Calculation**: Horizontal and vertical lines on the contour determine extreme points for shoulder, bust, hip, and waist.
6. **Size Calculation**: Utilizing the extreme points, the actual sizes are calculated based on the company’s size chart and previous databases.

## Virtual Try-On

### Execution

To experience the Virtual Try-On, the 'RantOn_Final.py' file is executed with three arguments:

```bash
python RantOn_Final.py <Path_of_our_File> <Path_of_the_image_of_the_customer> <Path_of_the_image_of_the_apparel_we_want_to_try_on>
```

### Supporting Files

1. **Apparel.py**: Handles preprocessing of the new apparel for the try-on.
2. **Customer.py**: Manages preprocessing of the customer's image.
3. **Join.py**: Integrates the new apparel onto the customer's image for a realistic try-on experience.

### Functions

- **grabcut()**: Gathers the required portion of the customer’s image and the cutout of the existing clothing.
- **userPreprocess()**: Breaks down the cutout into sections at joints for a detailed analysis and sizing.
- **catPreprocess()**: Processes the flattened image of the new apparel, resizing it with cutout sections of the original clothing.
- **userFit()**: Positions modified sections of the new apparel appropriately on the customer's image for a near-real-life visual.

## Conclusion

This project addresses the pain points of online apparel shopping. The Size Estimator and Virtual Try-On system not only enhances sizing accuracy but also provides customers with a virtual dressing room experience, reducing confusion and ensuring a seamless shopping journey. Embrace the future of online fashion retail with confidence and ease.
