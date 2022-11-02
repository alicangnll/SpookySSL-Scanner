# SpookySSL-Scanner
SpookySSL CVE-2022-3602 SSLv3 Scanner for Windows, Linux, macOS
<br><br>
<h2>What is the CVE-2022-3602?</h2>
<p>First of all, we must be know Remote code execution (RCE)
<br>
Remote code execution (RCE) attacks allow an attacker to remotely execute malicious code on a computer. The impact of an RCE vulnerability can range from malware execution to an attacker gaining full control over a compromised machine.
<br><br>
CVE-2022-3602 vulnerability in OpenSSL occurs due to incorrect processing of Punycode while checking X.509 certificates.<br>
Punycode is a representation of Unicode strings using the limited ASCII character subset. It is usually used to encode domain names containing non-ASCII characters, for example Japanese letters. A punycode-encoded string<br><br>
begins with “xn--” and is followed by English characters and digits.<br><br>
The vulnerable function ossl_punycode_decode may cause buffer overflow during Punycode string decoding. It is called when OpenSSL processes a certificate chain. In order to exploit vulnerability it is required to:<br><br>
1) Craft a CA (certificate authority) certificate or Intermediary certificate that contains the “nameConstraints” field with a malicious Punycode string. The Punycode string must contain at least 512 bytes excluding “xn--”.<br><br>
2) Craft a leaf certificate that contains a SubjectAlternateName (SAN) otherName field that specifies a SmtpUTF8Mailbox string<br><br>
Source : https://blog.checkpoint.com/2022/11/01/openssl-vulnerability-cve-2022-3602-remote-code-execution-and-cve-2022-3786-denial-of-service-check-point-research-update/
</p>
<h2>Installation</h2>
<ul>
<li>pip install win32api</li>
<li>pip install glob</li>
<li>pip install platform</li>
<li>pip install osquery (for Linux)</li>
</ul>
<br>
<h2>Pics</h2>
<img src="spooky.png" />
