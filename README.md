# WeBWorK Recollection

Helps you defeat WeBWorK

## Usage

- Run the script. It will guide you for the downloading of the question library
- Edit the following line of code to customize what the script is looking for. 
```py
target_string = b'Use the fact given above to evaluate the integral' ### EDIT THIS!
```

- Alternatively, write your own matching function. 

## Example

![question example](example.png)

Search for `Try substitution with`
Prompted to open `OpenProblemLibrary\Utah\AP_Calculus_I\set9_Basic_Methods_of_Integration\1220s10p6.pg`
Check the relevant code:
```perl
$ans = .5*log(exp(2) + exp(-2))- .5*log(2); 
ANS(num_cmp($ans));
```
Paste `.5*log(exp(2) + exp(-2))- .5*log(2)`, profit!

## Tips

- Do not select too much text at a time, as the problem files have line breaks in them which does not show up in WeBWork. 
- Go to `User Settings` in WeBWorK and Change Display Options: View equations as: images. 
  - Inspecting the images in developer tools. The `alt` parameter _may_ help you. 
