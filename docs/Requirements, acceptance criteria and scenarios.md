# Requirements  
* Req-1: The application must receive a decimal formatted number (from 1 to 3999 inclusive) and show its roman-number conversion.
* Req-2: The application must validate that the input has only numbers.
* Req-3: The application must print the roman conversion in the user's console.
* Req-4: In case of an invalid input, the application must ask the user for a valid input.
* Req-5: The application does not allow negative numbers.

# Acceptance Criteria
* Cri-2-1: The application receives and processes only valid inputs.
* Cri-3-1: The application prints in the console the decimal to roman number conversion requested.
* Cri-4-1: Given an invalid number, the application asks the user for another input.

# Test cases

## Ent-To-End
* E2E-1: The user's input and the text displayed by the program are in the same line.
* E2E-2: The user inserts '8us'. The program says "The given number is invalid. Try again."
* E2E-3: Given an invalid input, the program asks the user for another input until a valid one is given.

## Unitarian
* User input is 5. Application returns 'V'
* User input is 46. Application returns 'XLVI'
* User input is 690. Application returns 'DCXC'
* User input is 3900. Application returns 'MMMCM'
* User input is greater than 3999. Application returns 'Insert a whole number between 1 and 3999 inclusive. Try Again.'