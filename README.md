# Njord A – Isoleringsliste Lookup

Enkel webapp for å søke etter elektrisk utstyr i isoleringslisten for Njord A-plattformen.

Søk på utstyrs-TAG, navn eller tavlenummer – og få tilbake plassering, felt, tavle og låsnummer.

## Kjøre med Docker Compose (Unraid)

```bash
# Klon repoet
git clone https://github.com/<ditt-brukernavn>/njord-lookup.git
cd njord-lookup

# Bygg og start
docker compose up -d

# Appen kjører nå på http://<server-ip>:5088
```

### Unraid – Community Applications

Du kan også sette opp containeren manuelt i Unraid:

| Parameter       | Verdi                        |
| --------------- | ---------------------------- |
| Repository      | Bygg fra lokal Dockerfile    |
| Container Port  | `5000`                       |
| Host Port       | `5088` (eller valgfritt)     |
| Restart Policy  | Unless Stopped               |

## Oppdatere data

Utstyrsdata ligger i `data/equipment.json`. For å oppdatere:

1. Erstatt JSON-filen med oppdatert data
2. Rebuild containeren: `docker compose up -d --build`

## Cloudflare Tunnel

For remote tilgang via Cloudflare Tunnel, legg til en ny public hostname som peker til `http://localhost:5088`.

## Tailscale

Appen er tilgjengelig direkte via Tailscale-nettverket på `http://<tailscale-ip>:5055`.

## Teknisk

- **Backend:** Python / Flask / Gunicorn
- **Frontend:** Vanilla HTML/CSS/JS (ingen build-steg)
- **Database:** JSON-fil (741 oppføringer)
- **Container:** ~50 MB image

## Søkeeksempel

Søk: `EM-23-0009A`

| Felt        | Verdi                                |
| ----------- | ------------------------------------ |
| Tag         | EM-23-0009A                          |
| Beskrivelse | EL. MOTOR FOR HYDRAULISK START PUMPE A |
| Tavle       | EN-82-0002A                          |
| Plassering  | C33 LER (prosesstavle A)             |
| Felt        | 15 - M1R2ae                          |
| Lås nr.     | 66                                   |

## Lisens

Intern bruk.
