# Hemstruktur - Energisystem Köinge

Översikt över husets energisystem och hur komponenterna hänger ihop.

## Systemöversikt

```
                          ┌─────────────────┐
                          │   SOLFÅNGARE    │
                          │   (framtid)     │
                          └────────┬────────┘
                                   │
                                   ▼
┌─────────────┐           ┌─────────────────┐           ┌─────────────────┐
│     VP      │──── ▶ ────│      TANK       │──── ▶ ────│   GOLVVÄRME     │
│ KHC-06RY1-B │   värme   │ TIV-500L/FC110  │   värme   │                 │
└─────────────┘           └─────────────────┘           └─────────────────┘
```

## Komponenter

### Värmepump (vp)
- **Modell:** KHC-06RY1-B (Kaisai Arctic Mono)
- **Typ:** Luft-vatten värmepump
- **Funktion:** Utvinner värme från uteluften och värmer vatten som skickas till ackumulatortanken
- **Dokumentation:** `docs/vp/`

### Ackumulatortank
- **Modell:** TIV-500L/FC110/SOL10
- **Volym:** 500 liter
- **Funktion:** Lagrar värme från värmepumpen och distribuerar till golvvärmen
- **SOL-slingor:** Förberett för framtida solfångare
- **Dokumentation:** `docs/tank/`

### Golvvärme
- **Typ:** Vattenburen golvvärme
- **Funktion:** Värme distribueras jämnt via golvet i huset

## Framtida möjligheter

### Solfångare
Tanken har SOL-slingor (SOL10) som kan kopplas till solfångare för att:
- Komplettera värmepumpen med solenergi
- Minska elförbrukningen under soliga dagar
- Öka systemets energieffektivitet

## Energiflöde

1. **VP** utvinner värme från uteluften
2. Värmen överförs till **ackumulatortanken**
3. Tanken distribuerar värme till **golvvärmen**
4. *(Framtid)* Solfångare kan bidra med extra värme till tanken
