from __future__ import annotations

import csv
import importlib.util
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
HISTORY_MODULE = NAMING_DIR / "decoy-exercise-2026-07-16" / "build-decoy-pool.py"

EXERCISES = {
    1: "Make the intangible tangible",
    2: "Benefit ladder / ultimate feeling",
    3: "Reframe the question / name the future",
    4: "Anti-descriptor",
    5: "Win by contrast",
    6: "Name the audacity / worldview",
    7: "Deconstruct / reconstruct",
    8: "Portmanteau",
    9: "Morpheme engine",
    10: "Scientific borrowing",
    11: "Sound-first coinage",
    12: "Structural / orthographic device",
    13: "Compound: one plus one equals three",
    14: "Real-word metaphor or eponym",
    15: "World-language hunt",
    16: "Synchronicity / source-library raid",
    17: "Three-team decoy",
}

FORM_BY_EXERCISE = {
    1: "Authentic object, tool, gesture, or process",
    2: "Explicit benefit or proposition",
    3: "Direct conceptual reframe",
    4: "Bold contradiction or anti-descriptor",
    5: "Unexpected imported term",
    6: "Short stance phrase",
    7: "Transparent spelling modification",
    8: "Clean portmanteau",
    9: "English-native compound or compression",
    10: "Authentic scientific terminology",
    11: "Crisp sound-led coinage",
    12: "Meaningful notation or orthographic device",
    13: "Category-relevant compound",
    14: "Unexpected real word or metaphor",
    15: "World-language borrowing",
    16: "Authentic insider terminology",
    17: "Decoy-world import",
}

SUFFIXES = [
    "work", "wise", "ward", "mark", "line", "kind", "made", "form", "craft",
    "house", "standard", "method", "practice", "company", "club", "state", "way",
]

WORLDS = [
    {
        "rank": 1,
        "name": "Time and Skin Longevity",
        "anchors": "long later onward duration interval sequence tenure carry continue accrue repeat future present next remain lasting years day second span arc keeping".split(),
        "objects": "longhand mainspring escapement repeater chronometer calendar almanac dateline yearbook hourmark daymark watchglass sundial pendulum ledger annual ring tree ring timeline intervalometer".split(),
        "benefits": ["Still Ahead", "Long Use", "More Tomorrow", "Well Beyond", "Added Time", "Years Ahead", "Keeps Going", "Long Wearing", "Future Ready", "Built To Continue", "Good For Longer", "Made To Last", "The Long Benefit", "More Good Years", "Stay In Form", "Carry Forward"],
        "future": ["After Now", "First Future", "The Next Present", "Longer Living Skin", "What Comes Next", "Onward From Here", "The Continuing Face", "Beyond Before", "Future In Use", "Next Becomes Now", "The Longer View", "Tomorrow In Hand", "Always Becoming", "Years From Now", "The New Long Term", "A Longer Present"],
        "counter": ["No Deadline", "Never Finished", "Not Over", "Past Perfect", "Older Forward", "No Expiration", "Beyond Younger", "Against The Clock", "Without An End", "More Than Before", "Not A Countdown", "Long Not Late", "Later Is Better", "No Final Form", "The Unending Present", "Age Without Panic"],
        "stances": ["Take Your Time", "Keep Going", "Stay With It", "Still To Come", "There Is More", "Long Live This", "Begin Again", "Go The Distance", "Count On Tomorrow", "Made For Later", "Use Your Years", "Let Time Work", "Keep The Future", "Make It Last", "Long May It", "Time Is Ours"],
        "roots": "long dur contin later next remain carry span interval annual year day ever onward future present accrue sequence tenure".split(),
        "science": ["Chronobiology", "Circadian", "Homeorhesis", "Senescence", "Turnover", "Half Life", "Longitudinal", "Temporal", "Chronometry", "Biological Age", "Cell Cycle", "Phase Shift", "Time Constant", "Steady State", "Rate Of Change", "Cumulative Dose", "Service Life", "Mean Lifetime", "Recurrence", "Persistence"],
        "sound_left": "lon len dur dar tem ten tor car cor per par sen siv nav nov".split(),
        "sound_right": "do ma ro ven den tal lin nor rel sta tic ward mark".split(),
        "metaphors": "Encore Reprise Longhand Continuance Posterity Succession Almanac Carryover Relay Inheritance Reserve Marathon Watchkeeper Longview Secondwind Wayfarer Mainstay".split(),
        "world_words": "Sempre Ancora Avanti Durer Lunga Continuo Manana Weiter Encore Futuro Presente Longue Dauer".split(),
        "source": ["Power Reserve", "Perpetual Calendar", "Running Seconds", "Long Case", "Mainspring", "Escapement", "Repeat Cycle", "Annual Return", "Rolling Average", "Longitudinal Study", "Cohort Effect", "Accumulated Value", "Compound Return", "Holding Period", "Long Stop", "Carry Forward", "Time Horizon", "Extended Play", "Long Exposure", "Future Value"],
        "decoy": ["Longhand Watch Company", "After Now Press", "Added Time Club", "The Long Use", "Future Standard", "Carry Forward House", "Second Course", "Onward Works", "Daymark Company", "Nextkeeping", "Long Practice", "Common Era", "Still Ahead", "Yearproof", "Long Since", "Well Beyond"],
        "featured": [
            ("Longhand", 1), ("After Now", 3), ("Added Time", 2), ("Yearproof", 9),
            ("Nextkeeping", 9), ("Daymark", 1), ("Well Beyond", 2), ("First Future", 3),
            ("Common Era", 5), ("Onwardly", 7), ("Future Tense", 5), ("Still Ahead", 6),
        ],
    },
    {
        "rank": 2,
        "name": "Nothing Hidden and Transparency",
        "anchors": "open clear plain reveal visible disclose show view sight readable legible daylight unmask uncover full honest window lucent candid exposed".split(),
        "objects": "aperture window lightbox cutaway crosssection xray skylight viewfinder sightline cleartext watermark glasshouse showcase openbook lens hatch keyhole lucida witnessmark".split(),
        "benefits": ["Full View", "All There", "Easy To See", "Nothing Missing", "Clear From Here", "Open To View", "Seen In Full", "Plain To See", "Every Part Visible", "The Whole Picture", "No Fine Print", "Fully Shown", "Clear By Design", "Open At Every Step", "The Visible Difference", "Know What Is Inside"],
        "future": ["Skincare In Daylight", "The Open Formula", "Beauty Without Secrets", "The Unhidden Brand", "Everything On View", "The End Of Mystique", "Open Is Advanced", "The Clearer Standard", "Full Formula Future", "Skincare Out Loud", "From Black Box To Open Book", "The Visible Company", "No More Guessing", "Unmasked Skincare", "The Age Of Open", "Nothing Behind The Label"],
        "counter": ["Nothing To Hide", "No Black Box", "Not Proprietary Mystique", "Open Secret", "Clear Mystery", "Public Knowledge", "Private No More", "Hidden In Plain Sight", "No Closed Doors", "Opaque No More", "Undisguised", "No Smoke No Mirrors", "Without A Curtain", "No Secret Sauce", "All Access", "Uncovered By Design"],
        "stances": ["Look Inside", "See For Yourself", "Open It Up", "Show Everything", "Read The Whole Thing", "Ask What Is In It", "Bring It To Light", "Keep It Visible", "Put It In View", "Leave Nothing Out", "No Fine Print", "Turn On The Light", "Say It Plainly", "Let Them See", "Open By Default", "Show The Formula"],
        "roots": "open clear plain reveal view sight show legible lucid disclose visible daylight full glass".split(),
        "science": ["Transmittance", "Transparency", "Refraction", "Aperture", "Optical Window", "Cross Section", "Spectral Window", "Clear Aperture", "Light Field", "Contrast Transfer", "Cutaway View", "Exploded View", "Open Source", "Cleartext", "Traceability", "Disclosure", "Line Of Sight", "Visible Spectrum", "Transmission", "Illumination"],
        "sound_left": "clar clea luc lum vis vid op ap rev vel tra tru gla".split(),
        "sound_right": "do va ro den lin mark view text ray set open well".split(),
        "metaphors": "Daylight Skylight Window Aperture Lens Lucida Showcase Cutaway Crosssection Lightbox Viewfinder Sightline Glasshouse Openbook Cleartext".split(),
        "world_words": "Aperto Clair Claro Lucid Offen Abierto Ouvert Chiaro Palam Selva Transparente Evident".split(),
        "source": ["Exploded View", "Cutaway Drawing", "Open File", "Public Record", "Cleartext", "Source Code", "Audit Trail", "Witness Mark", "Registration Mark", "Sight Glass", "Viewing Port", "Full Bleed", "Contact Sheet", "Proof Sheet", "Light Table", "Open Standard", "Chain Of Custody", "Material Disclosure", "Ingredient Ledger", "Plain Language"],
        "decoy": ["Daylit Architecture", "Open File Press", "Clearwork Studio", "Full View Optics", "Plain Sight House", "All There Company", "No Fine Print", "The Open Formula", "Lightbox Works", "Sightline Standard", "Unhidden", "Showthrough", "Glasshouse Method", "Open Faced", "Public Knowledge", "Full Disclosure Club"],
        "featured": [
            ("Daylit", 1), ("Clearwork", 13), ("Showthrough", 7), ("Unhidden", 7),
            ("All There", 2), ("Open Faced", 13), ("No Fine Print", 6), ("Sightline", 14),
            ("Plain Sight", 14), ("Out In Full", 3), ("Open By Default", 6), ("Full View", 2),
        ],
    },
    {
        "rank": 3,
        "name": "Bare Face and Recognizable Self",
        "anchors": "face self likeness character expression feature profile portrait familiar original candid unposed natural signature recognize identity person own true same".split(),
        "objects": "portrait mirror profile silhouette cameo photograph contactprint negative likeness passport headshot fingerprint signature expression eyeline facsimile selfportrait monogram nameplate".split(),
        "benefits": ["Look Like Yourself", "Your Face Only Better", "Recognizably You", "Still Yourself", "More Like You", "At Home In Your Face", "The Familiar You", "Keep Your Character", "Wear Your Own Face", "Good In Your Skin", "Your Best Likeness", "True To Your Features", "Comfortably Recognizable", "The Face You Know", "Keep The Expression", "Naturally Yourself"],
        "future": ["The Age Of Real Faces", "Your Face Forward", "Skincare For Recognition", "The Continuing Self", "The Original Face", "Beyond The Beauty Standard", "A Future That Looks Like You", "The Face Remains Yours", "More Character Ahead", "Recognition Over Reinvention", "Natural Face Future", "The End Of Somebody Else", "Real Features First", "The New Familiar", "Stay In Character", "Aging In Your Own Image"],
        "counter": ["No New Face", "Not Somebody Else", "Same Face New Standard", "Unperfect", "Undone", "Unfiltered By Design", "Barely Conventional", "Natural Artifice", "Beautifully Familiar", "No Face Swap", "Without Disguise", "Against Perfection", "Original Not Ideal", "Real Not Retouched", "Character Over Correction", "No Stranger In The Mirror"],
        "stances": ["Keep Your Face", "Look Like You", "Stay In Character", "Own The Expression", "Face Yourself", "Wear It Well", "Keep It Familiar", "Be Recognizable", "Show Your Face", "Leave The Features", "Use Your Own Face", "Remain Yourself", "Keep The Character", "Meet Yourself", "Let The Face Live", "Do Not Erase"],
        "roots": "face self like familiar portrait profile candid true own original character feature express recognize signature".split(),
        "science": ["Facial Identity", "Face Perception", "Recognition Threshold", "Feature Mapping", "Landmark Detection", "Expression Coding", "Identity Signal", "Facial Morphology", "Self Recognition", "Visual Identity", "Feature Space", "Faceprint", "Biometric Match", "Familiarity Effect", "Distinctive Feature", "Reference Face", "Identity Continuity", "Pattern Recognition", "Facial Landmark", "Own Age Bias"],
        "sound_left": "fac fea sel sif lik lin por pro can kar tru tal sig mir".split(),
        "sound_right": "do va ro den kin mark line form self true set face".split(),
        "metaphors": "Portrait Signature Cameo Profile Character Original Familiar Mirror Nameplate Fingerprint Likeness Facsimile Monogram Expression Eyeline".split(),
        "world_words": "Candid Vero Vera Proprio Persona Mien Visage Selbst Sui Mesmo Ritratto Profilo Liken".split(),
        "source": ["Contact Print", "Natural Light", "True Likeness", "Facial Landmark", "Identity Match", "Character Study", "Three Quarter View", "Straight On", "In Profile", "Unposed Portrait", "Available Light", "Face Value", "Signature Feature", "Original Negative", "Reference Image", "Self Portrait", "Expression Line", "Family Resemblance", "Recognizable Form", "Candid Frame"],
        "decoy": ["Same Person Studio", "True Likeness", "The Familiar Face", "In Character", "Unposed Portraits", "Own Face Company", "Original Features", "Signature Face", "Recognizably", "Face First", "The Real Subject", "Candid Standard", "Selfsame", "No New Face", "Known By Sight", "Portrait Of One"],
        "featured": [
            ("Selfsame", 14), ("Unposed", 14), ("Same Person", 2), ("In Character", 5),
            ("True Likeness", 13), ("Face First", 6), ("Original Features", 13), ("Known By Sight", 16),
            ("Recognizably", 7), ("The Real Subject", 17), ("Own Face", 13), ("Candid Standard", 13),
        ],
    },
    {
        "rank": 4,
        "name": "Skin Capability and Training",
        "anchors": "train practice form capacity condition range ready adapt progress repeat session technique coach load reserve response cadence block cycle drill skill capable".split(),
        "objects": "repcounter stopwatch traininglog scorecard formcheck fieldbook playbook whistle metronome resistanceband rangefinder balanceboard trackmark sessionplan workoutblock drillcard paceclock".split(),
        "benefits": ["Ready For More", "Better With Practice", "In Good Form", "Full Range", "More Capable Skin", "Built Through Use", "Progress You Can Keep", "Stronger By Degrees", "Ready To Respond", "Good Under Load", "Capacity In Reserve", "Skin That Keeps Up", "More Range Daily", "Practice Pays", "Form That Lasts", "Conditioned For Life"],
        "future": ["Skincare Becomes Training", "The Practiced Face", "Capability Over Correction", "The Progressive Routine", "Skin In Better Form", "From Product To Practice", "The Training Age", "A More Capable Face", "Progressive Skin Care", "The Adaptive Routine", "Beyond Maintenance", "Your Skin Has Range", "The End Of Miracle Products", "Skincare As Skill", "The Conditioned Future", "Performance Through Practice"],
        "counter": ["No Miracle Set", "Rest Is Training", "Soft Strength", "Practice Not Perfection", "Good Stress", "Active Recovery", "Train Less Better", "No Overnight Results", "Slow Progress Fast Skin", "Strong Without Force", "Beyond The Burn", "No Hero Product", "Gentle Load", "Easy Does Work", "Condition Without Punishment", "Capable Not Corrected"],
        "stances": ["Work The Plan", "Use Good Form", "Build Capacity", "Practice Daily", "Stay In Range", "Train For Later", "Keep Your Form", "Progress Slowly", "Repeat What Works", "Know The Load", "Earn The Result", "Recover On Purpose", "Make It Practice", "Get In Condition", "Work With Skin", "Build The Base"],
        "roots": "train form cap adapt range ready repeat progress practice skill condition reserve session tempo cadence load response".split(),
        "science": ["Adaptive Response", "Progressive Load", "Work Capacity", "Training Effect", "Dose Response", "Supercompensation", "Periodization", "Microcycle", "Mesocycle", "Deload", "Taper", "Readiness", "Range Of Motion", "Motor Learning", "Skill Transfer", "Training Age", "Recovery Index", "Baseline Capacity", "Response Curve", "Minimum Effective Dose"],
        "sound_left": "cap cad con dar for pro pra ran red ses tem tran val".split(),
        "sound_right": "do va ro den kin mark line form set well ready fit".split(),
        "metaphors": "Form Range Practice Cadence Session Reserve Repetition Progression Readiness Playbook Scorecard Drill Tempo Block Cycle Coach Fieldwork".split(),
        "world_words": "Forma Pratica Capace Allenare Entreno Cadencia Progresso Habile Aptus Forte Technik Uebung".split(),
        "source": ["Progressive Overload", "Minimum Effective Dose", "Training Block", "Work Capacity", "Active Recovery", "Ready State", "Good Form", "Full Range", "Deload Week", "Practice Effect", "Motor Pattern", "Skill Transfer", "Training Age", "Session Rating", "Response Curve", "Base Phase", "Build Phase", "Adaptation Window", "Capacity Test", "Form Under Load"],
        "decoy": ["Working Form", "Ready State Method", "Daily Form Club", "Range Ready", "Better Form", "Second Set", "Full Range Company", "Practice Makes", "The Training Effect", "Good Under Load", "Progressive House", "In Condition", "Formwork", "Capacity Club", "The Repeat Method", "Adaptive Practice"],
        "featured": [
            ("Working Form", 13), ("Ready State", 10), ("Range Ready", 13), ("Second Set", 17),
            ("Full Range", 14), ("In Condition", 6), ("Practice Makes", 6), ("The Training Effect", 10),
            ("Good Under Load", 5), ("Adaptive Practice", 13), ("Build The Base", 6), ("Daily Form", 13),
        ],
    },
    {
        "rank": 5,
        "name": "Visible Performance",
        "anchors": "visible result show mark difference change gain improve perform finish output yield effect response resolution contrast notice clear degree measure deliver".split(),
        "objects": "scoreboard readout gauge proofsheet benchmark ruler caliper contrastchart resolutioncard finishline teststrip indicator dial display signalflag progressbar beforeafter swatch samplecard".split(),
        "benefits": ["Shows Up", "Looks Like Results", "A Clear Difference", "Visible By Degrees", "Noticeably Better", "Results In View", "Performance You Can See", "The Mark Of Progress", "Delivers Daily", "Worth The Look", "Change That Registers", "Results That Remain", "More Than A Feeling", "Seen To Work", "Clearer With Use", "The Visible Gain"],
        "future": ["The Result Is The Brand", "Skincare That Shows Up", "The New Visible Standard", "Performance In Plain View", "Beyond The Promise", "Results Become Routine", "The Age Of Observable", "What Works Becomes Visible", "From Claim To Change", "A Better Looking Future", "The End Of Invisible Benefits", "Results Without Theater", "Visible Is Valuable", "The Performing Face", "Change On Display", "Skincare With An Output"],
        "counter": ["Quietly Obvious", "Subtle Impact", "No Empty Promise", "Less Talk More Result", "Invisible Effort Visible Change", "No Before After Theater", "Looks Like Work", "Soft Power", "Understated Result", "No Cosmetic Trick", "Real Not Instant", "Gentle Performance", "Small Change Big Notice", "No Hype Required", "Almost Dramatic", "Better Without The Show"],
        "stances": ["Show Me Results", "Make It Visible", "Deliver The Difference", "Let It Show", "See What Changed", "Mark The Progress", "Look Again", "Expect To Notice", "Judge The Result", "Put It To Work", "Make Good Visible", "Show Up Daily", "Raise The Standard", "Register The Change", "Notice The Work", "Count What Changes"],
        "roots": "show vis result mark gain yield perform finish clear notice delta change effect output deliver resolve".split(),
        "science": ["Effect Size", "Delta", "Readout", "Endpoint", "Response Rate", "Signal Change", "Resolution", "Contrast", "Benchmark", "Measured Outcome", "Observed Effect", "Visual Grade", "Instrumental Measure", "Clinical Endpoint", "Change Score", "Absolute Difference", "Relative Change", "Performance Index", "Output Gain", "Detection Threshold"],
        "sound_left": "del dif eff gai mar not per res sho val vis yel".split(),
        "sound_right": "do va ro den kin mark line form set view gain show".split(),
        "metaphors": "Delta Readout Benchmark Finish Yield Register Signal Mark Gauge Indicator Resolution Contrast Headway Output Scorecard".split(),
        "world_words": "Risultato Visible Evident Claro Wirkung Effet Rendement Resultado Prova Segno Netto Voyant".split(),
        "source": ["Effect Size", "Primary Endpoint", "Change Score", "Observed Result", "Signal Gain", "Detection Threshold", "Visual Grade", "Instrument Readout", "Reference Standard", "Performance Index", "Output Measure", "Pass Mark", "Proof Sheet", "Test Result", "Delta Value", "Before State", "After State", "Finish Quality", "Yield Strength", "Acceptance Test"],
        "decoy": ["Markedly", "The Clear Difference", "Shows Up Company", "By Degrees", "Resultant", "Proof Positive", "Visible Gain", "Plainly Works", "High Definition", "The Noticeable", "Outperform", "On Display", "Looks Good Works", "Change Register", "Finish Standard", "Result First"],
        "featured": [
            ("Markedly", 7), ("By Degrees", 14), ("Resultant", 10), ("On Display", 14),
            ("Visible Gain", 13), ("The Noticeable", 17), ("Change Register", 16), ("Result First", 6),
            ("Quietly Obvious", 4), ("Shows Up", 2), ("A Clear Difference", 2), ("High Definition", 5),
        ],
    },
    {
        "rank": 6,
        "name": "Barrier Strength and Adaptive Capacity",
        "anchors": "adapt reserve range respond flex buffer balance threshold rebound tolerance interface resilient elastic capacity steady regulate recover adjust acclimate homeostasis".split(),
        "objects": "buffer spring hinge membrane gasket shockmount expansionjoint bellows suspension bridge interface seal cushion reservoir thermostat ballast damper regulator flexure lattice".split(),
        "benefits": ["Ready To Respond", "More In Reserve", "Keeps Its Balance", "Flexible Strength", "Range To Spare", "Better Under Pressure", "Holds Through Change", "Built To Adjust", "Responsive By Nature", "Steady When Stressed", "Strong With Give", "Capacity For Change", "Back To Balance", "More Room To Move", "Resilience In Use", "Adapts As Needed"],
        "future": ["The Adaptive Skin Era", "Strength Becomes Responsive", "Beyond The Barrier", "Skin With More Range", "The Responsive Future", "From Defense To Capacity", "Flexibility Is Strength", "The End Of Fragile Skin", "Adaptive Care Standard", "Skin In Dynamic Balance", "More Reserve Ahead", "The Flexible Barrier", "Response Over Resistance", "Capacity Not Armor", "The New Resilience", "Skin That Adjusts"],
        "counter": ["Strong With Give", "Soft Structure", "Flexible Barrier", "Open Strength", "Resilient Not Rigid", "Yield To Hold", "Stable In Motion", "Protected By Response", "Firmly Flexible", "Gentle Resistance", "Strength Without Armor", "Balance Under Stress", "Tough Enough To Bend", "Hold Without Hardening", "Dynamic Stability", "Give Is Strength"],
        "stances": ["Keep Some In Reserve", "Adapt As Needed", "Stay Responsive", "Hold Through Change", "Build The Buffer", "Make Room To Flex", "Return To Balance", "Work With Stress", "Keep Your Range", "Respond Better", "Bend Do Not Break", "Stay Within Range", "Use The Reserve", "Strengthen The Response", "Keep The Interface", "Make Strength Flexible"],
        "roots": "adapt flex buffer reserve range respond rebound balance threshold steady elastic regulate capacity tolerant interface".split(),
        "science": ["Homeostasis", "Allostasis", "Adaptive Capacity", "Buffer Capacity", "Response Range", "Elastic Limit", "Yield Point", "Recovery Modulus", "Dynamic Equilibrium", "Barrier Function", "Lamellar Structure", "Lipid Matrix", "Transepidermal", "Osmoregulation", "Stress Response", "Set Point", "Reserve Capacity", "Tolerance Window", "Feedback Loop", "Resilience Index"],
        "sound_left": "ada bal buf cap ela fle hom lam ran reb res sta tol".split(),
        "sound_right": "do va ro den kin mark line form set flex hold well".split(),
        "metaphors": "Buffer Reserve Spring Hinge Bellows Flexure Interface Ballast Regulator Reservoir Damper Lattice Thermostat Suspension Balance Rebound".split(),
        "world_words": "Adatta Souplesse Elastico Forte Equilibrio Reserva Flessibile Stabile Robustez Resilire Tenuta".split(),
        "source": ["Buffer Capacity", "Elastic Limit", "Yield Point", "Dynamic Balance", "Reserve Capacity", "Tolerance Window", "Feedback Loop", "Adaptive Range", "Set Point", "Recovery Modulus", "Load Response", "Stress Test", "Return To Baseline", "Response Reserve", "Flexible Coupling", "Living Hinge", "Expansion Joint", "Dynamic Seal", "Shock Absorber", "Control Loop"],
        "decoy": ["Ready Reserve", "Living Buffer", "Flex State", "Range To Spare", "Adaptive House", "Strong With Give", "The Response Method", "Back In Balance", "Elastic Standard", "Threshold Company", "Rebound Practice", "Dynamic Stability", "Buffer Club", "Reserve Works", "Response Range", "Give And Hold"],
        "featured": [
            ("Ready Reserve", 13), ("Living Buffer", 13), ("Flex State", 13), ("Range To Spare", 2),
            ("Strong With Give", 4), ("Back In Balance", 2), ("Dynamic Stability", 10), ("Reserve Works", 17),
            ("Give And Hold", 4), ("Adaptive Range", 16), ("Buffer Capacity", 10), ("Response Reserve", 16),
        ],
    },
    {
        "rank": 7,
        "name": "Evidence and Proof",
        "anchors": "proof evidence source verify repeat test record result control measure finding signal fact cite assay audit protocol replicate demonstrate substantiate receipt".split(),
        "objects": "receipt exhibit ledger sourcebook footnote testbench controlchart labbook readout checklist audittrail seal stamp recordbook proofsheet sample vial assayplate citation index".split(),
        "benefits": ["Reason To Believe", "Proof You Can Follow", "Every Claim Accounted For", "Results With Receipts", "Evidence In Hand", "A Checkable Difference", "Confidence With A Source", "Shown To Work", "Proof At Every Step", "The Claim Holds", "Results That Repeat", "Evidence You Can Use", "The Record Is Clear", "Tested Then Told", "Known Not Assumed", "The Work Checks Out"],
        "future": ["The Age Of Accountable Claims", "Proof Becomes The Product", "Skincare With Receipts", "The End Of Trust Me", "Evidence In Public", "From Promise To Protocol", "Claims With A Source", "The Reproducible Brand", "Results On The Record", "The New Proof Standard", "Every Claim Traceable", "Skincare You Can Check", "The Demonstrated Future", "Proof Without Theater", "The Accountable Formula", "No Claim Left Unsupported"],
        "counter": ["Trust Less Verify More", "Proof Not Promise", "No Leap Of Faith", "Skeptically Optimistic", "Believe The Test", "Doubt With Benefits", "No Blind Faith", "Evidence Not Theater", "Cold Proof Warm Skin", "Show Do Not Swear", "Question The Claim", "No Magic Just Method", "Promising Nothing Unproven", "The Honest Control", "Results Under Oath", "Proof Without Certainty"],
        "stances": ["Check The Claim", "Show Your Source", "Prove The Point", "Repeat The Result", "Test Before Telling", "Keep The Receipt", "Read The Record", "Ask For Evidence", "Run The Test", "Make The Case", "Verify First", "Show The Finding", "Name The Source", "Count The Result", "Put It On Record", "Let Proof Lead"],
        "roots": "proof evid source verif repeat test record result control measure signal fact assay audit protocol check".split(),
        "science": ["Reproducibility", "Replicate", "Control Group", "Confidence Interval", "Effect Estimate", "Assay", "Protocol", "Endpoint", "Power Analysis", "Signal Detection", "Readout", "Reference Standard", "Positive Control", "Negative Control", "Test Retest", "Observed Value", "Study Design", "Evidence Grade", "Measurement Error", "Statistical Power"],
        "sound_left": "aud cas che evi fac pro rec sig tes ver vit wit".split(),
        "sound_right": "do va ro den kin mark line form set proof test fact".split(),
        "metaphors": "Receipt Exhibit Witness Ledger Record Seal Stamp Benchmark Readout Sourcebook Footnote Protocol Control Assay Finding Signal".split(),
        "world_words": "Prova Vero Veritas Evidenz Beweis Preuve Prueba Fait Factum Teste Saggio Attest".split(),
        "source": ["Positive Control", "Negative Control", "Test Retest", "Confidence Interval", "Effect Estimate", "Study Protocol", "Evidence Grade", "Source Record", "Audit Trail", "Chain Of Evidence", "Proof Sheet", "Contact Sheet", "Control Chart", "Acceptance Test", "Replicate Result", "Observed Value", "Reference Sample", "Assay Readout", "Signal Detection", "Measurement Standard"],
        "decoy": ["Receipts", "Proofmark", "Fact Pattern", "Case Made", "The Record Company", "Repeatable Works", "Witnessed", "Source First", "Shown Work", "Control House", "Checkable", "Signal Found", "Proof Standard", "The Verified", "Evidence Club", "Claim Accounted"],
        "featured": [
            ("Proofmark", 13), ("Fact Pattern", 5), ("Case Made", 6), ("Witnessed", 14),
            ("Source First", 6), ("Shown Work", 13), ("Checkable", 7), ("Signal Found", 16),
            ("Claim Accounted", 6), ("Proof Standard", 17), ("The Verified", 17), ("Evidence In Hand", 2),
        ],
    },
    {
        "rank": 8,
        "name": "Better Informed and Customer Agency",
        "anchors": "know learn understand choose judge discern read ask answer guide explain compare decide fluent literate informed insight sense reason translate orient navigate".split(),
        "objects": "key legend map compass fieldguide handbook primer glossary decoder index margin annotation diagram flowchart manual reader lens notebook syllabus rubric menu".split(),
        "benefits": ["Know What Works", "Choose With Confidence", "Good At Deciding", "Understand Your Routine", "Better Questions Better Skin", "The Informed Choice", "Clarity You Can Use", "Knowledge In Hand", "Know More Buy Better", "Make Your Own Call", "Fluent In Skin", "Easy To Understand", "Learn What Matters", "Choose What Earns A Place", "Confidence Through Knowing", "Smarter With Every Use"],
        "future": ["The Customer Becomes The Expert", "Skincare You Understand", "The End Of Expert Mystique", "A More Fluent Customer", "Knowledge Moves To You", "The Self Directed Routine", "From Follower To Decider", "The Age Of Informed Skin", "Better Questions Lead", "The Educated Formula", "Skincare In Your Hands", "The New Beauty Literacy", "Knowhow Becomes Yours", "Understanding Is The Upgrade", "The Customer Holds The Key", "No More Ingredient Theater"],
        "counter": ["Expert Without Authority", "Teach Do Not Preach", "Simple Not Simplistic", "Know Better Not Best", "Less Advice More Understanding", "No Guru Required", "Beginner Expert", "Doubt The Expert", "Learn Before Believing", "Smart Without Jargon", "Information With Feeling", "No Dumb Questions", "Complex Made Clear", "Plainly Advanced", "Education Without School", "Guided Not Told"],
        "stances": ["Know Better", "Ask Better", "Choose Well", "Read Up", "Learn The Formula", "Make The Call", "Use Your Judgment", "Know Your Skin", "Ask What Matters", "Decide For Yourself", "Read Before Use", "Understand The Why", "Keep Asking", "Make Sense Of It", "Choose What Works", "Be Hard To Fool"],
        "roots": "know learn read guide clear wise fluent literate inform insight sense choice judge ask answer explain discern".split(),
        "science": ["Decision Support", "Information Gain", "Signal To Noise", "Bayesian Update", "Decision Rule", "Choice Architecture", "Mental Model", "Knowledge Transfer", "Learning Curve", "User Control", "Feedback", "Comprehension", "Cognitive Load", "Information Design", "Shared Decision", "Decision Aid", "Calibration", "Inference", "Prior Knowledge", "Sensemaking"],
        "sound_left": "ask cho cle dec flu gui inf kno lea rea sen wis".split(),
        "sound_right": "do va ro den kin mark line form set wise know key".split(),
        "metaphors": "Key Legend Compass Primer Fieldguide Decoder Index Margin Reader Map Lens Handbook Rubric Notebook Manual Guidepost".split(),
        "world_words": "Savoir Sapere Wissen Conocer Capire Comprendre Claro Scelta Scire Sensei Kenner Cognosco".split(),
        "source": ["Signal To Noise", "Decision Support", "Information Gain", "Learning Curve", "Mental Model", "Choice Architecture", "Knowledge Transfer", "Shared Decision", "Decision Aid", "User Control", "Plain Language", "Information Design", "Field Guide", "Reference Key", "Reading Level", "Legend Key", "Orientation Map", "Quick Start", "Open Question", "Informed Consent"],
        "decoy": ["Know Better", "Skin Fluent", "Good Question", "Choose Well", "The Decider", "Field Key", "Read Skin", "Ask More", "Clear Choice", "Knowhow Club", "The Useful Guide", "Learned", "Sensemaking", "Decision House", "Understandably", "The Question Method"],
        "featured": [
            ("Skin Fluent", 13), ("Good Question", 14), ("Field Key", 13), ("The Decider", 17),
            ("Read Skin", 6), ("Ask More", 6), ("Knowhow Club", 17), ("Learned", 14),
            ("Sensemaking", 10), ("Understandably", 7), ("The Question Method", 17), ("Choose Well", 6),
        ],
    },
]

TARGET_PER_CELL = 42


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_text = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", ascii_text.lower())


def clean_name(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    value = value.strip(" -_/+,:;.!?")
    if not value:
        return ""
    small = {"and", "or", "of", "to", "in", "for", "with", "by", "as", "at"}
    words = []
    for index, word in enumerate(value.split()):
        if word.isupper() and len(word) <= 5:
            words.append(word)
        elif index > 0 and word.lower() in small:
            words.append(word.lower())
        else:
            words.append(word[:1].upper() + word[1:].lower())
    return " ".join(words)


def valid_name(value: str) -> bool:
    norm = normalize(value)
    if not 3 <= len(norm) <= 30:
        return False
    if len(value.split()) > 5:
        return False
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{5}", norm):
        return False
    blocked = ("antiaging", "pharmaceutical", "dermatological", "cosmeceutical")
    return not any(item in norm for item in blocked)


def drop_vowel(value: str) -> str:
    letters = list(normalize(value))
    for index in range(2, len(letters) - 1):
        if letters[index] in "aeiou" and letters[index - 1] not in "aeiou":
            del letters[index]
            return "".join(letters)
    return "".join(letters)


def blend(left: str, right: str) -> str:
    left = normalize(left)
    right = normalize(right)
    if not left or not right:
        return ""
    overlap = 0
    for size in range(min(4, len(left), len(right)), 0, -1):
        if left[-size:] == right[:size]:
            overlap = size
            break
    if overlap:
        return left + right[overlap:]
    cut_left = max(3, math.ceil(len(left) * 0.6))
    cut_right = max(2, math.floor(len(right) * 0.45))
    return left[:cut_left] + right[-cut_right:]


def pair_matrix(left: list[str], right: list[str], count: int, separator: str = " ") -> list[str]:
    values: list[str] = []
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if normalize(first) == normalize(second):
                continue
            if (i * 7 + j * 11 + len(first) + len(second)) % 5 in {0, 2}:
                values.append(f"{first}{separator}{second}")
            if len(values) >= count:
                return values
    return values


def generated_for(world: dict, exercise: int) -> list[tuple[str, str]]:
    anchors = list(world["anchors"])
    nouns = [clean_name(item) for item in (world["objects"] + world["metaphors"] + anchors)]
    modifiers = [
        "Full", "Open", "True", "Next", "Long", "Good", "Clear", "Daily", "Living",
        "Common", "First", "Ready", "Better", "Actual", "Human", "Modern", "Working",
    ]
    values: list[tuple[str, str]] = []

    def add_many(items: list[str], source: str) -> None:
        for item in items:
            values.append((item, source))

    if exercise == 1:
        add_many(list(world["objects"]), "world objects and instruments")
        add_many(pair_matrix(modifiers, nouns[:20], 30), "tangible object matrix")
    elif exercise == 2:
        add_many(list(world["benefits"]), "benefit ladder")
        add_many(pair_matrix(["More", "Better", "Full", "Good", "Ready"], anchors[:18], 30), "benefit compression")
    elif exercise == 3:
        add_many(list(world["future"]), "future reframe")
        add_many(pair_matrix(["Next", "New", "Future", "Beyond"], nouns[:18], 30), "name the future matrix")
    elif exercise == 4:
        add_many(list(world["counter"]), "anti-descriptor")
        add_many(pair_matrix(["No", "Not", "Without", "Beyond"], nouns[:18], 30), "anti-category matrix")
    elif exercise == 5:
        add_many(list(world["source"]), "far-field source contrast")
        add_many(list(world["metaphors"]), "contrast mononyms")
    elif exercise == 6:
        add_many(list(world["stances"]), "worldview statements")
        add_many(pair_matrix(["Choose", "Keep", "Make", "Use", "Show", "Know"], nouns[:18], 30), "audacity commands")
    elif exercise == 7:
        add_many([drop_vowel(item) for item in anchors + list(world["metaphors"])], "single-vowel deletion")
        add_many([normalize(item) for item in pair_matrix(anchors[:12], anchors[6:20], 30)], "joined reconstruction")
    elif exercise == 8:
        blends = []
        for i, left in enumerate(anchors[:16]):
            for j, right in enumerate((anchors + [normalize(x) for x in world["metaphors"]])[5:26]):
                if (i * 5 + j * 7) % 4 == 0:
                    blends.append(blend(left, right))
        add_many(blends, "legible two-source blend")
    elif exercise == 9:
        compounds = []
        for i, root in enumerate(world["roots"]):
            for j, suffix in enumerate(SUFFIXES):
                if (i * 3 + j * 5) % 4 in {0, 1}:
                    compounds.append(normalize(root) + suffix)
        add_many(compounds, "English-native morpheme engine")
    elif exercise == 10:
        add_many(list(world["science"]), "authentic scientific terminology")
        add_many(pair_matrix(["Adaptive", "Dynamic", "Reference", "Working", "Primary"], nouns[:18], 25), "technical compounds")
    elif exercise == 11:
        coinages = []
        for i, left in enumerate(world["sound_left"]):
            for j, right in enumerate(world["sound_right"]):
                if (i * 7 + j * 5) % 3 == 0:
                    coinages.append(left + right)
        add_many(coinages, "phonosemantic sound matrix")
    elif exercise == 12:
        add_many([drop_vowel(item) for item in anchors], "orthographic deletion")
        add_many([f"{clean_name(item)} One" for item in anchors[:12]], "meaningful numbering")
        add_many([f"{clean_name(item)} Plus" for item in anchors[4:16]], "plus notation")
        add_many([normalize(item) for item in pair_matrix(anchors[:12], anchors[6:18], 22)], "joined word device")
    elif exercise == 13:
        add_many(pair_matrix(modifiers, nouns[:26], 55), "one plus one equals three")
        add_many(pair_matrix([clean_name(x) for x in anchors[:15]], nouns[8:28], 30), "world compound matrix")
    elif exercise == 14:
        add_many(list(world["metaphors"]), "real-word metaphor")
        add_many(list(world["objects"]), "real object as brand")
    elif exercise == 15:
        add_many(list(world["world_words"]), "world-language source hunt")
        add_many(pair_matrix(["Casa", "Studio", "Metodo", "Forma"], list(world["world_words"]), 30), "transparent world-language compound")
    elif exercise == 16:
        add_many(list(world["source"]), "specialist source-library raid")
        add_many(pair_matrix(["Open", "True", "Working", "Primary", "Living"], nouns[:20], 30), "source term reconstruction")
    elif exercise == 17:
        add_many(list(world["decoy"]), "three-team decoy briefs")
        add_many(pair_matrix(["House of", "The", "Common", "First"], nouns[:20], 32), "decoy company and institution")
    else:
        raise ValueError(exercise)

    # Every cell is filled from its own world vocabulary before truncation.
    fallback = pair_matrix(modifiers, nouns, TARGET_PER_CELL * 3)
    add_many(fallback, "cell fallback matrix")

    clean_values: list[tuple[str, str]] = []
    seen: set[str] = set()
    for value, source in values:
        name = clean_name(value)
        norm = normalize(name)
        if not valid_name(name) or norm in seen:
            continue
        seen.add(norm)
        clean_values.append((name, source))
        if len(clean_values) >= TARGET_PER_CELL:
            break
    if len(clean_values) < TARGET_PER_CELL:
        raise ValueError(f"Only {len(clean_values)} candidates for {world['name']} exercise {exercise}")
    return clean_values


def load_history() -> tuple[dict[str, str], Counter]:
    spec = importlib.util.spec_from_file_location("history_pool", HISTORY_MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {HISTORY_MODULE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.EXCLUDED_HISTORY_PARTS.add(HERE.name.lower())
    return module.build_historical_index()


def pronunciation_penalty(norm: str) -> float:
    penalty = 0.0
    if re.search(r"[bcdfghjklmnpqrstvwxyz]{4}", norm):
        penalty += 0.8
    if re.search(r"(aa|ii|uu|yy|jj|qq|xx)", norm):
        penalty += 0.35
    if len(norm) > 18:
        penalty += (len(norm) - 18) * 0.07
    return penalty


def score_row(row: dict[str, object]) -> dict[str, object]:
    name = str(row["Name"])
    norm = str(row["Normalized"])
    world_rank = int(row["WorldRank"])
    exercise = int(row["ExerciseNumber"])
    origin = str(row["Origin"])
    source = str(row["Source"])
    words = name.split()

    world_category = {1: 8.7, 2: 6.9, 3: 9.1, 4: 7.9, 5: 8.0, 6: 8.3, 7: 6.3, 8: 6.1}[world_rank]
    world_story = {1: 9.1, 2: 8.5, 3: 9.0, 4: 8.8, 5: 8.2, 6: 8.4, 7: 8.2, 8: 7.8}[world_rank]
    exercise_character = {
        1: 8.2, 2: 7.6, 3: 7.8, 4: 8.0, 5: 8.4, 6: 8.1, 7: 8.3, 8: 8.0,
        9: 7.9, 10: 7.8, 11: 7.8, 12: 8.0, 13: 8.4, 14: 8.5, 15: 7.2,
        16: 8.3, 17: 8.1,
    }[exercise]
    form_fit = {
        1: 8.7, 2: 8.3, 3: 8.5, 4: 8.6, 5: 8.8, 6: 8.5, 7: 9.0, 8: 8.4,
        9: 8.3, 10: 8.8, 11: 8.1, 12: 8.5, 13: 8.9, 14: 8.9, 15: 7.1,
        16: 8.8, 17: 8.3,
    }[exercise]

    brand_character = exercise_character
    if len(words) == 1 and 5 <= len(norm) <= 11:
        brand_character += 0.55
    elif len(words) == 2 and len(norm) <= 17:
        brand_character += 0.35
    elif len(words) >= 4:
        brand_character -= 0.75
    if origin == "hand-authored":
        brand_character += 0.35

    if exercise in {7, 8, 9, 11, 12}:
        distinctiveness = 8.8
    elif exercise in {5, 10, 14, 15, 16}:
        distinctiveness = 7.8
    elif exercise in {4, 6, 13, 17}:
        distinctiveness = 8.1
    else:
        distinctiveness = 7.4
    if len(words) == 1:
        distinctiveness += 0.25

    fluency = 8.8
    fluency -= pronunciation_penalty(norm)
    if len(words) >= 4:
        fluency -= 0.55
    if len(norm) < 5:
        fluency -= 0.3

    bottle = 9.0 if len(words) == 1 and len(norm) <= 11 else 8.4 if len(words) == 2 else 7.4
    if len(norm) > 20:
        bottle -= 0.7

    category = world_category
    category_tokens = ("skin", "face", "barrier", "formula", "result", "derm")
    if any(token in norm for token in category_tokens):
        category += 0.7
    if world_rank == 1 and any(token in norm for token in ("time", "year", "long", "future", "later", "day")):
        category += 0.35
    if world_rank == 4 and any(token in norm for token in ("form", "train", "range", "practice", "adapt", "capacity")):
        category += 0.35

    penalty = 0.0
    risk_flags: list[str] = []
    retired = ("quiet", "calm", "serene", "haven", "refuge", "stone", "tide", "moon", "aura", "luxe", "mend")
    if any(token in norm for token in retired):
        penalty += 1.1
        risk_flags.append("retired aesthetic")
    if len(words) >= 4:
        penalty += 0.55
        risk_flags.append("campaign-like length")
    if words and words[0].lower() in {"the", "your", "our", "this", "what", "why", "how"}:
        penalty += 0.25
        risk_flags.append("heading or campaign syntax")
    if any(token in norm for token in ("guide", "academy", "school", "manual", "handbook", "glossary")):
        penalty += 0.55
        risk_flags.append("education/content syntax")
    if exercise == 15:
        penalty += 0.35
        risk_flags.append("translation dependence")
    if exercise == 11 and pronunciation_penalty(norm) > 0.4:
        penalty += 0.35
        risk_flags.append("pronunciation risk")
    if name.lower().startswith(("no ", "not ", "without ")):
        penalty += 0.2
        risk_flags.append("negative construction")
    if norm in {"result", "results", "proof", "evidence", "skin", "face", "visible", "clear", "open", "guide", "practice"}:
        penalty += 0.8
        risk_flags.append("generic single word")

    # A mechanism is not a merit by itself. Systematic constructions must still
    # produce an attractive naked word; these penalties prevent a large matrix
    # of broken spellings or generic suffixes from outranking authored names.
    source_penalties = {
        "cell fallback matrix": 1.45,
        "joined reconstruction": 1.35,
        "joined word device": 1.20,
        "single-vowel deletion": 0.95,
        "orthographic deletion": 0.85,
        "meaningful numbering": 0.55,
        "plus notation": 0.55,
        "transparent world-language compound": 0.85,
        "benefit compression": 0.45,
        "tangible object matrix": 0.35,
        "name the future matrix": 0.45,
        "anti-category matrix": 0.45,
        "audacity commands": 0.40,
        "technical compounds": 0.35,
        "source term reconstruction": 0.40,
        "world compound matrix": 0.35,
        "decoy company and institution": 0.50,
        "one plus one equals three": 0.75,
        "phonosemantic sound matrix": 0.25,
        "legible two-source blend": 0.30,
    }
    if source in source_penalties and origin != "hand-authored":
        value = source_penalties[source]
        penalty += value
        risk_flags.append("mechanical construction")

    if source == "English-native morpheme engine" and origin != "hand-authored":
        if norm.endswith(("company", "method", "practice", "standard", "house", "club")):
            penalty += 0.75
            risk_flags.append("generic institutional suffix")
        else:
            penalty += 0.25

    vowel_count = sum(char in "aeiouy" for char in norm)
    if origin != "hand-authored" and source in {
        "single-vowel deletion", "orthographic deletion", "joined reconstruction", "joined word device"
    }:
        if len(norm) >= 7 and vowel_count / len(norm) < 0.24:
            penalty += 0.75
            risk_flags.append("weak pronounceability")
        if re.search(r"[bcdfghjklmnpqrstvwxyz]{3}", norm):
            penalty += 0.55
            risk_flags.append("consonant cluster")
    if re.search(r"(.)\1\1", norm):
        penalty += 1.0
        risk_flags.append("accidental repeated letter")

    world_truth = 8.7 if exercise not in {11, 15} else 7.8
    story = world_story
    rank_tiebreak = max(0.0, (9 - world_rank) * 0.025)

    total = (
        brand_character * 0.20
        + form_fit * 0.14
        + world_truth * 0.14
        + category * 0.13
        + distinctiveness * 0.14
        + fluency * 0.10
        + bottle * 0.08
        + story * 0.07
        + rank_tiebreak
        - penalty
    )
    total = max(3.0, min(9.7, total))
    decision = "ADVANCE" if total >= 8.35 else "HOLD" if total >= 7.65 else "CUT"

    return {
        **row,
        "BrandCharacter": f"{max(1, min(10, brand_character)):.1f}",
        "FounderFormFit": f"{max(1, min(10, form_fit)):.1f}",
        "WorldTruth": f"{world_truth:.1f}",
        "CategoryIgnition": f"{max(1, min(10, category)):.1f}",
        "Distinctiveness": f"{max(1, min(10, distinctiveness)):.1f}",
        "Fluency": f"{max(1, min(10, fluency)):.1f}",
        "BottleUsability": f"{max(1, min(10, bottle)):.1f}",
        "StoryHeadroom": f"{story:.1f}",
        "Penalty": f"{penalty:.2f}",
        "CreativeRating": f"{total:.1f}",
        "CreativeDecision": decision,
        "CreativeRisk": "; ".join(risk_flags) if risk_flags else "low structural risk",
    }


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str] | None = None) -> None:
    if not rows:
        raise ValueError(f"No rows for {path}")
    fields = fields or list(rows[0])
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    raw: list[dict[str, object]] = []
    for world in WORLDS:
        featured_by_exercise: dict[int, list[str]] = {}
        for name, exercise in world["featured"]:
            featured_by_exercise.setdefault(exercise, []).append(name)
        for exercise in EXERCISES:
            for featured in featured_by_exercise.get(exercise, []):
                raw.append(
                    {
                        "RawOrder": len(raw) + 1,
                        "WorldRank": world["rank"],
                        "World": world["name"],
                        "ExerciseNumber": exercise,
                        "Exercise": EXERCISES[exercise],
                        "Form": FORM_BY_EXERCISE[exercise],
                        "Origin": "hand-authored",
                        "Source": "curated depth seed",
                        "Name": clean_name(featured),
                        "Normalized": normalize(featured),
                    }
                )
            for name, source in generated_for(world, exercise):
                raw.append(
                    {
                        "RawOrder": len(raw) + 1,
                        "WorldRank": world["rank"],
                        "World": world["name"],
                        "ExerciseNumber": exercise,
                        "Exercise": EXERCISES[exercise],
                        "Form": FORM_BY_EXERCISE[exercise],
                        "Origin": "systematic generation",
                        "Source": source,
                        "Name": name,
                        "Normalized": normalize(name),
                    }
                )

    write_csv(HERE / "raw-pool.csv", raw)
    history, history_counts = load_history()
    survivors: list[dict[str, object]] = []
    rejections: list[dict[str, object]] = []
    internal: dict[str, str] = {}
    for row in raw:
        norm = str(row["Normalized"])
        if norm in history:
            rejections.append({**row, "RejectReason": "historical exact", "Collision": history[norm]})
        elif norm in internal:
            rejections.append({**row, "RejectReason": "internal duplicate", "Collision": internal[norm]})
        else:
            internal[norm] = str(row["Name"])
            survivors.append(score_row(row))

    survivors.sort(
        key=lambda row: (
            -float(row["CreativeRating"]),
            int(row["WorldRank"]),
            int(row["ExerciseNumber"]),
            int(row["RawOrder"]),
        )
    )
    for index, row in enumerate(survivors, 1):
        row["OverallRank"] = index

    rating_fields = ["OverallRank"] + [field for field in survivors[0] if field != "OverallRank"]
    write_csv(HERE / "deduped-rated-pool.csv", survivors, rating_fields)
    write_csv(HERE / "dedupe-rejections.csv", rejections)

    # Trademark screening must test the strongest work in every founder-approved
    # world, not merely the worlds favored by the category-ignition prior. Take a
    # 40-name floor per world, then fill by global rating with a 90-name ceiling.
    selected_ids: set[int] = set()
    selected: list[dict[str, object]] = []
    selected_world_counts: Counter = Counter()
    for world in WORLDS:
        world_rows = [row for row in survivors if row["World"] == world["name"]][:40]
        for row in world_rows:
            selected_ids.add(int(row["RawOrder"]))
            row["SelectionBasis"] = "top 40 within core world"
            selected.append(row)
            selected_world_counts[str(row["World"])] += 1
    for row in survivors:
        if len(selected) >= 500:
            break
        raw_order = int(row["RawOrder"])
        world_name = str(row["World"])
        if raw_order in selected_ids or selected_world_counts[world_name] >= 90:
            continue
        selected_ids.add(raw_order)
        row["SelectionBasis"] = "global rating fill"
        selected.append(row)
        selected_world_counts[world_name] += 1

    top500 = sorted(
        selected,
        key=lambda row: (
            -float(row["CreativeRating"]),
            int(row["WorldRank"]),
            int(row["OverallRank"]),
        ),
    )
    for index, row in enumerate(top500, 1):
        row["Top500Rank"] = index
    top_fields = ["Top500Rank", "SelectionBasis"] + [
        field for field in rating_fields if field not in {"Top500Rank", "SelectionBasis"}
    ]
    write_csv(HERE / "top-500-rated.csv", top500, top_fields)

    cell_counts = Counter((str(row["World"]), int(row["ExerciseNumber"])) for row in raw)
    survivor_cells = Counter((str(row["World"]), int(row["ExerciseNumber"])) for row in survivors)
    top_cells = Counter((str(row["World"]), int(row["ExerciseNumber"])) for row in top500)
    summary = {
        "world_count": len(WORLDS),
        "exercise_count": len(EXERCISES),
        "raw_candidates": len(raw),
        "historical_index_size": len(history),
        "historical_rejections": sum(row["RejectReason"] == "historical exact" for row in rejections),
        "internal_duplicate_rejections": sum(row["RejectReason"] == "internal duplicate" for row in rejections),
        "rated_survivors": len(survivors),
        "top500_count": len(top500),
        "raw_world_counts": dict(Counter(str(row["World"]) for row in raw)),
        "survivor_world_counts": dict(Counter(str(row["World"]) for row in survivors)),
        "top500_world_counts": dict(Counter(str(row["World"]) for row in top500)),
        "top500_exercise_counts": dict(Counter(str(row["Exercise"]) for row in top500)),
        "creative_decisions": dict(Counter(str(row["CreativeDecision"]) for row in survivors)),
        "raw_cell_min": min(cell_counts.values()),
        "survivor_cell_min": min(survivor_cells.values()),
        "top500_cells_represented": len(top_cells),
        "total_cells": len(WORLDS) * len(EXERCISES),
        "largest_historical_sources": history_counts.most_common(12),
    }
    (HERE / "generation-rating-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
