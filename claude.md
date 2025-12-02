# SmartHus - Köinge

Detta projekt handlar om vårt lilla hus i Köinge.

## Projektets mål

Målet är att skapa ett **smart energisystem** som är så enkelt och energieffektivt som möjligt. Vi går igenom all dokumentation grundligt för att förstå systemet på djupet och kunna optimera det.

## Syfte med detta repo

Detta repo fungerar som en kunskapsbas för att snabbt skapa kontext kring:
- Var vi befinner oss i projektet
- Vad vi håller på med
- Vilka beslut som har tagits och varför

## Projektstruktur

```
SmartHus/
├── docs/
│   ├── vp/                    # Värmepump-dokumentation
│   │   └── bruksanvisning/
│   │       ├── original.pdf   # Originaldokument
│   │       ├── kapitel.yaml   # Kapitelindelning
│   │       ├── sidor/         # Uppdelade sidor
│   │       └── kapitel/       # Grupperade kapitel
│   └── tank/                  # Ackumulatortank-dokumentation
├── scripts/                   # Verktyg
│   ├── split_pdfs.py          # Dela upp PDF i sidor
│   └── group_chapters.py      # Gruppera sidor till kapitel
└── system/
    └── hemstruktur.md         # Systembeskrivning
```

Se `system/hemstruktur.md` för detaljerad beskrivning av hur systemet hänger ihop.

## Instruktioner för Claude

**VIKTIGT:** När du ska läsa dokumentation för en komponent:
1. **Läs alltid `kapitel.yaml` först** om den finns - den beskriver dokumentets struktur
2. Använd kapitelindelningen för att hitta rätt avsnitt snabbt
3. Läs specifika sidor från `kapitel/` för att hålla kontexten liten

## Installerad utrustning

### Värmepump (vp)
- **Modell:** KHC-06RY1-B
- **Refereras alltid som:** `vp`
- **Dokumentation:** `docs/vp/`

### Ackumulatortank
- **Installerad modell:** TIV-500L/FC110/SOL10
- **Dokumentation:** `docs/tank/`
- **Notering:** Vi använder dokumentation för SOL12-modellen. Skillnaden är att solslingorna är lite längre i SOL12.

### Golvvärme
- **Typ:** Vattenburen golvvärme
