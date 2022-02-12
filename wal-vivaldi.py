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
    --customTabBar: transparent;
    --customFg: {fg};
    --customFgAlpha: {fg}1a;
    --customFgIntense: {fg};
    --customFgFaded: {fg};
    --customFgFadedMore: {fg};
    --customFgFadedMost: {fg};
    --customBg: {bg};
    --customBgAlpha: {bg}e6;
    --customBgAlphaHeavy: {bg}a6;
    --customBgAlphaHeavier: {bg}40;
    --customBgAlphaBlur: {bg}f2;
    --customBgDark: {bg};
    --customBgDarker: {bg};
    --customBgLight: {bg};
    --customBgLighter: {bg};
    --customBgLightIntense: {bg};
    --customBgIntense: {bg};
    --customBgIntenser: {bg};
    --customBgIntserAlpha: {bg}eb;
    --customBgInverse: {bg};
    --customBgInverser: {bg};
    --customBgFaded: {bg};
    --customHighlightBg: {col["color6"]};
    --customHighlightBgUnfocused: {col["color5"]};
    --customHighlightBgAlpha: {col["color6"]}1a;
    --customHighlightBgDark: {col["color4"]};
    --customHighlightFg: {col["color2"]};
    --customHighlightFgAlpha: {col["color2"]}80;
    --customHighlightFgAlphaHeavy: {col["color2"]}40;
    --customAccentBg: {col["color2"]};
    --customAccentBgAlpha: {col["color2"]}66;
    --customAccentBgAlphaHeavy: {col["color2"]}40;
    --customAccentBgDark: {col["color2"]};
    --customAccentBgDarker: {col["color2"]};
    --customAccentBgFaded: {col["color2"]};
    --customAccentBgFadedMore: {col["color2"]};
    --customAccentBgFadedMost: {col["color2"]};
    --customAccentBorder: {col["color3"]};
    --customAccentBorderDark: {col["color3"]};
    --customAccentFg: {fg};
    --customAccentFgFaded: {fg};
    --customAccentFgAlpha: {fg}40;
    --customBorder: #1c1c1c;
    --customBorderDisabled: #242424;
    --customBorderSubtle: #222222;
    --customBorderIntense: #0c0c0c;
    --customSuccessBg: #06a700;
    --customSuccessBgAlpha: #06a7001a;
    --customSuccessFg: #ffffff;
    --customWarningBg: #efaf00;
    --customWarningBgAlpha: #efaf001a;
    --customWarningFg: #000000;
    --customErrorBg: #c64539;
    --customErrorBgAlpha: #c645391a;
    --customErrorFg: #ffffff;
    --customWindowBg: #1d1e21;
    --customWindowFg: #ffffff;
}}"""

    print(output)

    with open(sys.argv[1], 'w') as file:
        file.write(output)

if __name__ == "__main__":
    __main__()

