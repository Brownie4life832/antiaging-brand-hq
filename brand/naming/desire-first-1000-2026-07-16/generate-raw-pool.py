from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "raw-pool.csv"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", value.lower())


rows: list[dict[str, str | int]] = []
seen: set[str] = set()


def add(name: str, direction: str, method: str, source: str) -> None:
    name = re.sub(r"\s+", " ", name).strip().title()
    norm = normalize(name)
    if not norm or norm in seen or not 2 <= len(norm) <= 24:
        return
    if len(name.split()) > 3:
        return
    if any(bad in norm for bad in ("pharma", "derma", "skincare", "antiaging", "vagina")):
        return
    seen.add(norm)
    rows.append(
        {
            "RawOrder": len(rows) + 1,
            "Name": name,
            "Direction": direction,
            "Method": method,
            "SourceWorld": source,
            "Normalized": norm,
        }
    )


def add_words(values: str, direction: str, method: str, source: str) -> None:
    for value in [item.strip() for item in values.split("|") if item.strip()]:
        add(value, direction, method, source)


# 1. THE INVENTED HOUSE
D = "The Invented House"
add_words(
    "Alderen|Alveren|Ambrin|Anveren|Ardelin|Asterel|Avelor|Belvern|Brennor|Calvere|Cervan|Corvell|Darven|Delvor|Dovren|Elvaren|Embray|Ervell|Farrenel|Galenor|Holleren|Iverell|Jorven|Kestrelle|Lioren|Maveren|Merron|Norvell|Orvane|Perrinor|Ravellen|Rellin|Seraven|Taveren|Valeron|Vellard|Verren|Wrennor|Zorell|Aldevan|Alvarel|Ambrel|Anvorel|Arvenor|Astelan|Avelen|Belvar|Brenell|Calven|Cerven|Corvenne|Darvell|Delvaren|Dorevan|Elverin|Emveren|Ervenne|Farenor|Gavrell|Halveren|Iveran|Jorell|Kerven|Lorven|Marden|Mervell|Norevan|Orrell|Paveren|Quarren|Ravern|Serren|Torvell|Varell|Velorin|Verrel|Werrenor|Yorven|Zavell",
    D,
    "Eponym / curated mononym",
    "Founderless fashion house",
)
house_stems = [
    "ald", "alv", "ambr", "anv", "ard", "ast", "avel", "belv", "bren", "calv",
    "cerv", "corv", "darv", "delv", "dore", "elv", "embr", "erv", "far", "gav",
    "halv", "iver", "jor", "kerv", "lior", "mav", "merr", "norv", "orv", "pav",
    "per", "rav", "rell", "ser", "tav", "val", "vell", "verr", "wren", "zor",
]
house_endings = ["en", "el", "ell", "er", "et", "in", "on", "ren", "sen", "ven", "ard", "ier"]
for i, stem in enumerate(house_stems):
    for j, ending in enumerate(house_endings):
        if (i * 5 + j * 7) % 4 != 0:
            add(stem + ending, D, "Morpheme engine", "Invented surname matrix")
for stem in ["avel", "bel", "cor", "dov", "elv", "ferr", "hal", "iver", "lor", "marr", "nor", "orel", "per", "ser", "tov", "val", "ver"]:
    for ending in ["ane", "ene", "enne", "ine", "ore", "enne", "aire", "airel"]:
        add(stem + ending, D, "World-language-shaped coinage", "Fashion-house phonology")


# 2. THE PURE SOUND LAB
D = "The Pure Sound Lab"
add_words(
    "Abrin|Adrel|Aevon|Aroven|Belune|Briven|Calune|Cavrel|Dalen|Dovik|Elaro|Elune|Emren|Evrel|Faven|Felor|Firae|Glaven|Ivro|Kalen|Kavro|Laven|Leron|Lunel|Mavik|Meloa|Miven|Navelin|Nelor|Nivon|Odrin|Ovela|Pavik|Pelor|Ravelin|Relune|Rivan|Savel|Selor|Sivon|Tavel|Tivra|Uvel|Vairel|Varen|Veloa|Virel|Zavel|Zorin|Aroa|Evere|Iviri|Olivo|Uruva|Avarin|Evelen|Irilis|Oroven|Uvelu",
    D,
    "Sound-first curated coinage",
    "No-semantic brief",
)
onsets = ["b", "br", "c", "d", "f", "g", "gl", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
nuclei = ["a", "e", "i", "o", "u", "ae", "ai", "eo", "io", "oa", "ue"]
codas = ["bel", "den", "len", "lor", "mel", "ner", "rel", "ren", "sen", "tal", "ven", "ver", "vin", "von", "zel", "ris", "mon", "dor", "lin", "nel"]
for i, onset in enumerate(onsets):
    for j, nucleus in enumerate(nuclei):
        for k, coda in enumerate(codas):
            if (i * 7 + j * 11 + k * 13) % 19 == 0:
                add(onset + nucleus + coda, D, "Sound-first coinage", "Consonant-vowel texture matrix")
for left in ["av", "el", "iv", "ol", "or", "ul", "ar", "ev", "il", "ur"]:
    for middle in ["a", "e", "i", "o", "u"]:
        mirrored = left + middle + left[::-1]
        add(mirrored, D, "Structural symmetry", "Palindromic sound shape")
for root in ["briv", "cal", "dav", "fel", "glav", "kel", "lav", "mel", "niv", "pel", "rav", "sel", "tav", "vel", "zav"]:
    for ending in ["o", "a", "en", "el", "ik", "um", "ae", "io", "une", "aro"]:
        add(root + ending, D, "Deconstruct / reconstruct", "Mouthfeel variation")


# 3. THE BEAUTIFUL OBJECT
D = "The Beautiful Object"
objects = [
    "Cameo", "Signet", "Folio", "Vellum", "Locket", "Bezel", "Inlay", "Clasp", "Seal",
    "Vessel", "Keepsake", "Talisman", "Armature", "Plinth", "Frame", "Mirror", "Lantern",
    "Vase", "Compass", "Chalice", "Brooch", "Medallion", "Portrait", "Glyph", "Emblem",
    "Token", "Curio", "Reliquary", "Album", "Letter", "Coffer", "Cabinet", "Screen", "Lens",
    "Prism", "Hourglass", "Thread", "Loom", "Kiln", "Cast", "Glaze", "Gesso", "Fresco",
    "Mosaic", "Filigree", "Marquetry", "Lacquer", "Porcelain", "Enamel", "Tondo", "Relief",
    "Carafe", "Decanter", "Goblet", "Pendant", "Buckle", "Casket", "Sculpture", "Etching",
    "Monogram", "Bookplate", "Watchcase", "Paperweight", "Diptych", "Triptych", "Miniature",
]
for value in objects:
    add(value, D, "Real-word object metaphor", "Decorative arts and heirlooms")
object_modifiers = [
    "Bright", "Civic", "Common", "Dear", "Fine", "Grand", "Human", "Kindred", "Lucent",
    "Modern", "Open", "Private", "Rare", "Quiet", "Warm", "Wild", "Tender", "Vivid",
    "Living", "Lasting", "New", "Good", "Everyday", "Honest", "Clear", "Full", "Inner",
]
for i, modifier in enumerate(object_modifiers):
    for j, obj in enumerate(objects[:48]):
        if (i * 7 + j * 5) % 11 == 0:
            add(f"{modifier} {obj}", D, "Compound 1+1=3", "Modern-heirloom collision")
for obj in ["cameo", "signet", "folio", "vellum", "locket", "bezel", "inlay", "lantern", "glyph", "token", "curio", "prism", "mosaic", "gesso", "relic"]:
    for ending in ["work", "house", "made", "mark", "form", "kind", "wise"]:
        add(obj + ending, D, "Deconstruct / reconstruct", "Object-to-house coinage")


# 4. THE MAGNETIC CHARACTER
D = "The Magnetic Character"
archetypes = [
    "Author", "Citizen", "Dame", "Darling", "Editor", "Expert", "Friend", "Host", "Icon",
    "Insider", "Keeper", "Maven", "Original", "Patron", "Reader", "Sage", "Scholar", "Sister",
    "Witness", "Muse", "Mentor", "Maker", "Minder", "Neighbor", "Heir", "Heroine", "Elder",
    "Principal", "Favorite", "Steward", "Advocate", "Confidante", "Benefactor", "Companion",
    "Curator", "Decider", "Diplomat", "Individual", "Natural", "Realist", "Romantic", "Modernist",
]
for value in archetypes:
    add(value, D, "Real-word eponym", "Social archetypes")
character_qualities = [
    "Able", "Brave", "Candid", "Clever", "Dear", "Fine", "Free", "Good", "Grand", "Honest",
    "Kind", "Lucid", "Modern", "Original", "Rare", "Real", "True", "Warm", "Wild", "Wise",
    "Witty", "Bold", "Bright", "Proper", "Quiet", "Vivid", "Certain", "Entire", "Private",
]
for i, quality in enumerate(character_qualities):
    for j, archetype in enumerate(archetypes):
        if (i * 3 + j * 7) % 10 == 0:
            add(f"{quality} {archetype}", D, "Archetypal compound", "Magnetic-character matrix")
add_words(
    "The Knowing One|The Good Sort|The Original One|Someone Wonderful|A Certain Person|Your Better Half|The Main Character|Good Company|The Favorite|The Individual|The Natural|The Modernist|The Realist|The Romantic|The Decider|The Connoisseur|The Confidante|The Benefactor|The Luminary|The Principal|Dear Someone|Known Personally|One Fine Person|Proper Company|Rare Company|In Good Company",
    D,
    "Character proposition",
    "Persona and social gravity",
)


# 5. THE PRIVATE WORLD
D = "The Private World"
places = [
    "Alcove", "Anteroom", "Arcade", "Atrium", "Belvedere", "Gallery", "Loggia", "Parlor",
    "Portico", "Salon", "Studio", "Sunroom", "Terrace", "Vestibule", "Wing", "Pavilion",
    "Orangerie", "Library", "Study", "Hall", "Court", "House", "Garden", "Room", "Landing",
    "Foyer", "Niche", "Hearth", "Veranda", "Observatory", "Rotunda", "Conservatory", "Cloister",
    "Mezzanine", "Drawing Room", "Music Room", "Winter Room", "Cabinet", "Sanctum", "Annex",
]
for value in places:
    add(value, D, "Real-word place metaphor", "Architecture and private rooms")
place_modifiers = [
    "After", "Blue", "Bright", "Common", "Dear", "East", "Fine", "First", "Good", "High",
    "Inner", "Last", "Little", "Long", "Lower", "Modern", "North", "Open", "Private", "Quiet",
    "Rare", "Red", "Secret", "South", "Upper", "Warm", "West", "Wild", "Winter", "New",
]
for i, modifier in enumerate(place_modifiers):
    for j, place in enumerate(places):
        if (i * 11 + j * 7) % 13 == 0:
            add(f"{modifier} {place}", D, "Place compound", "Private-world collision")
place_roots = ["alder", "amber", "arden", "aster", "briar", "calder", "dove", "ever", "hollis", "ivor", "linden", "morrow", "nor", "oren", "raven", "sable", "vale", "vel", "wren"]
place_endings = ["gate", "hall", "court", "field", "ward", "well", "mere", "mont", "house", "landing"]
for i, root in enumerate(place_roots):
    for j, ending in enumerate(place_endings):
        if (i + j * 3) % 3 != 0:
            add(root + ending, D, "Invented place name", "Geographic morpheme engine")


# 6. THE CULTURAL MONONYM
D = "The Cultural Mononym"
add_words(
    "Ligature|Kerning|Verso|Recto|Folio|Colophon|Aperture|Cadence|Chroma|Fresco|Gesso|Motif|Tempo|Aria|Coda|Encore|Proscenium|Soliloquy|Matinee|Vignette|Auteur|Montage|Cameo|Iris|Scrim|Rhapsody|Sonnet|Stanza|Quarto|Octavo|Serein|Brio|Sprezzatura|Parure|Intaglio|Tondo|Grisaille|Lustre|Moire|Ombre|Glissando|Rubato|Vivo|Sfumato|Impasto|Verdigris|Chiaroscuro|Pentimento|Fugue|Caprice|Nocturne|Prelude|Opus|Etude|Allegro|Andante|Adagio|Cantabile|Velluto|Tempera|Aquarelle|Atelier|Vernissage|Salon|Loggia|Arcade|Portico|Atrium|Belvedere|Orangerie|Pavilion|Alcove|Niche|Bijou|Curio|Reliquary|Talisman|Signet|Armature|Plinth|Frieze|Cornice|Oculus|Meridian|Parallax|Liminal|Penumbra|Aureole|Cartouche|Diptych|Triptych|Monograph|Marginalia|Endpaper|Frontispiece|Ex Libris|Serif|Italic|Roman|Blackletter|Foliose|Vitrine|Cabinet|Saloniste|Flaneur|Raconteur|Bonvivant|Aficionado|Virtuoso|Maestro|Prima|Doyenne|Ingenue|Soubrette|Reprise|Interlude|Overture|Finale|Syncopation|Timbre|Vibrato|Sonority|Chromatic|Arabesque|Pavane|Gavotte|Sarabande|Minuet|Mazurka|Bolero|Rondo|Toccata|Cadenza|Cantata|Sonata|Partita|Ricercar|Groundwork|Afterimage|Still Life|Vanishing Point|Golden Mean|Counterpoint|Fine Art|Full Bleed|First Edition",
    D,
    "Far-field real-word raid",
    "Typography, theatre, music, visual art, architecture",
)
add_words(
    "Quire|Gathering|Deckle|Endleaf|Flyleaf|Foreedge|Headband|Tailpiece|Rubric|Imprint|Signature|Leaf|Plate|Galley|Blueline|Fascicle|Chapbook|Broadside|Bookhand|Handpress|Letterpress|Woodtype|Foundry|Sort|Pica|Brevier|Nonpareil|Smallcap|Swash|Terminal|Ascender|Descender|Counterform|Baseline|X Height|Ductus|Uncial|Majuscule|Minuscule|Bastarda|Rotunda|Fraktur|Antiqua|Didone|Grotesk|Humanist|Basque|Bias|Dart|Pleat|Selvage|Facing|Notch|Lapel|Cambre|Toile|Muslin|Poplin|Twill|Taffeta|Organza|Voile|Batiste|Brocade|Jacquard|Damask|Faille|Georgette|Crepe|Boucle|Gabardine|Shantung|Pique|Sateen|Worsted|Apron|Greenroom|Flyloft|Cyclorama|Backdrop|Callboard|Limelight|Footlight|Houseleft|Tourbillon|Escapement|Rotor|Complication|Reserve|Repeater|Moonphase|Dailies|Rushes|Slate|Reel|Splice|Dissolve|Wipe|Dolly|Rackfocus|Jumpcut|Crosscut|Matchcut|Gouache|Conte|Sanguine|Ground|Mordant|Aquatint|Mezzotint|Drypoint|Linocut|Woodcut|Monotype|Collagraph|Chine Colle|Burin|Graver|Baren|Maquette|Bozzetto|Cartoon|Pochade|Alla Prima|Underpainting|Scumble|Glacis|Velatura|Craquelure|Gilding|Giltwork|Repousse|Cloisonne|Champleve|Niello|Granulation|Guilloche|Engine Turn|Parquetry|Intarsia|Pietra Dura|Ormolu|Marquetry|Boulle|Rocaille|Volute|Acroterion|Entablature|Architrave|Keystone|Spandrel|Soffit|Coffer|Lantern|Cupola|Ogee|Quatrefoil|Trefoil|Rosette|Cartouche|Arabesque|Guillochis|Festoon|Swag|Finial|Boss|Mullion|Tracery|Clerestory|Enfilade|Piano Nobile|Belle Etage|Cour D Honneur|Haute Epoque|Objet Trouve|Trompe Loeil|Mise En Scene|Pas De Deux|Corps De Ballet|Port De Bras|En Dehors|Ad Libitum|Dolce|Legato|Marcato|Sostenuto|Espressivo|Con Brio|Con Moto|Animato|Grazioso|Maestoso|Tranquillo|Lontano|Sempre|Subito|Attacca|Da Capo|Fine|Coda Mark|Fermata|Mordent|Appoggiatura|Acciaccatura|Turnaround|Blue Note|Grace Note|Leading Tone|Perfect Fifth|Open Fifth|Countermelody|Ostinato|Ground Bass|Partimento|Temperament|Tessitura|Register|Voicing|Divisi|Unison|Homophony|Polyphony",
    D,
    "Far-field real-word raid",
    "Book arts, couture, printmaking, stagecraft, architecture, music",
)


# 7. BEAUTIFUL MISCHIEF
D = "Beautiful Mischief"
mischief_adjectives = [
    "Civil", "Clever", "Dear", "Fine", "Gentle", "Good", "Grand", "Honest", "Kind", "Little",
    "Modern", "Modest", "Nice", "Polite", "Pretty", "Proper", "Quiet", "Rare", "Serious",
    "Small", "Tender", "Warm", "Wild", "Witty", "Velvet", "Bright", "Common", "Private",
]
mischief_nouns = [
    "Alibi", "Audacity", "Contrary", "Delight", "Disorder", "Dissent", "Excuse", "Fiction",
    "Folly", "Habit", "Mischief", "Nerve", "Rebel", "Revolt", "Riot", "Scandal", "Secret",
    "Trouble", "Vanity", "Vice", "Wonder", "Wrong", "Drama", "Plot", "Twist", "Opinion",
    "Side", "Story", "Case", "Point", "Provocation", "Exception", "Detour", "Diversion",
]
for i, adjective in enumerate(mischief_adjectives):
    for j, noun in enumerate(mischief_nouns):
        if (i * 5 + j * 7) % 9 == 0:
            add(f"{adjective} {noun}", D, "Contradictory compound", "Manners colliding with rebellion")
add_words(
    "As If|Why Not|Says Who|Quite Right|Come Again|Go On|By All Means|In Your Dreams|Fair Enough|Well Then|Just Because|What Next|So Be It|No Matter|Take Heart|Dare Say|Good For You|Not Quite|More Please|If You Please|Pardon Me|Of Course|No Doubt|All Nerve|Very Well|Oh Really|Do Tell|Try Me|Watch This|Says Me|On Second Thought|Think Again|Imagine That|Would You Rather|Naturally|Obviously|Apparently|Supposedly|Decidedly|Unapologetic|Contrarywise|Otherwise|Nevertheless|Some Nerve|Pleasure First|Good Bad Idea|Better Trouble|Perfectly Contrary|Wrong On Purpose|Nicely Done|Act Natural|Make Believe|Fine By Me|Well Played|Be Serious|Not A Chance|Charming Idea|Rare Behavior|Perfect Alibi|A Little Much|More Or Less|Almost Proper",
    D,
    "Audacity / proposition",
    "Conversational retorts and social wit",
)


# 8. SENSORY MOTION
D = "Sensory Motion"
add_words(
    "Lilt|Sway|Ripple|Dapple|Flicker|Glint|Glimmer|Drift|Turn|Pulse|Quiver|Tremor|Thrum|Cadence|Swing|Waltz|Step|Weave|Flutter|Glide|Orbit|Arc|Wave|Murmur|Rustle|Tingle|Spiral|Pivot|Sweep|Skim|Brush|Feather|Hover|Loop|Coast|Ripplework|Swayline|Liltwise|Turnwell|Glintward|Driftmark|Pulsework|Thrumline|Cadent|Undulate|Tremolo|Vibrato|Rondo|Pavane|Sarabande|Minuet|Reprise|Interlude|Gesture|Flourish|Downbeat|Upstroke|Afterbeat|Crossfade|Overtone|Undertone|Resonance|Reverberation|Kinetic|Momentum|Velocity|Poise|Balance|Counterpoise|Tension|Release|Lift|Spring|Bound|Current|Eddy|Wake|Tide|Rill|Rivulet|Breeze|Zephyr",
    D,
    "Action and sensory metaphor",
    "Dance, gesture, sound, fluid dynamics",
)
motion_roots = ["lilt", "sway", "glint", "drift", "turn", "pulse", "ripple", "trem", "hum", "thrum", "cad", "swing", "waltz", "weave", "glide", "orbit", "arc", "wave"]
motion_endings = ["en", "er", "ly", "line", "well", "wise", "work", "ward", "let", "elle", "kin", "al"]
for i, root in enumerate(motion_roots):
    for j, ending in enumerate(motion_endings):
        if (i * 7 + j * 5) % 4 != 0:
            add(root + ending, D, "Movement reconstruction", "Kinetic morpheme matrix")
for modifier in ["Bright", "Fine", "Full", "Inner", "Quiet", "Rare", "Warm", "Wild", "True", "Vivid"]:
    for motion in ["Cadence", "Gesture", "Pulse", "Turn", "Arc", "Drift", "Tremor", "Reprise", "Tempo", "Lift"]:
        add(f"{modifier} {motion}", D, "Sensory compound", "Movement and temperament")


# 9. TECHNICAL ELEGANCE
D = "Technical Elegance"
add_words(
    "Escapement|Chronometer|Datum|Tolerance|Vector|Axis|Helix|Spline|Fillet|Chamfer|Gimbal|Optic|Prism|Phase|Resonance|Harmonic|Modulus|Gradient|Flux|Moment|Torque|Bearing|Fine Thread|Zero Point|Datum Line|True Radius|Reference Arc|Prime Vector|Quiet Signal|Open Circuit|Living Hinge|Fine Tolerance|Set Screw|Balance Wheel|Main Spring|Watch Jewel|Index Mark|Maker's Mark|Surface Plate|Optical Flat|Master Gauge|Reference Standard|Control Surface|Dynamic Balance|Signal Path|Phase Line|Harmonic Mean|Golden Ratio|Common Measure|Human Scale|Fine Grain|High Fidelity|Full Spectrum|True North|Clean Room|Proof Mass|Gauge Block|Slip Gauge|Spring Rate|Clear Span|Free Body|Vector Field|Moment Arm|Neutral Axis|Tangent Point|Natural Frequency|Damping Ratio|Fine Structure|Calibration Curve|Working Standard|Primary Reference|First Principle|State Variable|Boundary Layer|Open Loop|Closed Loop|Steady State|Design Margin|Safety Factor|Fit And Finish|Calibre|Micrometer|Vernier|Parallax|Aperture|Lumen|Lux|Candela|Diopter|Focal Plane|Depth Of Field|Resolution|Contrast Ratio|Frequency Response|Signal Gain|Noise Floor",
    D,
    "Technical source raid",
    "Horology, optics, metrology, mechanics",
)
tech_roots = ["ax", "cal", "datum", "focal", "grad", "harm", "hel", "lumin", "mod", "optic", "phase", "prism", "reson", "toler", "vect", "vern"]
tech_endings = ["el", "en", "or", "is", "um", "al", "in", "on", "er", "ane"]
for i, root in enumerate(tech_roots):
    for j, ending in enumerate(tech_endings):
        if (i + j * 2) % 3 != 0:
            add(root + ending, D, "Technical morpheme engine", "Precision-root coinage")


# 10. DEEP TIME
D = "Deep Time"
add_words(
    "Strata|Epoch|Eon|Palimpsest|Sediment|Continuum|Almanac|Solstice|Equinox|Tidemark|Provenance|Lineage|Heirloom|Relic|Primeval|Later|Morrow|Longform|After Season|Dear Future|New Vintage|Future Antique|Living Relic|Daily Heirloom|Second Sun|Long Gold|New Eon|Fine Era|Ever Present|Full Season|Yearwork|Timewell|Eonwise|Erahouse|Deep Calendar|Inner Season|Golden Interval|Timefold|Longlight|Laterday|Old New|Still Becoming|Future Past|Living Memory|Lasting Present|The Next Era|Good Years Ahead|Full Circle|Long Arc|Age Of Now|Present Perfect|The Long Now|Before And After|Once And Future|Further Still|Hereafter|Henceforward|Year On Year|Day By Day|World Without End|In Due Season|Season Of One|Evergreen|Aftertime|Timepiece|Dateline|Era Mark|Long Measure|Futureproof|Weatherwise|Layerwork|Stratiform|Eonmark|Eraform|Timekind|Longmade|Afterlight|Continuance|Duration|Interval|Sequence|Accretion|Patination|Maturation|Distillation|Inheritance|Ancestry|Posterity|Legacy|Endurance|Persistence|Constancy|Recurrence|Return|Reprise|Remembrance|Chronicle|Annals|Archive|Record",
    D,
    "Deep-time metaphor and future reframe",
    "Geology, calendars, inheritance, continuity",
)


def main() -> None:
    fields = ["RawOrder", "Name", "Direction", "Method", "SourceWorld", "Normalized"]
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "raw_unique_count": len(rows),
        "direction_counts": dict(Counter(str(row["Direction"]) for row in rows)),
        "method_counts": dict(Counter(str(row["Method"]) for row in rows)),
    }
    (HERE / "raw-generation-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
