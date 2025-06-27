import argparse
from modules import xss, sqli, cmdi
from utils.encoders import encode_payload
import pyperclip
import json

def main():
    parser = argparse.ArgumentParser(description="Custom Payload Generator")
    parser.add_argument("--xss", action="store_true")
    parser.add_argument("--sqli", action="store_true")
    parser.add_argument("--cmdi", action="store_true")
    parser.add_argument("--encode", choices=["base64", "url", "hex"])
    parser.add_argument("--copy", action="store_true")
    parser.add_argument("--export", choices=["json", "txt"])

    args = parser.parse_args()
    payloads = []

    if args.xss: payloads += xss.get_xss_payloads()
    if args.sqli: payloads += sqli.get_sqli_payloads()
    if args.cmdi: payloads += cmdi.get_cmdi_payloads()

    if args.encode:
        payloads = [encode_payload(p, args.encode) for p in payloads]

    if args.copy:
        pyperclip.copy('\n'.join(payloads))
        print("[+] Copied to clipboard")

    if args.export == "json":
        with open("output/payloads.json", "w") as f:
            json.dump(payloads, f)
    elif args.export == "txt":
        with open("output/payloads.txt", "w") as f:
            f.write("\n".join(payloads))

    print("\n".join(payloads))

if __name__ == "__main__":
    main()
