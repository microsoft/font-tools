# Egyptian Open Type
This project parses an existing Egyptian Hieroglyphic font and generates a new font containing VOLT OpenType source code that can then be compiled using Microsoft's [Visual OpenType Layout Tool (VOLT)](https://learn.microsoft.com/en-us/typography/tools/volt/). Once compiled, the new font contains all of the OpenType logic needed to render Egyptian Hieroglyphic text with the [Unicode 15 format controls](http://unicode.org/charts/PDF/U13430.pdf). Correct rendering of the OpenType tables for blocks of Egyptian Hieroglyphs depends on font rendering via the [Universal Shaping Engine](https://learn.microsoft.com/en-us/typography/script-development/use) and its Hieroglyph cluster model:

>`SB* G [VS] [HR] [HM] SE* ( J SB* G [VS] [HR] [HM] SE* )*`

## Files
The project consists of the following core files:

- **config.py** — specifies the per-font details such as font name, key dimensions etc.
- **eotgen.py** — runs the project. It takes a commandline parameter to specify the config file to be used.
- **eotHelper.py** — the class file containing all the logic to process the font and generate the OpenType. It has additional functions for generating font tests and keyboard data.
- **featuredata.py** — contains static data for use in the project.
- **insertions.py** — contains per-font data specifying the size of insertion areas.
- **mark.py** — contains the data for the OpenType mark feature lookups.
- **mkmk.py** — contains the data for the OpenType mkmk feature lookups.
- **pres.py** — contains the data for the OpenType pres feature lookups.

Data for other OpenType features are integrated into the EotHelper class.

## Source font

The project depends on a suitable font in order to run. The font should be a TrueType font with the following characters, glyphs and conventions:

### Core Egyptian Unicode Characters
- **Egyptian Hieroglyphs** — The basic hierglyph signs with the exception of the signs which participate in enclosures (i.e., U+13000–13257, U+1325E–13285, U+1328A–13378, U+1337C–1342E). The font should include one or more Egyptian Hieroglyph characters. Some fonts will choose to include a subset of characters for stylistic, corpus, or other purposes. Characters should be named after their Gardiner names without padding zeros (e.g., G1). Variants should be suffixed with a lowercase letter (e.g., G7a). As such, Hieroglyph character names conform to the regular expression:
> ^[A-Z]+[0-9]+[a-z]?

![Sample hieroglyph characters](/png/eh.png)

- **Enclosure ends** — The enclosure ends get special treatment. They do not have to be included, but if included they should be named as follows:

| Sign | Code point | Name | Description |
| ---- | ---------- | ---- | ----------- |
| 𓉘 | U+13258 | hwtb | HWT enclosure begin |
| 𓉙 | U+13259 | hwtbb | HWT enclosure bottom (corner) begin |
| 𓉚 | U+1325A | hwttb | HWT enclosure top (corner) begin |
| 𓉛 | U+1325B | hwtte | HWT enclosure top (corner) end |
| 𓉜 | U+1325C | hwtbe | HWT enclosure bottom (corner) end |
| 𓉝 | U+1325D | hwte | HWT enclosure end |
| 𓊆 | U+13286 | cwb | Cartouche walled begin |
| 𓊇 | U+13287 | cwe | Cartouche walled end |
| 𓊈 | U+13288 | cwb | HWT walled begin |
| 𓊉 | U+13289 | cwe | HWT walled end |
| 𓍹 | U+13379 | cb | Cartouche begin |
| 𓍺 | U+1337A | cwe | Cartouche end |
| 𓍻 | U+1337B | cre | Cartouche reversed end |
| 𓐯 | U+1342F | crb | Cartouche reversed begin |

- **Egyptian Hieroglyph Format Controls** — The format controls should have conventional visible forms for fallback purposes. Only a subset need be included. When included, they should be named as follows:

| Sign | Code point | Name | Description |
| ---- | ---------- | ---- | ----------- |
| 𓐰 | U+13430 | vj | Vertical joiner |
| 𓐱 | U+13431 | hj | Horizontal joiner |
| 𓐲 | U+13432 | ts | Insertion top start |
| 𓐳 | U+13433 | bs | Insertion bottom start |
| 𓐴 | U+13434 | te | Insertion top end |
| 𓐵 | U+13435 | be | Insertion bottom end |
| 𓐶 | U+13436 | om | Overlay middle |
| 𓐷 | U+13437 | ss | Segment start |
| 𓐸 | U+13438 | se | Segment end |
| 𓐹 | U+13439 | mi | Middle insertion |
| 𓐺 | U+1343A | ti | Top insertion |
| 𓐻 | U+1343B | bi | Bottom insertion |
| 𓐼 | U+1343C | esb | Enclosure single begin |
| 𓐽 | U+1343D | ese | Enclosure single end |
| 𓐾 | U+1343E | ewb | Enclosure walled begin |
| 𓐿 | U+1343F | ewe | Enclosure walled end |
| 𓑀 | U+13440 | mr | Mirror horizontally |
| 𓑁 | U+13441 | BF1 | Blank full |
| 𓑂 | U+13442 | BQ1 | Blank quarter |
| 𓑃 | U+13443 | AS1 | Lost sign full |
| 𓑄 | U+13444 | AQ1 | Lost sign quarter |
| 𓑅 | U+13445 | AT1 | Lost sign tall |
| 𓑆 | U+13446 | AW1 | Lost sign wide |
| 𓑇 | U+13447 | dq1 | Damaged quarter 1 |
| 𓑈 | U+13448 | dq2 | Damaged quarter 2 |
| 𓑉 | U+13449 | dq12 | Damaged quarter 12 |
| 𓑊 | U+1344A | dq3 | Damaged quarter 3 |
| 𓑋 | U+1344B | dq13 | Damaged quarter 13 |
| 𓑌 | U+1344C | dq23 | Damaged quarter 23 |
| 𓑍 | U+1344D | dq123 | Damaged quarter 123 |
| 𓑎 | U+1344E | dq4 | Damaged quarter 4 |
| 𓑏 | U+1344F | dq14 | Damaged quarter 14 |
| 𓑐 | U+13450 | dq24 | Damaged quarter 24 |
| 𓑑 | U+13451 | dq124 | Damaged quarter 124 |
| 𓑒 | U+13452 | dq34 | Damaged quarter 34 |
| 𓑓 | U+13453 | dq134 | Damaged quarter 134 |
| 𓑔 | U+13454 | dq234 | Damaged quarter 234 |
| 𓑕 | U+13455 | df | Damaged full    1234 |

- **Variation Selectors** — Signs for the variation selectors should be included for fallback purposes (U+FE00–FE02). These signs need not be included if the rotational and other variants are not supported by the font.

### Recommended Unicode Characters
- **Latin letters** — OpenType Egyptian Hieroglyphic fonts work best when they include Latin characters to support input. In addition to the [ASCII range](http://unicode.org/charts/PDF/U0000.pdf), Latin coverage should include Egyptological transliteration characters, as follows:

| Sign | Code point | Description |
| ---- | ---------- | ----------- |
| Č | U+010C | LATIN CAPITAL LETTER C WITH CARON |
| č | U+010D | LATIN SMALL LETTER C WITH CARON |
| Ś | U+015A | LATIN CAPITAL LETTER S WITH ACUTE |
| ś | U+015B | LATIN SMALL LETTER S WITH ACUTE |
| Š | U+0160 | LATIN CAPITAL LETTER S WITH CARON |
| š | U+0161 | LATIN SMALL LETTER S WITH CARON |
| Ť | U+0164 | LATIN CAPITAL LETTER T WITH CARON |
| ť | U+0165 | LATIN SMALL LETTER T WITH CARON |
| Ž | U+017D | LATIN CAPITAL LETTER Z WITH CARON |
| ž | U+017E | LATIN SMALL LETTER Z WITH CARON |
| Ḏ | U+1E0E | LATIN CAPITAL LETTER D WITH LINE BELOW |
| ḏ | U+1E0F | LATIN SMALL LETTER D WITH LINE BELOW |
| Ḥ | U+1E24 | LATIN CAPITAL LETTER H WITH DOT BELOW |
| ḥ | U+1E25 | LATIN SMALL LETTER H WITH DOT BELOW |
| Ḫ | U+1E2A | LATIN CAPITAL LETTER H WITH BREVE BELOW |
| ḫ | U+1E2B | LATIN SMALL LETTER H WITH BREVE BELOW |
| Ḳ | U+1E32 | LATIN CAPITAL LETTER K WITH DOT BELOW |
| ḳ | U+1E33 | LATIN SMALL LETTER K WITH DOT BELOW |
| Ṭ | U+1E6C | LATIN CAPITAL LETTER T WITH DOT BELOW |
| ṭ | U+1E6D | LATIN SMALL LETTER T WITH DOT BELOW |
| Ṯ | U+1E6E | LATIN CAPITAL LETTER T WITH LINE BELOW |
| ṯ | U+1E6F | LATIN SMALL LETTER T WITH LINE BELOW |
| Ṱ | U+1E70 | LATIN CAPITAL LETTER T WITH CIRCUMFLEX BELOW |
| ṱ | U+1E71 | LATIN SMALL LETTER T WITH CIRCUMFLEX BELOW |
| ẖ | U+1E96 | LATIN SMALL LETTER H WITH LINE BELOW |
| Ꜣ | U+A722 | LATIN CAPITAL LETTER EGYPTOLOGICAL ALEF |
| ꜣ | U+A723 | LATIN SMALL LETTER EGYPTOLOGICAL ALEF |
| Ꜥ | U+A724 | LATIN CAPITAL LETTER EGYPTOLOGICAL AIN |
| ꜥ | U+A725 | LATIN SMALL LETTER EGYPTOLOGICAL AIN |
| Ꞽ | U+A7BC | LATIN CAPITAL LETTER GLOTTAL I |
| ꞽ | U+A7BD | LATIN SMALL LETTER GLOTTAL I |

**Note** — glyph names for these characters are unimportant as they are not included in the generation of OpenType layout tables. OpenType tables for the Latin range is outside of the scope of this project.

- **Egyptological brackets** — The following brackets should be included if support for Egyptological transliteration is intended. These brackets may also participate in Hieroglyph cluster formation in supporting software.

| Sign | Code point | Description |
| ---- | ---------- | ----------- |
| ⟦ | U+27E6 | MATHEMATICAL LEFT WHITE SQUARE BRACKET |
| ⟧ | U+27E7 | MATHEMATICAL RIGHT WHITE SQUARE BRACKET |
| ⟨ | U+27E8 | MATHEMATICAL LEFT ANGLE BRACKET |
| ⟩ | U+27E9 | MATHEMATICAL RIGHT ANGLE BRACKET |
| ⟮ | U+27EE | MATHEMATICAL LEFT FLATTENED PARENTHESIS |
| ⟯ | U+27EF | MATHEMATICAL RIGHT FLATTENED PARENTHESIS |
| ⸢ | U+2E22 | TOP LEFT HALF BRACKET |
| ⸣ | U+2E23 | TOP RIGHT HALF BRACKET |
| ⸤ | U+2E24 | BOTTOM LEFT HALF BRACKET |
| ⸥ | U+2E25 | BOTTOM RIGHT HALF BRACKET |

- **Directional controls and joiners** — when right-to-left layout support is planned, fonts should include glyphs for the directional controls and joiners:

| Code point | Description |
| ---------- | ----------- |
| U+200C | ZERO WIDTH NON-JOINER |
| U+200D | ZERO WIDTH JOINER |
| U+200E | LEFT-TO-RIGHT MARK |
| U+200F | RIGHT-TO-LEFT MARK |

- **Generic bases** — The generic base U+25CC DOTTED CIRCLE may be included in a font for participation in Hieroglyph cluster formation.

| Sign | Code point | Name | Description |
| ---- | ---------- | ---- | ----------- |
| ◌ | U+25CC | dottedcircle | DOTTED CIRCLE |

### Glyph convensions
Font glyphs for most visible 

### Recommended Glyphs
