## Simple Python Morse Code translator

Translates text to morse code and morse code to text using a small set of International morse code. Includes a small suite of basic tests.

### Usage

After cloning this repo, run:

```sh
python example.py
```

Output:

```sh
- .... .. ...   ... - .-. .. -. --.   .... .- ...   -... . . -.   - .-. .- -. ... .-.. .- - . -..   - ---   -- --- .-. ... .   -.-. --- -.. .   .- -. -..   -... .- -.-. -.-   .- --. .- .. -.
this string has been translated to morse code and back again
```

Feel free to change the text in the example. The example calls `translate_morse` using the output of `translate_text`, which is provided with a string.

### Tests

To run the tests:

```sh
python tests.py
```