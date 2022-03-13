#!/usr/bin/python
import json
import os

def generate():
    colors = {}

    with open(os.path.expanduser('~') + "/.cache/wal/colors.json", 'r') as file:
        colors = json.loads(file.read())
    
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
    --customHighlightBgUnfocused: {col["color6"]};
    --customHighlightBgAlpha: {col["color6"]}1a;
    --customHighlightBgDark: {col["color6"]};
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
    --customBorder: var(--colorBorder);
    --customBorderDisabled: var(--colorBorderDisabled);
    --customBorderSubtle: var(--colorBorderSubtle);
    --customBorderIntense: var(--colorBorderIntense);
    --customSuccessBg: var(--colorSuccessBg);
    --customSuccessBgAlpha: var(--colorSuccessBgAlpha);
    --customSuccessFg: var(--colorSuccessFg);
    --customWarningBg: var(--colorWarningBg);
    --customWarningBgAlpha: var(--colorWarningBgAlpha);
    --customWarningFg: var(--colorWarningFg);
    --customErrorBg: var(--colorErrorBg);
    --customErrorBgAlpha: var(--colorErrorBgAlpha);
    --customErrorFg: var(--colorErrorFg);
    --customWindowBg: {bg};
    --customWindowFg: {fg};
}}"""

    with open("./wal.css", 'w') as file:
        file.write(output)

def __main__():
    generate()
    

if __name__ == "__main__":
    __main__()

