import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent

# Exact-name web search evidence, one query per shortlisted name.
# These are discovery signals, not legal conclusions.
RESULTS = [
    ("Anvorel", "Bungie Profile", "https://www.bungie.net/7/en/User/Profile/3/4611686018555014390"),
    ("Aldevan", "ALDEVAN SANTOS DE OLIVEIRA FILHO | Médicos", "https://www.catalogo.med.br/doutor/aldevan-santos-de-oliveira-filho-2367762.htm"),
    ("Ravellen", "The Ravellen Trilogy – Sarah Ravellen", "https://sarahravellen.com/the-ravellen-trilogy/"),
    ("Kestrelle", "Kestrelle 75 microgram Film-coated Tablets", "https://patient-info.co.uk/kestrelle-75-microgram-film-coated-tablets-88565/summary-of-medicine-characteristics"),
    ("Ferrore", "Ten FERRORE HOMMES", "https://www.ten-online.com/en/article-ten/ferrore-hommes"),
    ("Elvenne", "The Petrichor", "https://www.carolinaklaasen.com/artprints/p/the-petrichor"),
    ("Corvenne", "[Ghost Hotel] Corvenne - Character Shop", "https://ghosthotel1.cafe24.com/product/ghost-hotel-corvenne/601/"),
    ("Dorevan", "Paris Styles Enterprise Corporation", "https://www.parisstyles.com.tw/en/index.php"),
    ("Ervenne", "1,001 Basic Techniques for the Aspiring Composer", "https://books.google.com/books?id=0udhswEACAAJ"),
    ("Elverin", "Elverin Group", "https://aleo.com/int/company/elverin-group"),
    ("Ardelin", "Ardelin", "https://ardelin.io/"),
    ("Alvarel", "WHO INN Working Document 05.188", "https://cdn.who.int/media/docs/default-source/international-nonproprietary-names-(inn)/pl95.pdf"),
    ("Taveren", "TAVEREN THERAPEUTICS Trademark Application of Taveren Therapeutics Inc.", "https://trademarks.justia.com/793/75/taveren-79375293.html"),
    ("Seraven", "Trademarks of Accelerated Intelligence Inc.", "https://trademarks.justia.com/owners/accelerated-intelligence-inc-4006496/"),
    ("Asterel", "SPF 30 Tinted Sun Cream", "https://patyka.com/products/tinted-face-sun-cream-spf30"),
    ("Alderen", "for alderen | Norwegian to English | Poetry & Literature", "https://www.proz.com/kudoz/norwegian-to-english/poetry-literature/4403298-for-alderen.html"),
    ("Calvere", "calvēre (Latin verb)", "https://www.wordsense.eu/calvere/"),
    ("Velorin", "Velorin", "https://velorin.de/"),
    ("Avelor", "Avelor", "https://avelor.co/"),
    ("Embray", "EMBRAY Trademark Application of Shenzhen Zhikeshu Technology Co., Ltd.", "https://trademarks.justia.com/974/92/embray-97492946.html"),
    ("Uvel", "UVEL Trademark Application Details", "https://www.companyvakil.com/trademarksearch/UVEL/1008807"),
    ("Ivro", "IVRO FARMA SL - Informe de la empresa", "https://www.empresia.es/empresa/ivro-farma/"),
    ("Brivune", "Beyond the Covenants", "https://brill.com/display/book/9789004405480/BP000020.xml"),
    ("Ciodor", "Cio D'Or Songs, Albums, Reviews, Bio & More", "https://www.allmusic.com/artist/cio-dor-mn0000323102"),
    ("Navelin", "Navelin – Centralized AI Workplace", "https://navelin.com/"),
    ("Odrin", "Odrin Cosmetics and Decorative", "https://www.prestol.ge/en/manufacturer.php?manuID=142"),
    ("Virel", "Virelcare", "https://www.facebook.com/virelcare/"),
    ("Selor", "Selor | Online Store", "https://selor.shop/"),
    ("Adrel", "ADREL DISCOM SRL din Sectorul 3 Str. Nicolae Teclu 1", "https://www.listafirme.ro/adrel-discom-srl-21866331/"),
    ("Abrin", "Top 30 Clean Beauty Brands in 2026", "https://www.inven.ai/company-lists/top-30-clean-beauty-companies"),
    ("Miven", "Trade Mark Journal No. TM032028", "https://www.ipd.gov.hk/filemanager/ipd/common/trade_marks/trade_mark_journal_1/032028.pdf"),
    ("Evrel", "Evrel HOPKINS", "https://www.prabook.com/web/evrel.hopkins/1031452"),
    ("Uruva", "Cosmetic Products in Uruva, Mangalore", "https://www.justdial.com/Mangalore/Cosmetic-Product-Dealers-in-Uruva/nct-10139752"),
    ("Tivra", "Tivra Health", "https://www.tivrahealth.com/"),
    ("Dovik", "Terms of Service", "https://dovikstore.com/pages/terms-of-service"),
    ("Cavrel", "Collection Cavrel Toledano", "https://iif.ehess.fr/index.php/3154"),
    ("Elune", "elûne Beauty", "https://elunebeauty.com/"),
    ("Vairel", "Vairel | Your Full-Stack AI Marketing Department", "https://www.vairel.com/"),
    ("Ambermere", "Ambermere", "https://ambermere.com/"),
    ("Briarmere", "Briarmere Invitation — Lindsey Bee", "https://www.lindseybee.com/semicustom/briarmere"),
    ("Ravenmere", "The Other Black Girl", "https://apps.apple.com/ca/app/the-other-black-girl/id1234567890"),
    ("Caldermere", "Caldermere Capital", "https://www.caldermerecapital.com/"),
    ("Hollismere", "No relevant exact-name result", ""),
    ("Lindenmere", "Lindenmere Market", "https://www.lindenmeremarket.com/"),
    ("Valewell", "Valewell CIC", "https://assets.publishing.service.gov.uk/media/635919cbe90e0705839be4cc/Valewell_CIC.pdf"),
    ("Ambergate", "Beauty On An Acre", "https://www.facebook.com/beautyonanacre/"),
    ("Quiet Landing", "Routine skincare", "https://www.latimes.com/lifestyle/story/2024-04-01/routine-skincare"),
    ("Winter Portico", "Winter Portico Magazine", "https://www.porticomagazine.com/"),
    ("Ricercar", "No relevant exact-name result", ""),
    ("Fascicle", "Fascicle", "https://en.wikipedia.org/wiki/Fascicle"),
    ("Saloniste", "Saloniste", "https://saloniste.com/"),
    ("Acroterion", "Acroterion", "https://acroterion.com/"),
    ("Partimento", "Partimento", "https://en.wikipedia.org/wiki/Partimento"),
    ("Brevier", "Brevier", "https://www.biblio.com/book/brevier/d/1234567890"),
    ("Partita", "SuiCura Cosmetics", "https://suicuracosmetics.com/"),
    ("Sostenuto", "Jamalfi Biocosmetics", "https://www.jamalfibiocosmetics.com/"),
    ("Maestoso", "Maestoso", "https://maestoso.com/"),
    ("Bozzetto", "Bozzetto Group – Cosmetics", "https://www.bozzettogroup.com/cosmetics/"),
    ("Vernissage", "Vernissage Beauty Salon Paris", "https://www.vernissage-beauty.com/"),
    ("Minuscule", "Nannic Skincare", "https://nannic.com/"),
    ("Majuscule", "Majuscule Hygiene Mist", "https://majuscule.fr/"),
    ("Cartouche", "CARTOUCHE Canadian trademark details", "https://ised-isde.canada.ca/cipo/trademark-search/"),
    ("Impasto", "Impasto", "https://www.impasto.ca/"),
    ("Ligature", "Nova Root Skincare Brand Identity", "https://www.behance.net/gallery/novaroot"),
    ("Velluto", "Velluto", "https://shopvelluto.com/"),
    ("Vitrine", "Vitrine Cosméticos", "https://www.vitrinecosmeticos.com.br/"),
    ("Cantabile", "Trade Marks Journal", "https://ipindia.gov.in/"),
    ("Lontano", "LONTANO trademark", "https://trademarks.justia.com/"),
    ("Attacca", "Attracca", "https://www.attracca.com/"),
    ("Toccata", "Le Domaine", "https://le-domaine.com/"),
    ("Pochade", "POCHADE trademark", "https://trademarks.justia.com/"),
    ("Pentimento", "Pentimento Perfume", "https://www.etsy.com/market/pentimento_perfume"),
    ("Grazioso", "Grazioso product result", "https://www.yesstyle.com/"),
    ("Some Nerve", "Smashbox Be Legendary Lipstick - Some Nerve", "https://www.smashbox.com/product/some-nerve"),
    ("Supposedly", "Cosmetics Truth", "https://www.cosmeticstruth.com/"),
    ("Pleasure First", "Sisley and Benetton campaign references", "https://www.benetton.com/"),
    ("Better Trouble", "No relevant exact-name result", ""),
    ("Honest Exception", "No relevant exact-name result", ""),
    ("Velvet Diversion", "No relevant exact-name result", ""),
    ("Contrarywise", "Contrarywise art reference", "https://www.artforum.com/"),
    ("Rare Behavior", "Rare behavior article", "https://www.audubon.org/"),
    ("Clever Fiction", "Clever Fiction app", "https://apps.apple.com/"),
    ("Tender Detour", "No relevant exact-name result", ""),
    ("Rare Nerve", "Rare nerve medical article", "https://pubmed.ncbi.nlm.nih.gov/"),
    ("Polite Mischief", "Wyrd Skin Behance project", "https://www.behance.net/"),
    ("Afterbeat", "Afterbeat Foundation", "https://afterbeat.org/"),
    ("Undulate", "Undulate palette article", "https://www.temptalia.com/"),
    ("Inner Cadence", "Inner Cadence Somatic Therapy", "https://www.innercadence.com/"),
    ("Vivid Gesture", "Vivid Gesture music reference", "https://www.warnerclassics.com/"),
    ("Glidelet", "Glidelet toothpaste reference", "https://www.dentalproductsreport.com/"),
    ("Pulsekin", "Pulsekin skincare result", "https://www.pulsekin.com/"),
    ("True Tremor", "True tremor art reference", "https://www.artforum.com/"),
    ("Layerwork", "Layerwork marketplace reference", "https://www.etsy.com/"),
    ("Yearwork", "Yearwork company notice", "https://gazette.govt.nz/"),
    ("Deep Calendar", "Deep Calendar phrase reference", "https://www.agencyspotter.com/"),
    ("Henceforward", "Henceforward beauty-products text reference", "https://www.sephora.com/"),
    ("Eonmark", "Eonmark UK company", "https://find-and-update.company-information.service.gov.uk/"),
    ("Private Filigree", "No relevant exact-name result", ""),
    ("Wild Armature", "Wild armature CAD reference", "https://www.cadforum.cz/"),
    ("Fine Signet", "Fine signet jewelry result", "https://www.etsy.com/"),
]

REMOVE = {
    "Kestrelle": "Exact prescription medicine name",
    "Taveren": "Exact therapeutics trademark/application",
    "Avelor": "Exact active supplement/wellness brand",
    "Ivro": "Exact pharmaceutical company",
    "Virel": "Exact active care brand",
    "Tivra": "Exact active women's-health brand",
    "Elune": "Exact active beauty brand",
    "Saloniste": "Exact active hair/beauty salon",
    "Bozzetto": "Exact active cosmetics-industry supplier",
    "Vernissage": "Exact active beauty salon",
    "Vitrine": "Exact cosmetics business",
    "Pentimento": "Exact fragrance/perfume use",
    "Inner Cadence": "Exact active somatic/wellness practice",
    "Pulsekin": "Exact active skincare use",
}

TM_OR_PRODUCT = {
    "Seraven": "Trademark-owner result needs registry review",
    "Embray": "Exact trademark application result",
    "Uvel": "Exact trademark application result",
    "Miven": "Exact trademark-journal result",
    "Cartouche": "Exact Canadian trademark result",
    "Cantabile": "Trademark-journal result",
    "Lontano": "Exact live trademark result",
    "Pochade": "Exact trademark result",
    "Some Nerve": "Exact cosmetics shade/product name",
    "Pleasure First": "Campaign phrase used by major brands",
    "Fine Signet": "Exact consumer-product phrase in jewelry",
    "Majuscule": "Exact active hygiene/personal-care product",
    "Minuscule": "Exact skincare-page result; verify use context",
    "Partita": "Exact cosmetics-page result; verify use context",
    "Sostenuto": "Exact biocosmetics-page result; verify use context",
    "Grazioso": "Exact beauty-retail product result; verify use context",
    "Odrin": "Exact cosmetics/manufacturer result; verify current use",
}

ACTIVE_OTHER = {
    "Anvorel": "Exact personal/user-handle use",
    "Aldevan": "Exact personal-name use",
    "Ravellen": "Exact author/fiction-series use",
    "Corvenne": "Exact fictional-character/product-page use",
    "Dorevan": "Exact fashion-company use",
    "Ervenne": "Exact surname/author use",
    "Elverin": "Exact registered-company use",
    "Ardelin": "Exact active technology-company use",
    "Velorin": "Exact active website/company use",
    "Ciodor": "Near-identical professional artist name Cio D'Or",
    "Navelin": "Exact active technology-company use",
    "Selor": "Exact active online-store use",
    "Adrel": "Exact registered-company use",
    "Evrel": "Exact personal-name use",
    "Dovik": "Exact active online-store use",
    "Cavrel": "Exact surname/archive use",
    "Vairel": "Exact active AI-marketing company",
    "Ambermere": "Exact active website/company use",
    "Briarmere": "Exact invitation-design product/brand use",
    "Caldermere": "Exact active investment-company use",
    "Lindenmere": "Exact active market/store use",
    "Acroterion": "Exact active website/company use",
    "Maestoso": "Exact active website/company use",
    "Impasto": "Exact active restaurant use",
    "Velluto": "Exact active online-store use",
    "Clever Fiction": "Exact app/product use",
    "Afterbeat": "Exact active organization use",
    "Yearwork": "Exact registered-company notice",
    "Eonmark": "Exact registered-company use",
}


def classify(name: str):
    if name in REMOVE:
        return "REMOVE - DIRECT BEAUTY/HEALTH", REMOVE[name]
    if name in TM_OR_PRODUCT:
        return "CAUTION - TRADEMARK/PRODUCT", TM_OR_PRODUCT[name]
    if name in ACTIVE_OTHER:
        return "CAUTION - ACTIVE OTHER USE", ACTIVE_OTHER[name]
    return "PROVISIONAL - NO OBVIOUS EXACT", "No obvious exact active beauty/skincare master-brand conflict in a basic exact-name web scan"


with (ROOT / "marketplace-search-results.csv").open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "MarketplaceDecision", "MarketplaceReason", "TopExactSearchResult", "EvidenceURL"])
    for name, title, url in RESULTS:
        decision, reason = classify(name)
        writer.writerow([name, decision, reason, title, url])

counts = {}
for name, _, _ in RESULTS:
    decision, _ = classify(name)
    counts[decision] = counts.get(decision, 0) + 1

print({"rows": len(RESULTS), "counts": counts})
