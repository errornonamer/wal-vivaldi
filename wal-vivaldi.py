import json
import sys
import os

def __main__():
    if len(sys.argv) != 2:
        print("usage: python wal-vivaldi.py output.css")
        return
    
    colors = {}
    with open(os.path.expanduser('~') + "/.cache/wal/colors.json", 'r') as file:
        string = ""
        for line in file:
            string += line
        colors = json.loads(string)
        print(colors)
    
    bg = colors["special"]["background"]
    fg = colors["special"]["foreground"]
    col = colors["colors"]

    output = f""":root {{
    --colorFg: {fg} !important;
    --colorFgAlpha: {fg}1a !important;
    --colorFgIntense: {fg} !important;
    --colorFgFaded: {fg} !important;
    --colorFgFadedMore: {fg} !important;
    --colorFgFadedMost: {fg} !important;
    --colorBg: {bg} !important;
    --colorBgAlpha: {bg}e6 !important;
    --colorBgAlphaHeavy: {bg}a6 !important;
    --colorBgAlphaHeavier: {bg}40 !important;
    --colorBgAlphaBlur: {bg}f2 !important;
    --colorBgDark: {bg} !important;
    --colorBgDarker: {bg} !important;
    --colorBgLight: {bg} !important;
    --colorBgLighter: {bg} !important;
    --colorBgLightIntense: {bg} !important;
    --colorBgIntense: {bg} !important;
    --colorBgIntenser: {bg} !important;
    --colorBgIntserAlpha: {bg}eb !important;
    --colorBgInverse: {bg} !important;
    --colorBgInverser: {bg} !important;
    --colorBgFaded: {bg} !important;
    --colorHighlightBg: {col["color6"]} !important;
    --colorHighlightBgUnfocused: {col["color5"]} !important;
    --colorHighlightBgAlpha: {col["color6"]}1a !important;
    --colorHighlightBgDark: {col["color4"]} !important;
    --colorHighlightFg: {col["color2"]} !important;
    --colorHighlightFgAlpha: {col["color2"]}80 !important;
    --colorHighlightFgAlphaHeavy: {col["color2"]}40 !important;
    --colorAccentBg: {col["color2"]} !important;
    --colorAccentBgAlpha: {col["color2"]}66 !important;
    --colorAccentBgAlphaHeavy: {col["color2"]}40 !important;
    --colorAccentBgDark: {col["color2"]} !important;
    --colorAccentBgDarker: {col["color2"]} !important;
    --colorAccentBgFaded: {col["color2"]} !important;
    --colorAccentBgFadedMore: {col["color2"]} !important;
    --colorAccentBgFadedMost: {col["color2"]} !important;
    --colorAccentBorder: {col["color3"]} !important;
    --colorAccentBorderDark: {col["color3"]} !important;
    --colorAccentFg: {fg} !important;
    --colorAccentFgFaded: {fg} !important;
    --colorAccentFgAlpha: {fg}40 !important;
}}"""

    print(output)

    with open(sys.argv[1], 'w') as file:
        file.write(output)

if __name__ == "__main__":
    __main__()
