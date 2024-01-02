# Barcode Scanner with Authentication

This Python script utilizes the OpenCV and pyzbar libraries to create a barcode scanner with added authentication. The program reads barcodes from an image or webcam feed, checks the decoded data against a list of authorized data, and provides feedback on the authentication status.

Prerequisites
Make sure you have the required libraries installed:

If you want to run this project locally, follow these steps:

1. Clone this repository:
```bash
  git clone git@github.com:HuzaifaIlyas02/QrScanner.git
```
2. Navigate to the folder:
```
cd QrScanner
```

3. Run Locally:
```
python Qrscanner.py
```


## Configuration
Place the image file containing barcodes in the project directory and update the script accordingly.
The myDataFile.txt file should contain a list of authorized barcode data, with each data on a new line.

## License
This project is licensed under the MIT License.