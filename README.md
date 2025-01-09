# mgc-cli-tests
funcional tests on Magalu Cloud CLI

## Requirements
- python 3.12
- poetry
- [MGC CLI](https://github.com/MagaluCloud/mgccli/) on path (or configured via `MGC_PATH` env var)

## How to run

```bash
poetry run pytest
```

## Modules tested

Settings:
- General
- Authorization
- Config
- Profile
- Workspaces

Products:
- Network
- Virtual machines
