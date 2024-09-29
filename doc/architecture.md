### Cluster Architecture

The cluster architecture is based on the following components:

- tp.h-kang.com: Server for reverse proxy (nginx), dnsmasq, fleet health monitoring
- pinas.h-kang.com: OpenMediaVault NAS for file storage, backup
- pi4[*].h-kang.com: Raspberry Pi 4B for Kubernetes cluster
  - pi4s.h-kang.com: Postgres database server (golang)
  - pi4p.h-kang.com: Custom Python application server (Compute)
  - pi4k.h-kang.com: SMTP server
  - pi4o.h-kang.com: Web server
