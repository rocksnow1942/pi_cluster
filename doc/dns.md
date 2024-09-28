To find out the DNS server that your system is using, you can check the
`/etc/resolv.conf` file. This file contains the IP addresses of the DNS
servers that your system is using.

```sh
cat /etc/resolv.conf
```

For home server name, name it as `<hostname>.<un_locode>.<domain_name>.<tld>`.
For example, `pi4s.sba.example.com`.

[UN Code for Trade and Transport Locations](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)

### References

1. [How to use domain names for servers in a home environment](https://samuelsson.dev/how-to-use-domain-names-for-servers-in-a-home-environment/)
