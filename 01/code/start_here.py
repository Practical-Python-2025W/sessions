input("""I wrote a little program to encode strings.
But I accidentally deleted the file containing the key to decrypt an encrypted string I need.
Can you help me recover the original string?
If the string happens to be an URL I take no responsibility for any damage caused by visiting it, nor do I endorse any content you may find there.
Press Enter to continue...""")
encrypted_string = "000000904800000100920000010092000000974400000100050000005046000000408900000040890000009744000000904800000099180000008439000000861300000093090000004002000000965700000099180000008961000000408900000091350000010005000001000500000101790000008787000001000500000040890000004785000000435000000040890000004263"
import decoder
print("\n\n\n")
print("decoded string:")
print(decoder.str_encoder_decoder(encrypted_string))
print("\n\n\n")