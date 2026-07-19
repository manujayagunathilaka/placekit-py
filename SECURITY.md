# Security Policy

## Supported versions

`placekit-py` is currently in early development.

Security updates will focus on the latest version of the project.

| Version | Supported |
| ------- | --------- |
| 0.1.x   | Yes       |

## Reporting a vulnerability

If you discover a security issue, please do not open a public issue.

Instead, report it privately through GitHub Security Advisories if available, or contact the maintainer directly.

When reporting a vulnerability, please include:

- A clear description of the issue
- Steps to reproduce the issue
- Potential impact
- Any suggested fix, if available

## Scope

Security issues may include:

- Exposure of secrets or API keys
- Unsafe handling of external provider credentials
- Unsafe network request behavior
- Dependency vulnerabilities
- Issues that could affect users integrating this package into larger applications

## Notes

This project does not currently include production external API providers.

Future providers such as OpenStreetMap and Google Places will require additional attention to API keys, request handling, timeouts, and provider-specific safety concerns.