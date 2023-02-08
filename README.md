# WeBWorK Recollection

Helps you defeat WeBWorK

## Usage

- Run the script. It will guide you for the downloading of the question library
- Edit the following line of code to customize what the script is looking for. 
```py
target_string = b'Use the fact given above to evaluate the integral' ### EDIT THIS!
```

- Alternatively, write your own matching function. 

## Tips

- Do not select too much text at a time, as the problem files have line breaks in them which does not show up in WeBWork. 
- Go to `User Settings` in WeBWorK and Change Display Options: View equations as: images. 
  - Inspecting the images in developer tools. The `alt` parameter _may_ help you. 
