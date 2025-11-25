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