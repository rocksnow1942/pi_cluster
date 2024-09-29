## Set up domain name for pi cluster servers

To find out the DNS server the system is using, check the `/etc/resolv.conf`
file. This file contains the IP addresses of the DNS servers.

```sh
$ cat /etc/resolv.conf
> search lan
> nameserver 192.168.86.1
```

For home server name, name it as `<hostname>.<un_locode>.<domain_name>.<tld>`.
For example, `pi4s.sba.example.com`.

[UN Code for Trade and Transport Locations](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)

For simplicity, I skipped the UN code and used the domain name `h-kang.com`.

Host name to IP address mapping is stored in [hosts file](./hosts).

Add the DNS records to registrar's DNS server.

> **Note**: My domain is registered at SquareSpace. However I hosted my site on
> Netlify. So I had to use Netlify's DNS server to add the DNS records.

| Hostname         | Type | Data           |
| ---------------- | ---- | -------------- |
| pinas.h-kang.com | A    | 192.168.86.247 |
| pi4s.h-kang.com  | A    | 192.168.86.203 |
| pi4p.h-kang.com  | A    | 192.168.86.204 |
| tp.h-kang.com    | A    | 192.168.86.201 |

These DNS records maps hostnames to IP addresses.

To map service names to hostnames, there are two options:

1. Add `CNAME`` records to map service names to hostnames.

   | Service Name | Type  | Data            |
   | ------------ | ----- | --------------- |
   | \*.home      | CNAME | tp.h-kang.com   |
   | k8s          | CNAME | pi4s.h-kang.com |

   Here `tp.h-kang.com` is the Nginx reverse proxy server.

1. Add `A`` records to map service names to IP addresses. I would favor the
   first option as it only exposes the proxy server.

### References

1. [How to use domain names for servers in a home environment](https://samuelsson.dev/how-to-use-domain-names-for-servers-in-a-home-environment/)
