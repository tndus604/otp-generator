.PHONY: all clean

all: submission

submission: main.py
	echo '#!/usr/bin/env python3' | cat - main.py > temp && mv temp submission
	chmod +x submission

clean:
	rm -f submission otp_qr.jpg secret.txt
