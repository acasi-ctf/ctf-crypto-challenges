FROM ghcr.io/acasi-ctf/ctf/penimage:latest

COPY challenges/crypto/symmetric/modes_of_operation/ctr_mode/ctr_mode_usedIV/ctr_mode_usedIV.py /home/player
COPY challenges/crypto/symmetric/modes_of_operation/ctr_mode/ctr_mode_usedIV/flawed_encryption.py /home/player
CMD ["python3", "ctr_mode_usedIV.py"]