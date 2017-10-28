import re
def celsius_to_fahrenheit(match):
    degCelsius = float(match.group("celsius"))
    degF=32.0 + (degCelsius * 9.0 / 5.0);
    return '{}F'.format(degF)
def substitution_example_logic():
    pattern = r"(?P<celsius>\d+)\u00B0C"
    text = "Todays temperature is 49°C"
    print("pattern {}".format(pattern))
    print("before : {}".format(text))
    new_text = re.sub(pattern, celsius_to_fahrenheit,text)
    print("New: {}".format(new_text))

substitution_example_logic()
