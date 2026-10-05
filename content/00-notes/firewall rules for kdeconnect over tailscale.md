---
tags:
  - atomic
  - tools/cli
up:
created: 2026-08-21
status: open
publish: true
---

Need this for kdeconnect to work across different networks.
```sh
firewall-cmd --permanent --new-zone=tailscale
firewall-cmd --permanent --zone=tailscale --add-interface=tailscale0
firewall-cmd --permanent --zone=tailscale --add-service=kdeconnect
firewall-cmd --reload

# Verify
firewall-cmd --get-zone-of-interface tailscale0
firewall-cmd --zone=tailscale --list-all
```

## References
