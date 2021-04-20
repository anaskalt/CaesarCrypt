encrypted_text   = input("Κρυπτογραφημένο κείμενο: ")
alphabet     = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
encrypted_list    = [b for b in encrypted_text]
alphabet_list    = [d for d in alphabet]
plain_text    = ''

for j in range(0,24):
   for c in encrypted_list:
      if c in alphabet_list:
         index    = alphabet_list.index(c)
         pIndex   = (index - j) % 24
         plain_text    += alphabet_list[pIndex]
      else:
         plain_text    += c
   print("Αρχικό κείμενο [ μετατοπισμένο κατά " + str(j) +"] : " + plain_text + "\r\n")
   plain_text = ''