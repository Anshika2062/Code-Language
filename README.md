# Code-Language
This Python program allows you to encode messages into a secret code language and decode them back to their original form. The encoding and decoding follow specific rules to transform the messages while maintaining their confidentiality.

## Encoding Rules:
If a word contains at least 3 characters:<br>
   Remove the first letter and append it at the end.<br>
   Append three random characters at the beginning and the end.<br>
   
If a word contains fewer than 3 characters:<br>
   Reverse the string.<br>

## Decoding Rules:
If a word contains less than 6 characters (at least 3 random characters, 1 letter, and 2 random characters):<br>
    Reverse the string.<br>

If a word contains 6 or more characters:<br>
    Remove the first 3 random characters from the start.<br>
    Remove the last letter and append it to the beginning.<br>

## Usage:
Run the program by executing the Python script in your terminal or IDE.<br>

You will be prompted to choose whether you want to "code" (encode) or "decode" a message.<br>

If you choose to "encode":<br>
   Enter the message you want to encode when prompted.<br>
   The program will apply the encoding rules and display the encoded message.<br>
   
If you choose to "decode":<br>
   Enter the encoded message you want to decode when prompted.<br>
   The program will apply the decoding rules and display the decoded message.<br>
Invalid choices will result in appropriate error messages.
