from __future__ import annotations

import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
NAMING_DIR = HERE.parent
ROUND1_SCRIPT = NAMING_DIR / "core-worlds-depth-2026-07-16" / "generate-and-rate.py"
HISTORY_MODULE = NAMING_DIR / "decoy-exercise-2026-07-16" / "build-decoy-pool.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load_module(ROUND1_SCRIPT, "round1_generation")


def pipe(value: str) -> list[str]:
    return [item.strip() for item in value.split("|") if item.strip()]


WORLDS = [
    {
        "rank": 1,
        "name": "Time and Skin Longevity",
        "anchors": "sustain serial edition volume sequel ongoing current carry remain endure extend continue succession duration longrun afterward nextward persist return lasting recurrent".split(),
        "objects": pipe("backlist|running edition|serial number|volume mark|sustain pedal|long play|service interval|maintenance log|flight hour|odometer|generation line|relay baton|edition notice|continuity sheet|running order|endurance gauge|life table|sequence card|reissue stamp|return date"),
        "benefits": pipe("Longer Still|More To Come|Stays Current|Keeps Its Place|Built For The Long Middle|Good Over Time|Use After Use|Carries On Well|More Life In It|Ready For Another Year|Worth Continuing|Holds Up Longer|A Better Long Run|Still In Progress|Keeps Becoming|Made For The Ongoing"),
        "future": pipe("Future Continuous|The Next Edition|The Ongoing Face|A Longer Middle|Skin In Continuation|The New Staying Power|What Lasts Learns|Continuation Becomes Care|The Running Edition|Tomorrow Has A Sequel|The Durable Present|The Future Keeps Going|Aging As Continuation|The Next Volume|Time In Active Use|The Long Run Begins"),
        "counter": pipe("No Final Edition|Never Out Of Print|Not Past Tense|Older Still Going|The End Keeps Moving|No Last Chapter|Against Obsolescence|Not A Limited Run|Continuous Not Eternal|Long Without Forever|No Expiry Story|Present Without Pause|Later Without Loss|Not Done Yet|A Sequel To Now|Duration Not Drama"),
        "stances": pipe("Stay Current|Continue This|Keep The Run Going|Make Another Edition|Use It Longer|Carry The Good Forward|Add Another Chapter|Keep Becoming|Run Long|Sustain The Result|Remain In Use|Take The Long Middle|Return Again|Keep The Sequence|Extend What Works|Leave Room For Later"),
        "roots": "sustain serial edition volume sequel ongoing current carry remain endure extend contin succ dur longrun after next persist return".split(),
        "science": pipe("Fatigue Limit|Endurance Limit|Mean Survival|Life Table|Hazard Rate|Renewal Process|Serial Passage|Replicative Lifespan|Chronological Age|Long Term Potentiation|Sustained Release|Decay Constant|Maintenance Interval|Cumulative Exposure|Exposure Time|Residence Time|Long Range Order|Persistence Length|Run Time|Survival Curve"),
        "sound_left": "sus sai ser edi vol seq ong cur car rem end ext dur lon nex per ret".split(),
        "sound_right": "tain tal den line mark well ward form run set more now".split(),
        "metaphors": pipe("Backlist|Sequel|Longplay|Sustain|Carry|Continuation|Reissue|Serial|Relay|Runway|Odometer|Second Printing|Return Date|Current|Edition|Volume|Afterword|Mainline|Long Run|Stayer"),
        "world_words": pipe("Sostenuto|Sempre|Weiter|Encore|Ancora|Avanti|Continuare|Dauer|Proximo|Longe|Suite|Demain"),
        "source": pipe("Sustain Pedal|Long Play|Running Order|Second Printing|New Edition|Backlist Title|Serial Publication|Continuity Sheet|Service Interval|Flight Hours|Endurance Limit|Fatigue Life|Life Table|Survival Curve|Renewal Process|Long Range Order|Holding Time|Residence Time|Return Date|Current Issue"),
        "decoy": pipe("Next Edition Press|Future Continuous|The Backlist Company|Longplay House|Still Running Club|Sustain Works|Second Printing|Current Issue|The Ongoing|Carry Forward Editions|Another Volume|Longer Still|Return Date Company|Continuous Form|The Durable Present|Run of Years"),
        "featured": [
            ("Future Continuous", 3), ("Next Edition", 17), ("Longer Still", 2),
            ("Longplay", 14), ("Still Running", 2), ("Current Issue", 16),
            ("The Ongoing", 17), ("Run of Years", 17), ("Nextward", 7),
            ("Sustain Works", 17), ("Durable Present", 3), ("Another Volume", 17),
            ("Stay Current", 6), ("Present Continuous", 10), ("Second Printing", 5),
            ("Continuous Form", 13),
        ],
    },
    {
        "rank": 2,
        "name": "Nothing Hidden and Transparency",
        "anchors": "inspect trace scan source window section layer expose transmit radiograph micrograph illuminate inspectable viewable openwork seethrough revealable allside legible transparent".split(),
        "objects": pipe("microscope slide|radiograph|inspection lamp|section plane|source map|trace window|scrim|light curtain|glass wall|inspection hatch|access panel|open chassis|wireframe|transparent model|sample window|viewing screen|contact print|transmission grid|inspection mirror|source tree"),
        "benefits": pipe("Every Side Visible|Open To Inspection|See The Assembly|Nothing Behind It|All Parts Showing|Trace It Back|View The Whole Build|Easy To Inspect|Clear All The Way Through|Every Layer Accounted For|Open From Source|Visible At The Join|The Whole Construction|No Hidden Assembly|Inspect What You Use|Everything Has A Window"),
        "future": pipe("The Inspectable Brand|Skincare In Cross Section|Every Formula Viewable|The Open Assembly|A Window Into Every Choice|Beauty In Source View|The End Of Black Boxes|The Transparent Build|From Surface To Source|The New Inspection Standard|Skincare Under Glass|All Sides Open|The Viewable Formula|Open Architecture For Skin|Nothing Behind The Screen|A Fully Visible System"),
        "counter": pipe("Clear As Mud Not|Private Made Public|Opaque On Purpose No More|Open Machinery|Visible Interior|No Back Room|Uncurtained|Without A Blind Side|No Hidden Layer|Closed Source Never|Transparent Structure|All Surface No Secret|Open Underneath|No False Front|Inside On The Outside|No Concealed Join"),
        "stances": pipe("Inspect The Formula|Trace Every Choice|Open The Assembly|Show The Interior|See Through It|Follow The Source|Turn The Model Around|Look At Every Side|Keep The Window Open|Expose The Join|Make It Inspectable|Put It Under Glass|Show The Section|Open The Source|Leave The Curtain Off|Trace It Home"),
        "roots": "inspect trace scan source window section layer expose transmit radio micro illum view open wire clear glass".split(),
        "science": pipe("Optical Density|Transmission Window|Radiopacity|Radiolucency|Microscopy|Tomography|Cross Section|Section Plane|Source Map|Trace Signal|Transparency Index|Light Transmission|Visible Transmittance|Inspection Plane|Surface Profilometry|Confocal Image|Depth Map|Open Architecture|Wireframe Model|Exploded Assembly"),
        "sound_left": "ins tra sca sou win sec lay exp trans rad mic illum vie op wir".split(),
        "sound_right": "pect tal den line mark glass view source set open trace light".split(),
        "metaphors": pipe("Scrim|Wireframe|Radiograph|Micrograph|Sourceview|Crosssection|Windowwall|Openwork|Light Curtain|Glasswall|Inspection|Trace|Section|Cutline|Source Tree|Depth Map|Contact Print|View Screen|Access Panel|Sample Window"),
        "world_words": pipe("Apercu|Clarte|Abierto|Offen|Chiaro|Palese|Aperto|Klar|Lucido|Vista|Transparente|Ouverture"),
        "source": pipe("Confocal Image|Cross Section|Depth Map|Source Tree|Wireframe Model|Open Chassis|Access Panel|Inspection Hatch|Transmission Window|Light Curtain|Glass Wall|Exploded Assembly|Contact Print|Trace Signal|Source Map|Section Plane|Inspection Mirror|Sample Window|Surface Profile|Visible Transmittance"),
        "decoy": pipe("Open Assembly Studio|All Sides Architecture|Sourceview Systems|Windowwall House|Inspectable Works|The Trace Company|Under Glass|Clear As Made|Open Section|Seen Through|No Back Room|Every Side|Source Open|Visible Join|Daylighted|Uncurtained"),
        "featured": [
            ("Open Assembly", 17), ("All Sides", 2), ("Under Glass", 14),
            ("Clear As Made", 2), ("Visible Join", 13), ("No Back Room", 4),
            ("Source Open", 13), ("Daylighted", 7), ("Uncurtained", 4),
            ("Seen Through", 14), ("Sourceview", 9), ("Open Section", 13),
            ("Windowed", 7), ("Every Side", 2), ("Inspectably", 7),
            ("Viewable", 14),
        ],
    },
    {
        "rank": 3,
        "name": "Bare Face and Recognizable Self",
        "anchors": "subject known image resemblance handwriting autograph continuity documentary casting sitter unretouched features countenance expression identity character familiar selfportrait trueimage ownimage stillself".split(),
        "objects": pipe("casting card|portrait sitting|contact sheet|proof portrait|autograph|handwriting sample|documentary frame|identity card|family photograph|screen test|camera test|sitter chair|character sheet|continuity photo|signature line|image match|face chart|feature map|portrait plate|name card"),
        "benefits": pipe("Still Looks Like You|Known At A Glance|The Same Character|Your Image Continues|Keeps The Resemblance|True To The Subject|Looks Like Home|The Face Remains Familiar|More You Not New You|Your Features Continue|Recognized Instantly|A Better Known Face|Comfortably The Same|Your Own Image Holds|Character Still Visible|The Subject Stays You"),
        "future": pipe("The Future Looks Familiar|A Face With Continuity|The Subject Remains You|Identity Over Reinvention|The Next Portrait Is Still Yours|More Character With Time|Aging In Character|The Unretouched Future|Known By Your Features|The New Natural Subject|Your Image In Continuation|The End Of Face Replacement|A Future In Your Own Image|The Familiar Face Ahead|Character Is The Standard|Real Faces Remain"),
        "counter": pipe("Self Evident|Same But Different|Unretouched Standard|No Replacement Face|A Stranger Never|Original Without Nostalgia|Familiar Not Fixed|Character Not Correction|Unmade Up|True Without Perfect|The Same New You|No Casting Change|Real Subject No Filter|Unpolished Identity|Known Not Idealized|Natural Without Disappearing"),
        "stances": pipe("Stay You|Keep The Resemblance|Hold The Character|Use Your Own Image|Remain The Subject|Keep It Recognizable|Sign Your Face|Own The Portrait|Leave The Identity|Be Known By Sight|Keep The Familiar|Show The Real Subject|Let Features Continue|Stay In Your Image|Keep Your Signature|Look Like Home"),
        "roots": "subject known image resemble handwrite autograph contin document cast sitter unretouch feature countenance express ident character familiar".split(),
        "science": pipe("Identity Continuity|Recognition Memory|Face Familiarity|Feature Invariance|Expression Invariance|Self Face Recognition|Within Person Variation|Identity Preservation|Facial Configuration|Characteristic Feature|Recognition Signal|Prototype Distance|Image Registration|Face Matching|Feature Correspondence|Identity Tracking|Longitudinal Face|Expression Signature|Perceptual Constancy|Person Identity"),
        "sound_left": "sub kno ima res han aut con doc cas sit ret fea cou exp ide char fam".split(),
        "sound_right": "ject tal den line mark self face image set known true form".split(),
        "metaphors": pipe("Sitter|Autograph|Documentary|Portrait Plate|Casting Card|Contact Sheet|Signature Line|Proof Portrait|Continuity Photo|Character Sheet|Own Image|True Subject|Known Face|Family Likeness|Screen Test|Camera Test|Handwriting|Name Card|Image Match|Feature Map"),
        "world_words": pipe("Soggetto|Ritratto|Persona|Vero|Mesmo|Proprio|Bekannt|Sitter|Imagen|Viso|Semejanza|Autoportrait"),
        "source": pipe("Portrait Sitting|Contact Sheet|Proof Portrait|Casting Card|Screen Test|Camera Test|Character Study|Continuity Photo|Identity Match|Face Familiarity|Within Person Variation|Characteristic Feature|Image Registration|Feature Correspondence|Recognition Memory|Person Identity|Expression Signature|Longitudinal Face|Handwriting Sample|Family Photograph"),
        "decoy": pipe("True Subject Studio|Still You Portraits|Known Face Company|In Your Image|The Sitter|Own Image House|Character Continues|Unretouched Standard|Self Evident|As Known|First Likeness|The Same Character|Portrait Continuity|Real Subject|Known At A Glance|Feature Signature"),
        "featured": [
            ("True Subject", 17), ("Still You", 2), ("In Your Image", 14),
            ("Self Evident", 4), ("As Known", 17), ("First Likeness", 17),
            ("Real Subject", 17), ("Known At A Glance", 2), ("Feature Signature", 13),
            ("Portrait Continuity", 16), ("Unretouched Standard", 4),
            ("Character Continues", 3), ("Own Image", 14), ("The Sitter", 14),
            ("Stillself", 9), ("In Full Face", 14),
        ],
    },
    {
        "rank": 4,
        "name": "Skin Capability and Training",
        "anchors": "learnable trainable coachable dose cue pattern progression readiness transfer acquisition rehearsal conditioning steadywork skillset practicecycle formcycle workload responsecraft capabilityset buildphase foundation".split(),
        "objects": pipe("cue card|training block|work set|practice log|progress chart|readiness score|load pin|pace marker|movement screen|skill ladder|rehearsal room|training lane|workbench|form guide|session timer|dose chart|response log|build sheet|foundation phase|transfer test"),
        "benefits": pipe("Gets Better With Use|Learns The Routine|More Ready Over Time|Built By Repetition|A Better Response Pattern|Keeps Its Training|Progress In Reserve|More Skill Per Step|Ready For The Next Load|Form Improves Daily|Practice Becomes Capacity|A Routine That Builds|More Able By Degrees|Works Better With Time|Conditioned Through Care|The Benefit Of Repetition"),
        "future": pipe("Trainable Skin Care|The Learnable Routine|Capability Becomes The Goal|The New Practice Cycle|Skin Learns The Pattern|The Coaching Brand For Skin|From Application To Adaptation|The Age Of Skillful Skin|A Routine With Progression|Practice Builds Response|The Next Phase Is Capacity|Skincare In Training Blocks|The Progressive Use System|Results Through Rehearsal|The Conditioned Face|Skin With A Learning Curve"),
        "counter": pipe("Trainable Not Fixable|Gentle Progression|Rest Builds Capacity|Practice Without Perfection|Minimum Work Maximum Adaptation|Soft Load Strong Response|No Punishing Routine|Easy Repetition|Less Force More Form|Slow Work Fast Learning|No Hero Set|Strength Through Restraint|Coach Not Command|Workable Not Perfect|Practice Before Promise|Load Without Burn"),
        "stances": pipe("Cue The Response|Build The Pattern|Practice The Form|Train What Matters|Dose The Work|Repeat With Purpose|Keep The Load Useful|Make It Learnable|Build By Degrees|Work The Cycle|Check Readiness|Transfer The Skill|Coach The Skin|Progress The Routine|Rehearse The Result|Keep A Training Log"),
        "roots": "learn train coach dose cue pattern progress ready transfer acquire rehearse condition steady skill practice form workload response build".split(),
        "science": pipe("Skill Acquisition|Learning Curve|Training Transfer|Motor Adaptation|Progressive Resistance|Work To Rest Ratio|Stimulus Response|Dose Titration|Readiness Score|Training Volume|Load Management|Adaptive Learning|Practice Schedule|Distributed Practice|Retention Test|Transfer Test|Response Adaptation|Conditioning Effect|Acquisition Phase|Consolidation Phase"),
        "sound_left": "lea tra coa dos cue pat pro rea trans acq reh con ste ski pra for loa res bui".split(),
        "sound_right": "rn tal den line mark set form work ready well kind craft".split(),
        "metaphors": pipe("Cue|Training Block|Practice Log|Skill Ladder|Work Set|Rehearsal|Readiness Score|Learning Curve|Build Phase|Foundation|Transfer Test|Pace Marker|Form Guide|Session Timer|Response Log|Dose Chart|Training Lane|Workload|Progress Chart|Movement Screen"),
        "world_words": pipe("Allenamento|Pratica|Forma|Esercizio|Habitus|Capace|Entreno|Uebung|Technik|Progresso|Aptitude|Rehearsal"),
        "source": pipe("Skill Acquisition|Training Transfer|Motor Adaptation|Learning Curve|Progressive Resistance|Training Volume|Load Management|Readiness Score|Distributed Practice|Retention Test|Transfer Test|Practice Schedule|Acquisition Phase|Consolidation Phase|Work To Rest Ratio|Dose Titration|Response Adaptation|Conditioning Effect|Movement Screen|Foundation Phase"),
        "decoy": pipe("Trainable Works|Practice Cycle|Formwise Studio|Rangecraft|Well Practiced|The Work Set|Responsecraft|Capability Set|Build Phase Company|Learning Curve Club|Steady Practice|The Cue Method|Skill Transfer House|Practice Ready|Form Cycle|Foundation Work"),
        "featured": [
            ("Trainable", 14), ("Practice Cycle", 17), ("Formwise", 17),
            ("Rangecraft", 17), ("Well Practiced", 17), ("Responsecraft", 9),
            ("Capability Set", 17), ("Steady Practice", 17), ("Practice Ready", 17),
            ("Form Cycle", 17), ("The Work Set", 17), ("Cue The Response", 6),
            ("Build By Degrees", 6), ("Skillful Skin", 3), ("Workable Skin", 3),
            ("Learnable", 14),
        ],
    },
    {
        "rank": 5,
        "name": "Visible Performance",
        "anchors": "outcome observable register inspect grade score delta threshold resolve compare afterstate netchange headway finishquality acceptance measurable apparent evident demonstrate improve".split(),
        "objects": pipe("inspection card|change gauge|finish sample|grade scale|comparison panel|delta chart|acceptance stamp|result window|output dial|score sheet|reference tile|test coupon|control sample|pass indicator|change marker|resolution target|contrast card|inspection table|result plate|benchmark block"),
        "benefits": pipe("Change You Can Point To|A Result That Registers|Good By Inspection|Better On The Scale|Visible At A Glance|Passes The Look Test|Progress With A Mark|Improvement In View|The Result Reads Clearly|A Better After State|Observable By Design|The Difference Holds Up|Results With Definition|The Finish Improves|Change Worth Measuring|A Clearer Outcome"),
        "future": pipe("The Observable Brand|Results Enter The Record|Skincare With A Pass Mark|The New After State|Change Becomes Apparent|Performance Under Inspection|The End Of Vague Improvement|An Outcome You Can See|The Result Has Definition|Beauty With A Benchmark|The Measurable Face|A Better Finish Standard|Visible Change Becomes Routine|The New Result Scale|From Effect To Evidence|The Age Of Observable Outcomes"),
        "counter": pipe("Subtle But Measurable|Small Delta Big Difference|No Vague Result|Understated Output|Visible Without Theater|Quiet Result Loud Evidence|Soft Change Clear Mark|No Cosmetic Illusion|Modest Gain Real Effect|A Better After Not A New Before|Less Promise More Outcome|No Result Blur|Plain Performance|Gentle Change High Definition|Measured Not Dramatic|Low Drama High Output"),
        "stances": pipe("Register The Result|Inspect The Change|Mark The Difference|Read The Outcome|Compare The Finish|Pass The Look Test|Show The Delta|Make Progress Apparent|Set The Benchmark|Grade The Result|Watch The Output|Measure The After|Raise The Finish|See The Net Change|Check The Difference|Make It Observable"),
        "roots": "outcome observe register inspect grade score delta threshold resolve compare after netchange headway finish accept measure apparent evident".split(),
        "science": pipe("Net Change|Outcome Measure|Observable Difference|Response Delta|Detection Limit|Visual Analog Scale|Instrument Grade|Comparison Standard|Acceptance Criterion|Resolution Target|Contrast Sensitivity|Change Detection|Effect Threshold|Performance Measure|Output Signal|Quality Grade|Finish Inspection|Pass Criterion|Measured Difference|Apparent Change"),
        "sound_left": "out obs reg ins gra sco del thr res com aft net hea fin acc mea app evi".split(),
        "sound_right": "come tal den line mark view grade set result gain clear show".split(),
        "metaphors": pipe("Passmark|Grade|Outcome|Afterstate|Netchange|Result Plate|Change Gauge|Finish Sample|Reference Tile|Test Coupon|Control Sample|Benchmark Block|Contrast Card|Resolution Target|Output Dial|Score Sheet|Acceptance Stamp|Result Window|Inspection Card|Delta Chart"),
        "world_words": pipe("Esito|Risultato|Resultat|Ergebnis|Resultado|Effetto|Cambio|Visible|Netto|Evidente|Misura|Progresso"),
        "source": pipe("Net Change|Outcome Measure|Response Delta|Detection Limit|Visual Analog Scale|Comparison Standard|Acceptance Criterion|Resolution Target|Change Detection|Effect Threshold|Performance Measure|Output Signal|Quality Grade|Finish Inspection|Pass Criterion|Measured Difference|Apparent Change|Reference Tile|Control Sample|Test Coupon"),
        "decoy": pipe("Net Change Company|Good Measure|Visible Delta|Result Mark|Afterstate|Change Seen|Passmark|The Outcome Standard|Observable Works|Result Scale|Plain Result|Clear Outcome|Notice Mark|Finish Grade|Improvement Index|The Look Test"),
        "featured": [
            ("Net Change", 17), ("Good Measure", 17), ("Visible Delta", 17),
            ("Result Mark", 17), ("Afterstate", 14), ("Change Seen", 17),
            ("Passmark", 14), ("Result Scale", 17), ("Plain Result", 17),
            ("Clear Outcome", 17), ("Notice Mark", 17), ("Finish Grade", 17),
            ("Improvement Index", 17), ("The Look Test", 17),
            ("Observable", 14), ("Measured Difference", 10),
        ],
    },
    {
        "rank": 6,
        "name": "Barrier Strength and Adaptive Capacity",
        "anchors": "margin headroom feedback coupling elasticity compliance damping recovery reserve resilience giveback flexure responsive dynamicbalance stressready livingrange softlimit returnrange adaptmargin controlmargin".split(),
        "objects": pipe("control margin|flex coupling|spring reserve|shock mount|feedback dial|compliance joint|damping ring|recovery spring|expansion gap|buffer zone|elastic margin|response curve|headroom gauge|reserve tank|return spring|dynamic joint|stress indicator|flex plate|control damper|adaptive valve"),
        "benefits": pipe("More Headroom|A Wider Response Range|Keeps Its Margin|Ready For Variability|Returns With More Ease|Flexible Under Stress|More Give In Reserve|Holds Dynamic Balance|Room To Respond|A Better Return Range|Elasticity With Purpose|Stability That Adjusts|Capacity Beyond Baseline|More Recovery Margin|A Responsive Reserve|Stronger Through Feedback"),
        "future": pipe("The Age Of Response Margin|Skin With More Headroom|Adaptive Strength Becomes Standard|The Dynamic Barrier|From Rigidity To Range|A Wider Tolerance Future|The Responsive Interface|Skin In Feedback|The New Recovery Margin|Capacity Through Flexibility|The End Of Brittle Strength|Dynamic Balance For Skin|More Range After Stress|The Adaptive Control Surface|Resilience With Headroom|The Flexible Future"),
        "counter": pipe("Soft Limit|Strong Compliance|Controlled Give|Flexible Resistance|Stable Feedback|Open Margin|Yielding Strength|Dynamic Rest|Responsive Structure|Firmly Adaptive|Giveback Strength|Soft Control|Stable Under Change|Elastic Not Loose|More Margin Less Armor|Recovery Before Defense"),
        "stances": pipe("Keep The Margin|Build More Headroom|Use The Feedback|Widen The Range|Leave Room To Respond|Return With Ease|Hold Dynamic Balance|Make The Coupling Flexible|Keep Some Give|Recover The Margin|Stay Within The Window|Adapt The Control|Use The Reserve|Build Recovery Range|Respond With Headroom|Protect The Feedback"),
        "roots": "margin headroom feedback coupling elastic compliance damp recovery reserve resilience give flex responsive dynamic stress return adapt control".split(),
        "science": pipe("Compliance|Damping|Control Margin|Response Margin|Elastic Recovery|Dynamic Compliance|Feedback Gain|Stability Margin|Recovery Time|Stress Adaptation|Dynamic Range|Headroom|Homeostatic Reserve|Adaptive Control|Return Ratio|Mechanical Hysteresis|Resilience Measure|Load Sharing|Buffering Power|Response Flexibility"),
        "sound_left": "mar hea fee cou ela com dam rec res giv fle resp dyn str ret ada con".split(),
        "sound_right": "gin tal den line mark flex range set hold well return more".split(),
        "metaphors": pipe("Headroom|Control Margin|Flex Coupling|Spring Reserve|Feedback Dial|Damping Ring|Recovery Spring|Expansion Gap|Buffer Zone|Elastic Margin|Return Spring|Dynamic Joint|Stress Indicator|Flex Plate|Control Damper|Adaptive Valve|Response Curve|Reserve Tank|Compliance Joint|Shock Mount"),
        "world_words": pipe("Souplesse|Elasticita|Reserva|Margen|Equilibrio|Risposta|Adatta|Flessibile|Stabilita|Recupero|Tensione|Ritorno"),
        "source": pipe("Control Margin|Response Margin|Dynamic Compliance|Feedback Gain|Stability Margin|Recovery Time|Stress Adaptation|Dynamic Range|Homeostatic Reserve|Adaptive Control|Return Ratio|Mechanical Hysteresis|Resilience Measure|Load Sharing|Buffering Power|Response Flexibility|Elastic Recovery|Damping Ratio|Compliance Joint|Expansion Gap"),
        "decoy": pipe("Response Margin|Flex Reserve|Ready Buffer|Adaptive Margin|Living Range|Elastic Reserve|Return Range|Steady Response|Rangeholder|Bufferwise|Stress Ready|Soft Limit|Responsive Form|Elastic Margin|Feedback Works|Headroom House"),
        "featured": [
            ("Response Margin", 17), ("Flex Reserve", 17), ("Ready Buffer", 17),
            ("Adaptive Margin", 17), ("Living Range", 17), ("Elastic Reserve", 17),
            ("Return Range", 17), ("Steady Response", 17), ("Rangeholder", 9),
            ("Bufferwise", 9), ("Stress Ready", 17), ("Soft Limit", 4),
            ("Responsive Form", 17), ("Elastic Margin", 17),
            ("Feedback Works", 17), ("Headroom", 14),
        ],
    },
    {
        "rank": 7,
        "name": "Evidence and Proof",
        "anchors": "observed checked traceable reproducible measured verified documented corroborate attest validate account audittrail proofline sourcetrace claimtrace finding replicate uncertainty calibration record".split(),
        "objects": pipe("verification stamp|audit mark|trace record|source trail|replicate plate|measurement log|calibration card|uncertainty budget|validation sheet|finding notice|test certificate|reference specimen|chain record|observation card|account book|evidence tag|inspection seal|result witness|source trace|proof line"),
        "benefits": pipe("Every Result Traceable|Proof With A Trail|The Finding Repeats|Checked From End To End|A Claim You Can Audit|Evidence With A Source|Measured Then Verified|The Result Has A Witness|Confidence Through Replication|A Record You Can Follow|Proof In The Details|Validated In Public|Every Measure Accounted For|The Source Stays Attached|A Result That Repeats|Known Within Limits"),
        "future": pipe("The Traceable Claim|Every Result Gets A Record|Skincare With A Source Trail|The Reproducible Standard|Evidence Becomes Visible|The End Of Unsupported Claims|A Formula Under Audit|From Result To Replicate|The Verified Future|Proof With Uncertainty Included|The Accountable Measure|Every Finding Has A Witness|The New Validation Standard|Skincare With A Chain Of Evidence|The Documented Result|Testing In The Open"),
        "counter": pipe("Certain About Uncertainty|Proof With Limits|Verified Not Absolute|No Unsupported Confidence|Warm Proof Cold Test|Evidence Without Authority|Measured Doubt|The Honest Error Bar|No Claim Without A Trail|Confidence With Conditions|Trust The Replicate|Checked Not Believed|Known Not Certain|Proof That Shows Its Work|No Hidden Assumption|Facts With Footnotes"),
        "stances": pipe("Trace The Result|Check It Twice|Replicate The Finding|Keep The Source Attached|Measure The Uncertainty|Validate The Claim|Audit The Formula|Follow The Evidence|Record What Happened|Show The Error Bar|Attach The Source|Verify The Result|Account For Every Claim|Name The Limit|Keep A Proof Trail|Test The Repeat"),
        "roots": "observe check trace reproduce measure verify document corroborate attest validate account audit proof source claim find replicate uncert calibrate record".split(),
        "science": pipe("Measurement Uncertainty|Error Bar|Confidence Bound|Validation Study|Inter Rater Reliability|Repeatability|Reproducibility|Calibration Standard|Traceability Chain|Reference Specimen|Verification Protocol|Observed Agreement|Method Validation|Detection Confidence|Source Verification|Audit Sample|Control Limit|Evidence Chain|Replicate Measure|Uncertainty Budget"),
        "sound_left": "obs che tra rep mea ver doc cor att val acc aud pro sou cla fin unc cal rec".split(),
        "sound_right": "serve tal den line mark trace proof set fact check record sure".split(),
        "metaphors": pipe("Error Bar|Proofline|Source Trace|Audit Mark|Evidence Tag|Verification Stamp|Trace Record|Replicate Plate|Calibration Card|Validation Sheet|Finding Notice|Test Certificate|Reference Specimen|Chain Record|Observation Card|Inspection Seal|Result Witness|Proof Trail|Control Limit|Source Trail"),
        "world_words": pipe("Verifica|Prova|Beweis|Preuve|Prueba|Attestato|Certum|Evidenza|Misura|Conferma|Trace|Validado"),
        "source": pipe("Measurement Uncertainty|Error Bar|Validation Study|Inter Rater Reliability|Repeatability|Reproducibility|Calibration Standard|Traceability Chain|Reference Specimen|Verification Protocol|Observed Agreement|Method Validation|Source Verification|Audit Sample|Control Limit|Evidence Chain|Replicate Measure|Uncertainty Budget|Proof Trail|Source Trail"),
        "decoy": pipe("Proofline|Source Trace|On Record|Evidence Mark|Repeat Finding|Verified Result|Open Assay|Factchecked|Claim Trace|Result Witness|Measurement First|The Error Bar|Audit Mark|Traceable Works|Observed Company|Checked Twice"),
        "featured": [
            ("Proofline", 17), ("Source Trace", 17), ("On Record", 17),
            ("Evidence Mark", 17), ("Repeat Finding", 17), ("Verified Result", 17),
            ("Open Assay", 17), ("Factchecked", 7), ("Claim Trace", 17),
            ("Result Witness", 17), ("Measurement First", 17), ("The Error Bar", 17),
            ("Audit Mark", 17), ("Traceable", 14), ("Observed", 14),
            ("Checked Twice", 17),
        ],
    },
    {
        "rank": 8,
        "name": "Better Informed and Customer Agency",
        "anchors": "decide interpret navigate orient compare question comprehend understandable choiceful userled sensefirst knowable learnable readable informedness discernment clearheaded mentalmodel decisionaid referencekey mapread fluentchoice agency".split(),
        "objects": pipe("decision tree|reference map|comparison card|choice grid|orientation point|legend box|navigation aid|route marker|question card|decision table|user guide|reading key|sense map|information panel|choice architecture|comparison scale|decision compass|interpretation key|wayfinding sign|reference point"),
        "benefits": pipe("Make A Better Call|Know The Difference|Choose With A Map|Understand Before Buying|Good Sense In Use|More Fluent Choices|A Question Worth Asking|The Why Makes Sense|Decisions Get Easier|Clarity At The Point Of Choice|Know Enough To Choose|Your Judgment Improves|Information You Can Act On|A More Readable Routine|Choice With Context|Understanding In Practice"),
        "future": pipe("The User Leads|Skincare Becomes Knowable|The Decision Moves To You|A More Readable Category|The Age Of Fluent Choice|The Customer Holds The Map|Understanding Before Authority|The Self Directed Standard|Every Routine Has A Why|Knowledge At The Point Of Use|The End Of Passive Expertise|A Better Decision System|Skincare With User Control|The Comprehensible Formula|Choice Becomes Capability|The Informed User Era"),
        "counter": pipe("Clearheaded Beauty|Expert Enough To Question|Simple With Context|No Guru Needed|Knowledge Without Authority|Readable Complexity|A Beginner With Judgment|Information Not Instruction|Guidance Without Control|Smart Enough To Ask|Advanced But Knowable|Choose Without Obeying|No Blind Recommendation|Informed Not Overwhelmed|Good Sense Over Expert Status|User Led Expertise"),
        "stances": pipe("Make The Call|Read The Difference|Ask The Next Question|Choose With Context|Use Your Good Sense|Keep The Map|Know Enough|Compare Before Choosing|Follow The Why|Read The Routine|Interpret The Result|Question The Expert|Navigate The Category|Decide What Stays|Learn What To Ignore|Hold The Reference Key"),
        "roots": "decide interpret navigate orient compare question comprehend understand choice user sense know learn read inform discern clear mental reference map fluent agency".split(),
        "science": pipe("Decision Quality|Decision Confidence|Information Literacy|Comprehension Check|Choice Set|Reference Frame|Decision Threshold|User Agency|Cognitive Map|Sensemaking|Information Scent|Wayfinding|Decision Path|Comparison Matrix|Interpretive Frame|Knowledge State|Question Formulation|Decision Context|Actionable Information|Comprehension Score"),
        "sound_left": "dec int nav ori com que pre und cho use sen kno lea rea inf dis cle men ref map flu age".split(),
        "sound_right": "cide tal den line mark key map set know wise choice clear".split(),
        "metaphors": pipe("Decision Tree|Reference Map|Choice Grid|Legend Box|Route Marker|Question Card|Decision Table|Reading Key|Sense Map|Information Panel|Comparison Scale|Decision Compass|Interpretation Key|Wayfinding Sign|Reference Point|Choice Architecture|Decision Path|Cognitive Map|User Guide|Orientation Point"),
        "world_words": pipe("Sapere|Savoir|Wissen|Capire|Comprendre|Scelta|Sentido|Conocer|Legere|Klarheit|Choix|Entender"),
        "source": pipe("Decision Quality|Decision Confidence|Information Literacy|Comprehension Check|Choice Set|Reference Frame|Decision Threshold|User Agency|Cognitive Map|Information Scent|Wayfinding|Decision Path|Comparison Matrix|Interpretive Frame|Knowledge State|Question Formulation|Decision Context|Actionable Information|Comprehension Score|Reference Key"),
        "decoy": pipe("Knowingly|Clearheaded|Question Ready|Knowledge In Use|Choice Fluent|Good Sense|User Led|Read Forward|Learnability|Understood|Choicecraft|Know The Difference|Sense First|Matter of Choice|Decision House|The Reference Key"),
        "featured": [
            ("Knowingly", 14), ("Clearheaded", 17), ("Question Ready", 17),
            ("Knowledge In Use", 17), ("Choice Fluent", 17), ("Good Sense", 17),
            ("User Led", 17), ("Read Forward", 17), ("Learnability", 14),
            ("Understood", 14), ("Choicecraft", 9), ("Know The Difference", 17),
            ("Sense First", 17), ("Matter of Choice", 17),
            ("The Reference Key", 17), ("Decision Quality", 10),
        ],
    },
]


def load_history():
    module = load_module(HISTORY_MODULE, "round2_history")
    module.EXCLUDED_HISTORY_PARTS.add(HERE.name.lower())
    return module.build_historical_index()


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
        for exercise in base.EXERCISES:
            for featured in featured_by_exercise.get(exercise, []):
                raw.append(
                    {
                        "RawOrder": len(raw) + 1,
                        "WorldRank": world["rank"],
                        "World": world["name"],
                        "ExerciseNumber": exercise,
                        "Exercise": base.EXERCISES[exercise],
                        "Form": base.FORM_BY_EXERCISE[exercise],
                        "Origin": "hand-authored",
                        "Source": "round-two curated depth seed",
                        "Name": base.clean_name(featured),
                        "Normalized": base.normalize(featured),
                    }
                )
            for name, source in base.generated_for(world, exercise):
                raw.append(
                    {
                        "RawOrder": len(raw) + 1,
                        "WorldRank": world["rank"],
                        "World": world["name"],
                        "ExerciseNumber": exercise,
                        "Exercise": base.EXERCISES[exercise],
                        "Form": base.FORM_BY_EXERCISE[exercise],
                        "Origin": "systematic generation",
                        "Source": source,
                        "Name": name,
                        "Normalized": base.normalize(name),
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
            survivors.append(base.score_row(row))

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
    rated_fields = ["OverallRank"] + [field for field in survivors[0] if field != "OverallRank"]
    write_csv(HERE / "deduped-rated-pool.csv", survivors, rated_fields)
    write_csv(HERE / "dedupe-rejections.csv", rejections)

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
        field for field in rated_fields if field not in {"Top500Rank", "SelectionBasis"}
    ]
    write_csv(HERE / "top-500-rated.csv", top500, top_fields)

    summary = {
        "round": 2,
        "world_count": len(WORLDS),
        "exercise_count": len(base.EXERCISES),
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
        "largest_historical_sources": history_counts.most_common(15),
    }
    (HERE / "generation-rating-audit.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
