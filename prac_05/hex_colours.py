COLOUR_TO_CODE = {"Bittersweet": "#fe6f5e", "Black Coffee": "#3b2f2f",
                  "Gamboge": "#e49b0f", "Zomp": "#39a78e",
                  "Wild Strawberry": "#ff43a4", "Green Sheen": "#6eaea1",
                  "Japanese Carmine": "#9d2933", "Deep Saffron": "#ff9933",
                  "Cinnabar": "#e34234", "LightSeaGreen": "#20b2aa"
                  }
colour_name = input("Enter a colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(COLOUR_TO_CODE[colour_name])
    colour_name = input("Enter a colour name: ")
