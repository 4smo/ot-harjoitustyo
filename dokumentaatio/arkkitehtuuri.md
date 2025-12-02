# Arkkitehtuurikuvaus

## Luokkakaavio

```mermaid
flowchart TD
    TextUI --> ConversionService
    ConversionService --> UnitRepository
```

Sovelluksen keskeiset luokat:
- **TextUI**: Käyttöliittymä
- **ConversionService**: Yksikkömuunnosten sovelluslogiikka
- **UnitRepository**: Yksikkötietojen hallinta

## Sekvenssikaavio: Yksikkömuunnos

```mermaid
sequenceDiagram
    actor User
    User->>TextUI: convert 100 m to km
    TextUI->>ConversionService: convert(100, "m", "km")
    ConversionService->>UnitRepository: get_unit_category("m")
    UnitRepository-->>ConversionService: "length"
    ConversionService->>UnitRepository: get_factor("m")
    UnitRepository-->>ConversionService: 1.0
    ConversionService->>UnitRepository: get_factor("km")
    UnitRepository-->>ConversionService: 1000.0
    ConversionService-->>TextUI: 0.1
    TextUI-->>User: 100 m = 0.1000 km
```